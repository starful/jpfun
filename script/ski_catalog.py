"""
Shared ski resort + nearby POI catalog helpers for OKSki (EN/KO only).
"""
from __future__ import annotations

import hashlib
import math
from datetime import datetime
from typing import Any

LANGS = ("en", "ko")

SKI_RESORT_SEEDS: list[dict[str, Any]] = [
    {
        "id": "niseko_grand_hirafu",
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
    },
    {
        "id": "niseko_hanazono",
        "region": "hokkaido",
        "names": {"en": "Niseko Hanazono", "ko": "니세코 하나조노"},
        "lat": 42.897,
        "lng": 140.715,
        "addresses": {
            "en": "Hanazono, Kutchan, Hokkaido, Japan",
            "ko": "일본 홋카이도 굿찬정 하나조노",
        },
        "features": "Powder, Family, Resort",
        "website": "https://www.niseko.ne.jp/",
    },
    {
        "id": "niseko_annupuri",
        "region": "hokkaido",
        "names": {"en": "Niseko Annupuri", "ko": "니세코 아누푸리"},
        "lat": 42.884,
        "lng": 140.684,
        "addresses": {
            "en": "Annupuri, Niseko, Hokkaido, Japan",
            "ko": "일본 홋카이도 니세코정 아누푸리",
        },
        "features": "Powder, Local vibe",
        "website": "",
    },
    {
        "id": "rusutsu",
        "region": "hokkaido",
        "names": {"en": "Rusutsu Resort", "ko": "루스츠 리조트"},
        "lat": 42.737,
        "lng": 140.904,
        "addresses": {
            "en": "Rusutsu, Abuta, Hokkaido, Japan",
            "ko": "일본 홋카이도 아부타군 루스츠",
        },
        "features": "Family, Resort, Powder",
        "website": "https://rusutsu.co.jp/",
    },
    {
        "id": "furano",
        "region": "hokkaido",
        "names": {"en": "Furano Ski Resort", "ko": "후라노 스키장"},
        "lat": 43.342,
        "lng": 142.384,
        "addresses": {
            "en": "Furano, Hokkaido, Japan",
            "ko": "일본 홋카이도 후라노",
        },
        "features": "Scenic, Family, Powder",
        "website": "https://www.princehotels.co.jp/ski/furano/",
    },
    {
        "id": "hakuba_happo_one",
        "region": "nagano",
        "names": {"en": "Hakuba Happo-one", "ko": "하쿠바 해포"},
        "lat": 36.698,
        "lng": 137.837,
        "addresses": {
            "en": "Happo, Hakuba, Nagano, Japan",
            "ko": "일본 나가노현 하쿠바촌 해포",
        },
        "features": "Championship, Olympic, Powder",
        "website": "https://www.happo-one.jp/",
    },
    {
        "id": "hakuba_goryu",
        "region": "nagano",
        "names": {"en": "Hakuba Goryu", "ko": "하쿠바 고류"},
        "lat": 36.698,
        "lng": 137.855,
        "addresses": {
            "en": "Kamishiro, Hakuba, Nagano, Japan",
            "ko": "일본 나가노현 하쿠바촌 고류",
        },
        "features": "Family, Tree runs",
        "website": "https://www.hakubaescal.com/",
    },
    {
        "id": "hakuba_47",
        "region": "nagano",
        "names": {"en": "Hakuba 47 Winter Sports Park", "ko": "하쿠바 47"},
        "lat": 36.692,
        "lng": 137.826,
        "addresses": {
            "en": "Kamishiro, Hakuba, Nagano, Japan",
            "ko": "일본 나가노현 하쿠바촌 47",
        },
        "features": "Park, Freestyle, Powder",
        "website": "https://www.hakuba47.co.jp/",
    },
    {
        "id": "nozawa_onsen",
        "region": "nagano",
        "names": {"en": "Nozawa Onsen Ski Resort", "ko": "노자와 온센 스키장"},
        "lat": 36.920,
        "lng": 138.440,
        "addresses": {
            "en": "Nozawaonsen, Nagano, Japan",
            "ko": "일본 나가노현 노자와온센",
        },
        "features": "Onsen, Village, Traditional",
        "website": "https://nozawaski.com/",
    },
    {
        "id": "gala_yuzawa",
        "region": "niigata",
        "names": {"en": "Gala Yuzawa", "ko": "갈라 유자와"},
        "lat": 36.901,
        "lng": 138.778,
        "addresses": {
            "en": "Yuzawa, Niigata, Japan",
            "ko": "일본 니가타현 유자와",
        },
        "features": "Day-trip, Tokyo access, Beginner",
        "website": "https://gala.co.jp/",
    },
    {
        "id": "naeba",
        "region": "niigata",
        "names": {"en": "Naeba Ski Resort", "ko": "나에바 스키장"},
        "lat": 36.871,
        "lng": 138.755,
        "addresses": {
            "en": "Yuzawa, Niigata, Japan",
            "ko": "일본 니가타현 유자와 나에바",
        },
        "features": "Resort, Family, Snow festival",
        "website": "https://www.princehotels.co.jp/ski/naeba/",
    },
    {
        "id": "myoko_suginohara",
        "region": "niigata",
        "names": {"en": "Myoko Suginohara", "ko": "묘코 스기노하라"},
        "lat": 36.876,
        "lng": 138.142,
        "addresses": {
            "en": "Myoko, Niigata, Japan",
            "ko": "일본 니가타현 묘코 시 스기노하라",
        },
        "features": "Longest run, Powder, Family",
        "website": "https://www.suginohara.com/",
    },
    # --- Expansion batch (~20) ---
    {
        "id": "niseko_village",
        "region": "hokkaido",
        "names": {"en": "Niseko Village", "ko": "니세코 빌리지"},
        "lat": 42.858,
        "lng": 140.682,
        "addresses": {
            "en": "Higashiyama, Niseko, Hokkaido, Japan",
            "ko": "일본 홋카이도 니세코정 히가시야마",
        },
        "features": "Resort hotel, Powder, United pass",
        "website": "https://www.niseko-village.com/",
    },
    {
        "id": "kiroro",
        "region": "hokkaido",
        "names": {"en": "Kiroro Resort", "ko": "키로로 리조트"},
        "lat": 43.063,
        "lng": 140.993,
        "addresses": {
            "en": "Akaigawa, Hokkaido, Japan",
            "ko": "일본 홋카이도 아카이가와촌",
        },
        "features": "Powder, Family, Resort",
        "website": "https://www.kiroro.co.jp/",
    },
    {
        "id": "tomamu",
        "region": "hokkaido",
        "names": {"en": "Hoshino Resorts Tomamu", "ko": "호시노 리조트 토마무"},
        "lat": 43.066,
        "lng": 142.610,
        "addresses": {
            "en": "Shimukappu, Hokkaido, Japan",
            "ko": "일본 홋카이도 시무캅푸촌 토마무",
        },
        "features": "Ice Village, Family, Scenic",
        "website": "https://www.snowtomamu.jp/",
    },
    {
        "id": "sahoro",
        "region": "hokkaido",
        "names": {"en": "Sahoro Resort", "ko": "사호로 리조트"},
        "lat": 43.168,
        "lng": 142.815,
        "addresses": {
            "en": "Shintoku, Hokkaido, Japan",
            "ko": "일본 홋카이도 신토쿠정",
        },
        "features": "Quiet powder, Bear mountain, Family",
        "website": "https://www.sahoro.co.jp/",
    },
    {
        "id": "sapporo_teine",
        "region": "hokkaido",
        "names": {"en": "Sapporo Teine", "ko": "삿포로 데이네"},
        "lat": 43.084,
        "lng": 141.208,
        "addresses": {
            "en": "Teine, Sapporo, Hokkaido, Japan",
            "ko": "일본 홋카이도 삿포로시 데이네",
        },
        "features": "City access, Night skiing, Olympic",
        "website": "https://sapporo-teine.com/",
    },
    {
        "id": "sapporo_kokusai",
        "region": "hokkaido",
        "names": {"en": "Sapporo Kokusai Ski Resort", "ko": "삿포로 고쿠사이"},
        "lat": 43.000,
        "lng": 141.098,
        "addresses": {
            "en": "Jozankei, Sapporo, Hokkaido, Japan",
            "ko": "일본 홋카이도 삿포로시 조잔케이",
        },
        "features": "Powder, Tree runs, Day trip from Sapporo",
        "website": "https://www.sapporo-kokusai.jp/",
    },
    {
        "id": "asahidake",
        "region": "hokkaido",
        "names": {"en": "Asahidake Ropeway Ski Area", "ko": "아사히다케 스키장"},
        "lat": 43.659,
        "lng": 142.810,
        "addresses": {
            "en": "Higashikawa, Hokkaido, Japan",
            "ko": "일본 홋카이도 히가시카와정 아사히다케",
        },
        "features": "Backcountry, Volcano views, Advanced",
        "website": "https://asahidake.hokkaido.jp/",
    },
    {
        "id": "hakuba_iwatake",
        "region": "nagano",
        "names": {"en": "Hakuba Iwatake Mountain Resort", "ko": "하쿠바 이와타케"},
        "lat": 36.712,
        "lng": 137.861,
        "addresses": {
            "en": "Hokujo, Hakuba, Nagano, Japan",
            "ko": "일본 나가노현 하쿠바촌 호쿠조",
        },
        "features": "Mountain views, Gondola dining, Intermediate",
        "website": "https://www.iwatake-mountain-resort.com/",
    },
    {
        "id": "hakuba_cortina",
        "region": "nagano",
        "names": {"en": "Hakuba Cortina", "ko": "하쿠바 코르티나"},
        "lat": 36.768,
        "lng": 137.874,
        "addresses": {
            "en": "Otari, Nagano, Japan",
            "ko": "일본 나가노현 오타리촌",
        },
        "features": "Powder, Quiet base, Onsen lodging",
        "website": "https://www.hakuba-cortina.jp/",
    },
    {
        "id": "tsugaike_kogen",
        "region": "nagano",
        "names": {"en": "Tsugaike Kogen", "ko": "츠가이케 고원"},
        "lat": 36.761,
        "lng": 137.845,
        "addresses": {
            "en": "Otari, Nagano, Japan",
            "ko": "일본 나가노현 오타리촌 츠가이케",
        },
        "features": "Family, Long season, Hakuba Valley",
        "website": "https://www.tsugaike.gr.jp/",
    },
    {
        "id": "shiga_kogen",
        "region": "nagano",
        "names": {"en": "Shiga Kogen", "ko": "시가 고원"},
        "lat": 36.738,
        "lng": 138.510,
        "addresses": {
            "en": "Yamanouchi, Nagano, Japan",
            "ko": "일본 나가노현 야마노우치정",
        },
        "features": "Multi-resort pass, Long season, Variety",
        "website": "https://www.shigakogen.gr.jp/",
    },
    {
        "id": "madarao_kogen",
        "region": "nagano",
        "names": {"en": "Madarao Kogen", "ko": "마다라오 고원"},
        "lat": 36.845,
        "lng": 138.280,
        "addresses": {
            "en": "Iiyama, Nagano, Japan",
            "ko": "일본 나가노현 이야마시",
        },
        "features": "Tree runs, Powder, Linked Tangram",
        "website": "https://www.madarao.jp/",
    },
    {
        "id": "tangram_ski_circus",
        "region": "nagano",
        "names": {"en": "Tangram Ski Circus", "ko": "탱그램 스키 서커스"},
        "lat": 36.833,
        "lng": 138.265,
        "addresses": {
            "en": "Shinano, Nagano, Japan",
            "ko": "일본 나가노현 시나노정",
        },
        "features": "Family, Night skiing, Linked Madarao",
        "website": "https://www.tangram.jp/",
    },
    {
        "id": "karuizawa_prince",
        "region": "nagano",
        "names": {"en": "Karuizawa Prince Hotel Ski Resort", "ko": "가루이자와 프린스 스키장"},
        "lat": 36.342,
        "lng": 138.597,
        "addresses": {
            "en": "Karuizawa, Nagano, Japan",
            "ko": "일본 나가노현 가루이자와",
        },
        "features": "Beginner-friendly, Tokyo access, Resort hotel",
        "website": "https://www.princehotels.co.jp/ski/karuizawa/",
    },
    {
        "id": "kagura",
        "region": "niigata",
        "names": {"en": "Kagura Ski Resort", "ko": "카구라 스키장"},
        "lat": 36.856,
        "lng": 138.776,
        "addresses": {
            "en": "Yuzawa, Niigata, Japan",
            "ko": "일본 니가타현 유자와정 카구라",
        },
        "features": "Linked Naeba, Long runs, Powder",
        "website": "https://www.princehotels.co.jp/ski/kagura/",
    },
    {
        "id": "iwappara",
        "region": "niigata",
        "names": {"en": "Iwappara Ski Resort", "ko": "이와파라 스키장"},
        "lat": 36.932,
        "lng": 138.812,
        "addresses": {
            "en": "Yuzawa, Niigata, Japan",
            "ko": "일본 니가타현 유자와정 이와파라",
        },
        "features": "Day-trip, Family, Wide slopes",
        "website": "https://www.iwappara.com/",
    },
    {
        "id": "yuzawa_kogen",
        "region": "niigata",
        "names": {"en": "Yuzawa Kogen", "ko": "유자와 고원"},
        "lat": 36.935,
        "lng": 138.805,
        "addresses": {
            "en": "Yuzawa, Niigata, Japan",
            "ko": "일본 니가타현 유자와정",
        },
        "features": "Town access, Beginner, Onsen town",
        "website": "https://www.yuzawakogen.com/",
    },
    {
        "id": "joetsu_kokusai",
        "region": "niigata",
        "names": {"en": "Joetsu Kokusai Ski Resort", "ko": "조에츠 고쿠사이"},
        "lat": 36.968,
        "lng": 138.745,
        "addresses": {
            "en": "Minamiuonuma, Niigata, Japan",
            "ko": "일본 니가타현 미나미우오누마",
        },
        "features": "Huge terrain, Family, Varied runs",
        "website": "https://www.j-kokusai.com/",
    },
    {
        "id": "maiko_snow_resort",
        "region": "niigata",
        "names": {"en": "Maiko Snow Resort", "ko": "마이코 스노우 리조트"},
        "lat": 37.036,
        "lng": 138.812,
        "addresses": {
            "en": "Minamiuonuma, Niigata, Japan",
            "ko": "일본 니가타현 미나미우오누마 마이코",
        },
        "features": "Powder, Tree skiing, Soft snow",
        "website": "https://www.maiko-resort.com/",
    },
    {
        "id": "ipponsugi",
        "region": "niigata",
        "names": {"en": "Ipponsugi Ski Resort", "ko": "잇폰스기 스키장"},
        "lat": 36.948,
        "lng": 138.802,
        "addresses": {
            "en": "Yuzawa, Niigata, Japan",
            "ko": "일본 니가타현 유자와정 잇폰스기",
        },
        "features": "Day-trip, Compact, Town base",
        "website": "https://www.ipponsugi.net/",
    },
    # --- New regions: tohoku / gifu / gunma / tochigi (4 each) ---
    {
        "id": "zao_onsen",
        "region": "tohoku",
        "names": {"en": "Zao Onsen Ski Resort", "ko": "자오 온센 스키장"},
        "lat": 38.166,
        "lng": 140.424,
        "addresses": {
            "en": "Zao Onsen, Yamagata, Japan",
            "ko": "일본 야마가타현 자오 온센",
        },
        "features": "Onsen, Juhyo, Varied terrain",
        "website": "https://www.zao-spa.or.jp/",
    },
    {
        "id": "appi_kogen",
        "region": "tohoku",
        "names": {"en": "Appi Kogen Ski Resort", "ko": "앗피 고원 스키장"},
        "lat": 40.000,
        "lng": 140.978,
        "addresses": {
            "en": "Appi Kogen, Hachimantai, Iwate, Japan",
            "ko": "일본 이와테현 하치만타이 앗피 고원",
        },
        "features": "Resort, High elevation, Powder",
        "website": "https://www.appi.co.jp/",
    },
    {
        "id": "geto_kogen",
        "region": "tohoku",
        "names": {"en": "Geto Kogen Ski Resort", "ko": "게토 고원 스키장"},
        "lat": 39.221,
        "lng": 140.890,
        "addresses": {
            "en": "Geto, Kitakami, Iwate, Japan",
            "ko": "일본 이와테현 기타카미 게토",
        },
        "features": "Powder, Tree runs, Quiet",
        "website": "https://www.getokogen.com/",
    },
    {
        "id": "alts_bandai",
        "region": "tohoku",
        "names": {"en": "Alts Bandai", "ko": "알츠 반다이"},
        "lat": 37.627,
        "lng": 140.055,
        "addresses": {
            "en": "Bandai, Yama, Fukushima, Japan",
            "ko": "일본 후쿠시마현 반다이",
        },
        "features": "Family, Big terrain, All levels",
        "website": "https://www.alts.co.jp/",
    },
    {
        "id": "takasu_snow_park",
        "region": "gifu",
        "names": {"en": "Takasu Snow Park", "ko": "다카스 스노우파크"},
        "lat": 36.004,
        "lng": 136.858,
        "addresses": {
            "en": "Takasu, Gujo, Gifu, Japan",
            "ko": "일본 기후현 구조시 다카스",
        },
        "features": "Powder, Linked dynaland, Distance",
        "website": "https://www.takasu.or.jp/",
    },
    {
        "id": "dynaland",
        "region": "gifu",
        "names": {"en": "Dynaland", "ko": "다이나랜드"},
        "lat": 35.983,
        "lng": 136.866,
        "addresses": {
            "en": "Takasu, Gujo, Gifu, Japan",
            "ko": "일본 기후현 구조시 다이나랜드",
        },
        "features": "Family, Linked Takasu, Beginner",
        "website": "https://www.dynaland.jp/",
    },
    {
        "id": "hirayu_onsen",
        "region": "gifu",
        "names": {"en": "Hirayu Onsen Ski Area", "ko": "히라유 온센 스키장"},
        "lat": 36.185,
        "lng": 137.555,
        "addresses": {
            "en": "Hirayu, Takayama, Gifu, Japan",
            "ko": "일본 기후현 다카야마 히라유",
        },
        "features": "Onsen, Compact, Scenic",
        "website": "https://hirayuonsen.jp/",
    },
    {
        "id": "washigatake",
        "region": "gifu",
        "names": {"en": "Washigatake Ski Resort", "ko": "와시가타케 스키장"},
        "lat": 35.920,
        "lng": 136.820,
        "addresses": {
            "en": "Gujo, Gifu, Japan",
            "ko": "일본 기후현 구조시 와시가타케",
        },
        "features": "Family, Night skiing, Local",
        "website": "https://www.washigatake.jp/",
    },
    {
        "id": "kusatsu_kokusai",
        "region": "gunma",
        "names": {"en": "Kusatsu Onsen Ski Area", "ko": "구사쓰 온센 스키장"},
        "lat": 36.621,
        "lng": 138.597,
        "addresses": {
            "en": "Kusatsu, Gunma, Japan",
            "ko": "일본 군마현 구사쓰",
        },
        "features": "Onsen, Day-trip, Village",
        "website": "https://www.kusatsu-onsen.or.jp/",
    },
    {
        "id": "manza_onsen",
        "region": "gunma",
        "names": {"en": "Manza Onsen Ski Resort", "ko": "만자 온센 스키장"},
        "lat": 36.645,
        "lng": 138.515,
        "addresses": {
            "en": "Manza, Tsumagoi, Gunma, Japan",
            "ko": "일본 군마현 쓰마고이 만자",
        },
        "features": "High elevation, Onsen, Snow",
        "website": "https://www.princehotels.co.jp/ski/manza/",
    },
    {
        "id": "kawaba",
        "region": "gunma",
        "names": {"en": "Kawaba Ski Resort", "ko": "카와바 스키장"},
        "lat": 36.714,
        "lng": 139.106,
        "addresses": {
            "en": "Kawaba, Tone, Gunma, Japan",
            "ko": "일본 군마현 카와바",
        },
        "features": "Powder, Tree runs, Day-trip",
        "website": "https://www.kawaba.co.jp/",
    },
    {
        "id": "minakami_hotaka",
        "region": "gunma",
        "names": {"en": "Minakami Hotaka Ski Resort", "ko": "미나카미 호타카 스키장"},
        "lat": 36.801,
        "lng": 138.990,
        "addresses": {
            "en": "Minakami, Tone, Gunma, Japan",
            "ko": "일본 군마현 미나카미",
        },
        "features": "Tokyo access, Family, Varied",
        "website": "https://www.hotaka.or.jp/",
    },
    {
        "id": "hunter_mountain_shiobara",
        "region": "tochigi",
        "names": {"en": "Hunter Mountain Shiobara", "ko": "헌터마운틴 시오바라"},
        "lat": 37.015,
        "lng": 139.835,
        "addresses": {
            "en": "Shiobara, Nasushiobara, Tochigi, Japan",
            "ko": "일본 도치기현 나스시오바라 시오바라",
        },
        "features": "Big resort, Park, Family",
        "website": "https://www.hunter.co.jp/",
    },
    {
        "id": "mt_jeans_nasu",
        "region": "tochigi",
        "names": {"en": "Mt. Jeans Nasu", "ko": "마운트진스 나스"},
        "lat": 37.116,
        "lng": 139.980,
        "addresses": {
            "en": "Nasu, Tochigi, Japan",
            "ko": "일본 도치기현 나스",
        },
        "features": "Family, Beginner, Day-trip",
        "website": "https://www.mtjeans.com/",
    },
    {
        "id": "kirifuri_kogen",
        "region": "tochigi",
        "names": {"en": "Kirifuri Kogen Ski Resort", "ko": "키리후리 고원 스키장"},
        "lat": 36.755,
        "lng": 139.530,
        "addresses": {
            "en": "Nikko, Tochigi, Japan",
            "ko": "일본 도치기현 닛코 키리후리",
        },
        "features": "Scenic, Family, Compact",
        "website": "https://www.kirifuri-kogen.com/",
    },
    {
        "id": "nasu_onsen_family",
        "region": "tochigi",
        "names": {"en": "Nasu Onsen Family Ski Area", "ko": "나스 온센 패밀리 스키장"},
        "lat": 37.091,
        "lng": 139.956,
        "addresses": {
            "en": "Nasu, Tochigi, Japan",
            "ko": "일본 도치기현 나스 온센",
        },
        "features": "Beginner, Family, Easy access",
        "website": "https://www.nasuonsen.co.jp/",
    },
]


