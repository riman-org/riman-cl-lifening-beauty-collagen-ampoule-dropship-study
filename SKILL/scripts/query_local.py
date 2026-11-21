#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Local CLI for this RIMAN open-science repository (summary | filter)."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def _find_one(pattern: str) -> Path | None:
    hits = sorted(REPO_ROOT.glob(pattern))
    return hits[0] if hits else None


def cmd_summary(_: argparse.Namespace) -> int:
    report = _find_one("*_report.json")
    if not report:
        print(f"[error] no *_report.json under {REPO_ROOT}", file=sys.stderr)
        return 1
    doc = json.loads(report.read_text(encoding="utf-8"))
    slug = doc.get("slug")
    theme_id = doc.get("theme_id")
    meta = doc.get("metadata") or {}
    stats = doc.get("quantitative_metrics") or {}
    en = (doc.get("locales") or {}).get("en") or {}
    print(f"repo_root: {REPO_ROOT}")
    print(f"slug: {slug}")
    print(f"theme_id: {theme_id}")
    print(f"title: {en.get('title')}")
    print(f"country: {meta.get('country_name')} ({meta.get('country_code')})")
    print(f"product: {meta.get('brand_line')} / {meta.get('product_name')} ({meta.get('product_id')})")
    print(f"sample_size: {stats.get('sample_size')}")
    print(f"overall_mean: {stats.get('overall_composite_mean')}")
    print(f"top2_box_pct: {stats.get('overall_top2_box_pct')}")
    print(f"detail: https://www.riman.win/www/en/reports/detail/{slug}.html")
    print(f"hub: https://www.riman.win/www/en/reports/hub/{theme_id}.html")
    print(f"kaggle_doi: 10.34740/kaggle/dsv/22383536")
    print(f"hf_doi: 10.57967/hf/11688")
    return 0


def cmd_filter(args: argparse.Namespace) -> int:
    column = (args.column or "").strip()
    contains = (args.contains or "").strip().lower()
    limit = max(1, int(args.limit or 20))
    shown = 0

    csv_path = _find_one("*_quantitative.csv")
    if csv_path and column:
        with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if column not in (reader.fieldnames or []):
                print(f"[warn] column '{column}' not in CSV; available={reader.fieldnames}", file=sys.stderr)
            else:
                print(f"## CSV hits from {csv_path.name}")
                for row in reader:
                    val = str(row.get(column, ""))
                    if contains and contains not in val.lower():
                        continue
                    print(json.dumps(row, ensure_ascii=False))
                    shown += 1
                    if shown >= limit:
                        break

    jsonl = _find_one("*_multilingual_corpus.jsonl")
    if jsonl and (contains or not column):
        print(f"## JSONL hits from {jsonl.name}")
        n = 0
        for line in jsonl.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            if contains and contains not in line.lower():
                continue
            if column and column not in line:
                # soft filter: require column token somewhere in the line
                if contains:
                    pass
                else:
                    continue
            print(line[:2000])
            n += 1
            if n >= limit:
                break
        shown += n

    if shown == 0:
        print("[info] no rows matched")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Query local RIMAN package files")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_sum = sub.add_parser("summary", help="Print report.json summary + portal links")
    p_sum.set_defaults(func=cmd_summary)
    p_f = sub.add_parser("filter", help="Filter quantitative CSV / multilingual JSONL")
    p_f.add_argument("--column", default="", help="CSV column name")
    p_f.add_argument("--contains", default="", help="Case-insensitive substring")
    p_f.add_argument("--limit", type=int, default=20)
    p_f.set_defaults(func=cmd_filter)
    args = parser.parse_args()
    return int(args.func(args) or 0)


if __name__ == "__main__":
    raise SystemExit(main())
