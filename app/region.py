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
            r"Tohoku|Yamagata|Iwate|Fukushima|도호쿠|야마가타|이와테|후쿠시마|東北|山形|岩手|福島",
            re.I,
        ),
    ),
    (
        "kanto",
        re.compile(
            r"Kanto|Tokyo|Kanagawa|Chiba|Ibaraki|도쿄|가나가와|치바|이바라키|関東|東京|神奈川|千葉|茨城|Fujisawa|Oarai|Isumi",
            re.I,
        ),
    ),
    (
        "chubu",
        re.compile(
            r"Chubu|Yamanashi|Shizuoka|Gifu|중부|야마나시|시즈오카|기후|中部|山梨|静岡|岐阜|Motosu|Fujikawaguchiko|Oshima",
            re.I,
        ),
    ),
    (
        "chugoku",
        re.compile(
            r"Chugoku|Onomichi|Imabari|Hiroshima|Ehime|주고쿠|오노미치|이마바리|中国|尾道|今治",
            re.I,
        ),
    ),
    (
        "okinawa",
        re.compile(
            r"Okinawa|Miyako|Ishigaki|Kerama|오키나와|미야코|이시가키|케라마|沖縄|宮古|石垣",
            re.I,
        ),
    ),
    ("gifu", re.compile(r"Gifu|기후|岐阜", re.I)),
    ("gunma", re.compile(r"Gunma|군마|群馬", re.I)),
    ("tochigi", re.compile(r"Tochigi|도치기|栃木", re.I)),
]


def base_id(item_id: str) -> str:
    return _LANG_SUFFIX.sub("", str(item_id or ""))


def parse_region(
    address: str | None,
    lat: Any = None,
    lng: Any = None,
    explicit: str | dict | None = None,
) -> dict:
    if isinstance(explicit, dict):
        key = explicit.get("sido") or explicit.get("key")
        if key and str(key).strip() and str(key).strip() != "all":
            return {"sido": str(key).strip().lower(), "district": explicit.get("district")}
    elif explicit and str(explicit).strip() and str(explicit).strip() != "all":
        return {"sido": str(explicit).strip().lower(), "district": None}
    text = address or ""
    for key, pattern in REGION_RULES:
        if pattern.search(text):
            return {"sido": key, "district": None}
    return {"sido": "other", "district": None}


def enrich_items_with_regions(items: list[dict]) -> None:
    for item in items:
        item["region"] = parse_region(
            item.get("address"),
            item.get("lat"),
            item.get("lng"),
            explicit=item.get("region"),
        )


def matches_region_filter(
    region: dict | None,
    region_filter: str,
    district_filter: str | None = None,
) -> bool:
    if region_filter == "all":
        return True
    if not region:
        return False
    if district_filter and district_filter != "all":
        return False
    return region.get("sido") == region_filter
