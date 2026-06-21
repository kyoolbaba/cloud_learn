---
tags: [cert/dea-c01, aws/data-engineering, readiness]
cert: DEA-C01
aliases: [DEA-C01 Readiness Checklist]
---
> [[DEA-C01|⬅ DEA-C01 Home]] · [[DEA-C01-practice|🧪 Practice Exam]]

# DEA-C01 — exam-readiness checklist

Book only when you can tick **every** box.

## Domain 1 — Ingestion & transformation
- [ ] Batch vs streaming — pick correctly from a scenario
- [ ] Kinesis Data Streams vs Data Firehose vs MSK vs Managed Flink
- [ ] Glue vs EMR vs Lambda vs Athena-CTAS for transforms
- [ ] DMS (incl. CDC), DataSync, Transfer Family, AppFlow, Snow Family — when each
- [ ] File formats: Parquet/ORC vs CSV/JSON/Avro; partitioning, compression, small-file problem
- [ ] Orchestration: Step Functions vs MWAA vs Glue Workflows vs EventBridge
- [ ] Idempotency, retries/DLQ, schema evolution

## Domain 2 — Data store management
- [ ] Pick the store: S3 / Redshift / Athena / DynamoDB / RDS-Aurora / Timestream / Neptune
- [ ] S3 storage classes + lifecycle + Intelligent-Tiering
- [ ] Redshift: RA3/Serverless, distribution & sort keys, COPY/UNLOAD, Spectrum
- [ ] Glue Data Catalog + crawlers; Iceberg / S3 Tables
- [ ] DynamoDB design around access patterns (partition key, GSIs, hot partitions)

## Domain 3 — Operations & support
- [ ] Athena cost/perf: partitioning, projection, Parquet, CTAS
- [ ] QuickSight (SPICE) for BI
- [ ] Automation: Step Functions / MWAA / EventBridge / Glue triggers / SNS
- [ ] Monitoring: CloudWatch vs CloudTrail vs EventBridge; troubleshoot a failed job
- [ ] Data quality: Glue Data Quality (DQDL), DataBrew; job bookmarks (incremental)

## Domain 4 — Security & governance
- [ ] Lake Formation fine-grained (column/row/cell) + LF-Tags
- [ ] Encryption: SSE-KMS vs SSE-S3, CMKs, TLS in transit
- [ ] Macie (PII discovery), masking/anonymization
- [ ] VPC endpoints/PrivateLink; CloudTrail/Config audit; S3 Object Lock retention

## Practice gate
- [ ] Scored **≥ 18/25** on [[DEA-C01-practice|the mock]]
- [ ] Took the official AWS Skill Builder **DEA-C01 practice exam**
- [ ] Built one real mini-pipeline (S3 → Glue crawler → Athena query) in the `learn` account

## Logistics
- [ ] Confirmed format on the **official DEA-C01 Exam Guide PDF**
- [ ] Registered (Pearson VUE); know cost (~$150), pass (~720/1000), ~130 min

## Free official resources
- **AWS Skill Builder** — "Data Engineer" learning plan + official practice question set
- **AWS Workshops** (workshops.aws) — Glue, Athena, Redshift, Lake Formation guided labs
- **Analytics Lens** (Well-Architected) + **DEA-C01 Exam Guide** PDF

When every box is ticked → **book it**, then continue to [[MLA-C01|MLA-C01 (your bullseye)]]. See [[CERT_ROADMAP]].