def offset_latlng(lat: float, lng: float, north_m: float, east_m: float) -> tuple[float, float]:
    dlat = north_m / 111_320.0
    dlng = east_m / (111_320.0 * max(0.2, math.cos(math.radians(lat))))
    return round(lat + dlat, 6), round(lng + dlng, 6)


def stable_id(*parts: str) -> str:
    raw = "|".join(parts)
    return hashlib.md5(raw.encode()).hexdigest()[:10]


def resort_article(lang: str, resort: dict[str, Any]) -> str:
    from ski_longform import LONGFORM

    today = datetime.now().strftime("%Y-%m-%d")
    name = resort["names"][lang]
    address = resort["addresses"][lang]
    features = resort.get("features") or "Ski resort"
    rid = resort["id"]
    website = resort.get("website") or ""

    longform = LONGFORM.get(rid)
    if longform:
        summary_key = f"summary_{lang}"
        summary = longform.get(summary_key) or (
            f"{name} — lift tickets, lodging, and access tips for Japan ski trips."
            if lang == "en"
            else f"{name} — 일본 스키 여행을 위한 리프트·숙소·접근 정보."
        )
        body = longform[lang]
        return f"""---
lang: {lang}
title: "{name}"
lat: {resort["lat"]}
lng: {resort["lng"]}
categories: ["Ski"]
thumbnail: "/static/images/{rid}.jpg"
address: "{address}"
date: "{today}"
website: "{website}"
summary: "{summary}"
image_prompt: ""
region: "{resort["region"]}"
---

{body}
"""

    summaries = {
        "en": f"{name} — lift tickets, lodging, and access tips for Japan ski trips.",
        "ko": f"{name} — 일본 스키 여행을 위한 리프트·숙소·접근 정보.",
    }

    bodies = {
        "en": f"""## Overview

{name} is one of Japan's most searched ski destinations ({features}). Use this page to plan lift access, lodging, and day-one logistics.

OKSki lists resorts on the map with curated **Stay** and **Food** pins nearby — not generic Google POIs.

## Resort highlights

- **Region:** {address}
- **Style:** {features}
- **Official site:** {website or "Check resort site before booking"}

## Planning tips

- Book lodging early for peak season (late Dec – Feb).
- Compare lift passes vs. multi-day tickets on the official site.
- Use the map's Stay / Food pins for walkable options after skiing.

## Getting there

- **Address:** {address}
- Shinkansen + bus or rental car are common from Tokyo (varies by resort).
- Confirm shuttle times from the nearest station when you book stay.
""",
        "ko": f"""## 개요

{name}은(는) 한국인 일본 스키 여행자가 자주 찾는 코스입니다 ({features}). 리프트, 숙소, 당일 이동을 여기서 정리하세요.

OKSki 지도에는 스키장 근처 **숙소(Stay)**·**맛집(Food)** 핀을 따로 표시합니다.

## 리조트 특징

- **위치:** {address}
- **스타일:** {features}
- **공식 사이트:** {website or "예약 전 공식 사이트 확인"}

## 실전 팁

- 성수기(12월 말~2월) 숙소는 미리 예약하세요.
- 리프트권·연속권은 공식 사이트에서 비교하는 것이 좋습니다.
- 지도의 Stay / Food 핀으로 근처 숙소·식사를 확인하세요.

## 오는 길

- **주소:** {address}
- 도쿄에서 신칸센+버스 또는 렌터카가 일반적입니다(리조트마다 다름).
- 숙소 예약 시 최근역 셔틀 시간을 꼭 확인하세요.
""",
    }

    return f"""---
lang: {lang}
title: "{name}"
lat: {resort["lat"]}
lng: {resort["lng"]}
categories: ["Ski"]
thumbnail: "/static/images/{rid}.jpg"
address: "{address}"
date: "{today}"
website: "{website}"
summary: "{summaries[lang]}"
image_prompt: ""
region: "{resort["region"]}"
---

{bodies[lang]}
"""


