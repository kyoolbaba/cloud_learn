# 🏗️ Data Engineering (Concept + AWS↔Azure)

> **Concept note:** Move data from where it's born to where it's useful: **ingest → store → transform → catalog → query/serve**. This is the backbone of analytics + ML.

## The pipeline
```
Sources → Ingest → Raw (lake) → Transform (ETL/ELT) → Curated → Catalog → Query / Warehouse / ML
```

| Stage | What happens |
|---|---|
| Ingest | Batch or streaming data in |
| Store (lake) | Cheap object storage, raw zone |
| Transform | Clean, join, aggregate (ETL/ELT) |
| Catalog | Metadata so data is discoverable + governed |
| Serve | Query (SQL), warehouse, dashboards, ML features |

## AWS ↔ Azure service mapping
| Capability | AWS | Azure |
|---|---|---|
| Data lake storage | S3 | Data Lake Storage (Blob) |
| ETL / integration | Glue | Data Factory / Synapse Pipelines |
| Streaming ingest | Kinesis | Event Hubs |
| Streaming (Kafka) | MSK | Event Hubs (Kafka) / HDInsight |
| Query in place | Athena | Synapse Serverless SQL |
| Data warehouse | Redshift | Synapse / Microsoft Fabric |
| Catalog/governance | Glue Data Catalog / Lake Formation | Microsoft Purview / Unity (Databricks) |
| Big data processing | EMR | HDInsight / Databricks |
| Orchestration | Step Functions / MWAA | Data Factory / Synapse pipelines |

## File format tip (cost + speed)
- Use **columnar formats (Parquet/ORC)** + **partitioning** + **compression** to cut scan cost dramatically. This shows up in DEA-C01 and DP exams.

## Hands-on lab
- Land CSV in object storage → crawl/catalog → query with Athena/Synapse → convert to Parquet.
- **Cleanup:** delete crawlers, catalog, query-result data, and any warehouse (Redshift/Synapse bill while running!).

## ⚠️ Common exam traps
- ETL (transform before load) vs ELT (load then transform) — know which tool fits.
- Athena/Synapse-serverless cost = **data scanned**; partition + columnar reduces it.
- Streaming Firehose buffers to storage; Kinesis Data Streams gives finer control.

## 🃏 Flashcards
| Q | A |
|---|---|
| Serverless SQL over S3? | Athena |
| Azure ETL service? | Data Factory |
| AWS streaming ingest? | Kinesis |
| Azure streaming ingest? | Event Hubs |
| Best analytics file format? | Parquet (columnar) |
| AWS catalog/governance? | Glue Data Catalog + Lake Formation |

🔗 Related: [[databases]] · [[ai-ml]] · [[cost-optimization]]
