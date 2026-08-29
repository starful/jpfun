"""A8.net affiliate banners for JPFun."""

from __future__ import annotations

import os
from typing import Any

_BANNERS: dict[str, dict[str, str]] = {
    "agoda": {
        "id": "agoda",
        "click_url": "https://px.a8.net/svt/ejp?a8mat=4BAH9J+13APSI+4X1W+5ZMCH",
        "image_url": "https://www24.a8.net/svt/bgt?aid=260829415066&wid=005&eno=01&mid=s00000022946001006000&mc=1",
        "pixel_url": "https://www10.a8.net/0.gif?a8mat=4BAH9J+13APSI+4X1W+5ZMCH",
        "label_en": "Agoda — hotels in Japan",
        "label_ko": "Agoda — 일본 숙소 예약",
        "desc_en": "Search stays near this spot on Agoda.",
        "desc_ko": "이 스팟 주변 숙소를 Agoda에서 검색.",
        "alt_en": "Agoda hotel booking — affiliate",
        "alt_ko": "Agoda 숙소 예약 — 제휴",
    },
    "tora_esim": {
        "id": "tora_esim",
        "click_url": "https://px.a8.net/svt/ejp?a8mat=4BAH9I+GEM3YQ+5NG6+5ZEMP",
        "image_url": "https://www26.a8.net/svt/bgt?aid=260829414992&wid=005&eno=01&mid=s00000026367001005000&mc=1",
        "pixel_url": "https://www13.a8.net/0.gif?a8mat=4BAH9I+GEM3YQ+5NG6+5ZEMP",
        "label_en": "TORA eSIM — travel data",
        "label_ko": "TORA eSIM — 여행용 eSIM",
        "desc_en": "eSIM for Japan trips — activate before you land.",
        "desc_ko": "일본 여행 eSIM — 도착 전 개통.",
        "alt_en": "TORA eSIM — affiliate",
        "alt_ko": "TORA eSIM — 제휴",
    },
    "ski_tour": {
        "id": "ski_tour",
        "click_url": "https://px.a8.net/svt/ejp?a8mat=4BAH9J+3RQXSI+57BW+BXB8X",
        "image_url": "https://www24.a8.net/svt/bgt?aid=260829415228&wid=005&eno=01&mid=s00000024278002003000&mc=1",
        "pixel_url": "https://www16.a8.net/0.gif?a8mat=4BAH9J+3RQXSI+57BW+BXB8X",
        "label_en": "Ski tours from Tokyo",
        "label_ko": "도쿄 발 스키 투어",
        "desc_en": "Package ski trips — Big Holiday.",
        "desc_ko": "패키지 스키 투어 — 빅홀리데이.",
        "alt_en": "Ski tour booking — affiliate",
        "alt_ko": "Ski tour booking — affiliate",
    },
    "glamping": {
        "id": "glamping",
        "click_url": "https://px.a8.net/svt/ejp?a8mat=4BAH9J+3L764Y+5Q4K+5Z6WX",
        "image_url": "https://www28.a8.net/svt/bgt?aid=260829415217&wid=005&eno=01&mid=s00000026714001004000&mc=1",
        "pixel_url": "https://www18.a8.net/0.gif?a8mat=4BAH9J+3L764Y+5Q4K+5Z6WX",
        "label_en": "Glamping.com — Japan camps",
        "label_ko": "Glamping.com — 일본 글램핑",
        "desc_en": "Book glamping stays across Japan.",
        "desc_ko": "일본 글램핑 숙소 예약.",
        "alt_en": "Glamping booking — affiliate",
        "alt_ko": "글램핑 예약 — 제휴",
    },
}


def _enabled() -> bool:
    return os.getenv("A8_JPFUN_ENABLED", "1").strip().lower() in (
        "1",
        "true",
        "yes",
        "on",
    )


def _copy(banner_id: str, *, lang: str) -> dict[str, str]:
    src = _BANNERS[banner_id]
    is_ko = (lang or "en").lower() == "ko"
    suffix = "ko" if is_ko else "en"
    env_key = banner_id.upper()
    return {
        "id": src["id"],
        "click_url": os.getenv(f"A8_{env_key}_CLICK_URL", src["click_url"]),
        "image_url": os.getenv(f"A8_{env_key}_BANNER_URL", src["image_url"]),
        "pixel_url": os.getenv(f"A8_{env_key}_PIXEL_URL", src["pixel_url"]),
        "label": src[f"label_{suffix}"],
        "desc": src[f"desc_{suffix}"],
        "alt": src[f"alt_{suffix}"],
    }


def a8_banners_context(*, activity: str = "", lang: str = "en") -> dict[str, Any]:
    """A8 banners for item detail pages by activity type."""
    if not _enabled():
        return {"show_a8_banners": False, "a8_banners": []}

    act = (activity or "").strip().lower()
    keys = ["agoda", "tora_esim"]
    if act == "ski":
        keys.insert(0, "ski_tour")
    elif act == "camp":
        keys.append("glamping")

    banners = [_copy(k, lang=lang) for k in keys]
    is_ko = (lang or "en").lower() == "ko"
    return {
        "show_a8_banners": True,
        "a8_banners": banners,
        "a8_banners_title": (
            "여행·숙소 제휴" if is_ko else "Trip & stay partners"
        ),
        "a8_banners_note": (
            "제휴 광고 · 새 탭에서 열림"
            if is_ko
            else "Affiliate ads · opens in new tab"
        ),
    }
