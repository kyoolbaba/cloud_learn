---
tags: [foundations, beginner, data-engineering, lakehouse]
aliases: [Lakehouse Basics, Data Lake vs Warehouse, Lakehouse]
---
> [[04-git-cicd-basics|◀ Git + CI/CD]] · [[HOME|🏠 Home]] · [[STUDY_PLAN|Plan (M5.5)]] · [[PROGRESS|Tracker]] · [[06-mlops-basics|MLOps ▶]]

# 05 · Lakehouse basics (where the data lives)

## In plain English
Three ways to store analytics data:
- **Data lake** — a giant cheap bucket (S3) holding *raw files* of any shape. Flexible, but messy.
- **Data warehouse** — a tidy database of *clean tables* built for fast SQL/BI (Redshift). Structured, but pricier and less flexible.
- **Lakehouse** — the **best of both**: cheap lake storage (S3) **+** warehouse-like reliability (ACID transactions, schema, fast queries) using **open table formats** (Delta / Iceberg / Hudi).

> Analogy: a **lake** is a warehouse full of unlabeled boxes; a **warehouse** is a neat filing cabinet; a **lakehouse** is the warehouse of boxes *with a smart index* so you get filing-cabinet speed at box-storage price.

## Why it matters for your career
This is the heart of the **Data Engineer / Cloud Data Engineer** role and feeds every ML model. Your forecasting data (Parquet in S3, partitioned by series) is already a baby lakehouse. [[DEA-C01]] tests exactly this.

## Key concepts
- **Parquet** — columnar file format: reads only the columns you need, compresses well → cheap, fast analytics. (vs row formats like CSV/JSON.)
- **Partitioning** — organize files as `year=/month=/day=/` so engines scan less = cheaper + faster.
- **Compaction** — merge many tiny files into fewer big ones (the "small-files problem").
- **Schema evolution** — safely add/change columns over time without breaking old data.
- **Open table formats** — **Delta Lake**, **Apache Iceberg**, **Apache Hudi**: add ACID transactions, time-travel, and schema evolution on top of Parquet-in-S3. (**S3 Tables** = managed Iceberg.)
- **Glue Data Catalog** — the central "table of contents" (schemas + partitions) engines read.
- **Lake Formation** — fine-grained (row/column/cell) permissions over the lake.
- **Athena optimization** — partition pruning, columnar Parquet, compression → pay per TB scanned, so scan less.
- **Unity Catalog** (Databricks) — governance + lineage across a Databricks lakehouse.
- **Data lineage / data quality** — track where data came from; validate it before publishing.

## Tools
S3 · Glue · Athena · Lake Formation · Spark · Databricks · Parquet · Delta / Iceberg / Hudi

## Mini lab (full version = [[STUDY_PLAN|STUDY_PLAN Module 5.5]])
1. Put the same data in S3 as **CSV** and as **Parquet**.
2. Compare file size + Athena query time (Parquet should win big).
3. **Partition** the data by `year/month`.
4. Create a **Glue** table (crawler or DDL).
5. Query it with **Athena**.
6. Simulate **schema evolution** (add a column).
7. Add basic **data-quality** checks (no nulls in key, freshness).
8. Write a short note comparing **Delta vs Iceberg vs Hudi**.

> 💸 Cost/safety: S3 + Glue + Athena are pennies for tiny data, but **use the personal `learn` account** and delete the bucket/catalog after. Athena bills per TB scanned — partition + Parquet keeps it ~free.

## ✅ Checkpoint
I can explain **lake vs warehouse vs lakehouse** and design a basic **S3 + Glue + Athena** data lake with partitioned Parquet.

---
Back to: [[HOME]] · [[START-HERE]] · [[STUDY_PLAN]] · [[PROGRESS]] · related cert: [[DEA-C01]]
