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
        "desc_en": "Powder, resorts, and village bases — filter by region.",
        "desc_ko": "파우더·리조트·마을 베이스. 지역으로 좁혀 보세요.",
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
        "desc_en": "Beach and point breaks near Tokyo, Chiba, and the islands.",
        "desc_ko": "쇼난·치바·섬 지역의 비치·포인트 브레이크.",
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
        "desc_en": "Okinawa, Kerama, Ishigaki, and Izu boat / shore dives.",
        "desc_ko": "오키나와·케라마·이시가키·이즈 보트·쇼어 다이빙.",
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
        "desc_en": "Lakeside, alpine, and island-hop camp bases.",
        "desc_ko": "호숫가·알파인·섬 캠프 베이스.",
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
    ],
    "surf": [
        {"key": "all", "label_en": "All", "label_ko": "전체"},
        {"key": "kanto", "label_en": "Kanto", "label_ko": "간토"},
        {"key": "okinawa", "label_en": "Okinawa", "label_ko": "오키나와"},
    ],
    "dive": [
        {"key": "all", "label_en": "All", "label_ko": "전체"},
        {"key": "okinawa", "label_en": "Okinawa", "label_ko": "오키나와"},
        {"key": "chubu", "label_en": "Izu / Chubu", "label_ko": "이즈·중부"},
    ],
    "camp": [
        {"key": "all", "label_en": "All", "label_ko": "전체"},
        {"key": "chubu", "label_en": "Chubu / Fuji", "label_ko": "중부·후지"},
        {"key": "nagano", "label_en": "Nagano", "label_ko": "나가노"},
        {"key": "chugoku", "label_en": "Chugoku / Shimanami", "label_ko": "주고쿠·시마나미"},
    ],
}

