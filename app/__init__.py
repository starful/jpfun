from flask import Flask, jsonify, render_template, abort, redirect, request, Response, send_from_directory
from flask_compress import Compress
import json, os, frontmatter, markdown, re, glob, hashlib, copy, random, urllib.parse, urllib.request, io
from datetime import datetime
from urllib.parse import quote

app = Flask(__name__)
Compress(app)

# ==========================================
# ✅ Config import (main customization point)
# ==========================================
try:
    from .config import SITE_CONFIG
except ImportError:
    from config import SITE_CONFIG

try:
    from .reactions import reactions_bp
except ImportError:
    from reactions import reactions_bp

app.register_blueprint(reactions_bp)

SITE_URL = SITE_CONFIG['site_url'].rstrip('/')
GCS_PREFIX = SITE_CONFIG['project_name']
SUPPORTED_LANGS = {'en', 'ko'}
LANG_SUFFIXES = ('en', 'ko')


def _split_lang_id(item_id: str):
    """Split `tourapi_clinic_zh_tw` → (`tourapi_clinic`, `zh_tw`)."""
    for suf in LANG_SUFFIXES:
        tail = f"_{suf}"
        if item_id.endswith(tail):
            return item_id[: -len(tail)], suf
    return item_id, "en"


def lang_switch_url(target_lang: str) -> str:
    """Same path as current request, with lang swapped (en omits ?lang=)."""
    path = request.path or '/'
    pairs: list[tuple[str, str]] = []
    if target_lang and target_lang != 'en':
        pairs.append(('lang', target_lang))
    for key in request.args:
        if key == 'lang':
            continue
        for value in request.args.getlist(key):
            pairs.append((key, value))
    if not pairs:
        return path
    return f"{path}?{urllib.parse.urlencode(pairs)}"


@app.context_processor
def _inject_lang_switch():
    return {'lang_switch_url': lang_switch_url}


@app.context_processor
def _inject_family_sites():
    # JPFun: no "family sites" strip — journey next-steps are passed per view instead.
    lang = request.args.get('lang', 'en')
    if lang not in SUPPORTED_LANGS:
        lang = 'en'
    return {
        'family_sites': [],
        'family_section_title': '',
        'family_lang': lang,
        'cross_site_links': [],
    }


# ==========================================
# Paths
# ==========================================
BASE_DIR    = app.root_path
STATIC_DIR  = os.path.join(BASE_DIR, 'static')
IMAGES_DIR  = os.path.join(STATIC_DIR, 'images')
DATA_FILE   = os.path.join(STATIC_DIR, 'json', 'items_data.json')
NEARBY_FILE = os.path.join(STATIC_DIR, 'json', 'nearby_pois.json')
CONTENT_DIR = os.path.join(BASE_DIR, 'content')
GUIDE_DIR   = os.path.join(CONTENT_DIR, 'guides')

GUIDE_IMAGES = SITE_CONFIG['guide_images']

# Hub art used when an activity pool is thin.
_HUB_GUIDE_IMAGES = {
    "ski": "/static/images/hub/ski.jpg",
    "dive": "/static/images/hub/dive.jpg",
    "surf": "/static/images/hub/surf.jpg",
    "camp": "/static/images/hub/camp.jpg",
}
_GUIDE_ACTIVITY_KEYS = ("ski", "dive", "surf", "camp")


def _is_usable_static_image(filename: str) -> bool:
    name = (filename or "").strip().lstrip("/")
    if name.startswith("static/images/"):
        name = name[len("static/images/") :]
    if not name or name in ("default.jpg", "default.png", "logo.png", "og_image.png"):
        return False
    if name.startswith("hub/"):
        path = os.path.join(IMAGES_DIR, name)
    else:
        path = os.path.join(IMAGES_DIR, os.path.basename(name))
    try:
        return os.path.isfile(path) and os.path.getsize(path) > 5000
    except OSError:
        return False


def _static_image_url(filename: str) -> str:
    name = (filename or "").strip().lstrip("/")
    if name.startswith("static/images/"):
        return "/" + name
    if name.startswith("hub/"):
        return f"/static/images/{name}"
    return f"/static/images/{os.path.basename(name)}"


def _build_guide_image_pools() -> dict[str, list[str]]:
    """Local ski/dive/surf/camp photos for guide cards (no remote Unsplash)."""
    pools: dict[str, list[str]] = {k: [] for k in _GUIDE_ACTIVITY_KEYS}
    seen: dict[str, set[str]] = {k: set() for k in _GUIDE_ACTIVITY_KEYS}

    def _add(act: str, url: str) -> None:
        if act not in pools or not url or url in seen[act]:
            return
        fname = url.split("/")[-1] if "/hub/" not in url else "hub/" + url.split("/")[-1]
        if "/hub/" in url:
            check = "hub/" + url.split("/")[-1]
        else:
            check = url.split("/")[-1]
        if not _is_usable_static_image(check):
            return
        pools[act].append(url)
        seen[act].add(url)

    # Item thumbnails from built JSON (preferred variety).
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            for item in data.get(SITE_CONFIG["data_key"], []) or []:
                if item.get("lang") and item.get("lang") != "en":
                    continue
                act = str(item.get("activity") or "").strip().lower()
                if act == "scuba":
                    act = "dive"
                if act not in pools:
                    continue
                thumb = str(item.get("thumbnail") or "").strip()
                item_id = str(item.get("id") or "")
                base = item_id
                for suf in ("_en", "_ko"):
                    if base.endswith(suf):
                        base = base[: -len(suf)]
                        break
                # Prefer real local file even when JSON still points at default.jpg
                local_name = f"{base}.jpg"
                if _is_usable_static_image(local_name):
                    _add(act, _static_image_url(local_name))
                elif thumb.startswith("/static/images/") and not thumb.endswith("default.jpg"):
                    _add(act, thumb)
    except Exception:
        pass

    # Hub fallbacks always available.
    for act, hub in _HUB_GUIDE_IMAGES.items():
        _add(act, hub)

    # Ensure non-empty pools.
    default = "/static/images/default.jpg"
    for act in _GUIDE_ACTIVITY_KEYS:
        if not pools[act]:
            pools[act] = [hub for hub in [_HUB_GUIDE_IMAGES.get(act), default] if hub]
    return pools


