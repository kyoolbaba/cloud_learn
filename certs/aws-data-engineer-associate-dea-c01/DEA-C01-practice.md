---
tags: [cert/dea-c01, aws/data-engineering, practice-exam]
cert: DEA-C01
aliases: [DEA-C01 Practice Exam, DEA-C01 Mock]
---
> [[DEA-C01|⬅ DEA-C01 Home]] · [[DEA-C01-readiness|Readiness Checklist ➡]]

# DEA-C01 — mixed mock exam (25 Q)

Domain-weighted (Ingestion/Transform 34% · Stores 26% · Operations 22% · Security 18%).
One ~35-min sitting, then review every miss. Target ≥ 72% (18/25).

1. Real-time stream, replayable, multiple consumers, sub-second:
   A) Data Firehose  B) **Kinesis Data Streams**  C) SQS  D) Glue

2. Deliver a stream into S3 + Redshift with no code, near-real-time:
   A) **Amazon Data Firehose**  B) Kinesis Data Streams  C) DMS  D) EMR

3. Serverless Spark ETL with a managed data catalog, lowest ops:
   A) EMR  B) **AWS Glue**  C) EC2 + Spark  D) Lambda

4. Ongoing change-data-capture from on-prem PostgreSQL to AWS:
   A) DataSync  B) **DMS (CDC)**  C) Snowball  D) AppFlow

5. Cut Athena cost on a 2 TB CSV dataset:
   A) SELECT *  B) **Partition + compressed Parquet**  C) Bigger workgroup  D) Add columns

6. Orchestrate a pipeline with retries, branching, and parallel fan-out:
   A) Cron on EC2  B) **Step Functions**  C) SNS  D) Glue crawler

7. Airflow-style DAG orchestration, managed:
   A) Step Functions  B) **MWAA**  C) EventBridge  D) SWF

8. Process only newly arrived files each Glue run:
   A) Re-crawl all  B) **Glue job bookmarks**  C) Bigger DPUs  D) EMR

9. Avro vs Parquet — Parquet is best for:
   A) Row-by-row streaming  B) **Columnar analytics scans**  C) Schema registry  D) Images

10. Petabyte analytical SQL with complex joins for BI:
    A) DynamoDB  B) **Redshift**  C) RDS  D) ElastiCache

11. Single-digit-ms key lookups at massive scale:
    A) Redshift  B) Athena  C) **DynamoDB**  D) Aurora

12. Central schema/partition metadata for Athena + Redshift Spectrum + EMR:
    A) S3 policy  B) **Glue Data Catalog**  C) DynamoDB  D) Secrets Manager

13. Reduce cross-node shuffles on a recurring Redshift join:
    A) Sort key only  B) **Distribution KEY on the join column**  C) More WLM queues  D) CSV

14. Add ACID + time-travel to S3 tables:
    A) Plain Parquet  B) **Apache Iceberg / S3 Tables**  C) DynamoDB  D) Glacier

15. Auto-move S3 data to cheaper tiers when access is unpredictable:
    A) One Zone-IA always  B) **S3 Intelligent-Tiering**  C) Deep Archive day 1  D) Standard only

16. Serverless SQL directly on S3, pay per TB scanned:
    A) Redshift  B) **Athena**  C) EMR  D) QuickSight

17. Interactive BI dashboards for business users:
    A) CloudWatch  B) **QuickSight**  C) Glue Studio  D) Athena

18. Enforce "no null customer_id, data < 24 h old" before publishing:
    A) IAM  B) **Glue Data Quality (DQDL)**  C) S3 lifecycle  D) Macie

19. Audit trail of who deleted a Glue job:
    A) CloudWatch Logs  B) **CloudTrail**  C) QuickSight  D) EventBridge

20. Speed up Athena on a huge table without listing all partitions:
    A) SELECT *  B) **Partition projection**  C) gzip CSV  D) Bigger workgroup

21. Analysts may query a table but not see the `ssn` column:
    A) Bucket policy  B) **Lake Formation column-level permissions**  C) KMS policy  D) NACL

22. Discover credit-card numbers stored in S3:
    A) GuardDuty  B) Inspector  C) **Macie**  D) Config

23. Auditable, customer-controlled encryption keys with usage logged:
    A) SSE-S3  B) **SSE-KMS (customer-managed CMK)**  C) Client gzip  D) None

24. Keep Glue/Athena data traffic off the public internet:
    A) NAT only  B) **VPC endpoints / PrivateLink**  C) CloudFront  D) Public subnet

25. Make objects immutable for a 7-year legal hold:
    A) Versioning only  B) **S3 Object Lock (compliance mode)**  C) Lifecycle expire  D) Glacier w/o lock

---

## Answer key
1-B, 2-A, 3-B, 4-B, 5-B, 6-B, 7-B, 8-B, 9-B, 10-B, 11-C, 12-B, 13-B, 14-B, 15-B,
16-B, 17-B, 18-B, 19-B, 20-B, 21-B, 22-C, 23-B, 24-B, 25-B

### Why (the ones people miss)
- **1 vs 2:** Streams = replay + custom consumers (you manage shards); Firehose = managed *delivery* to a destination, near-real-time, no replay.
- **3 vs (EMR):** Glue = serverless, low-ops default; EMR = full control/large custom Spark-Hadoop.
- **6 vs 7:** Step Functions = state machine (retries/branch/Map); MWAA = Airflow DAGs.
- **13:** distribution KEY co-locates joined rows → no shuffle; sort key only helps range filters.
- **20:** partition projection computes partitions from a pattern — avoids slow partition listing on huge tables.
- **21:** row/column/cell security = **Lake Formation**, never a bucket policy.

**Scoring:** 18+/25 → ready; do the readiness checklist. <18 → re-read the weak domain and retake.
