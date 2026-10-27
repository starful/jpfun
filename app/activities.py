"""JPFun activity + per-activity region registry (SEO paths)."""
from __future__ import annotations

from typing import Any

ACTIVITIES: tuple[str, ...] = ("ski", "surf", "dive", "camp")

# UI labels (EN). Dive is shown as Scuba.
ACTIVITY_META: dict[str, dict[str, str]] = {
    "ski": {
        "slug": "ski",
        "emoji": "⛷️",
        "label_en": "Ski",
        "label_ko": "스키",
        "title_en": "Japan ski resorts on the map",
        "title_ko": "일본 스키장 지도",
        "desc_en": "Powder, resorts, and village bases — filter by region or style.",
        "desc_ko": "파우더·리조트·마을 베이스. 지역·스타일로 좁혀 보세요.",
        "category": "Ski",
        "image": "/static/images/hub/ski.jpg",
        "tone": "#1b4f72",
    },
    "surf": {
        "slug": "surf",
        "emoji": "🏄",
        "label_en": "Surf",
        "label_ko": "서핑",
        "title_en": "Japan surf spots on the map",
        "title_ko": "일본 서핑 스팟 지도",
        "desc_en": "Beach and point breaks — filter by beginner, reef, or day trip.",
        "desc_ko": "비치·포인트 브레이크. 초보·리프·당일로 좁혀 보세요.",
        "category": "Surf",
        "image": "/static/images/hub/surf.jpg",
        "tone": "#0e7490",
    },
    "dive": {
        "slug": "dive",
        "emoji": "🤿",
        "label_en": "Scuba",
        "label_ko": "스쿠버",
        "title_en": "Japan scuba & dive sites on the map",
        "title_ko": "일본 스쿠버·다이빙 지도",
        "desc_en": "Okinawa to Izu — filter by beginner, reef, or wall dives.",
        "desc_ko": "오키나와~이즈. 초보·산호·월 다이브로 좁혀 보세요.",
        "category": "Dive",
        "image": "/static/images/hub/dive.jpg",
        "tone": "#0f766e",
    },
    "camp": {
        "slug": "camp",
        "emoji": "🏕️",
        "label_en": "Camp",
        "label_ko": "캠핑",
        "title_en": "Japan camping & glamping on the map",
        "title_ko": "일본 캠핑·글램핑 지도",
        "desc_en": "Lakeside and alpine bases — filter glamping, car camp, onsen.",
        "desc_ko": "호숫가·알파인 베이스. 글램핑·차박·온천으로 좁혀 보세요.",
        "category": "Camp",
        "image": "/static/images/hub/camp.jpg",
        "tone": "#3f6212",
    },
}

# Regions available as filters / SEO paths inside each activity.
REGIONS_BY_ACTIVITY: dict[str, list[dict[str, str]]] = {
    "ski": [
        {"key": "all", "label_en": "All", "label_ko": "전체"},
        {"key": "hokkaido", "label_en": "Hokkaido", "label_ko": "홋카이도"},
        {"key": "nagano", "label_en": "Nagano", "label_ko": "나가노"},
        {"key": "niigata", "label_en": "Niigata", "label_ko": "니가타"},
        {"key": "tohoku", "label_en": "Tohoku", "label_ko": "도호쿠"},
        {"key": "gifu", "label_en": "Gifu", "label_ko": "기후"},
        {"key": "gunma", "label_en": "Gunma", "label_ko": "군마"},
        {"key": "tochigi", "label_en": "Tochigi", "label_ko": "도치기"},
    ],
    "surf": [
        {"key": "all", "label_en": "All", "label_ko": "전체"},
        {"key": "kanto", "label_en": "Kanto", "label_ko": "간토"},
        {"key": "chubu", "label_en": "Chubu", "label_ko": "중부"},
        {"key": "tohoku", "label_en": "Tohoku", "label_ko": "도호쿠"},
        {"key": "kansai", "label_en": "Kansai", "label_ko": "간사이"},
        {"key": "chugoku", "label_en": "Chugoku", "label_ko": "주고쿠"},
        {"key": "shikoku", "label_en": "Shikoku", "label_ko": "시코쿠"},
        {"key": "kyushu", "label_en": "Kyushu", "label_ko": "규슈"},
        {"key": "okinawa", "label_en": "Okinawa", "label_ko": "오키나와"},
    ],
    "dive": [
        {"key": "all", "label_en": "All", "label_ko": "전체"},
        {"key": "okinawa", "label_en": "Okinawa", "label_ko": "오키나와"},
        {"key": "chubu", "label_en": "Izu", "label_ko": "이즈"},
        {"key": "kanto", "label_en": "Kanto", "label_ko": "간토"},
        {"key": "kansai", "label_en": "Kansai", "label_ko": "간사이"},
        {"key": "chugoku", "label_en": "Chugoku", "label_ko": "주고쿠"},
        {"key": "kyushu", "label_en": "Kyushu", "label_ko": "규슈"},
    ],
    "camp": [
        {"key": "all", "label_en": "All", "label_ko": "전체"},
        {"key": "hokkaido", "label_en": "Hokkaido", "label_ko": "홋카이도"},
        {"key": "tohoku", "label_en": "Tohoku", "label_ko": "도호쿠"},
        {"key": "kanto", "label_en": "Kanto", "label_ko": "간토"},
        {"key": "chubu", "label_en": "Chubu", "label_ko": "중부"},
        {"key": "nagano", "label_en": "Nagano", "label_ko": "나가노"},
        {"key": "kansai", "label_en": "Kansai", "label_ko": "간사이"},
        {"key": "chugoku", "label_en": "Chugoku", "label_ko": "주고쿠"},
        {"key": "kyushu", "label_en": "Kyushu", "label_ko": "규슈"},
    ],
}

