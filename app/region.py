"""Region keys for JPFun filters (Japan leisure regions)."""
from __future__ import annotations

import re
from typing import Any

_LANG_SUFFIX = re.compile(r"_(en|ko)$", re.I)

REGION_RULES: list[tuple[str, re.Pattern[str]]] = [
    ("hokkaido", re.compile(r"Hokkaido|홋카이도|北海道", re.I)),
    ("nagano", re.compile(r"Nagano|나가노|長野", re.I)),
    ("niigata", re.compile(r"Niigata|니가타|新潟", re.I)),
    (
        "tohoku",
        re.compile(
            r"Tohoku|Miyagi|Akita|Aomori|Yamagata|Iwate|Fukushima|"
            r"도호쿠|미야기|아키타|아오모리|야마가타|이와테|후쿠시마|"
            r"東北|宮城|秋田|青森|山形|岩手|福島",
            re.I,
        ),
    ),
    ("gifu", re.compile(r"Gifu|기후|岐阜", re.I)),
    ("gunma", re.compile(r"Gunma|군마|群馬", re.I)),
    ("tochigi", re.compile(r"Tochigi|도치기|栃木", re.I)),
    (
        "kanto",
        re.compile(
            r"Kanto|Tokyo|Kanagawa|Chiba|Ibaraki|Saitama|Shonan|"
            r"도쿄|가나가와|치바|이바라키|쇼난|"
            r"関東|東京|神奈川|千葉|茨城|Fujisawa|Oarai|Isumi",
            re.I,
        ),
    ),
    (
        "chubu",
        re.compile(
            r"Chubu|Yamanashi|Shizuoka|Aichi|Izu|Hokuriku|Fukui|"
            r"중부|야마나시|시즈오카|아이치|이즈|"
            r"中部|山梨|静岡|Motosu|Fujikawaguchiko|Oshima",
            re.I,
        ),
    ),
    (
        "kansai",
        re.compile(
            r"Kansai|Kyoto|Osaka|Hyogo|Nara|Wakayama|Mie|"
            r"간사이|교토|오사카|와카야마|미에|関西|京都|大阪|和歌山",
            re.I,
        ),
    ),
    (
        "chugoku",
        re.compile(
            r"Chugoku|Onomichi|Imabari|Hiroshima|Okayama|Tottori|Shimane|Setouchi|"
            r"주고쿠|오노미치|이마바리|히로시마|세토우치|"
            r"中国|尾道|今治",
            re.I,
        ),
    ),
    (
        "shikoku",
        re.compile(
            r"Shikoku|Kochi|Tokushima|Ehime|Kagawa|"
            r"시코쿠|고치|도쿠시마|四国|高知|徳島",
            re.I,
        ),
    ),
    (
        "kyushu",
        re.compile(
            r"Kyushu|Kagoshima|Miyazaki|Oita|Fukuoka|Nagasaki|Kumamoto|"
            r"큐슈|규슈|가고시마|미야자키|九州|鹿児島|Yakushima|Amami",
            re.I,
        ),
    ),
    (
        "okinawa",
        re.compile(
            r"Okinawa|Miyako|Ishigaki|Kerama|"
            r"오키나와|미야코|이시가키|케라마|沖縄|宮古|石垣",
            re.I,
        ),
    ),
]

