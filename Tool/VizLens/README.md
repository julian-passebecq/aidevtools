# VizLens

**Category:** Tool  
**Status:** Stable personal Chrome extension  
**Source:** https://github.com/julian-passebecq/VizLens

A browser-side visualization inspection tool: extract a page's visualization structure deterministically, then optionally pass structured context to a local Gemini companion for explanation and analysis.

## What I built

- Chrome extension workflow for inspecting web visualizations.
- Deterministic extraction kept separate from optional AI interpretation.
- Local/personal usage path rather than requiring a public hosted service.
- Extension packaging, icons and a documented feature/backlog trail.

## Engineering logic

The key boundary is **extract first, interpret second**. DOM/chart evidence is collected predictably so the optional model layer receives explicit structured context instead of being asked to guess from a webpage.

## Interview value

Shows browser-extension engineering, extraction/AI boundaries, practical tooling and an emphasis on inspectable evidence rather than model-only behavior.

## Visual evidence

**Runtime PNG pending.** The current repository contains extension icons but no UI screenshot; icons are not presented here as product screenshots.

See [`FEATURE_MATRIX.md`](FEATURE_MATRIX.md) and [`BACKLOG.md`](BACKLOG.md).
