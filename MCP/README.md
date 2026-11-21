# MCP — `riman-cl-lifening-beauty-collagen-ampoule-dropship-study`

Model Context Protocol pack for this RIMAN open-science repository (local stdio + official remote Registry).

## Official remote endpoint
- **MCP:** [https://mcp.riman.win/mcp](https://mcp.riman.win/mcp)
- **Repo index:** [https://mcp.riman.win/api/mcp/repos?repo_name=riman-cl-lifening-beauty-collagen-ampoule-dropship-study](https://mcp.riman.win/api/mcp/repos?repo_name=riman-cl-lifening-beauty-collagen-ampoule-dropship-study)
- **CDN package:** [https://cdn.riman.win/repos/riman-cl-lifening-beauty-collagen-ampoule-dropship-study/](https://cdn.riman.win/repos/riman-cl-lifening-beauty-collagen-ampoule-dropship-study/)
- **Portal:** [https://www.riman.win/www/en/reports/detail/cl-lifening-beauty-collagen-ampoule-dropship-study.html](https://www.riman.win/www/en/reports/detail/cl-lifening-beauty-collagen-ampoule-dropship-study.html)

## Tools
| Tool | Description |
| :--- | :--- |
| `list_repos` | List packages (theme / keyword filters) |
| `get_repo_overview` | Titles, metrics, portal links, dual DOIs |
| `query_quantitative_csv` | Filter `*_quantitative.csv` |
| `search_multilingual_corpus` | Search JSONL by query + language |
| `compare_repos` | Compare metrics with another `riman-{slug}` |
| `list_repo_files` | List package files |
| `get_citation` | BibTeX + dual benchmark DOIs |

## Resources
| URI | Description |
| :--- | :--- |
| `repo://riman-cl-lifening-beauty-collagen-ampoule-dropship-study/report` | Full `*_report.json` |
| `repo://riman-cl-lifening-beauty-collagen-ampoule-dropship-study/citation` | BibTeX + DOI block |

## Local stdio
```bash
cd /path/to/riman-cl-lifening-beauty-collagen-ampoule-dropship-study
pip install mcp
python MCP/server.py
```

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

## Remote client (HTTP) + proxy bridge
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

Suitable for Glama / PulseMCP as a **dataset-scoped read-only Registry MCP**.

## Provenance
- Kaggle DOI: [10.34740/kaggle/dsv/22383536](https://doi.org/10.34740/kaggle/dsv/22383536)
- Hugging Face DOI: [10.57967/hf/11688](https://doi.org/10.57967/hf/11688)
- Theme hub: https://www.riman.win/www/en/reports/hub/growth.html
