# MCP — `riman-cl-lifening-beauty-collagen-ampoule-dropship-study`

Independent Model Context Protocol server for this RIMAN open-science repository.

## Tools
| Tool | Description |
| :--- | :--- |
| `get_repo_overview` | Titles, metrics, portal links, dual benchmark DOIs |
| `query_quantitative_csv` | Filter `*_quantitative.csv` by column / substring |
| `search_multilingual_corpus` | Search `*_multilingual_corpus.jsonl` |
| Resource `repo://riman-cl-lifening-beauty-collagen-ampoule-dropship-study/report` | Full `*_report.json` payload |

## Local stdio launch
```bash
cd /path/to/riman-cl-lifening-beauty-collagen-ampoule-dropship-study
pip install mcp
python MCP/server.py
```

Cursor / Claude Desktop example (`mcp.json` fragment):
```json
{
  "mcpServers": {
    "riman-cl-lifening-beauty-collagen-ampoule-dropship-study": {
      "command": "python",
      "args": ["MCP/server.py"],
      "cwd": "/absolute/path/to/riman-cl-lifening-beauty-collagen-ampoule-dropship-study"
    }
  }
}
```

## Remote Cloudflare Worker (R2)
- Template: [`remote_mcp_config.json`](./remote_mcp_config.json)
- `repo_name`: `riman-cl-lifening-beauty-collagen-ampoule-dropship-study`
- `r2_prefix`: `repos/riman-cl-lifening-beauty-collagen-ampoule-dropship-study/`
- HTTP endpoints (ingestor Worker):
  - `POST /mcp` — JSON-RPC-style tool dispatch
  - `GET /api/mcp/repos?repo_name=riman-cl-lifening-beauty-collagen-ampoule-dropship-study` — list objects under the R2 prefix

Suitable for listing on Glama / PulseMCP as a **dataset-scoped read-only MCP**.

## Provenance
- Kaggle DOI: [10.34740/kaggle/dsv/22383536](https://doi.org/10.34740/kaggle/dsv/22383536)
- Hugging Face DOI: [10.57967/hf/11688](https://doi.org/10.57967/hf/11688)
- Portal: https://www.riman.win/www/en/reports/detail/cl-lifening-beauty-collagen-ampoule-dropship-study.html
- Hub: https://www.riman.win/www/en/reports/hub/growth.html
