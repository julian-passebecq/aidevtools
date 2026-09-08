# VizLens Personal v1.0

A Chrome side-panel extension for visual research. It deterministically recovers article/chart evidence from the active page and can optionally ask Gemini to make bounded semantic decisions over that evidence.

## Links

- GitHub: https://github.com/julian-passebecq/VizLens
- Runtime: Chrome Manifest V3 extension loaded unpacked for the personal line
- Website: none; the personal product runs as a browser extension
- Separate branch: `chrome-web-store-v1` for the store-oriented line

## Current version

**Personal v1.0 stable baseline**. The main line is optimized for personal/unpacked use; the Chrome Web Store-oriented line is kept separate.

## What it does

- Deterministic scan of SVG, Canvas, HTML tables, analytical images/iframes and chart runtime clues.
- D3 `__data__` recovery and bounded mark/data mapping where available.
- Article/main-content extraction with JSON-LD fallback.
- Stable text, visual and numeric evidence IDs.
- Localized numeric parsing and host-owned time/value binding.
- Visual candidate ranking and Focus / PNG / SVG / JSON actions.
- CSV export for recoverable data.
- Optional Gemini article planning through custom function calling.
- Optional viewport classification through structured JSON output.
- VizForge research-brief handoff.
- Power BI data-role/spec handoff (not `.pbiviz` packaging).
- Privacy-reduced Debug JSON.

## Stack / coding logic

- **Chrome Manifest V3** side panel using `activeTab`, `chrome.scripting` and `chrome.sidePanel`.
- **Vanilla JavaScript** UI/scanner: no React, bundler or production npm dependency.
- **Local Node companion** on `127.0.0.1:3987` only for explicit Gemini actions.
- Gemini key remains in the Windows environment and is never bundled into the extension.
- The page URL is not sent in Gemini prompts.

The central design rule is: **use deterministic code for evidence and numbers; use the model for bounded semantic selection/classification.**

## Interview talking points

1. Built a deterministic-first AI architecture rather than making the model the source of truth.
2. Minimized browser permissions with `activeTab` instead of persistent `<all_urls>` access.
3. Separated AI contracts: function calling for article planning, structured JSON for viewport classification.
4. Enforced host-owned numeric values and strict post-model validation to reduce hallucination risk.
5. Kept rendering concerns outside the extension through explicit VizForge and Power BI handoffs.

## PNG scenarios

1. `png/01_scan_visuals.png`
2. `png/02_article_evidence.png`
3. `png/03_recovered_data.png`
4. `png/04_grounded_gemini.png`
5. `png/05_downstream_handoffs.png`

The PNGs are explanatory UI reconstructions based on the current `sidepanel.html`/CSS and user guide, not claims of runtime screenshot validation.
