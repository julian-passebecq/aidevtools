# Backlog / versioning — J Utility Palette

## V1 — current clean baseline

- Standalone WPF app and local core.
- Project Clipboard with field-level copy semantics.
- Modular prompt composition and recent history.
- Sticky notes.
- Local JSON persistence / backup / import / export.
- Normal / Always on top / Summon-hide window modes.
- Mouse summon bindings and cursor-aware placement.

## V1.1 — usability hardening

1. Archive filters.
2. Safer project editing validation.
3. Dynamic editors for arbitrary `{{variable}}` placeholders.
4. Persist window position/size per view with off-screen recovery.

## V1.2 — optional integrations

1. Optional GitHub latest-commit status.
2. Manual refresh only.
3. No GitHub token stored in workspace JSON.

## V1.x release packaging

- Self-contained Windows build and installation/release workflow.

## Non-goals

- CPU/GPU monitoring.
- Power-plan management.
- f.lux replacement.
- News/stocks feeds.
- Browser automation.
- Cloud synchronization.
- Rewriting Microsoft PowerToys core.
