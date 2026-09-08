# Code Updates Site — Data & Coding Memory Toolbox

**Current version/snapshot:** Seed 2026-09-03  
**Website:** https://codeupdatesitev1.netlify.app/  
**GitHub:** https://github.com/julian-passebecq/codeupdate  
**Stack:** Static HTML/CSS/JS · JSON registry · Netlify

## Interview summary

No-build reference site for remembering what 38 tools are, their release snapshot, mental models, compatibility notes, history and first-party documentation.

## Coding logic

A static index loads data/tools.json and renders cards/drawers in plain JavaScript. The architecture intentionally avoids runtime APIs and npm dependencies; a future collector should update snapshots safely.

## Feature status

| Already implemented | Next / proposed |
|---|---|
| 38-tool searchable registry | Safe automated version refresh |
| Alias-aware search + category/depth filters | Last-known-good protection on collector failures |
| Tool detail drawer | Expand compatibility snapshots carefully |
| Release history and compatibility notes | Keep first-party verification workflow explicit |
| Deep links such as #tool=python |  |

## PNG scenario set

1. `01_tool_catalog.png` — Tool catalog
2. `02_search_filters.png` — Search + filters
3. `03_tool_detail_drawer.png` — Tool detail drawer
4. `04_history_compatibility.png` — History + compatibility
5. `05_related_freshness.png` — Related tools + freshness

## Image provenance

These PNGs are **repo-faithful UI explainers**, not claimed pixel-perfect browser captures. They were reconstructed from the current repository README, structure and CSS design tokens so another AI can safely use them in an interview portfolio/PDF without misrepresenting the app.
