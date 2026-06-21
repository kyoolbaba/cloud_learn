---
tags: [cert/dea-c01, aws/data-engineering, storage, databases]
cert: DEA-C01
domain: 2
aliases: [DEA-C01 Domain 2, Data Store Management]
---
> [[domain-1-ingestion-transformation|◀ Domain 1]] · [[DEA-C01|DEA-C01 Home]] · [[domain-3-data-operations-support|Domain 3 · Operations ▶]]

# Domain 2 — Data Store Management (26%)

Choosing and running the **right store** for the data and access pattern, plus the metadata
catalog that makes a lake queryable.

## 2.1 Pick the right store (the core skill)
| Access pattern | Store |
|---|---|
| Cheap, infinite **object storage / data lake** | **Amazon S3** |
| **Data warehouse** — big analytical SQL, joins, BI | **Amazon Redshift** |
| Serverless SQL **directly on S3** (no warehouse to run) | **Athena** (engine, see D3) |
| **Key-value / document**, single-digit-ms, huge scale | **DynamoDB** |
| **Relational OLTP** (transactions, app backend) | **RDS** / **Aurora** |
| In-memory cache / low-latency | **ElastiCache / MemoryDB** |
| Time-series at scale | **Timestream** |
| Graph (relationships) | **Neptune** |
| Wide-column (Cassandra) | **Keyspaces** |

**Trap:** "analytics warehouse" = Redshift; "S3 + serverless query" = Athena; "millisecond key lookups at scale" = DynamoDB; "relational transactions" = RDS/Aurora. Don't put OLTP on Redshift or analytics on DynamoDB.

## 2.2 S3 as the data lake
- **Storage classes:** Standard → Standard-IA / One Zone-IA → Glacier Instant/Flexible/Deep Archive (cold, cheapest). **Intelligent-Tiering** auto-moves data by access — good when patterns are unknown.
- **Lifecycle policies** transition/expire objects automatically (cost control).
- **Open table formats:** **Apache Iceberg** (and Hudi/Delta) add ACID transactions, time-travel, schema evolution on S3. **S3 Tables** = managed Iceberg. Increasingly tested.
- **Partitioning + Parquet** (from D1) is part of store design.

## 2.3 Redshift essentials (warehouse)
- **RA3** nodes = compute separate from managed storage (RMS); **Redshift Serverless** = no clusters to manage.
- **Distribution style** (KEY/EVEN/ALL) controls how rows spread across nodes — pick KEY on common join columns to avoid data shuffles.
- **Sort keys** speed range filters. **Redshift Spectrum** queries S3 directly (lake + warehouse together).
- **COPY** loads from S3 in parallel (the standard bulk-load path); **UNLOAD** exports to S3.
- **Workload Management (WLM)** / concurrency scaling for mixed workloads.

## 2.4 The metadata catalog (makes the lake usable)
- **AWS Glue Data Catalog** — central schema/table metadata used by Athena, Redshift Spectrum, EMR, Glue. **Crawlers** infer schema + partitions from S3.
- Without a catalog, query engines don't know your table's columns/partitions.

## 2.5 Governed lake & data sharing
- **AWS Lake Formation** — sits over S3 + Glue Catalog to give **fine-grained permissions** (database/table/**column/row/cell**) and centralized data-lake governance (more in D4).
- **Amazon DataZone** — business data catalog / governance + discovery across teams.
- **Redshift data sharing** / **AWS Data Exchange** — share data without copying.

## 2.6 Schema & lifecycle design
- Model for the **query pattern**, not just normalization (denormalize/star-schema for analytics).
- **DynamoDB**: design around access patterns; partition key spreads load; use GSIs for alternate queries; avoid hot partitions.
- Plan **retention/backup**: S3 versioning + Object Lock (WORM), RDS/Redshift snapshots, point-in-time recovery.

## Hands-on (cleanup included)
```powershell
$env:AWS_PROFILE = "learn"
# Add a lifecycle rule so lab data ages to cheap storage then expires (cost safety)
aws s3api put-bucket-lifecycle-configuration --bucket yourname-dea-lab `
  --lifecycle-configuration file://lifecycle.json   # transition→IA after 30d, expire 90d
# Redshift Serverless: create a namespace/workgroup in console, query, then DELETE it (it bills while up)
# CLEANUP: delete the Redshift Serverless workgroup + namespace, empty/delete the bucket.
```

## Flashcards
- Redshift = warehouse; Athena = serverless SQL on S3; DynamoDB = KV/doc ms-latency; RDS/Aurora = OLTP.
- Glue Data Catalog = central metadata; crawlers infer schema/partitions.
- Lake Formation = fine-grained (row/column) lake permissions.
- Redshift dist key = avoid shuffles; sort key = fast range filters; COPY = bulk load from S3.
- Iceberg / S3 Tables = ACID + time-travel on the lake.

## Practice questions
**Q1.** Petabyte-scale analytical SQL with complex joins for BI dashboards:
- A) DynamoDB  B) **Redshift** ✅  C) RDS  D) ElastiCache

**Q2.** Central schema/partition metadata shared by Athena, Redshift Spectrum, and EMR:
- A) S3 bucket policy  B) **AWS Glue Data Catalog** ✅  C) DynamoDB  D) Secrets Manager

**Q3.** Single-digit-millisecond key lookups at massive scale:
- A) Redshift  B) Athena  C) **DynamoDB** ✅  D) Aurora

**Q4.** Reduce a Redshift query that shuffles data across nodes on every join. Best lever?
- A) Add sort key only  B) **Choose a distribution KEY on the join column** ✅  C) More WLM queues  D) Convert to CSV

**Q5.** Add ACID transactions + time-travel to tables stored on S3:
- A) Plain Parquet  B) **Apache Iceberg / S3 Tables** ✅  C) DynamoDB  D) Glacier
