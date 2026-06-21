---
tags: [cert/dea-c01, aws/data-engineering, operations, analytics]
cert: DEA-C01
domain: 3
aliases: [DEA-C01 Domain 3, Data Operations and Support]
---
> [[domain-2-data-store-management|◀ Domain 2]] · [[DEA-C01|DEA-C01 Home]] · [[domain-4-data-security-governance|Domain 4 · Security ▶]]

# Domain 3 — Data Operations & Support (22%)

Serving the data (query + BI), automating pipelines, monitoring them, ensuring **data quality**,
and troubleshooting + tuning performance.

## 3.1 Query & serve
- **Amazon Athena** — serverless SQL on S3 via the Glue Catalog. **Pay per TB scanned** → cost = how much you scan. Uses Presto/Trino. **Workgroups** isolate teams + set per-query data limits.
- **Amazon QuickSight** — managed BI dashboards. **SPICE** = in-memory engine for fast viz; **Q** = natural-language questions. The "serve to business users" answer.
- **Redshift** for warehouse-style BI; **Redshift Spectrum** to reach S3 from the warehouse.

## 3.2 Athena performance & cost (high-yield)
- **Partition** the data and **prune** with WHERE on partition columns.
- **Partition projection** — compute partitions from a pattern instead of listing them (faster on huge tables).
- **Columnar Parquet/ORC + compression** → scan less.
- **CTAS / INSERT INTO** to materialize transformed/partitioned tables.
- Avoid `SELECT *`; select only needed columns (columnar pays off).

## 3.3 Automation & scheduling
| Need | Service |
|---|---|
| Orchestrate multi-step pipeline (retries, branching, Map) | **Step Functions** |
| Airflow DAGs | **MWAA** |
| Time/event triggers ("every night", "on new S3 object") | **EventBridge** (schedules + rules), S3 notifications |
| Glue-native chaining + triggers | **Glue Workflows / triggers** |
| Glue-cataloged streaming/job event handling, glue code | **Lambda** |
| Notify on success/failure | **SNS** (email/SMS), SQS |

## 3.4 Monitoring, logging & troubleshooting
| Service | Role |
|---|---|
| **CloudWatch** | metrics, **Logs**, **alarms**, dashboards (job duration, errors, DPU usage) |
| **CloudTrail** | API **audit** ("who started/deleted this job") |
| **EventBridge** | react to events (job state change → alert/trigger) |
| **Glue job logs / Spark UI** | debug ETL failures, skew, OOM |

Troubleshooting flow: read the **last error line** → check CloudWatch Logs for the job → look for skew / small files / OOM / IAM-denied → fix and re-run (idempotently).

## 3.5 Data quality
- **AWS Glue Data Quality** — define rules (**DQDL**) like completeness, uniqueness, freshness; runs on Catalog tables or in Glue jobs; can **stop the pipeline** or quarantine bad rows on failure.
- **Glue DataBrew** — profile data (nulls, distributions, outliers) and build cleaning recipes visually.
- Good pipelines **validate before publishing** (gate downstream consumers from bad data).

## 3.6 Performance & reliability practices
- Right-size Glue DPUs / EMR cluster; use **job bookmarks** in Glue to process only new data (incremental).
- Compact small files; tune partitions; cache hot data (SPICE, ElastiCache).
- Build for **retry/idempotency**; use DLQs; alarm on failures so issues surface fast.

## Hands-on (cleanup included)
```powershell
$env:AWS_PROFILE = "learn"
# Run an Athena query and cap cost with a workgroup data-scan limit
aws athena start-query-execution --query-string "SELECT count(*) FROM dea.raw" `
  --work-group primary --result-configuration OutputLocation=s3://yourname-dea-lab/athena/
# Alarm on a failed Glue job via CloudWatch (so failures page you, not surprise you)
# CLEANUP: delete Athena results prefix; remove the alarm.
aws s3 rm s3://yourname-dea-lab/athena/ --recursive
```

## Flashcards
- Athena = serverless SQL on S3, pay per TB scanned → partition + Parquet to cut cost.
- Partition projection = compute partitions from a pattern (fast on huge tables).
- QuickSight = BI dashboards; SPICE = in-memory.
- CloudWatch = metrics/logs/alarms; CloudTrail = audit; EventBridge = event routing/schedules.
- Glue Data Quality (DQDL) = rule-based validation; Glue job bookmarks = incremental processing.

## Practice questions
**Q1.** An Athena query scans 2 TB of CSV and costs too much. Best fix?
- A) Bigger workgroup  B) **Partition + convert to compressed Parquet** ✅  C) SELECT *  D) Add nodes

**Q2.** Build interactive BI dashboards for business users on AWS:
- A) CloudWatch  B) Athena only  C) **QuickSight** ✅  D) Glue Studio

**Q3.** Enforce "no nulls in customer_id and data must be < 24 h old" before publishing a table:
- A) IAM policy  B) **AWS Glue Data Quality (DQDL rules)** ✅  C) S3 lifecycle  D) Macie

**Q4.** Process only newly arrived files in a recurring Glue job (not the whole bucket):
- A) Crawl every run  B) **Enable Glue job bookmarks** ✅  C) Use EMR  D) Disable partitions

**Q5.** You need an audit trail of who deleted a Glue job. Which service?
- A) CloudWatch Logs  B) **CloudTrail** ✅  C) QuickSight  D) EventBridge
