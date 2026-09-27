"""A8.net affiliate banners for JPFun.

Agoda Partners + ski_tour (ski) + hinata (camp). TORA / glamping removed.
"""

from __future__ import annotations

import os
from typing import Any

_BANNERS: dict[str, dict[str, str]] = {
    "agoda": {
        "id": "agoda",
        "click_url": "",
        "image_url": "",
        "pixel_url": "",
        "label_en": "Agoda — Japan hotels",
        "label_ko": "Agoda — 일본 숙소 예약",
        "desc_en": "Search stays near this spot on Agoda.",
        "desc_ko": "이 스팟 주변 숙소를 Agoda에서 검색.",
        "alt_en": "Agoda hotel booking — affiliate",
        "alt_ko": "Agoda 숙소 예약 — 제휴",
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
    "hinata_rental": {
        "id": "hinata_rental",
        "click_url": "https://px.a8.net/svt/ejp?a8mat=4BCE3P+1C87V6+4U5Q+5YJRM",
        "image_url": "",
        "pixel_url": "https://www10.a8.net/0.gif?a8mat=4BCE3P+1C87V6+4U5Q+5YJRM",
        "label_en": "hinata — camp gear rental",
        "label_ko": "hinata렌탈 — 캠핑 용품",
        "desc_en": "Rent camping gear for pick-up at the campsite.",
        "desc_ko": "캠핑장에서 받는 캠핑 용품 렌탈.",
        "alt_en": "hinata rental — affiliate",
        "alt_ko": "hinata렌탈 — 제휴",
    },
}


def _enabled() -> bool:
    return os.getenv("A8_JPFUN_ENABLED", "1").strip().lower() in (
        "1",
        "true",
        "yes",
        "on",
    )


def _copy(
    banner_id: str,
    *,
    lang: str,
    lat: float | None = None,
    lng: float | None = None,
) -> dict[str, str]:
    src = _BANNERS[banner_id]
    is_ko = (lang or "en").lower() == "ko"
    suffix = "ko" if is_ko else "en"
    key = banner_id.upper()
    if banner_id == "agoda":
        try:
            from agoda_partners import url_for_location
        except ImportError:
            from .agoda_partners import url_for_location
        click = url_for_location(
            lang=lang,
            lat=lat,
            lng=lng,
            country="jp",
            default_city=5085,
        )
        return {
            "id": src["id"],
            "click_url": click,
            "image_url": "",
            "pixel_url": "",
            "label": src[f"label_{suffix}"],
            "desc": src[f"desc_{suffix}"],
            "alt": src[f"alt_{suffix}"],
        }
    return {
        "id": src["id"],
        "click_url": os.getenv(f"A8_{key}_CLICK_URL", src["click_url"]),
        "image_url": os.getenv(f"A8_{key}_BANNER_URL", src.get("image_url", "")),
        "pixel_url": os.getenv(f"A8_{key}_PIXEL_URL", src.get("pixel_url", "")),
        "label": src[f"label_{suffix}"],
        "desc": src[f"desc_{suffix}"],
        "alt": src[f"alt_{suffix}"],
    }


def a8_banners_context(
    *,
    activity: str = "",
    lang: str = "en",
    lat: float | None = None,
    lng: float | None = None,
) -> dict[str, Any]:
    if not _enabled():
        return {"show_a8_banners": False, "a8_banners": []}

    act = (activity or "").strip().lower()
    keys = ["agoda"]
    if act == "ski":
        keys.insert(0, "ski_tour")
    elif act == "camp":
        keys.append("hinata_rental")

    kw = {"lang": lang, "lat": lat, "lng": lng}
    banners = [_copy(k, **kw) for k in keys]
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
