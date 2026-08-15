#!/usr/bin/env python3
"""Seed ski resort markdown (EN/KO) and nearby POIs from ski_catalog.SKI_RESORT_SEEDS."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ski_catalog import (  # noqa: E402
    LANGS,
    SKI_RESORT_SEEDS,
    build_nearby_for_resort,
    resort_article,
)

NEARBY_OUT = ROOT / "app" / "static" / "json" / "nearby_pois.json"


def write_resorts(*, force: bool = False) -> int:
    content_dir = ROOT / "app" / "content"
    content_dir.mkdir(parents=True, exist_ok=True)
    written = 0
    for resort in SKI_RESORT_SEEDS:
        rid = resort["id"]
        for lang in LANGS:
            path = content_dir / f"{rid}_{lang}.md"
            if path.exists() and not force:
                continue
            path.write_text(resort_article(lang, resort), encoding="utf-8")
            written += 1
            print(f"wrote {path.name}")
    return written


def write_nearby() -> int:
    pois: list[dict] = []
    for resort in SKI_RESORT_SEEDS:
        pois.extend(build_nearby_for_resort(resort, stay_n=2, food_n=2))
    payload = {
        "anchor": {},
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "pois": pois,
    }
    NEARBY_OUT.parent.mkdir(parents=True, exist_ok=True)
    NEARBY_OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {NEARBY_OUT} ({len(pois)} POIs)")
    return len(pois)


def sync_csv() -> None:
    rows = []
    for resort in SKI_RESORT_SEEDS:
        rows.append(
            {
                "Name": resort["names"]["en"],
                "Name_KO": resort["names"]["ko"],
                "Id": resort["id"],
                "Lat": resort["lat"],
                "Lng": resort["lng"],
                "Address": resort["addresses"]["en"],
                "Features": resort.get("features") or "Ski",
                "Website": resort.get("website") or "",
                "Region": resort["region"],
            }
        )
    gen_path = ROOT / "script" / "csv" / "items.csv"
    gen_path.parent.mkdir(parents=True, exist_ok=True)
    with gen_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["Name", "Name_KO", "Id", "Lat", "Lng", "Address", "Features", "Website", "Region"],
        )
        w.writeheader()
        w.writerows(rows)
    print(f"synced {gen_path} ({len(rows)} resorts)")


def main() -> None:
    ap = argparse.ArgumentParser(description="Seed OKSki resort markdown + nearby JSON")
    ap.add_argument("--force", action="store_true", help="Overwrite existing md files")
    ap.add_argument("--csv-only", action="store_true")
    ap.add_argument("--skip-nearby", action="store_true")
    args = ap.parse_args()
    if not args.csv_only:
        n = write_resorts(force=args.force)
        print(f"seeded {n} markdown files")
    sync_csv()
    if not args.skip_nearby and not args.csv_only:
        write_nearby()


if __name__ == "__main__":
    main()
