# D3 Eco Site / Newsroom Observatory

**Current version/snapshot:** V4  
**Website:** https://d3ecosite.netlify.app/sandbox/  
**GitHub:** https://github.com/julian-passebecq/d3siteeco  
**Stack:** D3.js 7.9 · HTML/CSS/JS · Python ingestion · Netlify Functions

## Interview summary

Newsroom-style D3 observatory combining Economist corpus analysis, cover-to-dashboard storytelling, BBC/NRK story fingerprints and a recovered DataVis tutorial lab.

## Coding logic

Static D3 views consume derived JSON. Economist PDFs are processed offline with Python; BBC/NRK feeds are bridged server-side by a Netlify function. UI state is encoded in URL parameters for shareable views.

## Feature status

| Already implemented | Next / proposed |
|---|---|
| Economist topic/country trend views | Automate larger Economist corpus/catalog ingestion |
| Cover → derived-metric D3 dashboard | 4-week trend deltas and topic-country co-occurrence |
| BBC/NRK source cards + story fingerprints | Country network / Sankey views |
| 25-demo D3 Recovery Lab | Persist selected weekly BBC/NRK visual stories |
| Shareable URL filter state + Copy view | Editorial annotation layer |

## PNG scenario set

1. `01_observatory_dashboard.png` — Observatory dashboard
2. `02_cover_to_dashboard.png` — Cover → dashboard
3. `03_bbc_nrk_story_fingerprint.png` — BBC / NRK story fingerprint
4. `04_d3_recovery_lab.png` — D3 Recovery Lab
5. `05_search_filter_share.png` — Search, filter and share

## Image provenance

These PNGs are **repo-faithful UI explainers**, not claimed pixel-perfect browser captures. They were reconstructed from the current repository README, structure and CSS design tokens so another AI can safely use them in an interview portfolio/PDF without misrepresenting the app.
