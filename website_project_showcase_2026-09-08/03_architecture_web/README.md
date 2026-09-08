# Architecture Web — Cloud Architecture Atlas

**Current version/snapshot:** v0.9  
**Website:** https://architecturewebv1j.netlify.app/  
**GitHub:** https://github.com/julian-passebecq/architectureweb  
**Stack:** React · Vite · D3 capability graph · Mermaid secondary topology

## Interview summary

Cross-cloud learning atlas that starts from stable architecture capabilities, then translates the same stage into Databricks, Microsoft Fabric and Google Cloud services.

## Coding logic

React data models define logical stages and provider mappings. Custom React layouts render the primary diagrams; D3 powers the capability graph; Mermaid is kept as a copyable secondary technical-topology layer.

## Feature status

| Already implemented | Next / proposed |
|---|---|
| Conceptual Source→Move→Store→Process→Model→Serve model | Production-build verification in CI/local environment |
| 16 architecture variants across workload families | Broaden architecture scenarios and service matrices |
| Pin-able architecture stages | More export/copy workflows for diagrams |
| Cross-cloud Stage Lens | Keep 2026 runtime/availability notes current |
| Modern stack explorer + D3 capability map + Mermaid reference |  |

## PNG scenario set

1. `01_cross_cloud_home.png` — Cross-cloud home
2. `02_visual_architecture_flow.png` — Visual architecture flow
3. `03_stage_lens.png` — Pinned Stage Lens
4. `04_modern_stack_explorer.png` — Modern stack explorer
5. `05_deep_reference.png` — Deep reference workspace

## Image provenance

These PNGs are **repo-faithful UI explainers**, not claimed pixel-perfect browser captures. They were reconstructed from the current repository README, structure and CSS design tokens so another AI can safely use them in an interview portfolio/PDF without misrepresenting the app.
