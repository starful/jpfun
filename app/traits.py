"""Non-region style tags derived from title/summary (and youtube)."""
from __future__ import annotations

import re
from typing import Any

TRAIT_RULES: dict[str, re.Pattern[str]] = {
    "beginner": re.compile(r"beginner|초보|입문|완만|novice|\beasy\b|처음", re.I),
    "family": re.compile(r"family|가족|아이\s*동반|\bkids?\b|child", re.I),
    "powder": re.compile(r"powder|파우더", re.I),
    "onsen": re.compile(r"onsen|온천", re.I),
    "daytrip": re.compile(r"day\s*trip|당일|weekend|주말|near\s*tokyo|도쿄\s*근교|tokyo\s*day", re.I),
    "reef": re.compile(r"reef|산호|coral|point\s*break|reef\s*break", re.I),
    "wall": re.compile(r"wall|월\s*다이브|드롭오프|drop.?off|advanced|상급", re.I),
    "glamping": re.compile(r"글램핑|glamping", re.I),
    "carcamp": re.compile(r"차박|car\s*camp|vanlife|캠핑카", re.I),
}


def detect_traits(item: dict[str, Any]) -> list[str]:
    text = f"{item.get('title') or ''}\n{item.get('summary') or ''}"
    found = [key for key, pattern in TRAIT_RULES.items() if pattern.search(text)]
    if str(item.get("youtube_id") or "").strip():
        found.append("video")
    return found


def matches_trait_filter(item: dict[str, Any], trait: str | None) -> bool:
    key = (trait or "all").strip().lower()
    if not key or key == "all":
        return True
    traits = item.get("traits")
    if traits is None:
        traits = detect_traits(item)
    return key in traits


def normalize_trait(activity: str, trait: str | None) -> str:
    from .activities import TRAITS_BY_ACTIVITY

    key = (trait or "all").strip().lower()
    allowed = {t["key"] for t in TRAITS_BY_ACTIVITY.get(activity, [])}
    if key in allowed:
        return key
    return "all"
