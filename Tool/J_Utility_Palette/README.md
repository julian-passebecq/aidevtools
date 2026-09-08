# J Utility Palette

**Category:** Tool  
**Status:** Active desktop prototype  
**Source:** https://github.com/julian-passebecq/PowerToy_UI

A Windows-first utility palette for keeping project links, prompts and workspace context close at hand, with a summon/hide interaction designed for fast access rather than another permanently open dashboard.

## What I built

- .NET 8 Windows application with a compact palette UI.
- Global mouse summon/hide workflow, including middle-button style interaction.
- Local workspace persistence and window-placement restoration.
- Prompt composition, URL normalization and project clipboard formatting.
- Smoke-test/build scripts and a small Core/App separation.

## Engineering logic

The UI stays thin while reusable workspace, prompt and URL logic lives in `JUtility.Core`. Windows-specific summon and placement behavior stays in the app layer. The result is deliberately local-first and avoids a cloud dependency for everyday project context.

## Interview value

Shows Windows/.NET product work, state persistence, global-input handling and a practical AI-assisted workflow tool built around a real personal development need.

## Visual evidence

**Runtime PNG pending.** The current source repository contains code and documentation but no committed product screenshot. I am not substituting a generated image and calling it a runtime capture.

See also [`FEATURE_MATRIX.md`](FEATURE_MATRIX.md) and [`BACKLOG.md`](BACKLOG.md) for the feature/version trail.