# Prefecture / nickname → filter key (before activity fit).
REGION_ALIASES: dict[str, str] = {
    "miyagi": "tohoku",
    "akita": "tohoku",
    "iwate": "tohoku",
    "aomori": "tohoku",
    "yamagata": "tohoku",
    "fukushima": "tohoku",
    "chiba": "kanto",
    "tokyo": "kanto",
    "kanagawa": "kanto",
    "saitama": "kanto",
    "ibaraki": "kanto",
    "shonan": "kanto",
    "yamanashi": "chubu",
    "shizuoka": "chubu",
    "aichi": "chubu",
    "izu": "chubu",
    "hokuriku": "chubu",
    "fukui": "chubu",
    "mie": "kansai",
    "kyoto": "kansai",
    "osaka": "kansai",
    "hyogo": "kansai",
    "nara": "kansai",
    "wakayama": "kansai",
    "hiroshima": "chugoku",
    "okayama": "chugoku",
    "tottori": "chugoku",
    "shimane": "chugoku",
    "yamaguchi": "chugoku",
    "setouchi": "chugoku",
    "tokushima": "shikoku",
    "ehime": "shikoku",
    "kochi": "shikoku",
    "kagawa": "shikoku",
    "fukuoka": "kyushu",
    "miyazaki": "kyushu",
    "kumamoto": "kyushu",
    "kagoshima": "kyushu",
    "nagasaki": "kyushu",
    "oita": "kyushu",
    "saga": "kyushu",
}

# When activity chips omit a fine key, collapse toward a parent chip.
REGION_COLLAPSE: dict[str, str] = {
    "tochigi": "kanto",
    "gunma": "kanto",
    "gifu": "chubu",
    "nagano": "chubu",
    "niigata": "chubu",
    "kansai": "chubu",
    "shikoku": "chugoku",
    "kyushu": "chugoku",
    "tohoku": "kanto",
    "chugoku": "kansai",
    "kanto": "chubu",
    "okinawa": "kyushu",
}


def base_id(item_id: str) -> str:
    return _LANG_SUFFIX.sub("", str(item_id or ""))


def canonicalize_region_key(key: str | None) -> str:
    k = str(key or "").strip().lower()
    if not k or k == "all":
        return "other"
    return REGION_ALIASES.get(k, k)


def fit_region_to_activity(activity: str | None, key: str | None) -> str:
    """Map a region key onto a chip that exists for this activity."""
    current = canonicalize_region_key(key)
    if not activity:
        return current
    try:
        from .activities import REGIONS_BY_ACTIVITY
    except ImportError:
        from activities import REGIONS_BY_ACTIVITY

    allowed = {
        r["key"]
        for r in REGIONS_BY_ACTIVITY.get(activity, [])
        if r["key"] not in ("all", "other")
    }
    if not allowed:
        return current
    seen: set[str] = set()
    while current not in allowed and current not in seen:
        seen.add(current)
        nxt = REGION_COLLAPSE.get(current)
        if not nxt or nxt == current:
            break
        current = nxt
    return current if current in allowed else canonicalize_region_key(key)


def parse_region(
    address: str | None,
    lat: Any = None,
    lng: Any = None,
    explicit: str | dict | None = None,
    activity: str | None = None,
) -> dict:
    raw = None
    district = None
    if isinstance(explicit, dict):
        key = explicit.get("sido") or explicit.get("key")
        if key and str(key).strip() and str(key).strip() != "all":
            raw = str(key).strip().lower()
            district = explicit.get("district")
    elif explicit and str(explicit).strip() and str(explicit).strip() != "all":
        raw = str(explicit).strip().lower()

    if not raw:
        text = address or ""
        for key, pattern in REGION_RULES:
            if pattern.search(text):
                raw = key
                break
        else:
            raw = "other"

    sido = fit_region_to_activity(activity, raw) if activity else canonicalize_region_key(raw)
    return {"sido": sido, "district": district}


def enrich_items_with_regions(items: list[dict]) -> None:
    for item in items:
        activity = str(item.get("activity") or "").lower() or None
        item["region"] = parse_region(
            item.get("address"),
            item.get("lat"),
            item.get("lng"),
            explicit=item.get("region"),
            activity=activity,
        )


def matches_region_filter(
    region: dict | None,
    region_filter: str,
    district_filter: str | None = None,
    known_keys: set[str] | None = None,
) -> bool:
    if region_filter == "all":
        return True
    if not region:
        return False
    if district_filter and district_filter != "all":
        return False
    return region.get("sido") == region_filter
