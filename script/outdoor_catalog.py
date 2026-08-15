"""
JPFun MVP catalog — ski / surf / dive / camp seeds (EN/KO).
"""
from __future__ import annotations

from datetime import date
from typing import Any

LANGS = ("en", "ko")
TODAY = date.today().isoformat()

ACTIVITY_META = {
    "ski":  {"category": "Ski",  "emoji": "⛷️", "label_en": "Ski resort", "label_ko": "스키장"},
    "surf": {"category": "Surf", "emoji": "🏄", "label_en": "Surf spot",  "label_ko": "서핑 스팟"},
    "dive": {"category": "Dive", "emoji": "🤿", "label_en": "Dive site",  "label_ko": "다이빙 포인트"},
    "camp": {"category": "Camp", "emoji": "🏕️", "label_en": "Campground","label_ko": "캠핑장"},
}

# Lean MVP seed set (~14 places across four activities)
OUTDOOR_SEEDS: list[dict[str, Any]] = [
    # --- Ski ---
    {
        "id": "niseko_grand_hirafu",
        "activity": "ski",
        "region": "hokkaido",
        "names": {"en": "Niseko Grand Hirafu", "ko": "니세코 그란히라후"},
        "lat": 42.857,
        "lng": 140.706,
        "addresses": {
            "en": "Hirafu, Kutchan, Hokkaido, Japan",
            "ko": "일본 홋카이도 굿찬정 히라후",
        },
        "features": "Powder, Resort, Beginner",
        "website": "https://www.grand-hirafu.jp/",
        "blurb_en": "Niseko’s main powder base — village nightlife, English-friendly services, and linked United skiing.",
        "blurb_ko": "니세코의 대표 파우더 베이스. 히라후 마을 분위기와 United 연동 스키.",
    },
    {
        "id": "hakuba_happo_one",
        "activity": "ski",
        "region": "nagano",
        "names": {"en": "Hakuba Happo-one", "ko": "하쿠바 햇포원"},
        "lat": 36.702,
        "lng": 137.862,
        "addresses": {
            "en": "Happo, Hakuba, Nagano, Japan",
            "ko": "일본 나가노현 하쿠바촌 햇포",
        },
        "features": "Olympic, Vertical, Village",
        "website": "https://www.happo-one.jp/",
        "blurb_en": "Olympic-scale vertical in Hakuba Valley with strong Tokyo access and après options.",
        "blurb_ko": "하쿠바 밸리의 올림픽급 버티컬. 도쿄 접근성과 애프터스키가 강점.",
    },
    {
        "id": "gala_yuzawa",
        "activity": "ski",
        "region": "niigata",
        "names": {"en": "GALA Yuzawa Snow Resort", "ko": "가라 유자와"},
        "lat": 36.948,
        "lng": 138.803,
        "addresses": {
            "en": "Yuzawa, Niigata, Japan",
            "ko": "일본 니가타현 유자와마치",
        },
        "features": "Shinkansen, Day trip, Beginner",
        "website": "https://gala.co.jp/",
        "blurb_en": "Ski-in from the Shinkansen — classic Tokyo day-trip powder with onsen town below.",
        "blurb_ko": "신칸센 직결 스키장. 도쿄 당일 스키와 유자와 온천이 한 세트.",
    },
    {
        "id": "nozawa_onsen",
        "activity": "ski",
        "region": "nagano",
        "names": {"en": "Nozawa Onsen Ski Resort", "ko": "노자와온천 스키장"},
        "lat": 36.922,
        "lng": 138.441,
        "addresses": {
            "en": "Nozawaonsen, Nagano, Japan",
            "ko": "일본 나가노현 노자와온천촌",
        },
        "features": "Village, Onsen, Powder",
        "website": "https://www.nozawaski.com/",
        "blurb_en": "Historic onsen village skiing — slopes above public baths and traditional lodging.",
        "blurb_ko": "온천 마을 위 슬로프. 료칸·공동욕장과 파우더가 한곳에.",
    },
    # --- Surf ---
    {
        "id": "shonan_kugenuma",
        "activity": "surf",
        "region": "kanto",
        "names": {"en": "Shonan Kugenuma Beach", "ko": "쇼난 구게누마 비치"},
        "lat": 35.320,
        "lng": 139.486,
        "addresses": {
            "en": "Kugenuma, Fujisawa, Kanagawa, Japan",
            "ko": "일본 가나가와현 후지사와시 구게누마",
        },
        "features": "Beginner, Train access, Schools",
        "website": "",
        "blurb_en": "Classic Shonan beach break near Tokyo — schools, rentals, and easy Odakyu access.",
        "blurb_ko": "도쿄 근교 쇼난 대표 비치. 스쿨·렌탈과 전철 접근이 편함.",
    },
    {
        "id": "chiba_hebara",
        "activity": "surf",
        "region": "kanto",
        "names": {"en": "Hebara Beach (Isumi)", "ko": "헤바라 비치 (이스미)"},
        "lat": 35.254,
        "lng": 140.404,
        "addresses": {
            "en": "Hebara, Isumi, Chiba, Japan",
            "ko": "일본 치바현 이스미시 헤바라",
        },
        "features": "Consistent, Intermediate, Pacific",
        "website": "",
        "blurb_en": "Pacific-facing Chiba break popular with Tokyo weekenders — consistent swell windows.",
        "blurb_ko": "도쿄 주말러가 많이 찾는 치바 태평양 스팟. 스웰이 비교적 꾸준함.",
    },
    {
        "id": "okinawa_sunayama",
        "activity": "surf",
        "region": "okinawa",
        "names": {"en": "Sunayama Beach area (Miyako)", "ko": "스나야마 비치 (미야코)"},
        "lat": 24.805,
        "lng": 125.281,
        "addresses": {
            "en": "Hirara, Miyakojima, Okinawa, Japan",
            "ko": "일본 오키나와현 미야코지마 히라라",
        },
        "features": "Island, Scenic, Winter swell",
        "website": "",
        "blurb_en": "Miyako island surfing near iconic sand-hill beach — winter north swell season.",
        "blurb_ko": "미야코 모래언덕 비치 인근 서핑. 겨울 북쪽 스웰 시즌이 핵심.",
    },
    {
        "id": "ibaraki_oaraibaraki",
        "activity": "surf",
        "region": "kanto",
        "names": {"en": "Oarai Surf Area", "ko": "오아라이 서프 에리어"},
        "lat": 36.313,
        "lng": 140.592,
        "addresses": {
            "en": "Oarai, Ibaraki, Japan",
            "ko": "일본 이바라키현 오아라이정",
        },
        "features": "Point / Beach, Intermediate",
        "website": "",
        "blurb_en": "Ibaraki coast surf with harbor and beach options — popular north of Tokyo.",
        "blurb_ko": "도쿄 북쪽 이바라키 해안 서핑. 하버·비치 옵션이 다양.",
    },
    # --- Dive ---
    {
        "id": "okinawa_kerama",
        "activity": "dive",
        "region": "okinawa",
        "names": {"en": "Kerama Islands Dive Area", "ko": "케라마 제도 다이빙"},
        "lat": 26.200,
        "lng": 127.350,
        "addresses": {
            "en": "Kerama Islands, Okinawa, Japan",
            "ko": "일본 오키나와현 케라마 제도",
        },
        "features": "Clear water, Day boat, All levels",
        "website": "",
        "blurb_en": "World-class visibility day-boat diving from Naha / Zamami — turtles and soft coral gardens.",
        "blurb_ko": "나하·자마미 출발 데이보트 다이빙. 투명도와 바다거북으로 유명.",
    },
    {
        "id": "izu_oshima",
        "activity": "dive",
        "region": "chubu",
        "names": {"en": "Izu Oshima Dive Spots", "ko": "이즈 오시마 다이빙"},
        "lat": 34.737,
        "lng": 139.400,
        "addresses": {
            "en": "Oshima, Tokyo, Japan",
            "ko": "일본 도쿄도 오시마정",
        },
        "features": "Volcanic rock, Weekend, Schools",
        "website": "",
        "blurb_en": "Tokyo island diving with volcanic rock reefs — ferry access and local dive shops.",
        "blurb_ko": "화산암 리프의 도쿄 도서 다이빙. 페리와 로컬 샵 접근.",
    },
    {
        "id": "okinawa_ishigaki_manta",
        "activity": "dive",
        "region": "okinawa",
        "names": {"en": "Ishigaki Manta Scramble Area", "ko": "이시가키 만타 스크램블"},
        "lat": 24.336,
        "lng": 124.156,
        "addresses": {
            "en": "Ishigaki, Okinawa, Japan",
            "ko": "일본 오키나와현 이시가키시",
        },
        "features": "Manta, Boat, Intermediate+",
        "website": "",
        "blurb_en": "Famous manta cleaning-station dives off Ishigaki — book boats early in peak season.",
        "blurb_ko": "이시가키 만타 클리닝 스테이션. 성수기에는 보트 예약을 서두르세요.",
    },
    # --- Camp ---
    {
        "id": "fuji_motosu_camp",
        "activity": "camp",
        "region": "chubu",
        "names": {"en": "Lake Motosu Camp Area", "ko": "모토스코 캠프 에리어"},
        "lat": 35.462,
        "lng": 138.687,
        "addresses": {
            "en": "Lake Motosu, Fujikawaguchiko, Yamanashi, Japan",
            "ko": "일본 야마나시현 후지카와구치코 모토스코",
        },
        "features": "Fuji view, Car camp, Lakeside",
        "website": "",
        "blurb_en": "Fuji lakeside camping classic — car-camp sites and iconic Motosu reflections.",
        "blurb_ko": "후지산 호수 캠핑 클래식. 모토스코 역광 뷰와 차박 사이트.",
    },
    {
        "id": "hakuba_camp",
        "activity": "camp",
        "region": "nagano",
        "names": {"en": "Hakuba Alpine Camp Bases", "ko": "하쿠바 알파인 캠프"},
        "lat": 36.698,
        "lng": 137.862,
        "addresses": {
            "en": "Hakuba, Nagano, Japan",
            "ko": "일본 나가노현 하쿠바촌",
        },
        "features": "Mountain, Summer, Glamping",
        "website": "",
        "blurb_en": "Summer alpine camping and glamping near Hakuba trails — winter ski town flips to outdoor base.",
        "blurb_ko": "하쿠바 트레일 근처 여름 알파인 캠프·글램핑. 겨울 스키 타운이 야외 베이스로.",
    },
    {
        "id": "shimanami_camp",
        "activity": "camp",
        "region": "chugoku",
        "names": {"en": "Shimanami Kaido Camp Stops", "ko": "시마나미 해도 캠프 스톱"},
        "lat": 34.270,
        "lng": 133.050,
        "addresses": {
            "en": "Onomichi–Imabari route, Japan",
            "ko": "일본 오노미치–이마바리 시마나미 루트",
        },
        "features": "Cycle camp, Island hops, Sea view",
        "website": "",
        "blurb_en": "Island-hop camping along Japan’s famous cycle route — sea views and bike-friendly sites.",
        "blurb_ko": "시마나미 사이클 루트의 섬 캠핑. 바다 뷰와 자전거 친화 사이트.",
    },
]