REGION_LABELS_EN = {
    "all": "All",
    "hokkaido": "Hokkaido",
    "nagano": "Nagano",
    "niigata": "Niigata",
    "tohoku": "Tohoku",
    "kanto": "Kanto",
    "chubu": "Chubu",
    "chugoku": "Chugoku",
    "okinawa": "Okinawa",
    "other": "Other",
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


# Curated shortcuts on the LP hub (JPFun paths + peer leisure links).
HUB_SHORTCUTS: list[dict[str, str]] = [
    {
        "emoji": "⛷️",
        "activity": "ski",
        "region": "hokkaido",
        "label_en": "Ski · Hokkaido",
        "label_ko": "스키 · 홋카이도",
        "blurb_en": "Powder bases around Niseko & Furano",
        "blurb_ko": "니세코·후라노 파우더 베이스",
    },
    {
        "emoji": "🤿",
        "activity": "dive",
        "region": "okinawa",
        "label_en": "Scuba · Okinawa",
        "label_ko": "스쿠버 · 오키나와",
        "blurb_en": "Kerama clarity & Ishigaki mantas",
        "blurb_ko": "케라마 투명도·이시가키 만타",
    },
    {
        "emoji": "🏄",
        "activity": "surf",
        "region": "kanto",
        "label_en": "Surf · Kanto",
        "label_ko": "서핑 · 간토",
        "blurb_en": "Shonan, Chiba & Ibaraki weekends",
        "blurb_ko": "쇼난·치바·이바라키 주말 서프",
    },
    {
        "emoji": "🏕️",
        "activity": "camp",
        "region": "chubu",
        "label_en": "Camp · Fuji / Chubu",
        "label_ko": "캠핑 · 후지·중부",
        "blurb_en": "Motosu lakeside car-camp classics",
        "blurb_ko": "모토스코 호숫가 차박 클래식",
    },
    {
        "emoji": "⛳",
        "label_en": "Golf · Japan",
        "label_ko": "골프 · 일본",
        "blurb_en": "Courses on the map — green fees & booking",
        "blurb_ko": "골프장 지도 · 그린피·예약",
        "href_en": "https://okcaddie.net/",
        "href_ko": "https://okcaddie.net/?lang=ko",
    },
    {
        "emoji": "🍜",
        "label_en": "Ramen · Japan",
        "label_ko": "라멘 · 일본",
        "blurb_en": "Shop map for the same trip",
        "blurb_ko": "같은 여행에 붙는 라멘 지도",
        "href_en": "https://okramen.net/",
        "href_ko": "https://okramen.net/?lang=ko",
    },
    {
        "emoji": "♨️",
        "label_en": "Onsen · Japan",
        "label_ko": "온천 · 일본",
        "blurb_en": "Ryokan & hot-spring towns",
        "blurb_ko": "료칸·온천 마을",
        "href_en": "https://okonsen.net/",
        "href_ko": "https://okonsen.net/?lang=ko",
    },
]


def hub_shortcuts(lang: str = "en") -> list[dict[str, str]]:
    rows = []
    for s in HUB_SHORTCUTS:
        if s.get("href_en") or s.get("href_ko"):
            href = s["href_ko"] if lang == "ko" else s["href_en"]
        else:
            href = activity_path(s["activity"], s.get("region", "all"), lang)
        emoji = s.get("emoji") or ACTIVITY_META.get(s.get("activity", ""), {}).get("emoji", "🎉")
        rows.append(
            {
                "href": href,
                "label": s["label_ko"] if lang == "ko" else s["label_en"],
                "blurb": s["blurb_ko"] if lang == "ko" else s["blurb_en"],
                "emoji": emoji,
            }
        )
    return rows


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


def how_steps(lang: str = "en") -> list[dict[str, str]]:
    if lang == "ko":
        return [
            {"n": "1", "title": "레저 고르기", "body": "스키·스쿠버·서핑·캠핑 중 하나를 고릅니다."},
            {"n": "2", "title": "지역으로 좁히기", "body": "활동 맵에서 홋카이도·오키나와 같은 지역만 봅니다."},
            {"n": "3", "title": "스팟·일정", "body": "상세 가이드를 열고 숙소는 파트너 링크로 이어집니다."},
        ]
    return [
        {"n": "1", "title": "Pick leisure", "body": "Choose ski, scuba, surf, or camp."},
        {"n": "2", "title": "Filter region", "body": "Narrow the map to Hokkaido, Okinawa, and more."},
        {"n": "3", "title": "Plan the spot", "body": "Open a guide, then book stays via partner links."},
    ]


def _ext(url_en: str, url_ko: str, lang: str) -> str:
    return url_ko if lang == "ko" else url_en


def journey_next_for(
    lang: str = "en",
    activity: str | None = None,
    region: str = "all",
) -> list[dict[str, str]]:
    """Trip next-steps: mix of JPFun paths + soft external guides (no 'other site' framing)."""
    lang = "ko" if lang == "ko" else "en"
    region = (region or "all").lower()
    rows: list[dict[str, str]] = []

    def add(emoji: str, label_en: str, label_ko: str, blurb_en: str, blurb_ko: str, href: str) -> None:
        rows.append(
            {
                "emoji": emoji,
                "label": label_ko if lang == "ko" else label_en,
                "blurb": blurb_ko if lang == "ko" else blurb_en,
                "href": href,
            }
        )

    # --- Activity-scoped suggestions ---
    if activity == "ski":
        add(
            "♨️",
            "Onsen after the slopes",
            "슬로프 후 온천",
            "Soak near the ski towns",
            "스키 타운 근처에서 풀기",
            _ext("https://okonsen.net/", "https://okonsen.net/?lang=ko", lang),
        )
        add(
            "🍜",
            "Ramen after a cold day",
            "추운 날 라멘",
            "Warm bowls that fit the same trip",
            "같은 여행에 붙는 한 그릇",
            _ext("https://okramen.net/", "https://okramen.net/?lang=ko", lang),
        )
        if region in ("nagano", "all"):
            add(
                "🏕️",
                "Camp these mountains in summer",
                "여름엔 같은 산에서 캠프",
                "Hakuba alpine bases when snow melts",
                "눈 녹으면 하쿠바 알파인 캠프",
                activity_path("camp", "nagano", lang),
            )
        if region == "hokkaido":
            add(
                "⛷️",
                "More Hokkaido ski",
                "홋카이도 스키 더 보기",
                "Stay on the powder map",
                "파우더 맵에서 더 둘러보기",
                activity_path("ski", "hokkaido", lang),
            )

    elif activity == "dive":
        add("🏄", "Surf the same islands", "같은 섬에서 서핑",
            "Okinawa swell days between dives",
            "다이빙 사이 오키나와 스웰",
            activity_path("surf", "okinawa", lang))
        if region in ("okinawa", "all"):
            add("⛳", "Golf in Okinawa", "오키나와 골프",
                "Ocean courses when you want a dry day",
                "바다 코스로 쉬는 날",
                _ext("https://okcaddie.net/", "https://okcaddie.net/?lang=ko", lang))
            add("♨️", "Ryokan / spa stays", "료칸·스파 숙소",
                "Recover after boat days",
                "보트 다이빙 후 회복 숙소",
                _ext("https://okonsen.net/", "https://okonsen.net/?lang=ko", lang))

    elif activity == "surf":
        add("🤿", "Scuba when flat", "파도 없을 땐 스쿠버",
            "Swap the board for a tank in Okinawa / Izu",
            "오키나와·이즈에서 탱크로 전환",
            activity_path("dive", "okinawa" if region == "okinawa" else "all", lang))
        add("🍜", "Post-surf ramen", "서핑 후 라멘",
            "Shonan & Tokyo bowls after the session",
            "세션 후 쇼난·도쿄 라멘",
            _ext("https://okramen.net/", "https://okramen.net/?lang=ko", lang))

    elif activity == "camp":
        add("⛷️", "Same mountains in winter", "겨울엔 같은 산에서 스키",
            "Hakuba flips from camp to ski",
            "하쿠바가 캠프에서 스키로",
            activity_path("ski", "nagano", lang))
        add("♨️", "Onsen near camp", "캠프 근처 온천",
            "Rinse the trail dust",
            "트레일 먼지 씻고 온천",
            _ext("https://okonsen.net/", "https://okonsen.net/?lang=ko", lang))

    else:
        # Hub defaults — feel like continuing the trip, not leaving the product
        add("⛷️", "Ski map", "스키 지도",
            "Powder resorts by region",
            "지역별 파우더 리조트",
            activity_path("ski", "all", lang))
        add("🤿", "Scuba map", "스쿠버 지도",
            "Okinawa & Izu dive areas",
            "오키나와·이즈 다이빙",
            activity_path("dive", "all", lang))
        add("♨️", "Onsen after adventure", "액티비티 후 온천",
            "Soak when the day is done",
            "하루 마무리 온천",
            _ext("https://okonsen.net/", "https://okonsen.net/?lang=ko", lang))
        add("🍜", "Ramen nearby", "근처 라멘",
            "Bowls that fit the same trip",
            "같은 여행에 붙는 한 그릇",
            _ext("https://okramen.net/", "https://okramen.net/?lang=ko", lang))

    # Dedupe by href, cap at 4
    seen: set[str] = set()
    out: list[dict[str, str]] = []
    for row in rows:
        if row["href"] in seen:
            continue
        seen.add(row["href"])
        out.append(row)
        if len(out) >= 4:
            break
    return out