def _infer_guide_thumb_activities(base_id: str, activity: str, title: str, summary: str) -> list[str]:
    """Which activity image pools a guide card should draw from."""
    text = f"{base_id} {activity} {title} {summary}".lower()
    hits: list[str] = []
    rules = (
        ("ski", ("ski", "powder", "hakuba", "niseko", "yuzawa", "snow")),
        ("dive", ("dive", "scuba", "manta", "kerama", "ishigaki", "okinawa")),
        ("surf", ("surf", "shonan", "chiba", "wave", "swell")),
        ("camp", ("camp", "fuji", "motosu", "shimanami", "glamping", "tent")),
    )
    for key, needles in rules:
        if any(n in text for n in needles):
            hits.append(key)
    act = (activity or "").strip().lower()
    if act in _GUIDE_ACTIVITY_KEYS and act not in hits:
        hits.insert(0, act)
    if act in ("scuba",) and "dive" not in hits:
        hits.insert(0, "dive")
    # Leisure / generic hub guides: rotate across all activities.
    if not hits or act in ("leisure", "route", ""):
        if not hits:
            return list(_GUIDE_ACTIVITY_KEYS)
        # Keep specific hits but allow multi-activity leisure pages to mix.
        if act == "leisure":
            for key in _GUIDE_ACTIVITY_KEYS:
                if key not in hits:
                    hits.append(key)
    return hits or list(_GUIDE_ACTIVITY_KEYS)


_CACHED_GUIDE_IMAGE_POOLS: dict[str, list[str]] | None = None


def _guide_image_pools() -> dict[str, list[str]]:
    global _CACHED_GUIDE_IMAGE_POOLS
    if _CACHED_GUIDE_IMAGE_POOLS is None:
        _CACHED_GUIDE_IMAGE_POOLS = _build_guide_image_pools()
    return _CACHED_GUIDE_IMAGE_POOLS


def _invalidate_guide_image_pools() -> None:
    global _CACHED_GUIDE_IMAGE_POOLS
    _CACHED_GUIDE_IMAGE_POOLS = None


def _pick_guide_thumbnail(
    base_id: str,
    activities: list[str],
    pools: dict[str, list[str]],
    *,
    avoid: str | None = None,
    stable: bool = True,
) -> str:
    """Pick from activity pools. stable=True is hash-based (OG); False is per-request random."""
    acts = [a for a in activities if pools.get(a)] or list(_GUIDE_ACTIVITY_KEYS)
    # For multi-activity (leisure) guides, pick an activity first so ski photos
    # don't drown out dive/surf/camp when pools are unequal in size.
    if len(acts) > 1:
        if stable:
            act = acts[int(hashlib.md5(f"{base_id}:act".encode()).hexdigest(), 16) % len(acts)]
        else:
            act = random.choice(acts)
        pool = list(pools.get(act) or [])
        if not pool:
            pool = [u for a in acts for u in (pools.get(a) or [])]
    else:
        pool = list(pools.get(acts[0]) or [])
        if not pool:
            pool = [u for a in _GUIDE_ACTIVITY_KEYS for u in (pools.get(a) or [])]

    # de-dupe preserve order
    seen: set[str] = set()
    uniq: list[str] = []
    for url in pool:
        if url not in seen:
            seen.add(url)
            uniq.append(url)
    if not uniq:
        return GUIDE_IMAGES[0] if GUIDE_IMAGES else "/static/images/default.jpg"
    if avoid and len(uniq) > 1:
        uniq = [u for u in uniq if u != avoid] or uniq
    if stable:
        idx = int(hashlib.md5(base_id.encode()).hexdigest(), 16) % len(uniq)
        return uniq[idx]
    return random.choice(uniq)


def _with_random_thumbnails(guides: list) -> list:
    """Copy guide rows and assign a fresh random thumbnail for this request."""
    pools = _guide_image_pools()
    last_img = None
    out = []
    for g in guides:
        row = dict(g)
        gid = str(row.get("id") or "")
        base_id, _ = _split_lang_id(gid)
        acts = _infer_guide_thumb_activities(
            base_id,
            row.get("activity") or "",
            row.get("title") or "",
            row.get("summary") or "",
        )
        picked = _pick_guide_thumbnail(
            base_id, acts, pools, avoid=last_img, stable=False
        )
        row["thumbnail"] = picked
        last_img = picked
        out.append(row)
    return out


def get_mapped_image(base_id):
    pools = _guide_image_pools()
    acts = _infer_guide_thumb_activities(base_id, "", base_id, "")
    return _pick_guide_thumbnail(base_id, acts, pools, stable=True)


def _gcs_image_url(filename):
    return f"https://storage.googleapis.com/ok-project-assets/{GCS_PREFIX}/{filename}"


def _social_image_url(base_id):
    safe = re.sub(r"[^a-z0-9_-]", "", base_id.lower())
    return f"{SITE_URL}/social/{safe}.jpg"


def _og_image_context(base_id):
    return {
        "og_image_abs": _social_image_url(base_id),
        "og_image_width": 1200,
        "og_image_height": 630,
    }


def _card_path(kind, base_id, lang):
    path = f"/card/{kind}/{base_id}"
    if lang == 'ko':
        path += '?lang=ko'
    return path


def _share_context(slug, title, lang, page_path, base_id, kind):
    share_url = f"{SITE_URL}{page_path}"
    share_url_x = f"{SITE_URL}{_card_path(kind, base_id, lang)}"
    site_name = SITE_CONFIG['site_name']
    if lang == 'ko':
        share_tweet = f"{title} — {site_name}"
    else:
        share_tweet = f"{title} — Care guide on {site_name}"
    return {
        "share_id": slug,
        "share_url": share_url,
        "share_url_x": share_url_x,
        "share_tweet": share_tweet,
        "share_lang": lang,
        "og_page_url": share_url,
        "linkedin_inspector_url": f"https://www.linkedin.com/post-inspector/inspect/{quote(share_url, safe='')}",
    }


def _jpeg_bytes(img):
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=78, optimize=True, progressive=True)
    return buf.getvalue()


_PLAN_SECTION_TITLES = frozenset({
    "Listed details",
    "Before you book",
    "Visit checklist",
    "Getting there",
    "Nearby stay & food",
})


def _split_md_h2_sections(md_text: str) -> list[tuple[str, str]]:
    """Split markdown into [(heading_or_'', body), ...] by ## headings."""
    text = (md_text or "").strip()
    if not text:
        return []
    parts = re.split(r"(?m)^(## .+)$", text)
    out: list[tuple[str, str]] = []
    if parts and parts[0].strip():
        out.append(("", parts[0].strip()))
    i = 1
    while i < len(parts) - 1:
        heading = parts[i].lstrip("#").strip()
        body = parts[i + 1].strip()
        out.append((heading, body))
        i += 2
    return out


def _parse_md_link(text: str) -> tuple[str, str]:
    m = re.search(r"\[([^\]]+)\]\(([^)]+)\)", text or "")
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return (text or "").strip(), ""


