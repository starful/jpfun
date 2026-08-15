"""Affiliate CTAs for JPFun detail pages (KO: Coupang, EN: Klook + Rakuten Travel)."""

from __future__ import annotations

import os
from typing import Any
from urllib.parse import quote

from .config import SITE_CONFIG

_RAKUTEN_UT = "eyJwYWdlIjoidXJsIiwidHlwZSI6InRleHQiLCJjb2wiOjF9"

COUPANG_DISCLOSURE_KO = (
    "이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다."
)

# Prefer more specific prefixes first (needle matched inside slug).
_REGION_RULES: tuple[tuple[str, str, str, str], ...] = (
    ("niseko", "niseko", "ニセコ ホテル", "Niseko"),
    ("hakuba", "hakuba", "白馬 ホテル", "Hakuba"),
    ("tsugaike", "tsugaike", "栂池高原 ホテル", "Tsugaike"),
    ("shiga", "shiga", "志賀高原 ホテル", "Shiga Kogen"),
    ("madarao", "madarao", "斑尾 ホテル", "Madarao"),
    ("tangram", "tangram", "タングラム ホテル", "Tangram"),
    ("karuizawa", "karuizawa", "軽井沢 ホテル", "Karuizawa"),
    ("furano", "furano", "富良野 ホテル", "Furano"),
    ("rusutsu", "rusutsu", "ルスツ ホテル", "Rusutsu"),
    ("kiroro", "kiroro", "キロロ ホテル", "Kiroro"),
    ("tomamu", "tomamu", "トマム ホテル", "Tomamu"),
    ("sahoro", "sahoro", "サホロ ホテル", "Sahoro"),
    ("teine", "teine", "札幌手稲 ホテル", "Sapporo Teine"),
    ("sapporo_kokusai", "sapporo_kokusai", "札幌国際 ホテル", "Sapporo Kokusai"),
    ("asahidake", "asahidake", "旭岳 ホテル", "Asahidake"),
    ("nozawa", "nozawa", "野沢温泉 宿", "Nozawa Onsen"),
    ("yuzawa", "yuzawa", "湯沢 ホテル", "Yuzawa"),
    ("kagura", "kagura", "かぐら ホテル", "Kagura"),
    ("iwappara", "iwappara", "岩原 ホテル", "Iwappara"),
    ("joetsu", "joetsu", "上越国際 ホテル", "Joetsu Kokusai"),
    ("maiko", "maiko", "舞子 ホテル", "Maiko"),
    ("ipponsugi", "ipponsugi", "一本杉 ホテル", "Ipponsugi"),
    ("naeba", "naeba", "苗場 ホテル", "Naeba"),
    ("myoko", "myoko", "妙高 ホテル", "Myoko"),
    ("zao", "zao", "蔵王温泉 ホテル", "Zao Onsen"),
    ("appi", "appi", "安比高原 ホテル", "Appi Kogen"),
    ("geto", "geto", "夏油高原 ホテル", "Geto Kogen"),
    ("alts_bandai", "alts_bandai", "アルツ磐梯 ホテル", "Alts Bandai"),
    ("takasu", "takasu", "高鷲 ホテル", "Takasu"),
    ("dynaland", "dynaland", "ダイナランド ホテル", "Dynaland"),
    ("hirayu", "hirayu", "平湯温泉 宿", "Hirayu Onsen"),
    ("washigatake", "washigatake", "鷲ヶ岳 ホテル", "Washigatake"),
    ("kusatsu", "kusatsu", "草津温泉 宿", "Kusatsu Onsen"),
    ("manza", "manza", "万座温泉 ホテル", "Manza Onsen"),
    ("kawaba", "kawaba", "川場 ホテル", "Kawaba"),
    ("minakami", "minakami", "みなかみ ホテル", "Minakami"),
    ("hunter", "hunter", "ハンターマウンテン塩原 ホテル", "Hunter Mountain"),
    ("mt_jeans", "mt_jeans", "マウントジーンズ那須 ホテル", "Mt. Jeans Nasu"),
    ("kirifuri", "kirifuri", "霧降高原 ホテル", "Kirifuri Kogen"),
    ("nasu_onsen", "nasu_onsen", "那須温泉 宿", "Nasu Onsen"),
)

_FALLBACK_KEYWORD = "スキー場"
_FALLBACK_LABEL_EN = "Japan ski"


