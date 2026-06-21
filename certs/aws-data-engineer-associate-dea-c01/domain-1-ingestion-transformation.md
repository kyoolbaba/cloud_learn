---
tags: [cert/dea-c01, aws/data-engineering, ingestion, etl]
cert: DEA-C01
domain: 1
aliases: [DEA-C01 Domain 1, Data Ingestion and Transformation]
---
> [[DEA-C01|⬅ DEA-C01 Home]] · Next: [[domain-2-data-store-management|Domain 2 · Data Stores ▶]]

# Domain 1 — Data Ingestion & Transformation (34%)

The biggest domain. Getting data **in** (batch + streaming) and **reshaping** it. Know which
ingestion/transform/orchestration service fits each scenario.

## 1.1 Batch vs streaming (frame every question with this)
- **Batch** — bounded chunks on a schedule (nightly load). Tools: Glue, EMR, DMS, Lambda, Athena CTAS.
- **Streaming** — unbounded, continuous, low-latency (clickstream, IoT, logs). Tools: Kinesis, MSK, Managed Flink.
- Pick streaming when you need **near-real-time**; batch when periodic is fine (cheaper, simpler).

## 1.2 Ingestion services (match to scenario)
| Need | Service |
|---|---|
| Real-time stream, **replayable**, multiple consumers, sub-second | **Kinesis Data Streams** |
| Stream → **land in S3 / Redshift / OpenSearch**, no code, near-real-time (buffered) | **Amazon Data Firehose** (was Kinesis Firehose) |
| Apache **Kafka**, managed | **Amazon MSK** |
| Real-time analytics/aggregations on a stream (SQL/Java) | **Managed Service for Apache Flink** |
| Migrate/replicate a **database** (one-time or CDC ongoing) | **AWS DMS** |
| SaaS app data (Salesforce, etc.) → AWS | **AppFlow** |
| Big offline copy from on-prem | **Snow Family**; online file transfer = **DataSync**; SFTP = **Transfer Family** |
| Decouple producers/consumers (buffer/queue) | **SQS** (you've built this) |

**Trap:** Streams vs Firehose — **Streams** = custom consumers, replay, you manage shards/throughput; **Firehose** = fully managed *delivery* to a destination with buffering (≥ ~60s latency), no replay.

## 1.3 Transformation / ETL services
| Need | Service |
|---|---|
| **Serverless** Spark ETL + data catalog + crawlers | **AWS Glue** (jobs, Glue Studio, Spark/Python shell) |
| Visual, no-code data prep/cleaning | **Glue DataBrew** |
| Big, tunable **Spark/Hadoop/Hive/Presto** clusters | **Amazon EMR** |
| SQL-based transform over S3 (CREATE TABLE AS SELECT) | **Athena (CTAS / INSERT)** |
| Lightweight, event-driven transform (<15 min) | **Lambda** |

**Glue vs EMR:** Glue = serverless, pay-per-job, less ops, great default. EMR = full control, custom frameworks, large/long jobs, can be cheaper at scale (spot).

## 1.4 File formats & layout (DEA loves this — directly optimizes cost/speed)
- **Columnar** (**Parquet**, **ORC**) → analytics: read only needed columns, compress well. **Row** (CSV, JSON, Avro) → record-by-record/ingest. **Avro** = row + schema, good for streaming/schema evolution.
- **Convert raw CSV/JSON → Parquet** for query engines (Athena/Redshift Spectrum) — huge scan savings.
- **Compression:** Snappy (fast, splittable — default for Parquet), gzip (smaller, not splittable), Zstd.
- **Partitioning:** organize S3 by `year=/month=/day=/` so engines prune (scan less). Avoid **small-files problem** — compact into larger files (~128 MB+).

> Your forecasting already writes Parquet partitioned by series — that's textbook DEA Domain 1.

## 1.5 Orchestration (sequencing the pipeline)
| Need | Service |
|---|---|
| State machine: steps, **retries, Choice/branch, Map fan-out** | **Step Functions** (you've built this) |
| Complex DAGs, Python, Airflow ecosystem | **Amazon MWAA** (Managed Airflow) |
| Glue-native job chaining | **Glue Workflows** |
| Event-driven triggers ("on S3 put → start job") | **EventBridge** / S3 notifications |

## 1.6 Programming/quality concepts they test
- **Idempotency** — reprocessing the same input doesn't duplicate results (use dedup keys, upserts).
- **Error handling** — retries with backoff, **dead-letter queues**, Step Functions Catch.
- **CDC (change data capture)** — DMS streams ongoing DB changes.
- **Schema evolution** — Glue Schema Registry / Avro handle changing schemas.

## Hands-on (`$env:AWS_PROFILE="learn"` — cleanup included)
```powershell
$env:AWS_PROFILE = "learn"
# Crawl S3 data into the Glue Data Catalog, then query with Athena (serverless, cheap)
aws s3 cp .\sample.parquet s3://yourname-dea-lab/raw/
aws glue create-crawler --name dea-lab --role <GlueRole> `
  --database-name dea --targets '{"S3Targets":[{"Path":"s3://yourname-dea-lab/raw/"}]}'
aws glue start-crawler --name dea-lab
# ...query in Athena console: SELECT * FROM dea.raw LIMIT 10;
# CLEANUP (avoid charges):
aws glue delete-crawler --name dea-lab
aws s3 rm s3://yourname-dea-lab/raw/ --recursive
```

## Flashcards
- Streams = replayable custom consumers; Firehose = managed delivery to S3/Redshift.
- Glue = serverless Spark ETL + Catalog; EMR = full Spark/Hadoop clusters.
- Parquet/ORC = columnar (analytics); partition + compress to cut scans.
- Step Functions = retries/branch/Map; MWAA = Airflow DAGs.
- Idempotency = safe reprocessing.

## Practice questions
**Q1.** Stream events with **replay** and multiple independent consumers, sub-second:
- A) Data Firehose  B) **Kinesis Data Streams** ✅  C) SQS  D) Glue

**Q2.** Land a stream into S3 and Redshift with **no code**, near-real-time:
- A) **Amazon Data Firehose** ✅  B) Kinesis Data Streams  C) EMR  D) DMS

**Q3.** Cheapest, lowest-ops way to run **serverless Spark ETL** with a data catalog:
- A) EMR  B) **AWS Glue** ✅  C) EC2 + Spark  D) Lambda

**Q4.** Reduce Athena cost on a large CSV dataset. Best change?
- A) Add more columns  B) **Convert to partitioned Parquet (compressed)** ✅  C) Use gzip CSV only  D) Bigger workgroup

**Q5.** Continuously replicate ongoing changes from an on-prem PostgreSQL to AWS:
- A) DataSync  B) Snowball  C) **DMS with CDC** ✅  D) AppFlow