def _format_inline_html(text: str) -> str:
    """Escape text; keep **bold** and bare http(s) links."""
    import html as html_mod

    raw = text or ""
    parts = re.split(r"(\*\*[^*]+\*\*|https?://[^\s<]+)", raw)
    out: list[str] = []
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            out.append(f"<strong>{html_mod.escape(part[2:-2])}</strong>")
        elif part.startswith("http://") or part.startswith("https://"):
            href = html_mod.escape(part.rstrip(".,);"))
            out.append(
                f'<a href="{href}" target="_blank" rel="noopener noreferrer">{href}</a>'
            )
        else:
            out.append(html_mod.escape(part))
    return "".join(out)


def _is_empty_display(value: str) -> bool:
    v = (value or "").strip()
    if not v:
        return True
    low = v.lower()
    markers = (
        "not in public listing",
        "confirm with clinic",
        "ask the clinic",
        "공개정보なし",
        "公開情報なし",
        "公开信息未收录",
        "公開資訊未收錄",
        "클리닉에 문의",
        "クリニックへ確認",
        "请向诊所确认",
        "請向診所確認",
        "데이터 없음",
    )
    return any(m in low or m in v for m in markers)


def _parse_labeled_rows(body: str) -> list[dict]:
    rows = []
    for line in body.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("- "):
            s = s[2:].strip()
        m = re.match(r"\*\*([^*]+)\*\*\s*:?\s*(.*)$", s)
        if m:
            label = m.group(1).strip().rstrip(":")
            value = m.group(2).strip()
            empty = _is_empty_display(value)
            href = ""
            if not empty:
                if value.startswith("http://") or value.startswith("https://"):
                    href = value
                elif value.startswith("+") or re.match(r"^\d[\d\-\s]+$", value):
                    href = "tel:" + re.sub(r"[\s\-]", "", value)
            rows.append({
                "label": label,
                "text": value,
                "text_html": _format_inline_html(value),
                "href": href,
                "empty": empty,
            })
        else:
            rows.append({
                "label": "",
                "text": s,
                "text_html": _format_inline_html(s),
                "href": "",
                "empty": _is_empty_display(s),
            })
    return rows


def _extract_clinic_plan(md_text: str) -> tuple[str, dict]:
    """Pull structured ## sections into cards; return remnant markdown."""
    sections = _split_md_h2_sections(md_text)
    if not sections:
        return md_text or "", {}

    remnant_parts: list[str] = []
    plan: dict = {}

    for heading, body in sections:
        key = heading.strip()
        if key not in _PLAN_SECTION_TITLES:
            if heading:
                remnant_parts.append(f"## {heading}\n\n{body}".strip())
            elif body:
                remnant_parts.append(body)
            continue

        if key == "Listed details":
            plan["listed"] = {"title": key, "rows": _parse_labeled_rows(body)}

        elif key == "Before you book":
            paras: list[str] = []
            asks: list[str] = []
            for line in body.splitlines():
                s = line.strip()
                if not s:
                    continue
                if s.startswith("- "):
                    asks.append(s[2:].strip())
                else:
                    paras.append(s)
            # Drop the short prompt line that only introduces the list (keep as heading hint)
            prompt = ""
            body_paras = []
            for p in paras:
                low = p.lower()
                if asks and (
                    p.rstrip(":").endswith("about")
                    or "문의" in p
                    or "確認" in p
                    or "确认" in p
                    or "確認：" in p
                    or p.rstrip(":").endswith("：")
                    or "directly about" in low
                    or "ご確認" in p
                ) and len(p) < 80:
                    prompt = p.rstrip(":")
                else:
                    body_paras.append(p)
            plan["before"] = {
                "title": key,
                "paras_html": [_format_inline_html(p) for p in body_paras],
                "prompt": prompt or "",
                "asks": asks,
            }

        elif key == "Visit checklist":
            items = []
            intro = ""
            notes = []
            for line in body.splitlines():
                s = line.strip()
                if not s:
                    continue
                m = re.match(r"^- \[[ xX]?\]\s+(.*)$", s)
                if m:
                    items.append(m.group(1).strip())
                    continue
                if not items and not intro:
                    intro = s
                else:
                    notes.append(s)
            plan["checklist"] = {
                "title": key,
                "intro": intro,
                "checks": items,
                "note": " ".join(notes).strip(),
            }

        elif key == "Getting there":
            plan["getting"] = {"title": key, "rows": _parse_labeled_rows(body)}

        elif key == "Nearby stay & food":
            intro_lines = []
            places = []
            for line in body.splitlines():
                s = line.strip()
                if not s:
                    continue
                if not s.startswith("- "):
                    intro_lines.append(s)
                    continue
                s = s[2:].strip()
                meta = ""
                rest = s
                hm = re.match(r"\*\*([^*]+)\*\*\s*:?\s*(.*)$", s)
                if hm:
                    meta = hm.group(1).strip().rstrip(":")
                    rest = hm.group(2).strip()
                name, href = _parse_md_link(rest)
                tip = ""
                if ")" in rest:
                    after = rest.split(")", 1)[-1].strip()
                    if after.startswith("—") or after.startswith("–") or after.startswith("-"):
                        tip = after.lstrip("—–- ").strip()
                kind = meta.split("·")[0].strip() if meta else "Place"
                places.append({
                    "kind": kind,
                    "meta": meta,
                    "name": name,
                    "href": href,
                    "tip": tip,
                })
            intro_text = " ".join(intro_lines)
            map_href = ""
            map_label = ""
            lm = re.search(r"\[([^\]]+)\]\(([^)]+)\)", intro_text)
            if lm:
                map_label, map_href = lm.group(1), lm.group(2)
                intro_text = re.sub(r"\[[^\]]+\]\([^)]+\)", map_label, intro_text)
            plan["nearby"] = {
                "title": key,
                "intro": intro_text.strip(),
                "map_href": map_href,
                "map_label": map_label,
                "places": places,
            }

    return "\n\n".join(remnant_parts).strip(), plan


def _resolve_item_id(base_id, lang):
    candidate = f"{base_id}_{lang}"
    if os.path.exists(os.path.join(CONTENT_DIR, f"{candidate}.md")):
        return candidate
    fallback = f"{base_id}_en"
    if os.path.exists(os.path.join(CONTENT_DIR, f"{fallback}.md")):
        return fallback
    return None

def _resolve_guide_id(base_id, lang):
    candidate = f"{base_id}_{lang}"
    if os.path.exists(os.path.join(GUIDE_DIR, f"{candidate}.md")):
        return candidate
    fallback = f"{base_id}_en"
    if os.path.exists(os.path.join(GUIDE_DIR, f"{fallback}.md")):
        return fallback
    return None


def _social_source_url(base_id):
    if os.path.exists(os.path.join(GUIDE_DIR, f"{base_id}_en.md")) or os.path.exists(os.path.join(GUIDE_DIR, f"{base_id}_ko.md")):
        return get_mapped_image(base_id)
    return _gcs_image_url(f"{base_id}.jpg")


