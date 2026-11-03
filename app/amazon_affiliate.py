"""Amazon.co.jp Associates search links for JPFun.

Keyword search links tagged with the Starful Associates id. Keywords are picked
by activity/kind; unknown kinds fall back to the outdoor-goods default.
"""

from __future__ import annotations

import os
from typing import Any
from urllib.parse import quote_plus

AMAZON_TAG = os.getenv("AMAZON_JP_TAG", "starful06-22").strip() or "starful06-22"
AMAZON_BASE = "https://www.amazon.co.jp/s"

DEFAULT_KEYWORD = "アウトドア グッズ"

_KEYWORDS: dict[str, str] = {
    "default": DEFAULT_KEYWORD,
    "ski": "スキー ウェア",
    "camp": "キャンプ用品",
    "glamping": "グランピング グッズ",
}

_LABELS: dict[str, dict[str, str]] = {
    "default": {"en": "Outdoor gear on Amazon", "ko": "Amazon에서 아웃도어 용품 보기"},
    "ski": {"en": "Ski wear on Amazon", "ko": "Amazon에서 스키 웨어 보기"},
    "camp": {"en": "Camping gear on Amazon", "ko": "Amazon에서 캠핑 용품 보기"},
    "glamping": {"en": "Glamping goods on Amazon", "ko": "Amazon에서 글램핑 용품 보기"},
}


def _enabled() -> bool:
    return os.getenv("AMAZON_JPFUN_ENABLED", "1").strip().lower() in (
        "1",
        "true",
        "yes",
        "on",
    )


def _norm_kind(kind: str) -> str:
    k = (kind or "").strip().lower()
    return k if k in _KEYWORDS else "default"


def amazon_keyword_for(kind: str = "") -> str:
    return _KEYWORDS[_norm_kind(kind)]


def amazon_url_for(kind: str = "") -> str:
    kw = amazon_keyword_for(kind)
    return f"{AMAZON_BASE}?k={quote_plus(kw)}&tag={AMAZON_TAG}"


def amazon_context(kind: str = "", lang: str = "en") -> dict[str, Any]:
    """Template context: show_amazon, amazon_cta."""
    if not _enabled():
        return {"show_amazon": False, "amazon_cta": None}
    k = _norm_kind(kind)
    suffix = "ko" if (lang or "en").lower() == "ko" else "en"
    return {
        "show_amazon": True,
        "amazon_cta": {
            "id": "amazon",
            "kind": k,
            "keyword": _KEYWORDS[k],
            "click_url": amazon_url_for(k),
            "label": _LABELS[k][suffix],
        },
    }
