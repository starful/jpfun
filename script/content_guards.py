"""Generation guards: reject thin/duplicate/low-quality output.

Same-topic regeneration is allowed. Near-duplicate guide IDs in
GUIDE_DUPLICATE_OF are blocked. Every write must pass a quality gate.
"""

from __future__ import annotations

import re
from pathlib import Path

# Near-identical guide topics → keep only the canonical id.
GUIDE_DUPLICATE_OF: dict[str, str] = {}

ITEM_MIN_CHARS = 4500
GUIDE_MIN_CHARS = 4000
# Hangul packs more meaning per character. Live KO spots sit ~300–1,100 chars;
# Claude KO drafts that cover season/access/tips land ~2,500–3,300. Character
# quota is a stub floor — visitor themes are the real gate.
KO_MIN_CHARS = 2200
# Sibling locale fill (one lang already live) uses a higher bar for English.
SIBLING_FILL_MIN_CHARS = 5500

HANGUL_RE = re.compile(r"[\uac00-\ud7a3]")
FM_SPLIT = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.S)

# Body-text themes (unique ## titles are required, so match content not headings).
THEME_NEEDLES: dict[str, dict[str, tuple[str, ...]]] = {
    "season": {
        "en": ("season", "winter", "summer", "autumn", "fall", "spring", "swell", "powder", "snow"),
        "ko": ("시즌", "계절", "적설", "수온", "파우더", "스웰", "겨울", "여름", "가을", "봄"),
    },
    "access": {
        "en": ("airport", "train", "shinkansen", "shuttle", "drive", "station", "rental car", "access"),
        "ko": ("접근", "오는 길", "공항", "신칸센", "렌터카", "셔틀", "기차", "열차", "버스"),
    },
    "tips": {
        "en": ("tip", "book", "rental", "etiquette", "lodging", "onsen", "gear", "reserv"),
        "ko": ("팁", "주의", "예약", "렌탈", "에티켓", "숙소", "온천", "장비", "강습"),
    },
}


def base_slug(stem: str) -> str:
    if stem.endswith("_en") or stem.endswith("_ko"):
        return stem.rsplit("_", 1)[0]
    return stem


def lang_from_stem(stem: str) -> str:
    return "ko" if stem.endswith("_ko") else "en"


