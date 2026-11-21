#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Repo-scoped MCP server for riman-cl-lifening-beauty-collagen-ampoule-dropship-study (stdio / FastMCP)."""

from __future__ import annotations

import csv
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REPO_NAME = "riman-cl-lifening-beauty-collagen-ampoule-dropship-study"
SLUG = "cl-lifening-beauty-collagen-ampoule-dropship-study"
DEFAULT_THEME_ID = "growth"
KAGGLE_DOI = "10.34740/kaggle/dsv/22383536"
HF_DOI = "10.57967/hf/11688"

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as e:  # pragma: no cover
    raise SystemExit(
        "Missing dependency: pip install mcp\n"
        f"Original import error: {e}"
    )


mcp = FastMCP(REPO_NAME)


def _find_one(pattern: str) -> Path | None:
    hits = sorted(REPO_ROOT.glob(pattern))
    return hits[0] if hits else None


def _load_report() -> dict:
    path = _find_one("*_report.json")
    if not path:
        raise FileNotFoundError(f"no *_report.json under {REPO_ROOT}")
    return json.loads(path.read_text(encoding="utf-8"))


@mcp.tool()
def get_repo_overview() -> str:
    """Return structured overview: titles, metrics, portal links, dual benchmark DOIs."""
    doc = _load_report()
    en = (doc.get("locales") or {}).get("en") or {}
    meta = doc.get("metadata") or {}
    stats = doc.get("quantitative_metrics") or {}
    theme_id = doc.get("theme_id") or DEFAULT_THEME_ID
    slug = doc.get("slug") or SLUG
    payload = {
        "repo_name": REPO_NAME,
        "repo_root": str(REPO_ROOT),
        "slug": slug,
        "theme_id": theme_id,
        "title_en": en.get("title"),
        "abstract_en": (en.get("abstract") or "")[:1200],
        "country": meta.get("country_name"),
        "product_id": meta.get("product_id"),
        "sample_size": stats.get("sample_size"),
        "overall_mean": stats.get("overall_composite_mean"),
        "top2_box_pct": stats.get("overall_top2_box_pct"),
        "portal_detail": f"https://www.riman.win/www/en/reports/detail/{slug}.html",
        "portal_hub": f"https://www.riman.win/www/en/reports/hub/{theme_id}.html",
        "dois": {
            "kaggle": KAGGLE_DOI,
            "huggingface": HF_DOI,
        },
        "readme_exists": (REPO_ROOT / "README.md").exists(),
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


@mcp.tool()
def query_quantitative_csv(column: str = "", contains: str = "", limit: int = 20) -> str:
    """Filter *_quantitative.csv by column substring (case-insensitive)."""
    path = _find_one("*_quantitative.csv")
    if not path:
        return json.dumps({"error": "csv_not_found"})
    contains_l = (contains or "").lower()
    rows = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        for row in reader:
            if column and column not in row:
                continue
            if column:
                cell = str(row.get(column, ""))
                if contains_l and contains_l not in cell.lower():
                    continue
            elif contains_l and contains_l not in json.dumps(row, ensure_ascii=False).lower():
                continue
            rows.append(row)
            if len(rows) >= max(1, int(limit)):
                break
    return json.dumps(
        {"file": path.name, "columns": fields, "n": len(rows), "rows": rows},
        ensure_ascii=False,
    )


@mcp.tool()
def search_multilingual_corpus(query: str, limit: int = 10) -> str:
    """Substring search over *_multilingual_corpus.jsonl lines."""
    path = _find_one("*_multilingual_corpus.jsonl")
    if not path:
        return json.dumps({"error": "jsonl_not_found"})
    q = (query or "").lower()
    hits = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        if q and q not in line.lower():
            continue
        try:
            hits.append(json.loads(line))
        except json.JSONDecodeError:
            hits.append({"raw": line[:2000]})
        if len(hits) >= max(1, int(limit)):
            break
    return json.dumps({"file": path.name, "n": len(hits), "hits": hits}, ensure_ascii=False)


@mcp.resource("repo://riman-cl-lifening-beauty-collagen-ampoule-dropship-study/report")
def report_resource() -> str:
    """Expose the full *_report.json document as an MCP resource."""
    return json.dumps(_load_report(), ensure_ascii=False)


if __name__ == "__main__":
    mcp.run()