def _fetch_remote_image(url):
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            raw = resp.read()
            if raw:
                return raw
    except Exception:
        pass
    return None

# ==========================================
# Data loading (startup cache)
# ==========================================
CACHED_DATA   = {SITE_CONFIG['data_key']: [], "last_updated": ""}
CACHED_GUIDES = {lang: [] for lang in ('en', 'ko')}


def _guides_for(lang: str, activity: str | None = None) -> list:
    """Filter cached guides. activity='leisure'|'route' for hub; 'ski'|'dive'|... for maps."""
    rows = CACHED_GUIDES.get(lang) or CACHED_GUIDES.get('en') or []
    if activity:
        key = activity.strip().lower()
        rows = [g for g in rows if (g.get('activity') or '') == key]
    else:
        rows = list(rows)
    return _with_random_thumbnails(rows)


CACHED_NEARBY = {"anchor": {}, "pois": [], "last_updated": ""}


def load_items():
    global CACHED_DATA
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                CACHED_DATA = json.load(f)
            try:
                from .region import enrich_items_with_regions
            except ImportError:
                from region import enrich_items_with_regions
            enrich_items_with_regions(CACHED_DATA.get(SITE_CONFIG['data_key'], []))
            _invalidate_guide_image_pools()
            print(f"✅ Data loaded: {len(CACHED_DATA.get(SITE_CONFIG['data_key'], []))} items")
        except Exception as e:
            print(f"❌ Data load error: {e}")


def load_nearby():
    """Stay/Food POIs near clinics — API-style cards, no detail markdown pages."""
    global CACHED_NEARBY
    if not os.path.exists(NEARBY_FILE):
        print("⚠️  nearby_pois.json not found")
        return
    try:
        with open(NEARBY_FILE, 'r', encoding='utf-8') as f:
            raw = json.load(f)
        if isinstance(raw, list):
            CACHED_NEARBY = {"anchor": {}, "pois": raw, "last_updated": ""}
        elif isinstance(raw, dict):
            pois = raw.get('pois')
            if not isinstance(pois, list):
                pois = []
            CACHED_NEARBY = {
                "anchor": raw.get('anchor') or {},
                "pois": pois,
                "last_updated": raw.get('last_updated') or '',
            }
        else:
            CACHED_NEARBY = {"anchor": {}, "pois": [], "last_updated": ""}
        print(f"✅ Nearby POIs loaded: {len(CACHED_NEARBY.get('pois', []))} places")
    except Exception as e:
        print(f"❌ Nearby load error: {e}")


def _nearby_for_lang(lang: str) -> list[dict]:
    if lang not in SUPPORTED_LANGS:
        lang = 'en'
    out = []
    for poi in CACHED_NEARBY.get('pois', []):
        i18n = (poi.get('i18n') or {})
        loc = i18n.get(lang) or i18n.get('en') or {}
        kind = str(poi.get('kind') or 'Stay')
        out.append({
            "id": poi.get('id'),
            "kind": kind,
            "categories": [kind],
            "lat": poi.get('lat'),
            "lng": poi.get('lng'),
            "thumbnail": poi.get('thumbnail') or '/static/images/default.jpg',
            "tel": (poi.get('tel') or '').strip(),
            "website": (poi.get('website') or '').strip(),
            "source": poi.get('source') or 'nearby',
            "near_clinics": list(poi.get('near_clinics') or poi.get('near_resorts') or []),
            "near_resorts": list(poi.get('near_resorts') or poi.get('near_clinics') or []),
            "region": poi.get('region') or '',
            "title": loc.get('title') or poi.get('id'),
            "address": loc.get('address') or '',
            "overview": loc.get('overview') or '',
            "subtype": loc.get('subtype') or '',
            "hours": loc.get('hours') or '',
            "parking": loc.get('parking') or '',
            "transit": loc.get('transit') or '',
            "tips": loc.get('tips') or '',
            "link": None,
            "is_nearby": True,
        })
    return out


def load_guides():
    global CACHED_GUIDES
    _invalidate_guide_image_pools()
    if not os.path.exists(GUIDE_DIR):
        return

    all_raw = []
    for fpath in glob.glob(os.path.join(GUIDE_DIR, '*.md')):
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                raw = f.read().strip()
            raw = _clean_md(raw)
            post = frontmatter.loads(raw)
            full_id = os.path.basename(fpath).replace('.md', '')
            base_id, lang_from_id = _split_lang_id(full_id)
            lang = str(post.get('lang') or lang_from_id or 'en')
            if lang not in SUPPORTED_LANGS:
                lang = 'en'
            all_raw.append({
                'base_id': base_id,
                'lang': lang,
                'full_id': full_id,
                'title': str(post.get('title', 'Guide')),
                'summary': str(post.get('summary', '')),
                'date': str(post.get('date', '2026-01-01')),
                'activity': str(post.get('activity', '')).strip().lower(),
                'emoji': str(post.get('emoji', '')).strip(),
            })
        except Exception:
            continue

    # Prefer EN order for shared thumbnails; fall back to any lang
    ref = sorted(
        [g for g in all_raw if g['lang'] == 'en'] or all_raw,
        key=lambda x: x['date'],
        reverse=True,
    )
    pools = _guide_image_pools()
    last_img = None
    id_to_img = {}
    for g in ref:
        if g['base_id'] in id_to_img:
            continue
        acts = _infer_guide_thumb_activities(
            g['base_id'], g.get('activity') or '', g.get('title') or '', g.get('summary') or ''
        )
        picked = _pick_guide_thumbnail(g['base_id'], acts, pools, avoid=last_img, stable=True)
        id_to_img[g['base_id']] = picked
        last_img = picked

    fallback = (
        _HUB_GUIDE_IMAGES.get("ski")
        or (GUIDE_IMAGES[0] if GUIDE_IMAGES else "/static/images/default.jpg")
    )
    new_guides = {lang: [] for lang in SUPPORTED_LANGS}
    for g in all_raw:
        new_guides.setdefault(g['lang'], []).append({
            'id': g['full_id'],
            'title': g['title'],
            'summary': g['summary'],
            'thumbnail': id_to_img.get(g['base_id'], fallback),
            'published': g['date'],
            'activity': g.get('activity') or '',
            'emoji': g.get('emoji') or '',
        })
    for lang in new_guides:
        new_guides[lang].sort(key=lambda x: x['published'], reverse=True)

    CACHED_GUIDES = new_guides
    total = sum(len(v) for v in new_guides.values())
    print(f"✅ Guides loaded: {total}")

def _clean_md(text):
    """Clean common AI output artifacts from markdown."""
    text = re.sub(r'^```[a-z]*\n', '', text)
    text = re.sub(r'\n```$', '', text)
    text = re.sub(r'^(##\s*)?yaml\n', '', text, flags=re.IGNORECASE)
    if '---' in text and not text.startswith('---'):
        text = '---' + text.split('---', 1)[1]
    return text.strip()


