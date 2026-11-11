"""
jpfun SEO indexing health check — diagnose "0 search clicks / 0 conversions".

Covers the usual technical culprits before anything else is blamed:
  1. robots.txt / sitemap.xml must respond 200 and sitemap must be valid XML
     (a 404/500 on either silently empties the index).
  2. Recent git history for app/templates/* and the robots.txt route in
     app/__init__.py, scanned for an accidentally-added "noindex" or a
     full-site "Disallow: /" slipped in by a deploy.
  3. In-process code-level check (no deployed server needed): runs the real
     robots_txt()/sitemap_xml() route functions via a Flask test client and
     cross-checks the generated URLs for duplicate <loc> entries, items/guides
     the app loaded but the sitemap generator dropped, sitemap URLs that
     contradict robots.txt's own Disallow rules, and a noindex meta tag on
     the actual rendered HTML. Can export a CSV of per-URL findings.
  4. Optional: classify a GSC "Pages"/Coverage CSV export ("제외됨" rows) by
     exclusion reason, so triage doesn't start from a raw reason string.

Run manually:
  python script/check_seo_indexing.py
  python script/check_seo_indexing.py --since-commits 30
  python script/check_seo_indexing.py --export-csv out/seo_urls.csv
  python script/check_seo_indexing.py --gsc-csv path/to/excluded_pages.csv
"""
from __future__ import annotations

import argparse
import csv
import re
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


