# PbiBench

**Category:** Power BI  
**Status:** Architecture + implementation handoff, first-pass product target defined  
**Source:** https://github.com/julian-passebecq/powerbi_enhanced_dev

A Windows-first C#/.NET engineering workbench for Power BI and Fabric semantic-model development. The product unifies model editing, DAX workflows, automation, PBIP/Git engineering, QA and Fabric control-plane work behind one shell.

## Product concept

- `Model` -> TE2-derived semantic-model editor.
- `DAX` -> routine DAX lab/tests with DAX Studio bridge.
- `Automate` -> typed bulk actions and trusted C# macros.
- `PBIP/Git` -> source engineering for PBIP/TMDL/PBIR.
- `QA` -> BPA, DAX tests and model/report validation.
- `Fabric` -> REST/XMLA/control-plane workflows.
- `Knowledge` -> senior playbook and SQLBI-oriented guidance.

## Engineering logic

The architecture keeps mature specialist engines where they are strong, then adds a unified workflow shell, explicit preview/change-plan safety for mutations, Git-aware source engineering and productized QA around them.

## Interview value

Shows Power BI engineering beyond report authoring: semantic models, DAX tooling, source control, automation, QA, PBIP/TMDL/PBIR and Fabric management boundaries.

## Visual evidence

**Runtime PNG pending.** This repository is currently a detailed implementation/handoff pack rather than a completed runtime UI. It is therefore presented as a serious product architecture, not falsely as a finished application.
