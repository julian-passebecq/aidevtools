# VizForge

**Category:** D3js  
**Status:** Active visualization framework / V1.2 QA baseline  
**Source:** https://github.com/julian-passebecq/Fluent2_J_Viz

A framework-independent D3 visualization engine and studio layer designed to be consumed by Fluent/React products without locking the rendering core to React.

## What I built

- Reusable D3 renderers, adapters and studio patterns across a broad chart-family baseline.
- Cross-engine and flagship stories for comparison, time, ranking, maps and other visual forms.
- Real-data/provenance-oriented examples and a React host integration boundary.
- Playwright/QA screenshot coverage across desktop/mobile and chart families.
- A deliberate consumer architecture so Datapass/Fluent applications can use the visualization engine rather than duplicate chart logic.

## Engineering logic

D3 owns rendering and visualization behavior; host frameworks own composition and product UI. This separation makes the visualization layer reusable, testable and less sensitive to frontend-framework changes.

## Real QA screenshots

These images come directly from the VizForge source repository's `docs/qa` corpus.

![Cross-engine visualization](https://raw.githubusercontent.com/julian-passebecq/Fluent2_J_Viz/main/docs/qa/desktop-cross-engine.png)

| Choropleth | Event map |
|---|---|
| ![Choropleth](https://raw.githubusercontent.com/julian-passebecq/Fluent2_J_Viz/main/docs/qa/desktop-choropleth.png) | ![Event map](https://raw.githubusercontent.com/julian-passebecq/Fluent2_J_Viz/main/docs/qa/desktop-event-map.png) |

| Ranking flagship | Time flagship |
|---|---|
| ![Ranking](https://raw.githubusercontent.com/julian-passebecq/Fluent2_J_Viz/main/docs/qa/desktop-flagship-ranking-0.png) | ![Time](https://raw.githubusercontent.com/julian-passebecq/Fluent2_J_Viz/main/docs/qa/desktop-flagship-time-0.png) |

## Interview value

Shows D3 architecture beyond one-off charts: reusable rendering, framework boundaries, visual QA, responsive coverage and evidence-oriented examples.
