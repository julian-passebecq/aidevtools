# Feature matrix — VizLens Personal v1.0

| Capability | Status | Notes |
| --- | --- | --- |
| Chrome MV3 side panel | Implemented | Persistent research UI, Chrome 114+ |
| `activeTab` + `chrome.scripting` | Implemented | Temporary page access after explicit user action |
| SVG discovery | Implemented | Deterministic local scan |
| Canvas discovery | Implemented | Metadata may be recoverable without values |
| HTML table discovery | Implemented | Local scan |
| Analytical image / iframe discovery | Implemented | Includes lazy URL clues |
| D3 `__data__` recovery | Implemented | Bounded rows / mapping clues |
| Plotly/ECharts/Highcharts/Chart.js clues | Implemented | Where runtime surfaces are accessible |
| Primary visual ranking | Implemented | Deterministic heuristic |
| Article/main extraction | Implemented | Rendered content + JSON-LD fallback |
| Stable T#/V#/N# evidence IDs | Implemented | Used in grounding contracts |
| Localized numeric parsing | Implemented | Compatibility grouping |
| PNG crop | Implemented | Currently visible rendered region |
| SVG export | Implemented | For SVG visual candidates |
| JSON / CSV export | Implemented | Evidence and data outputs |
| Privacy-reduced Debug JSON | Implemented | Diagnostic package |
| Article → visual Gemini planning | Implemented | Constrained custom function calling |
| Text → visual JSON | Implemented | Deterministic facts + same grounded planner |
| Viewport analysis | Implemented | Structured JSON classification + normalized bbox |
| Host-owned numeric values | Implemented | Model cannot author authoritative values |
| Host-owned time/year binding | Implemented | Deterministic association rules |
| Localhost Gemini companion | Implemented | 127.0.0.1:3987 |
| VizForge research brief | Implemented | Neutral semantic handoff |
| Power BI role/spec handoff | Implemented | Not `.pbiviz` generation |
| Zero-quota regression gate | Implemented | `npm run verify:personal` |
| Live Gemini contract smoke | Optional | Two synthetic requests when invoked |
| Full Canvas/custom-runtime value extraction | Known limit | Not always possible |
| Cross-origin iframe internals | Known limit | Browser security boundary |
| Chrome-protected page scripting | Known limit | Unsupported by Chrome |
| Full PDF DOM extraction | Known limit | Viewport + copied-text workflow |
| Background Gemini without local Node | Not current | Personal v1 requires local companion |
| Chrome Web Store personal main | Not current | Store line is separated |
