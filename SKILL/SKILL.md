---
name: riman-repo-cl-lifening-beauty-collagen-ampoule-dropship-study
description: "Use when querying RIMAN open-science package `riman-cl-lifening-beauty-collagen-ampoule-dropship-study` / slug `cl-lifening-beauty-collagen-ampoule-dropship-study` (theme `growth`): local CSV/JSONL retrieval, report summary, compare metrics, or remote Registry MCP at https://mcp.riman.win/mcp. Study: RIMAN RESEARCH: Clinical & Market Viability of LIFENING Beauty Collagen Ampoule via Zero-Inventory D"
repo_name: riman-cl-lifening-beauty-collagen-ampoule-dropship-study
slug: cl-lifening-beauty-collagen-ampoule-dropship-study
theme_id: growth
mcp_endpoint: https://mcp.riman.win/mcp
mcp_repos: https://mcp.riman.win/api/mcp/repos
official_dois:
  kaggle: 10.34740/kaggle/dsv/22383536
  huggingface: 10.57967/hf/11688
portal:
  detail_en: https://www.riman.win/www/en/reports/detail/cl-lifening-beauty-collagen-ampoule-dropship-study.html
  hub_en: https://www.riman.win/www/en/reports/hub/growth.html
  home_en: https://www.riman.win/www/en/home/index.html
cdn_prefix: https://cdn.riman.win/repos/riman-cl-lifening-beauty-collagen-ampoule-dropship-study/
---

# RIMAN Agent Skill — `riman-cl-lifening-beauty-collagen-ampoule-dropship-study`

## When to use
- User asks about this study (`cl-lifening-beauty-collagen-ampoule-dropship-study`), its n=200 CSV, 6-language corpus, descending INCI, or DOIs.
- Need **local** summary / filter / compare / BibTeX without leaving the checkout.
- Need the **official Registry MCP** at `https://mcp.riman.win/mcp` with `repo_name=riman-cl-lifening-beauty-collagen-ampoule-dropship-study`.

## Repository metadata
| Field | Value |
| :--- | :--- |
| `repo_name` | `riman-cl-lifening-beauty-collagen-ampoule-dropship-study` |
| `slug` | `cl-lifening-beauty-collagen-ampoule-dropship-study` |
| `theme_id` | `growth` |
| MCP | [https://mcp.riman.win/mcp](https://mcp.riman.win/mcp) |
| CDN | [https://cdn.riman.win/repos/riman-cl-lifening-beauty-collagen-ampoule-dropship-study/](https://cdn.riman.win/repos/riman-cl-lifening-beauty-collagen-ampoule-dropship-study/) |
| Kaggle DOI | [10.34740/kaggle/dsv/22383536](https://doi.org/10.34740/kaggle/dsv/22383536) |
| Hugging Face DOI | [10.57967/hf/11688](https://doi.org/10.57967/hf/11688) |

## 6-language portal matrix
| Lang | Detail | Hub |
| :--- | :--- | :--- |
| `en` | https://www.riman.win/www/en/reports/detail/cl-lifening-beauty-collagen-ampoule-dropship-study.html | https://www.riman.win/www/en/reports/hub/growth.html |
| `zh-TW` | https://www.riman.win/www/zh-tw/reports/detail/cl-lifening-beauty-collagen-ampoule-dropship-study.html | https://www.riman.win/www/zh-tw/reports/hub/growth.html |
| `zh-CN` | https://www.riman.win/www/zh-cn/reports/detail/cl-lifening-beauty-collagen-ampoule-dropship-study.html | https://www.riman.win/www/zh-cn/reports/hub/growth.html |
| `ja` | https://www.riman.win/www/ja/reports/detail/cl-lifening-beauty-collagen-ampoule-dropship-study.html | https://www.riman.win/www/ja/reports/hub/growth.html |
| `es` | https://www.riman.win/www/es/reports/detail/cl-lifening-beauty-collagen-ampoule-dropship-study.html | https://www.riman.win/www/es/reports/hub/growth.html |
| `fr` | https://www.riman.win/www/fr/reports/detail/cl-lifening-beauty-collagen-ampoule-dropship-study.html | https://www.riman.win/www/fr/reports/hub/growth.html |

## Local workflow (aligned with MCP tools)
1. `python SKILL/scripts/query_local.py summary` → overview + DOIs + portal links
2. `python SKILL/scripts/query_local.py filter --column <col> --contains <kw> [--lang en]`
3. `python SKILL/scripts/query_local.py compare --other <sibling-riman-slug>`
4. `python SKILL/scripts/query_local.py cite` → BibTeX + dual DOIs
5. Optional stdio MCP: `python MCP/server.py`

## Remote Registry MCP
```bash
npx -y mcp-proxy https://mcp.riman.win/mcp
```

```json
{
  "mcpServers": {
    "riman-cl-lifening-beauty-collagen-ampoule-dropship-study": {
      "url": "https://mcp.riman.win/mcp",
      "transport": "http",
      "headers": {},
      "repo_name": "riman-cl-lifening-beauty-collagen-ampoule-dropship-study",
      "notes": "Official RIMAN Registry MCP. Pass repo_name=riman-{slug} on tool calls. List: https://mcp.riman.win/api/mcp/repos?repo_name=riman-cl-lifening-beauty-collagen-ampoule-dropship-study"
    }
  }
}
```

Tools (remote): `list_repos`, `get_repo_overview`, `query_quantitative_csv`, `search_multilingual_corpus`, `compare_repos`, `list_repo_files`, `get_citation`.
