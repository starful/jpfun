"""Rakuten Travel affiliate module for JPFun.

Named to match the sibling affiliate modules (a8_affiliate.py, agoda_partners.py)
used across the okramen/okcaddie/okonsen family of sites. The actual Rakuten
search/affiliate-link logic already lives in `affiliate.py`; this module is the
dedicated entry point other code and setup checks should import for Rakuten.
"""

from __future__ import annotations

try:
    from .affiliate import _rakuten_hgc, rakuten_url_for
except ImportError:
    from affiliate import _rakuten_hgc, rakuten_url_for

_DEFAULT_HGC = "55b9427b.a63c2df8.55b9427c.3a0d270c"

__all__ = ["rakuten_url_for", "is_configured"]


def is_configured() -> bool:
    """True when a real Rakuten HGC id is set (not just the shared default)."""
    return _rakuten_hgc() != _DEFAULT_HGC