def strip_code_fences(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```[a-z]*\n", "", text, flags=re.I)
    text = re.sub(r"\n```$", "", text)
    return text.replace("```markdown", "").replace("```", "").strip()


def parse_frontmatter_body(raw: str) -> tuple[dict[str, str], str]:
    raw = strip_code_fences(raw)
    m = FM_SPLIT.match(raw)
    if not m:
        return {}, raw
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        meta[key.strip()] = val.strip().strip('"').strip("'")
    return meta, m.group(2).strip()


def hangul_ratio(text: str) -> float:
    if not text:
        return 0.0
    hangul = len(HANGUL_RE.findall(text))
    return hangul / max(len(text), 1)


def duplicate_guide_reason(base_id: str, guide_dir: str | Path) -> str | None:
    """Return skip reason if base_id is a blocked duplicate of an existing/canonical guide."""
    base_id = (base_id or "").strip()
    if not base_id:
        return "missing_id"
    canonical = GUIDE_DUPLICATE_OF.get(base_id)
    if not canonical:
        return None
    guide_dir = Path(guide_dir)
    if any(guide_dir.glob(f"{canonical}_*.md")):
        return f"duplicate_of:{canonical}"
    return f"alias_blocked:{canonical}"


def min_chars_for(*, kind: str, sibling_exists: bool, lang: str = "en") -> int:
    if str(lang).lower() == "ko":
        return KO_MIN_CHARS
    if sibling_exists:
        return SIBLING_FILL_MIN_CHARS
    return ITEM_MIN_CHARS if kind == "item" else GUIDE_MIN_CHARS


def _body_haystack(body: str, lang: str) -> str:
    return body.lower() if str(lang).lower() == "en" else body


def theme_gaps(body: str, *, lang: str) -> list[str]:
    """Return missing visitor themes. Match body text, not H2 titles."""
    hay = _body_haystack(body, lang)
    lang_key = "ko" if str(lang).lower() == "ko" else "en"
    missing: list[str] = []
    for theme, by_lang in THEME_NEEDLES.items():
        needles = by_lang[lang_key]
        if not any(n in hay for n in needles):
            missing.append(f"missing_theme:{theme}")
    return missing


def quality_prompt_block(*, lang: str) -> str:
    """Shared generation rules: themes over English-length character quotas."""
    if str(lang).lower() == "ko":
        return """[HARD RULES]
- Write ONLY in Korean. Proper nouns in Latin script are OK; do not mix sentences.
- At least 4 unique ## sections. Never use H1 (#).
- Cover ALL of these themes (invent unique ## titles; do not copy Overview / Getting there / Tips):
  1. Who this is for and what makes THIS place or topic distinct
  2. Conditions — slopes, swell, dive sites, camp layout, or the how-to for a guide
  3. Season AND access — when to go, plus airport / train / car / time from a real hub
  4. Practical tips — booking, gear, etiquette, stay or food
- Do not target an English-style character count. A Korean visitor page is complete when those themes have concrete facts, not padding."""
    return """[HARD RULES]
- Write ONLY in English.
- At least 4 unique ## sections. Never use H1 (#).
- Cover ALL of these themes with unique ## titles:
  1. Who this is for and what makes THIS place or topic distinct
  2. Conditions — slopes, swell, dive sites, camp layout, or the how-to for a guide
  3. Season AND access — when to go, plus airport / train / car / time from a real hub
  4. Practical tips — booking, gear, etiquette, stay or food
- Invent unique ## titles; do not reuse Overview / Getting there / Tips across articles."""


def validate_generated_markdown(
    raw: str,
    *,
    kind: str,
    lang: str,
    sibling_exists: bool = False,
) -> tuple[bool, list[str]]:
    """Quality gate before writing. Same topic OK; thin/wrong-lang output is not."""
    errors: list[str] = []
    meta, body = parse_frontmatter_body(raw)
    min_chars = min_chars_for(kind=kind, sibling_exists=sibling_exists, lang=lang)

    if not meta:
        errors.append("missing_frontmatter")
    else:
        required = ["lang", "title", "summary", "date"]
        if kind == "item":
            required.extend(["lat", "lng", "address", "categories", "thumbnail"])
        for key in required:
            if not str(meta.get(key, "")).strip():
                errors.append(f"missing_meta:{key}")
        meta_lang = str(meta.get("lang", "")).strip().lower()
        if meta_lang and meta_lang != lang:
            errors.append(f"lang_mismatch_meta:{meta_lang}!={lang}")

    if len(body) < min_chars:
        errors.append(f"too_short:{len(body)}<{min_chars}")

    ratio = hangul_ratio(body)
    if lang == "ko" and ratio < 0.08:
        errors.append(f"ko_too_little_hangul:{ratio:.3f}")
    if lang == "en" and ratio > 0.12:
        errors.append(f"en_too_much_hangul:{ratio:.3f}")

    heading_count = len(re.findall(r"^##\s+\S", body, re.M))
    if heading_count < 3:
        errors.append(f"too_few_sections:{heading_count}")

    errors.extend(theme_gaps(body, lang=lang))

    return (len(errors) == 0), errors


def sibling_path(content_dir: str | Path, base: str, lang: str) -> Path:
    other = "ko" if lang == "en" else "en"
    return Path(content_dir) / f"{base}_{other}.md"


def sibling_exists(content_dir: str | Path, base: str, lang: str) -> bool:
    return sibling_path(content_dir, base, lang).is_file()


def locale_pair_status(content_dir: str | Path, base: str) -> str:
    """Return 'complete', 'half' (one lang), or 'new' (neither en nor ko)."""
    root = Path(content_dir)
    en = (root / f"{base}_en.md").is_file()
    ko = (root / f"{base}_ko.md").is_file()
    if en and ko:
        return "complete"
    if en or ko:
        return "half"
    return "new"