def check_sitemap_generation_inprocess(out_csv: Path | None, max_render_checks: int) -> bool:
    """Run the real robots_txt()/sitemap_xml() route code via a Flask test
    client (no deployed server needed) and cross-check the output for
    duplicate, missing, or noindex/robots-blocked pages."""
    try:
        from app import app as flask_app, CACHED_DATA, CACHED_GUIDES, SITE_CONFIG as APP_SITE_CONFIG
    except Exception as exc:
        print(f"❌ could not import the Flask app in-process: {exc}")
        return False

    client = flask_app.test_client()
    base = APP_SITE_CONFIG['site_url'].rstrip('/')

    robots_res = client.get('/robots.txt')
    sitemap_res = client.get('/sitemap.xml')
    if robots_res.status_code != 200 or sitemap_res.status_code != 200:
        print(f"❌ in-process /robots.txt={robots_res.status_code} /sitemap.xml={sitemap_res.status_code}")
        return False

    disallow_prefixes = [
        line.split(':', 1)[1].strip()
        for line in robots_res.get_data(as_text=True).splitlines()
        if line.lower().startswith('disallow:') and line.split(':', 1)[1].strip()
    ]

    try:
        root = ET.fromstring(sitemap_res.data)
    except ET.ParseError as exc:
        print(f"❌ in-process /sitemap.xml did not parse: {exc}")
        return False

    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    locs = [el.text for el in root.findall('sm:url/sm:loc', ns) if el.text]

    dup_counts = Counter(locs)
    duplicates = {loc: n for loc, n in dup_counts.items() if n > 1}
    if duplicates:
        print(f"❌ {len(duplicates)} duplicate <loc> entries in sitemap.xml:")
        for loc, n in duplicates.items():
            print(f"   x{n}  {loc}")
    else:
        print(f"✅ no duplicate <loc> entries ({len(locs)} URLs)")

    # Each <url> block carries one canonical <loc> plus hreflang alternates for
    # the other language — a ko page is "covered" via its alternate href, not
    # a <loc> of its own, so both must be scanned or every ko page false-positives
    # as "missing".
    xhtml_link_tag = '{http://www.w3.org/1999/xhtml}link'
    sitemap_item_ids: set[str] = set()
    sitemap_guide_ids: set[str] = set()
    for url_el in root.findall('sm:url', ns):
        loc_el = url_el.find('sm:loc', ns)
        hrefs = [loc_el.text] if loc_el is not None and loc_el.text else []
        hrefs += [link.get('href') for link in url_el.findall(xhtml_link_tag) if link.get('href')]
        for href in hrefs:
            if '/item/' in href:
                sitemap_item_ids.add(href.rsplit('/', 1)[-1])
            elif '/guide/' in href:
                sitemap_guide_ids.add(href.rsplit('/', 1)[-1])

    missing_items = [
        item.get('id') for item in CACHED_DATA.get(APP_SITE_CONFIG['data_key'], [])
        if item.get('id') and item.get('lang', 'en') in ('en', 'ko') and item.get('id') not in sitemap_item_ids
    ]
    missing_guides = [
        guide.get('id') for lang in ('en', 'ko') for guide in CACHED_GUIDES.get(lang, [])
        if guide.get('id') and guide.get('id') not in sitemap_guide_ids
    ]
    if missing_items or missing_guides:
        print(f"❌ {len(missing_items)} item page(s) and {len(missing_guides)} guide page(s) loaded by the app but absent from sitemap.xml:")
        for mid in missing_items[:20]:
            print(f"   item  {mid}")
        for mid in missing_guides[:20]:
            print(f"   guide {mid}")
    else:
        print(f"✅ every loaded en/ko item ({len(sitemap_item_ids)}) and guide ({len(sitemap_guide_ids)}) page is in sitemap.xml")

    blocked: list[tuple[str, str]] = []
    for loc in locs:
        path = loc[len(base):] if loc.startswith(base) else loc
        for prefix in disallow_prefixes:
            if path.startswith(prefix):
                blocked.append((loc, prefix))
                break
    if blocked:
        print(f"❌ {len(blocked)} sitemap URL(s) blocked by a robots.txt Disallow rule:")
        for loc, prefix in blocked[:20]:
            print(f"   {loc} ← Disallow: {prefix}")
    else:
        print("✅ no sitemap URL is blocked by robots.txt")

    noindex_hits: list[str] = []
    sample = locs[:max_render_checks] if max_render_checks > 0 else locs
    meta_re = re.compile(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']*)["\']', re.I)
    for loc in sample:
        path = loc[len(base):] if loc.startswith(base) else loc
        res = client.get(path or '/')
        if res.status_code != 200:
            continue
        match = meta_re.search(res.get_data(as_text=True))
        if match and 'noindex' in match.group(1).lower():
            noindex_hits.append(loc)
    if noindex_hits:
        print(f"❌ {len(noindex_hits)} rendered page(s) carry a noindex meta tag:")
        for loc in noindex_hits:
            print(f"   {loc}")
    else:
        print(f"✅ no noindex meta tag found on the {len(sample)} rendered page(s) sampled")

    if out_csv:
        missing_urls = {f"{base}/item/{mid}" for mid in missing_items} | {f"{base}/guide/{mid}" for mid in missing_guides}
        blocked_urls = {loc for loc, _ in blocked}
        noindex_urls = set(noindex_hits)
        out_csv.parent.mkdir(parents=True, exist_ok=True)
        with open(out_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['url', 'duplicate_count', 'missing_from_sitemap', 'blocked_by_robots', 'noindex_detected'])
            for loc in sorted(set(locs) | missing_urls):
                writer.writerow([
                    loc,
                    dup_counts.get(loc, 0),
                    loc in missing_urls,
                    loc in blocked_urls,
                    loc in noindex_urls,
                ])
        print(f"📄 wrote {out_csv} — diff this against a Search Console 'Pages' export to see which flagged URLs GSC also excludes")

    return not duplicates and not missing_items and not missing_guides and not blocked and not noindex_hits


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
    parser.add_argument("--export-csv", type=Path, default=None, help="write the in-process sitemap findings to this CSV path, for diffing against a GSC 'Pages' export")
    parser.add_argument("--max-render-checks", type=int, default=200, help="max sitemap URLs to render in-process when scanning for noindex meta tags (0 = all)")
    parser.add_argument("--gsc-csv", type=Path, default=None, help="path to a GSC Coverage/Pages 'excluded' CSV export")
    args = parser.parse_args()

    print("🔍 jpfun SEO indexing check")
    robots_sitemap_ok = check_robots_and_sitemap(args.base_url)
    generation_ok = check_sitemap_generation_inprocess(args.export_csv, args.max_render_checks)
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

    if robots_sitemap_ok and generation_ok and noindex_ok and gsc_ok:
        print("✅ SEO indexing check passed")
    else:
        print("⚠️  SEO indexing check needs attention — see messages above")


if __name__ == "__main__":
    main()
