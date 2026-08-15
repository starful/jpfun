#!/usr/bin/env python3
"""Seed JPFun outdoor markdown (EN/KO) from outdoor_catalog.OUTDOOR_SEEDS."""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from outdoor_catalog import LANGS, OUTDOOR_SEEDS, article  # noqa: E402


def write_items(*, force: bool = False) -> int:
    content_dir = ROOT / "app" / "content"
    content_dir.mkdir(parents=True, exist_ok=True)
    written = 0
    for seed in OUTDOOR_SEEDS:
        sid = seed["id"]
        for lang in LANGS:
            path = content_dir / f"{sid}_{lang}.md"
            if path.exists() and not force:
                continue
            path.write_text(article(lang, seed), encoding="utf-8")
            written += 1
            print(f"wrote {path.name}")
    return written


def sync_csv() -> None:
    rows = []
    for seed in OUTDOOR_SEEDS:
        rows.append(
            {
                "Name": seed["names"]["en"],
                "Name_KO": seed["names"]["ko"],
                "Id": seed["id"],
                "Activity": seed["activity"],
                "Lat": seed["lat"],
                "Lng": seed["lng"],
                "Address": seed["addresses"]["en"],
                "Features": seed.get("features") or seed["activity"],
                "Website": seed.get("website") or "",
                "Region": seed["region"],
            }
        )
    gen_path = ROOT / "script" / "csv" / "items.csv"
    gen_path.parent.mkdir(parents=True, exist_ok=True)
    with gen_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "Name",
                "Name_KO",
                "Id",
                "Activity",
                "Lat",
                "Lng",
                "Address",
                "Features",
                "Website",
                "Region",
            ],
        )
        w.writeheader()
        w.writerows(rows)
    print(f"synced {gen_path} ({len(rows)} items)")


def main() -> None:
    ap = argparse.ArgumentParser(description="Seed JPFun outdoor markdown")
    ap.add_argument("--force", action="store_true", help="Overwrite existing md files")
    ap.add_argument("--csv-only", action="store_true")
    args = ap.parse_args()
    if not args.csv_only:
        n = write_items(force=args.force)
        print(f"seeded {n} markdown files")
    sync_csv()


if __name__ == "__main__":
    main()