_LIST_LINE_RE = re.compile(r'^(\s*)([*+-]|\d+\.)\s+\S')


def _normalize_md_lists(text: str) -> str:
    """Insert blank lines before list blocks so Python-Markdown parses them as lists.

    Gemini (and similar) often writes `paragraph\\n* item` without the blank line
    Markdown requires; without it, markers stay inside a single <p>.
    """
    if not text:
        return text
    lines = text.split('\n')
    out = []
    in_fence = False
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('```'):
            in_fence = not in_fence
            out.append(line)
            continue
        if (
            not in_fence
            and _LIST_LINE_RE.match(line)
            and out
            and out[-1].strip()
            and not _LIST_LINE_RE.match(out[-1])
        ):
            out.append('')
        out.append(line)
    return '\n'.join(out)


def _md_to_html(text: str, extensions=None) -> str:
    """Convert markdown to HTML with list-friendly normalization."""
    if not text:
        return ''
    if extensions is None:
        extensions = ['tables', 'fenced_code']
    return markdown.markdown(_normalize_md_lists(text), extensions=extensions)

def _get_footer_stats(lang):
    items = CACHED_DATA.get(SITE_CONFIG['data_key'], [])
    count = len([i for i in items if i.get('lang') == lang])
    return {
        'total_items':   count if count > 0 else len(items) // 2,
        'last_updated':  CACHED_DATA.get('last_updated', ''),
        'site':          SITE_CONFIG
    }


def _absolute_url(path_or_url):
    if not path_or_url:
        return ""
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        return path_or_url
    return f"{SITE_CONFIG['site_url'].rstrip('/')}/{path_or_url.lstrip('/')}"

# Initial startup load
load_items()
load_nearby()
load_guides()

# ==========================================
# Category mapping
# ==========================================
CATEGORY_MAPPING = SITE_CONFIG.get('category_mapping', {})

# ==========================================
# Routes
# ==========================================
def _item_activity(item: dict) -> str:
    raw = str(item.get("activity") or "").strip().lower()
    if raw in ("ski", "surf", "dive", "camp"):
        return raw
    for c in item.get("categories") or []:
        s = str(c).strip().lower()
        if "ski" in s:
            return "ski"
        if "surf" in s:
            return "surf"
        if "dive" in s or "scuba" in s:
            return "dive"
        if "camp" in s:
            return "camp"
    return ""


def _items_for_lang(lang: str) -> list:
    items = CACHED_DATA.get(SITE_CONFIG["data_key"], [])
    filtered = [i for i in items if i.get("lang") == lang]
    if not filtered:
        filtered = [i for i in items if i.get("lang") == "en"]
    return filtered


def _filter_items(lang: str, activity: str | None = None, region: str = "all") -> list:
    try:
        from .region import matches_region_filter, parse_region
    except ImportError:
        from region import matches_region_filter, parse_region

    out = []
    for item in _items_for_lang(lang):
        if activity and _item_activity(item) != activity:
            continue
        reg = item.get("region") or parse_region(
            item.get("address"), item.get("lat"), item.get("lng"), explicit=item.get("region")
        )
        if isinstance(reg, str):
            reg = {"sido": reg, "district": None}
        if not matches_region_filter(reg, region):
            continue
        row = dict(item)
        row["region"] = reg
        row["activity"] = _item_activity(item)
        out.append(row)
    return out


@app.route("/")
def index():
    try:
        from .activities import hub_cards, hub_lp_cards, season_banner, ACTIVITIES
    except ImportError:
        from activities import hub_cards, hub_lp_cards, season_banner, ACTIVITIES

    lang = request.args.get("lang", "en")
    if lang not in SUPPORTED_LANGS:
        lang = "en"

    all_items = _items_for_lang(lang)
    activity_counts = {a: 0 for a in ACTIVITIES}
    for item in all_items:
        act = _item_activity(item)
        if act in activity_counts:
            activity_counts[act] += 1

    stats = _get_footer_stats(lang)
    canonical = SITE_CONFIG["site_url"] if lang == "en" else f"{SITE_CONFIG['site_url']}?lang={lang}"
    hub_guides = _guides_for(lang, "leisure")
    route_guides = _guides_for(lang, "route")
    return render_template(
        "index.html",
        lang=lang,
        guides=CACHED_GUIDES,
        hub_guides=hub_guides,
        route_guides=route_guides,
        hero_slides=hub_cards(lang),
        activity_cards=hub_lp_cards(lang),
        activity_counts=activity_counts,
        season=season_banner(lang),
        canonical=canonical,
        **stats,
    )


@app.route("/scuba")
@app.route("/scuba/<region>")
def scuba_alias(region: str = "all"):
    lang = request.args.get("lang", "en")
    target = f"/dive/{region}" if region and region != "all" else "/dive"
    if lang != "en":
        target += f"?lang={lang}"
    return redirect(target, code=301)


@app.route("/ski")
@app.route("/ski/<region>")
@app.route("/surf")
@app.route("/surf/<region>")
@app.route("/dive")
@app.route("/dive/<region>")
@app.route("/camp")
@app.route("/camp/<region>")
def activity_map(region: str = "all"):
    try:
        from .activities import (
            ACTIVITY_META,
            REGION_LABELS_EN,
            activity_path,
            hub_cards,
            is_activity,
            normalize_region,
            regions_for,
        )
    except ImportError:
        from activities import (
            ACTIVITY_META,
            REGION_LABELS_EN,
            activity_path,
            hub_cards,
            is_activity,
            normalize_region,
            regions_for,
        )

    activity = request.path.strip("/").split("/")[0].lower()
    if not is_activity(activity):
        abort(404)

    lang = request.args.get("lang", "en")
    if lang not in SUPPORTED_LANGS:
        lang = "en"

    region = normalize_region(activity, region)
    # Canonicalize unknown region → /activity
    path_region = request.view_args.get("region") if request.view_args else None
    if path_region and path_region != region and region == "all":
        return redirect(activity_path(activity, "all", lang), code=302)

    meta = ACTIVITY_META[activity]
    activity_label = meta["label_ko"] if lang == "ko" else meta["label_en"]
    region_label = (
        next((r["label"] for r in regions_for(activity, lang) if r["key"] == region), region)
    )
    if lang == "ko":
        page_heading = meta["title_ko"] if region == "all" else f"{region_label} {activity_label}"
        page_description = meta["desc_ko"]
        page_title = page_heading
    else:
        page_heading = meta["title_en"] if region == "all" else f"{REGION_LABELS_EN.get(region, region)} {meta['label_en']}"
        page_description = meta["desc_en"]
        page_title = page_heading

    items = _filter_items(lang, activity=activity, region=region)
    items = sorted(items, key=lambda x: str(x.get("published") or ""), reverse=True)

    stats = _get_footer_stats(lang)
    path = activity_path(activity, region, "en")
    path_ko = activity_path(activity, region, "ko")
    base = SITE_CONFIG["site_url"].rstrip("/")
    canonical = f"{base}{path}" if lang == "en" else f"{base}{path_ko}"
    maps_lang = {"en": "en", "ko": "ko"}.get(lang, "en")

    return render_template(
        "activity.html",
        lang=lang,
        activity=activity,
        region=region,
        activity_meta=meta,
        activity_label=activity_label,
        region_label=region_label,
        region_buttons=regions_for(activity, lang),
        hub_nav=hub_cards(lang),
        initial_items=items[:48],
        page_title=page_title,
        page_heading=page_heading,
        page_description=page_description,
        canonical=canonical,
        hreflang_en=f"{base}{path}",
        hreflang_ko=f"{base}{path_ko}",
        maps_lang=maps_lang,
        activity_guides=_guides_for(lang, activity),
        **stats,
    )


