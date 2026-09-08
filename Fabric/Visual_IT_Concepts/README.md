# Datapass Visual IT Concepts — Fluent 2 Microsoft J

**Category:** Fabric  
**Status:** In progress / clean product bootstrap  
**Source:** https://github.com/julian-passebecq/Fluent2_Microsoft_J

A clean React + Microsoft Fluent shell for the next Datapass Visual IT Concepts product. The repository intentionally avoids dragging the historical monorepo forward; it is designed to selectively import only proven semantic/rendering pieces through an audited boundary.

## Current scope

- Small React/Vite + Fluent product shell.
- Explicit import/handoff documentation before implementation.
- Clean separation from the historical Datapass monorepo.
- Planned integration with the proven visualization work instead of rebuilding it from zero.

## Engineering logic

The project is a controlled migration boundary: start from a minimal product surface, then bring in the smallest verified semantic/rendering closure. This reduces inherited complexity and makes each imported dependency deliberate.

## Interview value

Shows architectural cleanup, migration discipline, Fluent UI product work and an ability to distinguish between reusable proven components and legacy project baggage.

## Visual evidence

**Runtime PNG pending.** This repository is currently a clean bootstrap/integration boundary, so it is labelled in progress rather than presented as a finished Fabric application.
