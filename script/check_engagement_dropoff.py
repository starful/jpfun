"""
jpfun session-spike / engagement-rate drop diagnosis.

When sessions spike but engagement rate craters at the same time, the usual
cause is bot/crawler traffic that passes GA4's built-in "known bots and
spiders" filter because it uses a browser-like user agent (SEO tools,
scrapers, some AI fetchers). This script adds a lightweight bot/crawler
filter segment on top of the GA4 Data API and breaks engagement rate down
by session source and by device category, so a drop hidden inside the
site-wide average becomes visible.

Run manually:
  python script/check_engagement_dropoff.py
  python script/check_engagement_dropoff.py --days 14
  python script/check_engagement_dropoff.py --export-csv out/engagement_by_source.csv
"""
from __future__ import annotations

import argparse
import csv
import os
import re
from datetime import date, timedelta
from pathlib import Path

import requests
from dotenv import load_dotenv

from app.config import SITE_CONFIG

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

GA4_PROPERTY_ID = os.getenv("JPFUN_GA4_PROPERTY_ID", "")
GA4_ACCESS_TOKEN = os.getenv("GA4_ACCESS_TOKEN", "")

# Known bot/crawler sources that show up in GA4's sessionSource dimension
# despite not being caught by GA4's own "known bots and spiders" filter.
BOT_SOURCE_PATTERNS = (
    "bot", "crawl", "spider", "slurp", "ahrefs", "semrush", "mj12",
    "petalbot", "bytespider", "yandex", "dotbot", "seznambot", "serpstat",
    "screaming frog", "headlesschrome",
)
BOT_SOURCE_RE = re.compile(
    r"\b(?:" + "|".join(re.escape(p) for p in BOT_SOURCE_PATTERNS) + r")", re.I
)

# 15%: past session spikes traced to bot/crawler traffic have put the bot-like
# share well above this, while normal day-to-day noise stays below it.
BOT_SHARE_ALERT_THRESHOLD = 0.15


def is_bot_source(source: str) -> bool:
    return bool(BOT_SOURCE_RE.search(source or ""))


def _run_report(dimensions: list[str], date_range: tuple[str, str]) -> list[dict]:
    """GA4 Data API runReport: sessions / engagedSessions / engagementRate by dimensions."""
    url = f"https://analyticsdata.googleapis.com/v1beta/properties/{GA4_PROPERTY_ID}:runReport"
    body = {
        "dateRanges": [{"startDate": date_range[0], "endDate": date_range[1]}],
        "dimensions": [{"name": d} for d in dimensions],
        "metrics": [{"name": "sessions"}, {"name": "engagedSessions"}, {"name": "engagementRate"}],
        "limit": 1000,
    }
    res = requests.post(
        url,
        json=body,
        headers={"Authorization": f"Bearer {GA4_ACCESS_TOKEN}"},
        timeout=20,
    )
    res.raise_for_status()
    data = res.json()

    rows = []
    for row in data.get("rows", []):
        dim_values = [v.get("value", "") for v in row.get("dimensionValues", [])]
        metric_values = [v.get("value", "0") for v in row.get("metricValues", [])]
        rows.append({
            **dict(zip(dimensions, dim_values)),
            "sessions": int(metric_values[0]),
            "engaged_sessions": int(metric_values[1]),
            "engagement_rate": float(metric_values[2]),
        })
    return rows


def check_bot_segment(date_range: tuple[str, str]) -> None:
    """Split sessions into a bot/crawler-like sessionSource segment vs the rest."""
    rows = _run_report(["sessionSource"], date_range)
    bot_rows = [r for r in rows if is_bot_source(r["sessionSource"])]
    human_rows = [r for r in rows if not is_bot_source(r["sessionSource"])]

    def _summarize(label: str, group: list[dict]) -> dict:
        sessions = sum(r["sessions"] for r in group)
        engaged = sum(r["engaged_sessions"] for r in group)
        rate = engaged / sessions if sessions else 0.0
        return {"segment": label, "sessions": sessions, "engagement_rate": rate}

    total_sessions = sum(r["sessions"] for r in rows) or 1
    bot_summary = _summarize("bot/crawler-like source", bot_rows)
    human_summary = _summarize("other sources", human_rows)
    bot_share = bot_summary["sessions"] / total_sessions

    print(f"🔍 bot/crawler filter segment ({date_range[0]} → {date_range[1]}):")
    for summary in (bot_summary, human_summary):
        print(
            f"   {summary['segment']:<24} sessions={summary['sessions']:>8}  "
            f"engagement_rate={summary['engagement_rate']:.1%}"
        )
    print(f"   bot-like share of sessions: {bot_share:.1%}")
    if bot_share > BOT_SHARE_ALERT_THRESHOLD:
        print(
            f"⚠️  bot/crawler-like sources are >{BOT_SHARE_ALERT_THRESHOLD:.0%} of sessions — "
            "likely driving the session spike while dragging the site-wide engagement rate down"
        )
    else:
        print("✅ bot/crawler-like share of sessions looks normal")

    if bot_rows:
        print("   matched sources:", ", ".join(sorted({r["sessionSource"] for r in bot_rows})))


def check_engagement_by_source(date_range: tuple[str, str]) -> list[dict]:
    rows = _run_report(["sessionSource"], date_range)
    rows.sort(key=lambda r: r["sessions"], reverse=True)
    print(f"🔍 engagement rate by session source ({date_range[0]} → {date_range[1]}):")
    for row in rows[:20]:
        flag = " ⚠️ bot-like" if is_bot_source(row["sessionSource"]) else ""
        print(f"   {row['sessionSource']:<28} sessions={row['sessions']:>8}  engagement_rate={row['engagement_rate']:.1%}{flag}")
    return rows


def check_engagement_by_device(date_range: tuple[str, str]) -> list[dict]:
    rows = _run_report(["deviceCategory"], date_range)
    rows.sort(key=lambda r: r["sessions"], reverse=True)
    print(f"🔍 engagement rate by device category ({date_range[0]} → {date_range[1]}):")
    for row in rows:
        print(f"   {row['deviceCategory']:<12} sessions={row['sessions']:>8}  engagement_rate={row['engagement_rate']:.1%}")
    return rows


def _write_source_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["sessionSource", "sessions", "engaged_sessions", "engagement_rate", "bot_like"])
        for row in rows:
            writer.writerow([
                row["sessionSource"],
                row["sessions"],
                row["engaged_sessions"],
                f"{row['engagement_rate']:.4f}",
                is_bot_source(row["sessionSource"]),
            ])
    print(f"📄 wrote {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="jpfun session-spike / engagement-rate drop diagnosis")
    parser.add_argument("--days", type=int, default=7, help="lookback window in days")
    parser.add_argument("--export-csv", type=Path, default=None, help="write per-source engagement rows to this CSV path")
    args = parser.parse_args()

    end = date.today()
    start = end - timedelta(days=args.days)
    date_range = (start.isoformat(), end.isoformat())

    print("🔍 jpfun engagement-rate drop check (bot filter segment + source/device split)")
    if not GA4_ACCESS_TOKEN or not GA4_PROPERTY_ID:
        print("⚠️  GA4_ACCESS_TOKEN / JPFUN_GA4_PROPERTY_ID not set — skipping live GA4 queries")
        return

    try:
        check_bot_segment(date_range)
        source_rows = check_engagement_by_source(date_range)
        check_engagement_by_device(date_range)
    except requests.RequestException as exc:
        print(f"❌ GA4 Data API request failed: {exc}")
        return

    if args.export_csv:
        _write_source_csv(args.export_csv, source_rows)


if __name__ == "__main__":
    main()
