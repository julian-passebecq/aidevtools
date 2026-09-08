# Contoso Forge — Pipeline Studio

**Category:** Cloud  
**Status:** Active multi-engine data-engineering project  
**Source:** https://github.com/julian-passebecq/Contoso-Data-Generator-V2

A practical synthetic-data and pipeline studio built to exercise the same data workflow across multiple execution engines, then add orchestration, dbt Gold modelling, ML/evidence paths and Fabric-compatible outputs.

## What I built

- Synthetic Contoso-style data generation for repeatable engineering scenarios.
- Comparable processing paths across pandas, Polars, DuckDB and Spark.
- dbt Gold modelling and Airflow/Cosmos orchestration/evidence work.
- Delta outputs designed to be consumable by Fabric Lakehouse workflows.
- A Windows Pipeline Studio surface plus smoke/evidence contracts.
- ML/evaluation paths that make the project more than a static generator.

## Engineering logic

The project uses one business scenario to compare engines and orchestration patterns instead of hiding them behind one abstraction. That makes trade-offs visible and gives a reproducible way to discuss local engines, Spark/lakehouse processing, dbt modelling and workflow evidence in an interview.

## Interview value

Shows end-to-end data engineering: generation, transforms, multiple compute engines, Delta, dbt, orchestration, evidence/QA and a path toward Fabric workloads.

## Visual evidence

**Current runtime PNG pending in this showcase.** The application source includes a renderer capable of emitting `pipeline-studio.png` and per-step PNGs, but the referenced runtime artifact is not committed on the current source branch. Older Fabric documentation imagery is intentionally not presented as if it were the Pipeline Studio UI.
