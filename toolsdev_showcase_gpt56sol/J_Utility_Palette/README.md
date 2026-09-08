# J Utility Palette

A lightweight standalone Windows productivity companion for reusable prompts, project links and temporary notes.

## Links

- GitHub: https://github.com/julian-passebecq/PowerToy_UI
- Runtime: Windows desktop application
- Website: none; this is a local desktop app

## Current version

**V1 clean standalone rewrite**. The project deliberately moved away from a full Microsoft PowerToys fork to a much smaller WPF application with its own local data model.

## What it does

- Project Clipboard for repository/site/extra links with explicit Open and Copy actions.
- Modular prompt composer with reusable modules and project variables.
- Recent prompt history.
- Sticky notes with pin/archive state and labels.
- Three window modes: Normal, Always on top, Summon / hide.
- Mouse summon bindings: Mouse 4, Mouse 5, middle click, or Ctrl + middle click.
- Optional hide-on-focus-loss and cursor-relative placement.
- Local JSON workspace with backup, import and export.

## Stack / coding logic

- **C# / .NET 8 / WPF** for a native Windows desktop shell.
- `JUtility.Core` owns models, JSON persistence, project formatting, URL normalization and deterministic prompt composition.
- `JUtility.App` owns the WPF UI and native Windows interactions.
- `JUtility.SmokeTests` provides package-free executable smoke tests.
- Local-first storage lives under `%LOCALAPPDATA%\\JUtilityPalette\\workspace.json`.

The main design choice is to keep the utility small: the UI is intentionally independent from Microsoft PowerToys internals, cloud accounts, Electron and Node.

## Interview talking points

1. Re-scoped an over-large PowerToys-fork prototype into a maintainable standalone product.
2. Used explicit interaction semantics to prevent ambiguous UI behavior: Open opens, Copy copies.
3. Designed a small local-first state model rather than adding unnecessary backend/cloud infrastructure.
4. Added a useful desktop interaction mode: summon/hide from global mouse buttons while preserving a temporary keep-open override.

## PNG scenarios

1. `png/01_project_clipboard.png`
2. `png/02_prompt_composer.png`
3. `png/03_sticky_notes.png`
4. `png/04_window_settings.png`
5. `png/05_summon_hide_workflow.png`

The PNGs are explanatory UI reconstructions based on the current WPF source, not claims of runtime screenshot validation.