def _category(activity: str) -> str:
    return ACTIVITY_META[activity]["category"]


def article(lang: str, seed: dict[str, Any]) -> str:
    activity = seed["activity"]
    meta = ACTIVITY_META[activity]
    name = seed["names"][lang]
    addr = seed["addresses"][lang]
    website = (seed.get("website") or "").strip()
    website_line = f"website: \"{website}\"\n" if website else "website: \"\"\n"
    cat = _category(activity)

    if lang == "ko":
        blurb = seed["blurb_ko"]
        body = f"""## 개요

**{name}** — {blurb}

JPFun 지도에서 같은 지역의 다른 레저 스팟과 함께 볼 수 있습니다.

## 포인트

- 활동: {meta['label_ko']}
- 지역 키: {seed['region']}
- 특징: {seed.get('features') or meta['label_ko']}

## 여행 팁

- 시즌·날씨·조수(서프/다이브)를 출발 전에 확인하세요.
- 렌탈·스쿨·보트는 성수기 예약을 권장합니다.
- 근처 숙소는 지도의 Stay 핀 또는 Rakuten / Klook로 이어집니다.
"""
        summary = blurb
    else:
        blurb = seed["blurb_en"]
        body = f"""## Overview

**{name}** — {blurb}

Browse it on the JPFun map alongside other leisure spots in the same region.

## Highlights

- Activity: {meta['label_en']}
- Region key: {seed['region']}
- Features: {seed.get('features') or meta['label_en']}

## Trip tips

- Check season, weather, and tides (surf/dive) before you go.
- Book rentals, schools, and boats early in peak months.
- Nearby lodging: map Stay pins or Rakuten / Klook from the detail page.
"""
        summary = blurb

    return f"""---
lang: {lang}
title: "{name}"
lat: {seed['lat']}
lng: {seed['lng']}
activity: "{activity}"
categories: ["{cat}"]
thumbnail: "/static/images/default.jpg"
address: "{addr}"
date: "{TODAY}"
{website_line}summary: "{summary}"
image_prompt: ""
region: "{seed['region']}"
---

{body}
"""