@app.route("/api/items")
def api_items():
    lang = request.args.get("lang", "en")
    if lang not in SUPPORTED_LANGS:
        lang = "en"
    activity = (request.args.get("activity") or "").strip().lower() or None
    region = (request.args.get("region") or "all").strip().lower()

    try:
        from .activities import is_activity
    except ImportError:
        from activities import is_activity

    if activity and not is_activity(activity):
        activity = None

    filtered = _filter_items(lang, activity=activity, region=region if activity else "all")
    if not activity and region and region != "all":
        filtered = _filter_items(lang, activity=None, region=region)

    spoofed = []
    for item in filtered:
        s = copy.deepcopy(item)
        s["lang"] = lang
        new_cats = [CATEGORY_MAPPING.get(c.strip(), c.strip()) for c in s.get("categories", [])]
        s["categories"] = list(set(new_cats))
        spoofed.append(s)

    return jsonify(
        {
            SITE_CONFIG["data_key"]: spoofed,
            "last_updated": CACHED_DATA.get("last_updated"),
            "activity": activity or "all",
            "region": region,
        }
    )


@app.route("/api/nearby")
def api_nearby():
    """Stay/Food POIs for map pins — resolved for UI language, no detail pages."""
    lang = request.args.get("lang", "en")
    if lang not in SUPPORTED_LANGS:
        lang = "en"
    pois = _nearby_for_lang(lang)
    return jsonify({
        "anchor": CACHED_NEARBY.get("anchor") or {},
        "pois": pois,
        "last_updated": CACHED_NEARBY.get("last_updated") or "",
        "counts": {
            "stay": sum(1 for p in pois if p.get("kind") == "Stay"),
            "food": sum(1 for p in pois if p.get("kind") == "Food"),
            "all": len(pois),
        },
    })


@app.route('/guide')
def guide_list():
    lang = request.args.get('lang', 'en')
    if lang not in SUPPORTED_LANGS:
        lang = 'en'
    stats = _get_footer_stats(lang)
    guide_rows = _guides_for(lang)
    canonical = f"{SITE_CONFIG['site_url']}/guide" if lang == 'en' else f"{SITE_CONFIG['site_url']}/guide?lang={lang}"
    return render_template(
        'guide_list.html',
        guides=CACHED_GUIDES,
        guide_rows=guide_rows,
        lang=lang,
        canonical=canonical,
        **stats,
    )


