"""
jpfun SEO indexing health check — diagnose "0 search clicks / 0 conversions".

Covers the three usual technical culprits before anything else is blamed:
  1. robots.txt / sitemap.xml must respond 200 and sitemap must be valid XML
     (a 404/500 on either silently empties the index).
  2. Recent git history for app/templates/* and the robots.txt route in
     app/__init__.py, scanned for an accidentally-added "noindex" or a
     full-site "Disallow: /" slipped in by a deploy.
  3. Optional: classify a GSC "Pages"/Coverage CSV export ("제외됨" rows) by
     exclusion reason, so triage doesn't start from a raw reason string.

Run manually:
  python script/check_seo_indexing.py
  python script/check_seo_indexing.py --since-commits 30
  python script/check_seo_indexing.py --gsc-csv path/to/excluded_pages.csv
"""
from __future__ import annotations

import argparse
import csv
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

import requests

BASE_DIR = Path(__file__).resolve().parent.parent

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from app.config import SITE_CONFIG  # noqa: E402

NOINDEX_PATHS = ("app/templates", "app/__init__.py")

# (keywords to match against a GSC reason string, category label, short note)
REASON_CATEGORIES = [
    (("noindex",), "noindex 태그", "의도한 제외인지 확인 — 최근 배포에서 실수로 추가됐을 수 있음"),
    (("robots.txt",), "robots.txt 차단", "robots.txt의 Disallow 규칙 확인"),
    (("soft 404",), "소프트 404", "콘텐츠가 비어있거나 얇은지, 템플릿 렌더링 오류인지 확인"),
    (("not found", "404"), "404 (페이지 없음)", "사이트맵에 죽은 링크가 남아있는지 확인"),
    (("server error", "5xx", "500"), "서버 오류 (5xx)", "배포/호스팅 상태 확인"),
    (("redirect",), "리다이렉트", "캐노니컬 체인과 리다이렉트 목적지 확인"),
    (("duplicate", "canonical"), "중복/캐노니컬", "캐노니컬 태그와 중복 슬러그 확인"),
    (("crawled", "discovered"), "크롤링/발견됨-미색인", "콘텐츠 품질 또는 신호 부족 — 급히 조치할 필요 없을 수 있음"),
    (("unauthorized", "forbidden", "401", "403"), "접근 차단 (401/403)", "Googlebot을 막는 인증/방화벽 규칙 확인"),
]


def check_robots_and_sitemap(base_url: str) -> bool:
    base = base_url.rstrip("/")
    ok = True

    try:
        res = requests.get(f"{base}/robots.txt", timeout=15)
        if res.status_code != 200:
            print(f"❌ /robots.txt returned HTTP {res.status_code}")
            ok = False
        elif any(line.strip() == "Disallow: /" for line in res.text.splitlines()):
            print("❌ /robots.txt disallows the entire site (bare 'Disallow: /' rule)")
            ok = False
        else:
            print("✅ /robots.txt returns 200")
    except requests.RequestException as exc:
        print(f"❌ /robots.txt request failed: {exc}")
        ok = False

    try:
        res = requests.get(f"{base}/sitemap.xml", timeout=15)
        if res.status_code != 200:
            print(f"❌ /sitemap.xml returned HTTP {res.status_code}")
            ok = False
        else:
            try:
                ET.fromstring(res.content)
                print("✅ /sitemap.xml returns 200 and parses as valid XML")
            except ET.ParseError as exc:
                print(f"❌ /sitemap.xml returned 200 but is not valid XML: {exc}")
                ok = False
    except requests.RequestException as exc:
        print(f"❌ /sitemap.xml request failed: {exc}")
        ok = False

    return ok


def check_noindex_regressions(since_commits: int) -> bool:
    try:
        diff = subprocess.check_output(
            ["git", "log", f"-{since_commits}", "-p", "--", *NOINDEX_PATHS],
            cwd=BASE_DIR,
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as exc:
        print(f"❌ git log failed: {exc}")
        return False

    commit, file_path = None, None
    findings: list[tuple[str, str, str]] = []
    for line in diff.splitlines():
        if line.startswith("commit "):
            commit = line.split()[1][:10]
        elif line.startswith("+++ b/"):
            file_path = line[6:]
        elif line.startswith("+") and not line.startswith("+++"):
            lowered = line.lower()
            if "noindex" in lowered or "disallow: /" == lowered[1:].strip():
                findings.append((commit or "?", file_path or "?", line[1:].strip()))

    if findings:
        print(f"❌ found {len(findings)} line(s) adding noindex/full-disallow in the last {since_commits} commits touching {', '.join(NOINDEX_PATHS)}:")
        for commit_hash, file_path, line in findings:
            print(f"   {commit_hash} {file_path}: {line}")
        return False

    print(f"✅ no noindex/full-disallow additions in the last {since_commits} commits touching {', '.join(NOINDEX_PATHS)}")
    return True


def _find_column(fieldnames: list[str], candidates: tuple[str, ...]) -> str | None:
    lowered = {name.lower(): name for name in fieldnames}
    for candidate in candidates:
        if candidate in lowered:
            return lowered[candidate]
    return None


def classify_gsc_coverage(csv_path: Path) -> bool:
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        print(f"⚠️  {csv_path} has no rows")
        return True

    fieldnames = list(rows[0].keys())
    reason_col = _find_column(fieldnames, ("reason", "status", "coverage state", "validation status", "이유", "상태"))
    count_col = _find_column(fieldnames, ("pages", "valid pages", "count", "페이지수", "페이지"))

    if not reason_col:
        print(f"❌ could not find a reason/status column in {csv_path} (columns: {fieldnames})")
        return False

    counts: Counter[str] = Counter()
    for row in rows:
        reason = (row.get(reason_col) or "").strip()
        if not reason:
            continue
        n = 1
        if count_col:
            try:
                n = int(row[count_col])
            except (ValueError, TypeError):
                n = 1
        counts[reason] += n

    print(f"🔍 GSC excluded-page reasons from {csv_path.name}:")
    for reason, n in counts.most_common():
        lowered = reason.lower()
        category, note = "기타", "알려진 카테고리에 없음 — GSC 리포트에서 직접 확인"
        for keywords, cat_label, cat_note in REASON_CATEGORIES:
            if any(kw in lowered for kw in keywords):
                category, note = cat_label, cat_note
                break
        print(f"   {n:>5}  {reason!r} → [{category}] {note}")

    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="jpfun SEO indexing health check")
    parser.add_argument("--base-url", default=SITE_CONFIG["site_url"], help="site base URL to probe")
    parser.add_argument("--since-commits", type=int, default=20, help="how many recent commits to scan for noindex regressions")
    parser.add_argument("--gsc-csv", type=Path, default=None, help="path to a GSC Coverage/Pages 'excluded' CSV export")
    args = parser.parse_args()

    print("🔍 jpfun SEO indexing check")
    robots_sitemap_ok = check_robots_and_sitemap(args.base_url)
    noindex_ok = check_noindex_regressions(args.since_commits)

    gsc_ok = True
    if args.gsc_csv:
        if args.gsc_csv.exists():
            gsc_ok = classify_gsc_coverage(args.gsc_csv)
        else:
            print(f"❌ --gsc-csv path does not exist: {args.gsc_csv}")
            gsc_ok = False
    else:
        print("ℹ️  no --gsc-csv passed — skipping GSC excluded-reason classification")

    if robots_sitemap_ok and noindex_ok and gsc_ok:
        print("✅ SEO indexing check passed")
    else:
        print("⚠️  SEO indexing check needs attention — see messages above")


if __name__ == "__main__":
    main()
