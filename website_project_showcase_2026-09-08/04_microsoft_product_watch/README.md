# Microsoft / Cloud News Hub — Product Watch

**Current version/snapshot:** v3  
**Website:** https://cloudmicrosgoftnewsvj2.netlify.app/  
**GitHub:** https://github.com/julian-passebecq/microsoft_news_hub_netlify_v2  
**Stack:** React · Vite · Python feed collector · GitHub Actions · Netlify

## Interview summary

Focused Microsoft product-news dashboard for Power BI, Fabric, Azure, Power Apps and Power Automate with trusted-source, publication and social views.

## Coding logic

A Python collector normalizes RSS/Atom/YouTube/HTML listing sources into static JSON. React/Vite renders the four views. GitHub Actions refresh the data; Netlify serves the static front end.

## Feature status

| Already implemented | Next / proposed |
|---|---|
| Discover view with search/filter/sort | Stronger dedupe/classification quality checks |
| Sources directory + per-source history | Source-health observability and stale-source alerts |
| Publications separated from trusted feed | Expand supported social APIs only when reliable |
| YouTube social history | Improve archive/live-history browsing |
| Daily GitHub Actions JSON refresh + source health |  |

## PNG scenario set

1. `01_discover.png` — Discover view
2. `02_sources_health.png` — Sources + health
3. `03_publications.png` — Publications view
4. `04_social_video.png` — Social / video
5. `05_source_history.png` — Source history

## Image provenance

These PNGs are **repo-faithful UI explainers**, not claimed pixel-perfect browser captures. They were reconstructed from the current repository README, structure and CSS design tokens so another AI can safely use them in an interview portfolio/PDF without misrepresenting the app.
