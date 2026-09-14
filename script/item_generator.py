"""JPFun leisure spot generator (ski / surf / dive / camp).

Reads script/csv/items.csv (or the okadmin queue) and writes
app/content/{Id}_{en,ko}.md. Images are fetched later by fetch_images.py.
"""
from __future__ import annotations

import csv
import os
import re
import sys
import concurrent.futures
from datetime import datetime
from dotenv import load_dotenv

from topic_queue_csv import resolve as resolve_queue_csv
from content_guards import (
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

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DEFAULT_ITEM_CSV = os.path.join(SCRIPT_DIR, "csv", "items.csv")
CONTENT_DIR = os.path.join(BASE_DIR, "app", "content")
os.makedirs(CONTENT_DIR, exist_ok=True)

TARGET_LANGS = ("en", "ko")
CATEGORY_FOR_ACTIVITY = {
    "ski": "Ski",
    "surf": "Surf",
    "dive": "Dive",
    "camp": "Camp",
}


def _claude_md(prompt: str) -> str:
    """MD text via Claude CLI subscription (not Claude API)."""
    from pathlib import Path

    _shared = Path(__file__).resolve().parents[2] / "_shared"
    if str(_shared) not in sys.path:
        sys.path.insert(0, str(_shared))
    from site_llm import generate_md_text

    return generate_md_text(prompt)


def _items_csv_path() -> str:
    return resolve_queue_csv("items", DEFAULT_ITEM_CSV)


def _want_fill_half() -> bool:
    return os.environ.get("FILL_HALF", "").strip().lower() in ("1", "true", "yes")


def _infer_activity(row: dict) -> str:
    raw = (row.get("Activity") or row.get("activity") or "").strip().lower()
    if raw == "scuba":
        return "dive"
    if raw in CATEGORY_FOR_ACTIVITY:
        return raw
    blob = " ".join(
        str(row.get(k) or "")
        for k in ("Id", "id", "Name", "Name_KO", "Features", "Activity")
    ).lower()
    if any(k in blob for k in ("scuba", "dive", "다이빙", "스쿠버")):
        return "dive"
    if any(k in blob for k in ("surf", "서핑", "쇼난")):
        return "surf"
    if any(k in blob for k in ("ski", "powder", "스키")):
        return "ski"
    if any(k in blob for k in ("camp", "glamping", "캠핑")):
        return "camp"
    return ""


def _activity_limits_from_env():
    caps = {
        "ski": int(os.environ.get("SKI_ITEM_LIMIT") or 0),
        "surf": int(os.environ.get("SURF_ITEM_LIMIT") or 0),
        "dive": int(os.environ.get("DIVE_ITEM_LIMIT") or 0),
        "camp": int(os.environ.get("CAMP_ITEM_LIMIT") or 0),
    }
    if any(caps.values()):
        return caps
    return None


def _item_id(row: dict) -> str:
    raw = (row.get("Id") or row.get("id") or "").strip()
    if raw:
        return re.sub(r"[^a-z0-9_]", "", raw.lower().replace("-", "_"))
    name = (row.get("Name") or "").strip()
    return re.sub(r"[^a-z0-9_]", "", name.lower().replace(" ", "_").replace("'", ""))


def _display_name(row: dict, lang: str) -> str:
    if lang == "ko":
        return (row.get("Name_KO") or row.get("Name") or "").strip()
    return (row.get("Name") or row.get("Name_KO") or "").strip()


def _ensure_yaml_field(content: str, key: str, value: str) -> str:
    if not value:
        return content
    if re.search(rf"(?m)^{re.escape(key)}:\s*\S+", content):
        return content
    patched, n = re.subn(
        r"(?m)^(lang:\s*\S+\s*\n)",
        rf"\1{key}: {value}\n",
        content,
        count=1,
    )
    return patched if n else content


def _patch_item_frontmatter(
    content: str,
    *,
    activity: str,
    lat: str,
    lng: str,
    address: str,
    website: str,
    region: str,
    safe_name: str,
) -> str:
    cat = CATEGORY_FOR_ACTIVITY.get(activity, "")
    content = _ensure_yaml_field(content, "activity", f'"{activity}"' if activity else "")
    content = _ensure_yaml_field(content, "lat", lat)
    content = _ensure_yaml_field(content, "lng", lng)
    content = _ensure_yaml_field(content, "categories", f'["{cat}"]' if cat else "")
    content = _ensure_yaml_field(content, "thumbnail", f'"/static/images/{safe_name}.jpg"')
    content = _ensure_yaml_field(content, "address", f'"{address}"' if address else "")
    content = _ensure_yaml_field(content, "website", f'"{website}"')
    content = _ensure_yaml_field(content, "image_prompt", '""')
    content = _ensure_yaml_field(content, "region", f'"{region}"' if region else "")
    return content


def generate_item(row: dict, lang: str) -> str:
    safe_name = _item_id(row)
    if not safe_name:
        return "❌ 에러: id 없음"

    name = _display_name(row, lang)
    activity = _infer_activity(row)
    lat = (row.get("Lat") or row.get("lat") or "").strip()
    lng = (row.get("Lng") or row.get("lng") or "").strip()
    address = (row.get("Address") or row.get("address") or "").strip()
    features = (row.get("Features") or row.get("features") or "").strip()
    website = (row.get("Website") or row.get("website") or "").strip()
    region = (row.get("Region") or row.get("region") or "").strip()
    cat = CATEGORY_FOR_ACTIVITY.get(activity, "Leisure")
    filename = f"{safe_name}_{lang}.md"
    filepath = os.path.join(CONTENT_DIR, filename)
    filling_sibling = sibling_exists(CONTENT_DIR, safe_name, lang)
    length_line = ""
    if lang != "ko":
        if filling_sibling:
            length_line = "Length: at least 6,500 characters — filling a missing locale; match sibling depth.\n"
        else:
            length_line = "Length: at least 5,000 characters.\n"
    rules = quality_prompt_block(lang=lang)

    prompt = f"""
    Write a practical SEO leisure-spot page for JPFun about '{name}' in Japan.
    Activity: {activity or "leisure"} ({cat}).
    Target Language: {lang}
    Location: {address}
    Features: {features or "(sparse — invent concrete visitor logistics anyway)"}
    Region slug: {region or "japan"}
    {length_line}{rules}

    Output format:
    ---
    lang: {lang}
    title: "Catchy SEO Title mentioning {name}"
    lat: {lat or "0"}
    lng: {lng or "0"}
    activity: "{activity}"
    categories: ["{cat}"]
    thumbnail: "/static/images/{safe_name}.jpg"
    address: "{address}"
    date: "{datetime.now().strftime('%Y-%m-%d')}"
    website: "{website}"
    summary: "Engaging 2-line summary on one line"
    image_prompt: ""
    region: "{region}"
    ---
    (Body content in Markdown)

    IMPORTANT: Do NOT use markdown code blocks. Start directly with '---'.
    Leave image_prompt empty. Images are fetched separately.
    """

    try:
        print(f"📡 API 호출 시작: {filename}")
        response_text = _claude_md(prompt)
        content = strip_code_fences(response_text or "")
        content = _patch_item_frontmatter(
            content,
            activity=activity,
            lat=lat or "0",
            lng=lng or "0",
            address=address,
            website=website,
            region=region,
            safe_name=safe_name,
        )
        ok, errors = validate_generated_markdown(
            content,
            kind="item",
            lang=lang,
            sibling_exists=filling_sibling,
        )
        if not ok:
            return f"⛔ 품질미달·저장안함: {filename} — {', '.join(errors)}"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return f"✅ 성공: {filename}"
    except Exception as e:
        return f"❌ 에러: {filename} - {str(e)}"


def _missing_langs(item_id: str) -> list[str]:
    missing = []
    for lang in TARGET_LANGS:
        if not os.path.isfile(os.path.join(CONTENT_DIR, f"{item_id}_{lang}.md")):
            missing.append(lang)
    return missing


def run_batch(limit=10):
    """New spots: en+ko as a set (half pairs skipped). FILL_HALF=1: missing locale only."""
    tasks_to_run = []
    pairs_queued = 0
    half_skipped = 0
    fill_half = _want_fill_half()
    activity_caps = None if fill_half else _activity_limits_from_env()
    activity_used = {"ski": 0, "dive": 0, "camp": 0, "surf": 0, "": 0}

    csv_path = _items_csv_path()
    if not os.path.exists(csv_path):
        print(f"❌ CSV 파일을 찾을 수 없습니다: {csv_path}")
        return

    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not activity_caps and limit > 0 and pairs_queued >= limit:
                break
            item_id = _item_id(row)
            if not item_id:
                continue
            act = _infer_activity(row)
            if activity_caps is not None:
                if act not in activity_caps or activity_caps[act] <= 0:
                    continue
                if activity_used.get(act, 0) >= activity_caps[act]:
                    continue
            status = locale_pair_status(CONTENT_DIR, item_id)
            if status == "complete":
                continue
            if fill_half:
                if status != "half":
                    continue
                for lang in _missing_langs(item_id):
                    tasks_to_run.append((row, lang))
                pairs_queued += 1
                continue
            if status == "half":
                half_skipped += 1
                continue
            for lang in TARGET_LANGS:
                tasks_to_run.append((row, lang))
            pairs_queued += 1
            activity_used[act] = activity_used.get(act, 0) + 1

    if fill_half:
        print(f"ℹ️  반쪽 채우기: {pairs_queued}주제 · {len(tasks_to_run)}파일")
    elif half_skipped:
        print(f"⏭️  반쪽(en/ko 한쪽만) 스팟 {half_skipped}건 — 신규 페어 우선으로 스킵")

    if not tasks_to_run:
        msg = "💡 채울 반쪽 스팟이 없습니다." if fill_half else "💡 새로 생성할 스팟 페어가 없습니다."
        print(msg)
        _emit_pipeline_result(step="items", topics=0, generated=0, skipped=half_skipped)
        return

    if activity_caps:
        print(
            "🎯 활동별 한도: "
            f"ski={activity_caps['ski']} surf={activity_caps['surf']} "
            f"dive={activity_caps['dive']} camp={activity_caps['camp']}"
        )
    print(f"🚀 {pairs_queued}페어 · {len(tasks_to_run)}파일 스팟 생성 시작...")

    workers = max(1, min(len(tasks_to_run), 5))
    ok = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(generate_item, t[0], t[1]) for t in tasks_to_run]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(result)
            if result and result.startswith("✅"):
                ok += 1
    _emit_pipeline_result(
        step="items",
        topics=pairs_queued,
        generated=ok,
        failed=len(tasks_to_run) - ok,
        skipped=half_skipped,
    )


if __name__ == "__main__":
    env_limit = os.environ.get("CONTENT_LIMIT")
    arg_limit = sys.argv[1] if len(sys.argv) > 1 else None
    try:
        run_limit = int(arg_limit or env_limit or 10)
    except ValueError:
        run_limit = 10
    run_batch(limit=run_limit)