REGION_LABELS_EN = {
    "all": "All",
    "hokkaido": "Hokkaido",
    "nagano": "Nagano",
    "niigata": "Niigata",
    "tohoku": "Tohoku",
    "gifu": "Gifu",
    "gunma": "Gunma",
    "tochigi": "Tochigi",
    "kanto": "Kanto",
    "chubu": "Chubu",
    "kansai": "Kansai",
    "kyushu": "Kyushu",
    "shikoku": "Shikoku",
    "chugoku": "Chugoku",
    "okinawa": "Okinawa",
    "other": "Other",
}

# Non-region style filters (title/summary keyword tags). Per-activity chip sets.
TRAITS_BY_ACTIVITY: dict[str, list[dict[str, str]]] = {
    "ski": [
        {"key": "all", "label_en": "All", "label_ko": "전체"},
        {"key": "beginner", "label_en": "Beginner", "label_ko": "초보"},
        {"key": "family", "label_en": "Family", "label_ko": "가족"},
        {"key": "powder", "label_en": "Powder", "label_ko": "파우더"},
        {"key": "onsen", "label_en": "Onsen", "label_ko": "온천"},
        {"key": "daytrip", "label_en": "Day trip", "label_ko": "당일"},
    ],
    "surf": [
        {"key": "all", "label_en": "All", "label_ko": "전체"},
        {"key": "beginner", "label_en": "Beginner", "label_ko": "초보"},
        {"key": "reef", "label_en": "Reef / Point", "label_ko": "리프·포인트"},
        {"key": "daytrip", "label_en": "Day trip", "label_ko": "당일"},
    ],
    "dive": [
        {"key": "all", "label_en": "All", "label_ko": "전체"},
        {"key": "beginner", "label_en": "Beginner", "label_ko": "초보"},
        {"key": "reef", "label_en": "Reef", "label_ko": "산호·리프"},
        {"key": "wall", "label_en": "Wall / Advanced", "label_ko": "월·상급"},
        {"key": "video", "label_en": "Has video", "label_ko": "영상"},
    ],
    "camp": [
        {"key": "all", "label_en": "All", "label_ko": "전체"},
        {"key": "glamping", "label_en": "Glamping", "label_ko": "글램핑"},
        {"key": "carcamp", "label_en": "Car camp", "label_ko": "차박"},
        {"key": "beginner", "label_en": "Beginner", "label_ko": "초보"},
        {"key": "onsen", "label_en": "Onsen", "label_ko": "온천"},
    ],
}


def is_activity(slug: str | None) -> bool:
    return bool(slug) and slug in ACTIVITY_META


def normalize_region(activity: str, region: str | None) -> str:
    key = (region or "all").strip().lower()
    allowed = {r["key"] for r in REGIONS_BY_ACTIVITY.get(activity, [])}
    if key in allowed:
        return key
    return "all"


def activity_path(activity: str, region: str = "all", lang: str = "en") -> str:
    path = f"/{activity}" if region in ("", "all") else f"/{activity}/{region}"
    if lang and lang != "en":
        return f"{path}?lang={lang}"
    return path