def _rakuten_hgc() -> str:
    return (
        os.getenv("RAKUTEN_TRAVEL_HGC")
        or str(SITE_CONFIG.get("rakuten_travel_hgc") or "")
        or "55b9427b.a63c2df8.55b9427c.3a0d270c"
    )


def _strip_lang_suffix(slug: str) -> str:
    base = (slug or "").strip().lower()
    for suf in ("_en", "_ko", "_ja", "_zh_tw", "_zh"):
        if base.endswith(suf):
            return base[: -len(suf)]
    return base


def resolve_ski_region(slug: str) -> tuple[str, str, str]:
    """Return (region_key, jp_keyword, en_label)."""
    base = _strip_lang_suffix(slug)
    for key, needle, keyword, label_en in _REGION_RULES:
        if needle in base:
            return key, keyword, label_en
    return "ski", _FALLBACK_KEYWORD, _FALLBACK_LABEL_EN


def _travel_search_raw(keyword: str) -> str:
    # Partner tool uses Shift_JIS f_query (same as Rakuten link share).
    q = quote(keyword.encode("shift_jis", errors="replace"), safe="")
    return (
        "https://kw.travel.rakuten.co.jp/keyword/Search.do?"
        f"f_query={q}"
        "&f_cd_application=affiliate&f_invoice_qualified=0&f_max=30"
        "&f_flg=&f_category=0&f_teikei=&f_area=&f_chu=&f_shou="
        "&f_cd_chain=&f_all_chain=0&f_sort=0"
    )


def _affiliate_wrap(destination_url: str) -> str:
    pc = quote(destination_url, safe="")
    return (
        f"https://hb.afl.rakuten.co.jp/hgc/{_rakuten_hgc()}/"
        f"?pc={pc}&link_type=text&ut={_RAKUTEN_UT}"
    )


def rakuten_url_for(slug: str) -> str:
    _key, keyword, _label = resolve_ski_region(slug)
    return _affiliate_wrap(_travel_search_raw(keyword))


def affiliate_context(slug: str, *, lang: str = "en") -> dict[str, Any]:
    """Template vars for detail-page booking CTAs."""
    is_ko = (lang or "en").lower() == "ko"
    _key, _keyword, region_label_en = resolve_ski_region(slug)
    klook_url = str(SITE_CONFIG.get("klook_url") or "").strip()
    coupang_travel = str(SITE_CONFIG.get("coupang_travel_url") or "").strip()
    coupang_shop = str(SITE_CONFIG.get("coupang_shop_url") or "").strip()

    if is_ko:
        return {
            "aff_lang": "ko",
            "show_coupang": bool(coupang_travel or coupang_shop),
            "coupang_travel_url": coupang_travel,
            "coupang_shop_url": coupang_shop,
            "coupang_disclosure": COUPANG_DISCLOSURE_KO if (coupang_travel or coupang_shop) else "",
            "show_klook": False,
            "klook_url": "",
            "show_rakuten": False,
            "rakuten_search_url": "",
            "region_label": region_label_en,
            "booking_title": "숙소·여행 준비는 외부 사이트에서",
            "booking_desc": (
                "이 페이지는 스키장 안내입니다. 쿠팡트래블에서 숙소·여행을, "
                "쿠팡에서 스키·여행용품을 찾을 수 있습니다."
            ),
            "coupang_travel_label": "쿠팡트래블에서 숙소·여행 보기 →",
            "coupang_shop_label": "쿠팡에서 스키·여행용품 보기 →",
            "klook_label": "",
            "rakuten_label": "",
        }

    return {
        "aff_lang": "en",
        "show_coupang": False,
        "coupang_travel_url": "",
        "coupang_shop_url": "",
        "coupang_disclosure": "",
        "show_klook": bool(klook_url),
        "klook_url": klook_url,
        "show_rakuten": True,
        "rakuten_search_url": rakuten_url_for(slug),
        "region_label": region_label_en,
        "booking_title": f"Stay & trip prep near {region_label_en}",
        "booking_desc": (
            "This page is a resort guide. Buttons open Klook or Rakuten Travel "
            f"to search stays and packages around {region_label_en}."
        ),
        "coupang_travel_label": "",
        "coupang_shop_label": "",
        "klook_label": "Find stays & transfers on Klook →",
        "rakuten_label": f"Search {region_label_en} hotels on Rakuten Travel →",
    }
