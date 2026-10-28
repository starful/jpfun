"""
jpfun analytics reporting pipeline health check.

Verifies the GA4 property ID / GSC site URL mapping for jpfun matches
SITE_CONFIG, confirms API credentials are usable, and retries transient
auth failures before sending a Slack alert.

Run manually or wire into a cron step:
  python script/check_analytics_pipeline.py
"""
from __future__ import annotations

import importlib.util
import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def _load_site_config() -> dict:
    config_path = BASE_DIR / "app" / "config.py"
    spec = importlib.util.spec_from_file_location("jpfun_config", config_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.SITE_CONFIG


SITE_CONFIG = _load_site_config()

# jpfun's expected GA4 property / GSC site mapping.
# Override via env if the GA4 property is re-created or the verified GSC site changes.
ANALYTICS_SITE_MAP = {
    "jpfun": {
        "ga4_property_id": os.getenv("JPFUN_GA4_PROPERTY_ID", ""),
        "gsc_site_url": os.getenv("JPFUN_GSC_SITE_URL", SITE_CONFIG["site_url"]),
    }
}

GA4_ACCESS_TOKEN = os.getenv("GA4_ACCESS_TOKEN", "")
GSC_ACCESS_TOKEN = os.getenv("GSC_ACCESS_TOKEN", "")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "")

RETRY_ATTEMPTS = 3
RETRY_BACKOFF_SECONDS = 5


def notify_slack(message: str) -> None:
    if not SLACK_WEBHOOK_URL:
        print(f"⚠️  SLACK_WEBHOOK_URL not set, skipping alert: {message}")
        return
    try:
        requests.post(SLACK_WEBHOOK_URL, json={"text": message}, timeout=10)
    except Exception as exc:
        print(f"⚠️  Slack alert failed to send: {exc}")


def with_retry(label: str, func) -> bool:
    """Run func() up to RETRY_ATTEMPTS times with backoff; alert Slack on final failure."""
    last_exc: Exception | None = None
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            func()
            return True
        except Exception as exc:
            last_exc = exc
            print(f"  attempt {attempt}/{RETRY_ATTEMPTS} failed: {exc}")
            if attempt < RETRY_ATTEMPTS:
                time.sleep(RETRY_BACKOFF_SECONDS * attempt)
    notify_slack(f"🚨 jpfun analytics pipeline: {label} failed after {RETRY_ATTEMPTS} attempts — {last_exc}")
    return False


def check_site_mapping(site: str = "jpfun") -> bool:
    mapping = ANALYTICS_SITE_MAP.get(site)
    if not mapping:
        print(f"❌ no analytics mapping configured for site '{site}'")
        return False

    ok = True
    if not mapping["ga4_property_id"]:
        print("❌ JPFUN_GA4_PROPERTY_ID is not set")
        ok = False
    if not mapping["gsc_site_url"]:
        print("❌ JPFUN_GSC_SITE_URL is not set")
        ok = False
    elif mapping["gsc_site_url"].rstrip("/") != SITE_CONFIG["site_url"].rstrip("/"):
        print(
            f"⚠️  GSC site URL ({mapping['gsc_site_url']}) does not match "
            f"SITE_CONFIG['site_url'] ({SITE_CONFIG['site_url']})"
        )

    if ok:
        print(f"✅ mapping ok: GA4 property {mapping['ga4_property_id']} / GSC site {mapping['gsc_site_url']}")
    return ok


def _ga4_auth_ping(property_id: str) -> None:
    url = f"https://analyticsdata.googleapis.com/v1beta/properties/{property_id}/metadata"
    res = requests.get(url, headers={"Authorization": f"Bearer {GA4_ACCESS_TOKEN}"}, timeout=15)
    if res.status_code in (401, 403):
        raise RuntimeError(f"GA4 auth rejected (HTTP {res.status_code})")
    res.raise_for_status()


def _gsc_auth_ping(site_url: str) -> None:
    quoted = requests.utils.quote(site_url, safe="")
    url = f"https://searchconsole.googleapis.com/webmasters/v3/sites/{quoted}"
    res = requests.get(url, headers={"Authorization": f"Bearer {GSC_ACCESS_TOKEN}"}, timeout=15)
    if res.status_code in (401, 403):
        raise RuntimeError(f"GSC auth rejected (HTTP {res.status_code})")
    res.raise_for_status()


def check_auth(site: str = "jpfun") -> bool:
    mapping = ANALYTICS_SITE_MAP.get(site, {})
    property_id = mapping.get("ga4_property_id", "")
    site_url = mapping.get("gsc_site_url", "")

    ga4_ok = True
    if not GA4_ACCESS_TOKEN:
        print("⚠️  GA4_ACCESS_TOKEN not set — skipped live auth check")
    elif not property_id:
        print("⚠️  GA4 property id missing — skipped live auth check")
    else:
        ga4_ok = with_retry("GA4 auth check", lambda: _ga4_auth_ping(property_id))
        print("✅ GA4 auth ok" if ga4_ok else "❌ GA4 auth failed")

    gsc_ok = True
    if not GSC_ACCESS_TOKEN:
        print("⚠️  GSC_ACCESS_TOKEN not set — skipped live auth check")
    elif not site_url:
        print("⚠️  GSC site url missing — skipped live auth check")
    else:
        gsc_ok = with_retry("GSC auth check", lambda: _gsc_auth_ping(site_url))
        print("✅ GSC auth ok" if gsc_ok else "❌ GSC auth failed")

    return ga4_ok and gsc_ok


def main() -> None:
    print("🔍 jpfun analytics pipeline check")
    mapping_ok = check_site_mapping()
    auth_ok = check_auth()
    if mapping_ok and auth_ok:
        print("✅ analytics pipeline healthy")
    else:
        print("⚠️  analytics pipeline needs attention — see messages above")


if __name__ == "__main__":
    main()