def regions_for(activity: str, lang: str = "en") -> list[dict[str, Any]]:
    rows = []
    for r in REGIONS_BY_ACTIVITY.get(activity, []):
        label = r["label_ko"] if lang == "ko" else r["label_en"]
        rows.append(
            {
                "key": r["key"],
                "label": label,
                "count_id": f"count-region-{r['key']}",
                "path": activity_path(activity, r["key"], lang),
            }
        )
    return rows


def traits_for(activity: str, lang: str = "en") -> list[dict[str, Any]]:
    rows = []
    for t in TRAITS_BY_ACTIVITY.get(activity, []):
        label = t["label_ko"] if lang == "ko" else t["label_en"]
        rows.append(
            {
                "key": t["key"],
                "label": label,
                "count_id": f"count-trait-{t['key']}",
            }
        )
    return rows


def hub_cards(lang: str = "en") -> list[dict[str, str]]:
    """Internal activity cards (used by hub nav on map pages)."""
    cards = []
    for slug in ACTIVITIES:
        meta = ACTIVITY_META[slug]
        cards.append(
            {
                "slug": slug,
                "emoji": meta["emoji"],
                "label": meta["label_ko"] if lang == "ko" else meta["label_en"],
                "title": meta["title_ko"] if lang == "ko" else meta["title_en"],
                "desc": meta["desc_ko"] if lang == "ko" else meta["desc_en"],
                "href": activity_path(slug, "all", lang),
                "image": meta["image"],
                "tone": meta["tone"],
                "external": False,
            }
        )
    return cards


# Peer leisure tiles on the hub LP only (image + outbound link, no /golf|/onsen maps).
HUB_EXTERNAL_CARDS: list[dict[str, str]] = [
    {
        "slug": "golf",
        "emoji": "⛳",
        "label_en": "Golf",
        "label_ko": "골프",
        "desc_en": "Courses on the map — green fees & booking.",
        "desc_ko": "골프장 지도 · 그린피·예약.",
        "image": "/static/images/hub/golf.jpg",
        "tone": "#1a7a4c",
        "href_en": "https://okcaddie.net/",
        "href_ko": "https://okcaddie.net/?lang=ko",
    },
    {
        "slug": "onsen",
        "emoji": "♨️",
        "label_en": "Onsen",
        "label_ko": "온천",
        "desc_en": "Ryokan & hot-spring towns across Japan.",
        "desc_ko": "료칸·온천 마을을 지도로.",
        "image": "/static/images/hub/onsen.jpg",
        "tone": "#b45309",
        "href_en": "https://okonsen.net/",
        "href_ko": "https://okonsen.net/?lang=ko",
    },
]


def hub_lp_cards(lang: str = "en") -> list[dict[str, Any]]:
    """Hub 'What are you here for?' grid: JPFun maps + peer leisure links."""
    cards: list[dict[str, Any]] = hub_cards(lang)
    for meta in HUB_EXTERNAL_CARDS:
        cards.append(
            {
                "slug": meta["slug"],
                "emoji": meta["emoji"],
                "label": meta["label_ko"] if lang == "ko" else meta["label_en"],
                "desc": meta["desc_ko"] if lang == "ko" else meta["desc_en"],
                "href": meta["href_ko"] if lang == "ko" else meta["href_en"],
                "image": meta["image"],
                "tone": meta["tone"],
                "external": True,
            }
        )
    return cards


def season_banner(lang: str = "en", month: int | None = None) -> dict[str, str]:
    """Lightweight 'this season' hint for the LP hero."""
    from datetime import date

    m = month if month is not None else date.today().month
    # Rough Japan leisure seasons
    if m in (12, 1, 2, 3):
        focus = "ski"
        line_en = "Ski season — Hokkaido & Nagano powder windows"
        line_ko = "스키 시즌 — 홋카이도·나가노 파우더"
    elif m in (4, 5):
        focus = "camp"
        line_en = "Spring camping & early surf along the Pacific"
        line_ko = "봄 캠핑·태평양 초반 서핑"
    elif m in (6, 7, 8, 9):
        focus = "dive"
        line_en = "Summer water — scuba, surf & island camps"
        line_ko = "여름 워터 시즌 — 스쿠버·서핑·섬 캠프"
    else:
        focus = "surf"
        line_en = "Autumn swells & crisp alpine camp weekends"
        line_ko = "가을 스웰·알파인 캠프 주말"

    meta = ACTIVITY_META[focus]
    return {
        "focus": focus,
        "line": line_ko if lang == "ko" else line_en,
        "cta_label": meta["label_ko"] if lang == "ko" else meta["label_en"],
        "cta_href": activity_path(focus, "all", lang),
        "emoji": meta["emoji"],
    }