def build_nearby_for_resort(resort: dict[str, Any], *, stay_n: int = 2, food_n: int = 2) -> list[dict]:
    """Seed Stay/Food POIs around a ski resort (EN/KO i18n)."""
    lat0, lng0 = float(resort["lat"]), float(resort["lng"])
    region = resort["region"]
    rid = resort["id"]
    pois: list[dict] = []

    stay_offsets = [(180, 80), (-120, 220), (90, -160)]
    food_offsets = [(60, -70), (-90, 110), (140, 150)]

    stay_names = {
        "en": ["Ski Lodge Hotel", "Onsen Stay Inn", "Base Village Hotel"],
        "ko": ["스키 롯지 호텔", "온천 스테이 인", "베이스 빌리지 호텔"],
    }
    food_names = {
        "en": ["Slope-side Ramen", "Hokkaido Izakaya", "Café & Bakery"],
        "ko": ["슬로프 라멘", "이자카야", "카페 & 베이커리"],
    }

    for i in range(stay_n):
        n, e = stay_offsets[i % len(stay_offsets)]
        lat, lng = offset_latlng(lat0, lng0, n, e)
        poi_id = f"stay_{region}_{stable_id(rid, 'stay', str(i))}"
        i18n = {}
        for lang in LANGS:
            short = resort["names"][lang].split("(")[0].strip()
            title = f"{stay_names[lang][i]} ({short})"
            i18n[lang] = {
                "title": title,
                "address": resort["addresses"][lang],
                "overview": {
                    "en": f"Lodge-style stay near {resort['names']['en']}. Walk or shuttle to lifts; confirm check-in.",
                    "ko": f"{resort['names']['ko']} 근처 숙소. 리프트 셔틀·체크인 시간을 확인하세요.",
                }[lang],
                "subtype": {"en": "Hotel / Lodge", "ko": "호텔 / 롯지"}[lang],
                "hours": {"en": "Front desk varies by property", "ko": "프론트 시간은 숙소별 상이"}[lang],
                "parking": {"en": "Often available in ski areas", "ko": "스키장 인근 주차 가능한 경우 많음"}[lang],
                "transit": {
                    "en": "Short shuttle or walk from resort base",
                    "ko": "리조트 베이스에서 셔틀 또는 도보",
                }[lang],
                "tips": {
                    "en": "Book early for New Year and February weekends.",
                    "ko": "연말·2월 주말은 조기 예약 권장.",
                }[lang],
            }
        pois.append({
            "id": poi_id,
            "kind": "Stay",
            "lat": lat,
            "lng": lng,
            "thumbnail": "/static/images/default.jpg",
            "tel": "",
            "website": "",
            "source": "seed_nearby",
            "near_resorts": [rid],
            "near_clinics": [rid],
            "region": region,
            "i18n": i18n,
        })

    for i in range(food_n):
        n, e = food_offsets[i % len(food_offsets)]
        lat, lng = offset_latlng(lat0, lng0, n, e)
        poi_id = f"food_{region}_{stable_id(rid, 'food', str(i))}"
        i18n = {}
        for lang in LANGS:
            short = resort["names"][lang].split("(")[0].strip()
            title = f"{food_names[lang][i]} ({short})"
            i18n[lang] = {
                "title": title,
                "address": resort["addresses"][lang],
                "overview": {
                    "en": f"Meal spot near {resort['names']['en']}. Good after a ski day; confirm hours.",
                    "ko": f"{resort['names']['ko']} 근처 식사. 슬로프 후 이용; 영업시간 확인.",
                }[lang],
                "subtype": {"en": "Restaurant / café", "ko": "식당 / 카페"}[lang],
                "hours": {"en": "Typically lunch–dinner in ski villages", "ko": "스키 마을은 점심~저녁 영업이 일반적"}[lang],
                "parking": {"en": "Village parking or walk from stay", "ko": "마을 주차 또는 숙소 도보"}[lang],
                "transit": {"en": "Near resort village", "ko": "리조트 마을 인근"}[lang],
                "tips": {
                    "en": "Peak lunch hours 11:30–13:00 — go early or late.",
                    "ko": "점심 피크 11:30~13:00 — 이른 시간 또는 늦은 시간 추천.",
                }[lang],
            }
        pois.append({
            "id": poi_id,
            "kind": "Food",
            "lat": lat,
            "lng": lng,
            "thumbnail": "/static/images/default.jpg",
            "tel": "",
            "website": "",
            "source": "seed_nearby",
            "near_resorts": [rid],
            "near_clinics": [rid],
            "region": region,
            "i18n": i18n,
        })

    return pois