@app.route('/resorts')
@app.route('/clinics')
def resort_list():
    """Directory of all leisure spots (optional activity query)."""
    lang = request.args.get('lang', 'en')
    if lang not in SUPPORTED_LANGS:
        lang = 'en'
    activity = (request.args.get('activity') or '').strip().lower() or None
    region = (request.args.get('region') or request.args.get('sido') or 'all').strip().lower()
    try:
        page = max(1, int(request.args.get('page', 1)))
    except ValueError:
        page = 1
    per_page = 24

    try:
        from .activities import ACTIVITY_META, is_activity, regions_for
    except ImportError:
        from activities import ACTIVITY_META, is_activity, regions_for

    if activity and not is_activity(activity):
        activity = None

    filtered = _filter_items(lang, activity=activity, region=region)
    filtered.sort(key=lambda x: str(x.get('title') or ''))
    total = len(filtered)
    pages = max(1, (total + per_page - 1) // per_page)
    page = min(page, pages)
    start = (page - 1) * per_page
    page_items = filtered[start:start + per_page]

    base_items = _filter_items(lang, activity=activity, region='all')
    region_counts = {'all': len(base_items)}
    region_keys = [r['key'] for r in regions_for(activity or 'ski', lang) if r['key'] != 'all']
    if not activity:
        region_keys = ['hokkaido', 'nagano', 'niigata', 'tohoku', 'kanto', 'chubu', 'chugoku', 'okinawa', 'other']
    for key in region_keys:
        region_counts[key] = sum(
            1 for i in base_items
            if (i.get('region') or {}).get('sido') == key
        )

    filter_buttons = [{'label': 'All', 'theme': 'all', 'count_id': 'count-region-all'}]
    for key in region_keys:
        filter_buttons.append({
            'label': key.title(),
            'theme': key,
            'count_id': f'count-region-{key}',
        })

    stats = _get_footer_stats(lang)
    qs_base = f"/resorts?lang={lang}" if lang != 'en' else "/resorts"
    canonical = f"{SITE_CONFIG['site_url']}{qs_base}"
    if activity:
        canonical += f"{'&' if lang != 'en' else '?'}activity={activity}"
    if region != 'all':
        sep = '&' if ('?' in canonical.split(SITE_CONFIG['site_url'], 1)[-1]) else '?'
        # simpler:
        canonical = f"{SITE_CONFIG['site_url']}/resorts"
        parts = []
        if lang != 'en':
            parts.append(f'lang={lang}')
        if activity:
            parts.append(f'activity={activity}')
        if region != 'all':
            parts.append(f'region={region}')
        if parts:
            canonical += '?' + '&'.join(parts)

    return render_template(
        'resorts.html',
        lang=lang,
        resorts=page_items,
        clinics=page_items,
        total=total,
        page=page,
        pages=pages,
        region=region,
        sido=region,
        region_counts=region_counts,
        sido_counts=region_counts,
        filter_buttons=filter_buttons,
        canonical=canonical,
        **stats,
    )


@app.route('/guide/<guide_id>')
def guide_detail(guide_id):
    path = os.path.join(GUIDE_DIR, f"{guide_id}.md")
    if not os.path.exists(path):
        lang_q = request.args.get('lang', 'en')
        return redirect(f"/guide?lang={lang_q}" if lang_q != 'en' else '/guide')

    with open(path, 'r', encoding='utf-8') as f:
        raw = _clean_md(f.read())
    post  = frontmatter.loads(raw)
    post['id'] = guide_id
    body  = re.sub(r'---.*?---', '', post.content, flags=re.DOTALL)
    body  = body.replace('```markdown', '').replace('```', '').strip()

    title   = str(post.get('title') or guide_id)
    lang    = str(post.get('lang', 'en'))
    base_id, _ = _split_lang_id(guide_id)
    image   = _pick_guide_thumbnail(
        base_id,
        _infer_guide_thumb_activities(
            base_id,
            str(post.get('activity') or ''),
            title,
            str(post.get('summary') or ''),
        ),
        _guide_image_pools(),
        stable=False,
    )
    stats   = _get_footer_stats(lang)
    alt_en = f"{SITE_CONFIG['site_url']}/guide/{base_id}_en"
    alt_ja = f"{SITE_CONFIG['site_url']}/guide/{base_id}_ja"
    alt_zh = f"{SITE_CONFIG['site_url']}/guide/{base_id}_zh"
    alt_zh_tw = f"{SITE_CONFIG['site_url']}/guide/{base_id}_zh_tw"

    content_html = _md_to_html(body, extensions=['tables', 'toc', 'fenced_code'])
    page_path = f"/guide/{guide_id}"
    share_ctx = _share_context(guide_id, title, lang, page_path, base_id, 'guide')
    return render_template('guide_detail.html',
                           title=title, content=content_html, lang=lang,
                           guide_id=guide_id, base_id=base_id,
                           image_url=image, image_url_abs=_absolute_url(image),
                           canonical=f"{SITE_CONFIG['site_url']}/guide/{guide_id}",
                           alt_en=alt_en, alt_ja=alt_ja, alt_zh=alt_zh, alt_zh_tw=alt_zh_tw,
                           post=post,
                           **_og_image_context(base_id), **share_ctx, **stats)

@app.route('/item/<item_id>')
def item_detail(item_id):
    md_path = os.path.join(CONTENT_DIR, f"{item_id}.md")
    if not os.path.exists(md_path):
        abort(404)

    with open(md_path, 'r', encoding='utf-8') as f:
        raw = _clean_md(f.read())
    post = frontmatter.loads(raw)
    post['id'] = item_id

    if isinstance(post.get('categories'), str):
        post['categories'] = [c.strip() for c in post['categories'].split(',')]

    content_md, plan = _extract_clinic_plan(post.content)
    content_html = _md_to_html(content_md) if content_md else ''
    lang = str(post.get('lang', 'en'))
    base_id, _lang_from_id = _split_lang_id(item_id)
    stats = _get_footer_stats(lang)
    page_path = f"/item/{item_id}"
    share_ctx = _share_context(
        item_id,
        str(post.get('title', item_id)),
        lang,
        page_path,
        base_id,
        'item',
    )
    try:
        from .affiliate import affiliate_context
    except ImportError:
        from affiliate import affiliate_context
    aff = affiliate_context(item_id, lang=lang)
    return render_template(
        'detail.html',
        post=post,
        content=content_html,
        plan=plan,
        base_id=base_id,
        thumbnail_abs=_absolute_url(str(post.get('thumbnail', '/static/images/default.jpg'))),
        **_og_image_context(base_id),
        **share_ctx,
        **stats,
        **aff,
    )


@app.route('/social/<slug>.jpg')
def social_image(slug):
    """Serve thumbnail on-site for OG/Twitter (1200×630 JPEG, no redirect)."""
    safe = re.sub(r"[^a-z0-9_-]", "", slug.lower())
    if not safe:
        abort(404)

    source_urls = [_social_source_url(safe)]
    is_guide = os.path.exists(os.path.join(GUIDE_DIR, f"{safe}_en.md")) or os.path.exists(os.path.join(GUIDE_DIR, f"{safe}_ko.md"))
    if not is_guide:
        source_urls.append(get_mapped_image(safe))

    raw = None
    for source_url in source_urls:
        raw = _fetch_remote_image(source_url)
        if raw:
            break
    if not raw:
        abort(404)

    try:
        from PIL import Image, ImageOps

        img = Image.open(io.BytesIO(raw)).convert("RGB")
        data = _jpeg_bytes(ImageOps.fit(img, (1200, 630), Image.Resampling.LANCZOS))
    except Exception:
        data = raw

    return Response(
        data,
        mimetype="image/jpeg",
        headers={"Cache-Control": "public, max-age=86400"},
    )


@app.route('/card/item/<base_id>')
def item_social_card(base_id):
    lang = request.args.get('lang', 'en').strip().lower()
    if lang not in SUPPORTED_LANGS:
        lang = 'en'
    item_id = _resolve_item_id(base_id, lang)
    if not item_id:
        abort(404)

    md_path = os.path.join(CONTENT_DIR, f"{item_id}.md")
    with open(md_path, 'r', encoding='utf-8') as f:
        post = frontmatter.loads(_clean_md(f.read()))

    title = str(post.get('title', base_id))
    summary = str(post.get('summary', ''))
    page_path = f"/item/{item_id}"
    card_path = _card_path('item', base_id, lang)

    return render_template(
        'social_card.html',
        lang=lang,
        title=title,
        seo_title=f"{title} - {SITE_CONFIG['site_name']}",
        seo_desc=summary,
        site_name=SITE_CONFIG['site_name'],
        page_url=f"{SITE_URL}{page_path}",
        card_url=f"{SITE_URL}{card_path}",
        **_og_image_context(base_id),
    )


@app.route('/card/guide/<base_id>')
def guide_social_card(base_id):
    lang = request.args.get('lang', 'en').strip().lower()
    if lang not in SUPPORTED_LANGS:
        lang = 'en'
    guide_id = _resolve_guide_id(base_id, lang)
    if not guide_id:
        abort(404)

    md_path = os.path.join(GUIDE_DIR, f"{guide_id}.md")
    with open(md_path, 'r', encoding='utf-8') as f:
        post = frontmatter.loads(_clean_md(f.read()))

    title = str(post.get('title', base_id))
    summary = str(post.get('summary', ''))
    page_path = f"/guide/{guide_id}"
    card_path = _card_path('guide', base_id, lang)

    return render_template(
        'social_card.html',
        lang=lang,
        title=title,
        seo_title=f"{title} - {SITE_CONFIG['site_name']} Guide",
        seo_desc=summary,
        site_name=SITE_CONFIG['site_name'],
        page_url=f"{SITE_URL}{page_path}",
        card_url=f"{SITE_URL}{card_path}",
        **_og_image_context(base_id),
    )

# Static assets / SEO
@app.route('/static/images/<path:filename>')
def serve_images(filename):
    """로컬에 파일이 있으면 우선 사용, 없으면 GCS(ok-project-assets/krcare)."""
    image_dir = os.path.join(STATIC_DIR, 'images')
    local_path = os.path.join(image_dir, filename)
    if os.path.exists(local_path):
        return send_from_directory(image_dir, filename)
    project_name = SITE_CONFIG['project_name']
    url = f"https://storage.googleapis.com/ok-project-assets/{project_name}/{filename}"
    if request.query_string:
        url = f"{url}?{request.query_string.decode()}"
    return redirect(url, code=302)

@app.route('/favicon.ico')
@app.route('/favicon-32x32.png')
@app.route('/favicon-48x48.png')
@app.route('/apple-touch-icon.png')
@app.route('/android-chrome-192x192.png')
@app.route('/android-chrome-512x512.png')
def serve_favicons():
    image_dir = os.path.join(STATIC_DIR, 'images')
    filename = request.path[1:]
    if filename == 'favicon.ico':
        for candidate in ('favicon.ico', 'favicons.ico'):
            if os.path.exists(os.path.join(image_dir, candidate)):
                filename = candidate
                break
    local_path = os.path.join(image_dir, filename)
    if os.path.exists(local_path):
        mimetype = 'image/png' if filename.endswith('.png') else 'image/vnd.microsoft.icon'
        return send_from_directory(image_dir, filename, mimetype=mimetype)
    return serve_images(filename)

@app.route('/site.webmanifest')
def webmanifest():
    manifest_path = os.path.join(STATIC_DIR, 'site.webmanifest')
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r', encoding='utf-8') as f:
            return Response(f.read(), mimetype='application/manifest+json')
    return Response('{"name":"OK Series","icons":[]}', mimetype='application/manifest+json')

@app.route('/robots.txt')
def robots_txt():
    base = SITE_CONFIG['site_url'].rstrip('/')
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /api/\n"
        "Disallow: /card/\n"
        "Disallow: /social/\n"
        f"Sitemap: {base}/sitemap.xml\n"
    )
    return Response(content, mimetype='text/plain')


