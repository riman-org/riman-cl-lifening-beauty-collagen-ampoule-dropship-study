---
name: riman-repo-cl-lifening-beauty-collagen-ampoule-dropship-study
description: "Use when querying RIMAN open-science package `riman-cl-lifening-beauty-collagen-ampoule-dropship-study` / slug `cl-lifening-beauty-collagen-ampoule-dropship-study` (theme `growth`): local CSV/JSONL retrieval, report summary, or R2 MCP tools. Study: RIMAN RESEARCH: Clinical & Market Viability of LIFENING Beauty Collagen Ampoule via Zero-Inventory Drop-Shipping in Chil"
repo_name: riman-cl-lifening-beauty-collagen-ampoule-dropship-study
slug: cl-lifening-beauty-collagen-ampoule-dropship-study
theme_id: growth
official_dois:
  kaggle: 10.34740/kaggle/dsv/22383536
  huggingface: 10.57967/hf/11688
portal:
  detail_en: https://www.riman.win/www/en/reports/detail/cl-lifening-beauty-collagen-ampoule-dropship-study.html
  hub_en: https://www.riman.win/www/en/reports/hub/growth.html
  home_en: https://www.riman.win/www/en/home/index.html
---

# RIMAN Agent Skill — `riman-cl-lifening-beauty-collagen-ampoule-dropship-study`

## When to use
- User asks about this study (`cl-lifening-beauty-collagen-ampoule-dropship-study`), its n=200 CSV, 6-language corpus, or descending INCI / portal links.
- Need a **local** summary or filtered rows without leaving the repo checkout.
- Need to call the **repo MCP** (`MCP/server.py`) or the cloud Worker with `repo_name=riman-cl-lifening-beauty-collagen-ampoule-dropship-study`.

## Repository metadata
| Field | Value |
| :--- | :--- |
| `repo_name` | `riman-cl-lifening-beauty-collagen-ampoule-dropship-study` |
| `slug` | `cl-lifening-beauty-collagen-ampoule-dropship-study` |
| `theme_id` | `growth` |
| Detail (EN) | https://www.riman.win/www/en/reports/detail/cl-lifening-beauty-collagen-ampoule-dropship-study.html |
| Hub (EN) | https://www.riman.win/www/en/reports/hub/growth.html |
| Kaggle DOI | [10.34740/kaggle/dsv/22383536](https://doi.org/10.34740/kaggle/dsv/22383536) |
| Hugging Face DOI | [10.57967/hf/11688](https://doi.org/10.57967/hf/11688) |

## Local workflow
1. `python SKILL/scripts/query_local.py summary`
2. `python SKILL/scripts/query_local.py filter --column <col> --contains <kw>`
3. Optional MCP: `python MCP/server.py` (stdio)

## Remote MCP workflow
1. Read `MCP/remote_mcp_config.json`
2. Call Worker `/mcp` or `GET /api/mcp/repos?repo_name=riman-cl-lifening-beauty-collagen-ampoule-dropship-study` against R2 prefix `repos/riman-cl-lifening-beauty-collagen-ampoule-dropship-study/`
