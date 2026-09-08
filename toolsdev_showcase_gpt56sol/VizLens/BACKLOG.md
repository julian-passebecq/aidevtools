# Backlog / versioning — VizLens

## Personal v1.0 — current stable baseline

- Unpacked Chrome MV3 side panel.
- Vanilla JavaScript UI/scanner.
- Deterministic-first evidence recovery.
- Localhost Gemini companion for explicit AI actions.
- Function calling for article planning.
- Structured JSON output for viewport classification.
- Host-owned numeric values/time binding.
- Zero-quota automated release gate.

## Current known limits / hardening targets

1. Some Canvas/custom runtime charts expose no underlying values.
2. Cross-origin iframe internals remain inaccessible.
3. Chrome-protected pages cannot be DOM-scripted.
4. PDF viewer workflow remains viewport + copied-text oriented.
5. PNG export is limited to the visible rendered region.
6. Personal Gemini features require the local Node companion.

## Parallel release lines

- `main`: personal/unpacked release optimized for local use and experimentation.
- `chrome-web-store-v1`: separate store-oriented baseline so store constraints do not force unnecessary complexity into the personal workflow.

## Product boundary

Do not turn VizLens into the final visualization/rendering system. Keep evidence recovery and semantic handoffs here; let VizForge own rich D3 rendering and downstream adapters own Power BI packaging.