_HREFLANG = {
    'en': 'en',
    'ja': 'ja',
    'zh': 'zh-Hans',
    'zh_tw': 'zh-Hant',
    'ko': 'ko',
}


def _lang_url(path: str, lang: str) -> str:
    """Build absolute URL with ?lang= for non-en list/home pages."""
    base = SITE_CONFIG['site_url'].rstrip('/')
    path = path if path.startswith('/') else f'/{path}'
    if lang == 'en':
        return f"{base}{path}"
    sep = '&' if '?' in path else '?'
    return f"{base}{path}{sep}lang={lang}"


def _sitemap_url_node(loc: str, lastmod: str, alternates: dict | None = None, changefreq: str = 'weekly', priority: str | None = None) -> str:
    parts = [f'<url><loc>{loc}</loc><lastmod>{lastmod}</lastmod><changefreq>{changefreq}</changefreq>']
    if priority:
        parts.append(f'<priority>{priority}</priority>')
    if alternates:
        # Include xhtml alternates + x-default (prefer EN)
        for lang, href in sorted(alternates.items()):
            hl = _HREFLANG.get(lang, lang)
            parts.append(f'<xhtml:link rel="alternate" hreflang="{hl}" href="{href}" />')
        default_href = alternates.get('en') or next(iter(alternates.values()), loc)
        parts.append(f'<xhtml:link rel="alternate" hreflang="x-default" href="{default_href}" />')
    parts.append('</url>')
    return ''.join(parts)


@app.route('/sitemap.xml')
def sitemap_xml():
    try:
        from .activities import ACTIVITIES, REGIONS_BY_ACTIVITY, activity_path
    except ImportError:
        from activities import ACTIVITIES, REGIONS_BY_ACTIVITY, activity_path

    base = SITE_CONFIG['site_url'].rstrip('/')
    today = datetime.now().strftime('%Y-%m-%d')
    list_langs = ('en', 'ko')

    nodes = []

    # Home
    home_alts = {lang: _lang_url('/', lang) for lang in list_langs}
    nodes.append(_sitemap_url_node(home_alts['en'], today, home_alts, priority='1.0'))

    # Activity + region landings (SEO)
    for activity in ACTIVITIES:
        for row in REGIONS_BY_ACTIVITY.get(activity, []):
            region = row['key']
            path_en = activity_path(activity, region, 'en')
            path_ko = activity_path(activity, region, 'ko')
            alts = {
                'en': f'{base}{path_en}',
                'ko': f'{base}{path_ko}',
            }
            pri = '0.9' if region == 'all' else '0.8'
            nodes.append(_sitemap_url_node(alts['en'], today, alts, priority=pri))

    # Guide index
    guide_alts = {lang: _lang_url('/guide', lang) for lang in list_langs}
    nodes.append(_sitemap_url_node(guide_alts['en'], today, guide_alts, priority='0.8'))

    # Static pages
    for path in ('/about.html', '/contact.html', '/privacy.html'):
        nodes.append(_sitemap_url_node(f'{base}{path}', today, changefreq='monthly', priority='0.3'))

    # Item detail pages
    item_pairs: dict[str, dict[str, str]] = {}
    for item in CACHED_DATA.get(SITE_CONFIG['data_key'], []):
        item_id = item.get('id')
        lang = item.get('lang', 'en')
        if not item_id or lang not in list_langs:
            continue
        base_id, _ = _split_lang_id(item_id)
        item_pairs.setdefault(base_id, {})[lang] = f'{base}/item/{item_id}'
    for pair in item_pairs.values():
        primary = pair.get('en') or next(iter(pair.values()))
        nodes.append(_sitemap_url_node(primary, today, pair, priority='0.6'))

    # Guide detail pages
    guide_pairs: dict[str, dict[str, str]] = {}
    for lang in list_langs:
        for guide in CACHED_GUIDES.get(lang, []):
            gid = guide.get('id')
            if not gid:
                continue
            base_id, _ = _split_lang_id(gid)
            guide_pairs.setdefault(base_id, {})[lang] = f'{base}/guide/{gid}'
    for pair in guide_pairs.values():
        primary = pair.get('en') or next(iter(pair.values()))
        nodes.append(_sitemap_url_node(primary, today, pair, priority='0.7'))

    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">'
        + ''.join(nodes)
        + '</urlset>'
    )
    return Response(xml, mimetype='application/xml')

@app.route('/about.html')
def about():
    lang  = request.args.get('lang', 'en')
    stats = _get_footer_stats(lang)
    return render_template('about.html', **stats)

@app.route('/privacy.html')
def privacy():
    return render_template('privacy.html', site=SITE_CONFIG)

@app.route('/contact.html')
@app.route('/contact')
def contact():
    return render_template('contact.html', site=SITE_CONFIG)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
