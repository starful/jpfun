import os
import csv
import sys
import re
import concurrent.futures
from datetime import datetime
from dotenv import load_dotenv

from topic_queue_csv import resolve as resolve_queue_csv
from content_guards import (
    duplicate_guide_reason,
    locale_pair_status,
    quality_prompt_block,
    sibling_exists,
    strip_code_fences,
    validate_generated_markdown,
)


def _emit_pipeline_result(**kwargs):
    try:
        from generation_result import emit_generation_result

        emit_generation_result(**kwargs)
    except ImportError:
        pass

load_dotenv()

def _claude_md(prompt: str) -> str:
    """MD text via Claude CLI subscription (not Claude API)."""
    import sys
    from pathlib import Path
    _shared = Path(__file__).resolve().parents[2] / "_shared"
    if str(_shared) not in sys.path:
        sys.path.insert(0, str(_shared))
    from site_llm import generate_md_text
    return generate_md_text(prompt)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DEFAULT_GUIDE_CSV = os.path.join(SCRIPT_DIR, "csv", "guides.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "app", "content", "guides")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def _guides_csv_path() -> str:
    return resolve_queue_csv("guides", DEFAULT_GUIDE_CSV)


def generate_guide(row, lang):
    base_id = (row.get('id') or '').strip()
    if not base_id:
        return "❌ 에러: id 없음"

    dup = duplicate_guide_reason(base_id, OUTPUT_DIR)
    if dup:
        return f"⏭️ 스킵(중복주제): {base_id}_{lang} — {dup}"

    topic = row.get(f'topic_{lang}') or ''
    keywords = row.get('keywords') or ''
    activity = _infer_activity(row)
    filename = f"{base_id}_{lang}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    filling_sibling = sibling_exists(OUTPUT_DIR, base_id, lang)
    if lang == "ko":
        length_line = (
            "Length: at least 2,500 characters in the Markdown body "
            "(exclude YAML). Prefer 2,800+ with concrete visitor logistics.\n"
        )
    elif filling_sibling:
        length_line = "Length: at least 6,500 characters — filling a missing locale; match sibling depth.\n"
    else:
        length_line = "Length: at least 5,000 characters.\n"
    activity_yaml = f"\n    activity: {activity}" if activity else ""
    rules = quality_prompt_block(lang=lang)

    prompt = f"""
    Write a practical SEO leisure travel guide for JPFun about '{topic}' in Japan (ski / scuba dive / surf / camp when relevant).
    Target Language: {lang}
    Keywords to include: {keywords}
    {length_line}{rules}

    Also include historical or cultural context when it helps a visitor decide.
    If keywords are sparse, still write concrete logistics (hub city, season window, what to book).

    Output format:
    ---
    lang: {lang}{activity_yaml}
    title: "Catchy SEO Title about {topic}"
    summary: "Engaging 2-line summary"
    date: "{datetime.now().strftime('%Y-%m-%d')}"
    ---
    (Body content in Markdown)
    """

    try:
        print(f"📡 API 호출 시작: {filename}")
        content = None
        errors: list[str] = []
        ok = False
        for attempt in range(2):
            call_prompt = prompt
            if attempt == 1:
                call_prompt = (
                    prompt
                    + "\n\nRETRY: Previous draft was too short. Expand every ## section "
                    "with concrete numbers, place names, booking steps, and season windows "
                    "until the body is at least 2,500 characters.\n"
                )
                print(f"🔁 짧은 초안 재작성: {filename}")
            response_text = _claude_md(call_prompt)
            content = strip_code_fences(response_text or "")
            ok, errors = validate_generated_markdown(
                content,
                kind="guide",
                lang=lang,
                sibling_exists=filling_sibling,
            )
            if ok:
                break
            if not any(e.startswith("too_short:") for e in errors):
                break
        if not ok:
            return f"⛔ 품질미달·저장안함: {filename} — {', '.join(errors)}"
        content = _ensure_activity_frontmatter(content, activity)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"✅ 성공: {filename}"
    except Exception as e:
        return f"❌ 에러: {filename} - {str(e)}"
def _activity_limits_from_env():
    """Per-activity caps from okadmin (ski / surf / dive=scuba / camp)."""
    caps = {
        "ski": int(os.environ.get("SKI_GUIDE_LIMIT") or 0),
        "surf": int(os.environ.get("SURF_GUIDE_LIMIT") or 0),
        "dive": int(os.environ.get("DIVE_GUIDE_LIMIT") or 0),
        "camp": int(os.environ.get("CAMP_GUIDE_LIMIT") or 0),
    }
    if any(caps.values()):
        return caps
    return None


def _ensure_activity_frontmatter(content: str, activity: str) -> str:
    """Hub /surf /ski /dive /camp filter on YAML activity; never rely on the model."""
    if not activity:
        return content
    if re.search(r"(?m)^activity:\s*\S+", content):
        return content
    patched, n = re.subn(
        r"(?m)^(lang:\s*\S+\s*\n)",
        rf"\1activity: {activity}\n",
        content,
        count=1,
    )
    return patched if n else content


def _infer_activity(row: dict) -> str:
    raw = (row.get("activity") or "").strip().lower()
    if raw == "scuba":
        return "dive"
    if raw in ("ski", "dive", "camp", "surf"):
        return raw
    blob = " ".join(str(row.get(k) or "") for k in ("id", "topic_en", "topic_ko", "keywords")).lower()
    if any(k in blob for k in ("scuba", "dive", "다이빙", "스쿠버")):
        return "dive"
    if any(k in blob for k in ("surf", "서핑", "쇼난")):
        return "surf"
    if any(k in blob for k in ("ski", "powder", "스키")):
        return "ski"
    if any(k in blob for k in ("camp", "glamping", "캠핑")):
        return "camp"
    return ""


def _want_fill_half() -> bool:
    return os.environ.get("FILL_HALF", "").strip().lower() in ("1", "true", "yes")


def _missing_langs(base_id: str) -> list[str]:
    missing = []
    for lang in ("en", "ko"):
        if not os.path.isfile(os.path.join(OUTPUT_DIR, f"{base_id}_{lang}.md")):
            missing.append(lang)
    return missing


def run_batch(limit=3):
    """New topics: en+ko as a set (half pairs skipped). FILL_HALF=1: missing locale only."""
    tasks_to_run = []
    pairs_queued = 0
    half_skipped = 0
    fill_half = _want_fill_half()
    activity_caps = None if fill_half else _activity_limits_from_env()
    activity_used = {"ski": 0, "dive": 0, "camp": 0, "surf": 0, "": 0}

    csv_path = _guides_csv_path()
    if not os.path.exists(csv_path):
        print(f"❌ CSV 파일을 찾을 수 없습니다: {csv_path}")
        return

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not activity_caps and limit > 0 and pairs_queued >= limit:
                break
            gid = (row.get('id') or '').strip()
            if not gid:
                continue
            act = _infer_activity(row)
            if activity_caps is not None:
                if act not in activity_caps or activity_caps[act] <= 0:
                    continue
                if activity_used.get(act, 0) >= activity_caps[act]:
                    continue
            dup = duplicate_guide_reason(gid, OUTPUT_DIR)
            if dup:
                print(f"⏭️ 큐에서 제외(중복주제): {gid} — {dup}")
                continue
            status = locale_pair_status(OUTPUT_DIR, gid)
            if status == "complete":
                continue
            if fill_half:
                if status != "half":
                    continue
                for lang in _missing_langs(gid):
                    tasks_to_run.append((row, lang))
                pairs_queued += 1
                continue
            if status == "half":
                half_skipped += 1
                continue
            for lang in ['en', 'ko']:
                tasks_to_run.append((row, lang))
            pairs_queued += 1
            activity_used[act] = activity_used.get(act, 0) + 1

    if fill_half:
        print(f"ℹ️  반쪽 채우기: {pairs_queued}주제 · {len(tasks_to_run)}파일")
    elif half_skipped:
        print(f"⏭️  반쪽(en/ko 한쪽만) 가이드 {half_skipped}건 — 신규 페어 우선으로 스킵")

    if not tasks_to_run:
        msg = "💡 채울 반쪽 가이드가 없습니다." if fill_half else "💡 새로 생성할 가이드 페어가 없습니다."
        print(msg)
        _emit_pipeline_result(step="guides", topics=0, generated=0, skipped=half_skipped)
        return

    if activity_caps:
        print(
            "🎯 활동별 한도: "
            f"ski={activity_caps['ski']} surf={activity_caps['surf']} "
            f"dive={activity_caps['dive']} camp={activity_caps['camp']}"
        )
    print(f"🚀 {pairs_queued}페어 · {len(tasks_to_run)}파일 가이드 생성 시작...")

    workers = max(1, min(len(tasks_to_run), 5))
    ok = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(generate_guide, t[0], t[1]) for t in tasks_to_run]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(result)
            if result and result.startswith("✅"):
                ok += 1
    _emit_pipeline_result(
        step="guides",
        topics=pairs_queued,
        generated=ok,
        failed=len(tasks_to_run) - ok,
        skipped=half_skipped,
    )

if __name__ == "__main__":
    env_limit = os.environ.get("GUIDE_LIMIT")
    arg_limit = sys.argv[1] if len(sys.argv) > 1 else None
    try:
        run_limit = int(arg_limit or env_limit or 3)
    except ValueError:
        run_limit = 3
    run_batch(limit=run_limit)
