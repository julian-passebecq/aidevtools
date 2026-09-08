# Portfolio Main — Project Radar

**Current version/snapshot:** v5  
**Website:** https://portfoliomainvj1.netlify.app/  
**GitHub:** https://github.com/julian-passebecq/aichakra  
**Stack:** Static HTML/CSS/JS · SVG animation · Netlify

## Interview summary

Minimal portfolio index reduced to one visual: a role radar linking deployed projects to Cloud, SQL/Warehouse and Analyst/BI capability nodes plus a compact business card.

## Coding logic

A static SVG network is driven by deterministic JavaScript animations. Project nodes are anchors, routes map projects to capability roles, and small packet animations communicate the portfolio progression without a framework.

## Feature status

| Already implemented | Next / proposed |
|---|---|
| Single Role Radar view | Keep project links synchronized with current portfolio |
| Six project nodes as direct links | Optional lightweight project-status/version badges |
| Animated packets along project→role routes | Preserve single-view simplicity rather than re-adding panels |
| Pulsing role icons |  |
| Central datapassj.com link + right-side contact card/QR |  |

## PNG scenario set

1. `01_role_radar_overview.png` — Role Radar overview
2. `02_project_role_routes.png` — Project → role routes
3. `03_role_node_pulses.png` — Role node pulses
4. `04_center_portfolio_link.png` — Central portfolio link
5. `05_business_card_qr.png` — Business card + QR

## Image provenance

These PNGs are **repo-faithful UI explainers**, not claimed pixel-perfect browser captures. They were reconstructed from the current repository README, structure and CSS design tokens so another AI can safely use them in an interview portfolio/PDF without misrepresenting the app.
