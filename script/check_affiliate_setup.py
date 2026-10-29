"""
jpfun affiliate banner/tracking module install check.

Confirms the affiliate modules used across the okramen/okcaddie/okonsen site
family — a8_affiliate.py (A8.net), agoda_partners.py (Agoda), and
rakuten_affiliate.py (Rakuten Travel) — are present under app/ and report
their basic config status.

Run manually:
  python script/check_affiliate_setup.py
"""
from __future__ import annotations

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = BASE_DIR / "app"

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

MODULES = ("a8_affiliate", "agoda_partners", "rakuten_affiliate")


def check_modules_present() -> bool:
    ok = True
    for name in MODULES:
        path = APP_DIR / f"{name}.py"
        if path.exists():
            print(f"✅ {name}.py present")
        else:
            print(f"❌ {name}.py missing")
            ok = False
    return ok


def check_module_config() -> bool:
    ok = True

    from app.a8_affiliate import _enabled as a8_enabled

    if a8_enabled():
        print("✅ a8_affiliate: A8_JPFUN_ENABLED is on")
    else:
        print("⚠️  a8_affiliate: A8_JPFUN_ENABLED is off — banners will not render")

    from app.agoda_partners import AGODA_CID

    print(f"✅ agoda_partners: using CID {AGODA_CID}")

    from app.rakuten_affiliate import is_configured as rakuten_configured

    if rakuten_configured():
        print("✅ rakuten_affiliate: RAKUTEN_TRAVEL_HGC is set")
    else:
        print("⚠️  rakuten_affiliate: using the shared default HGC — set RAKUTEN_TRAVEL_HGC for jpfun's own tracking")
        ok = False

    return ok


def main() -> None:
    print("🔍 jpfun affiliate banner/tracking install check")
    present_ok = check_modules_present()
    config_ok = check_module_config() if present_ok else False
    if present_ok and config_ok:
        print("✅ affiliate setup healthy")
    else:
        print("⚠️  affiliate setup needs attention — see messages above")


if __name__ == "__main__":
    main()
