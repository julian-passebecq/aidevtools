# DrawCloud

**Category:** Cloud  
**Status:** Active architecture-tool concept / implementation repo  
**Source:** https://github.com/julian-passebecq/DrawCloud

A lightweight workbench around Draw.io for creating, archiving and revising cloud architecture diagrams with a semantic JSON representation that can be edited by an AI and round-tripped back into the diagram workflow.

## What I built / designed

- Draw.io-first workflow rather than replacing a mature diagram editor.
- Reusable cloud-architecture templates and provider-oriented diagram concepts.
- Semantic JSON export for structured review and AI-assisted modification.
- Git-friendly archive/versioning direction for diagrams and their intent.
- Direct-edit/round-trip concept so a diagram can be changed without redrawing everything manually.

## Engineering logic

The tool keeps Draw.io as the visual editor and adds a structured layer around it. The JSON representation captures diagram intent in a form that is easier to version, review and modify programmatically than raw visual coordinates alone.

## Interview value

Shows cloud-architecture thinking, practical tooling around an established ecosystem, versionable design artifacts and a constrained AI-assisted editing workflow.

## Visual evidence

**Runtime PNG pending.** The current source repository does not contain a committed product screenshot, so the showcase does not invent one.
