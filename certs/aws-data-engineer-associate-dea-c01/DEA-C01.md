---
tags: [cert/dea-c01, aws/data-engineering, moc]
cert: DEA-C01
level: associate
aliases: [DEA-C01, AWS Data Engineer Associate]
---
> **Track notes:** [[domain-1-ingestion-transformation|1 · Ingestion & Transform]] · [[domain-2-data-store-management|2 · Data Stores]] · [[domain-3-data-operations-support|3 · Operations]] · [[domain-4-data-security-governance|4 · Security & Governance]] · [[DEA-C01-practice|🧪 Practice]] · [[DEA-C01-readiness|✅ Readiness]]
> **Up:** [[CERTS-MOC|All certs]] · [[CERT_ROADMAP|Roadmap]]

# AWS Certified Data Engineer – Associate (DEA-C01) — study track

The **pipelines** lane: ingest → transform → store → serve → secure data on AWS. This is the
associate that maps to your day job — you already move Parquet through S3 and fan work out with
Step Functions/SQS. Associate level = scenario questions ("which service / which design"), more
depth than foundational.

> ✅ **Verified 2026-06-21** against [aws.amazon.com](https://aws.amazon.com/certification/certified-data-engineer-associate/) + the official **DEA-C01 Exam Guide** (docs.aws.amazon.com): 65 Q · 130 min · pass **720/1000** · **$150** · domains **34/26/22/18**. Still re-skim the current Exam Guide PDF before booking.

## Exam facts (verified 2026-06-21)
| | |
|---|---|
| Code | **DEA-C01** |
| Level | Associate |
| Questions | **65** (multiple-choice + multiple-response) |
| Time | **130 minutes** |
| Pass | **720 / 1000** (scaled) |
| Cost | **$150 USD** |
| Prereqs | none (recommended: CLF-C02 + ~1 yr data experience) |
| Validity | 3 years |

## The 4 domains (memorize the weightings)
| # | Domain | Weight | File |
|---|---|---|---|
| 1 | Data Ingestion & Transformation | **34%** | [[domain-1-ingestion-transformation\|open]] |
| 2 | Data Store Management | **26%** | [[domain-2-data-store-management\|open]] |
| 3 | Data Operations & Support | **22%** | [[domain-3-data-operations-support\|open]] |
| 4 | Data Security & Governance | **18%** | [[domain-4-data-security-governance\|open]] |

Domain 1 alone is **a third of the exam** — Glue, Kinesis/Firehose, EMR, orchestration. Live there.

## 4–6 week study plan (~1 hr/day)
| Week | Do |
|---|---|
| 1–2 | Domain 1 (ingestion + ETL: Glue, Kinesis, EMR, Step Functions/MWAA) |
| 3 | Domain 2 (S3 lake, Redshift, DynamoDB, Lake Formation, catalog) |
| 4 | Domain 3 (Athena, QuickSight, monitoring, data quality, troubleshooting) |
| 5 | Domain 4 (Lake Formation perms, KMS, Macie, governance) |
| 6 | `practice-questions.md` + official practice exam → `exam-readiness-checklist.md` → **book** |

## What you've already built that maps here
| Already done | Covers (DEA-C01) |
|---|---|
| `projects/01-s3-file-vault`, `06-s3-trigger-pipeline` | D1/D2 (S3 lake, event-driven ingestion) |
| `projects/08-sqs-worker`, `09-stepfunctions-fanout` | D1 (decoupling, orchestration of transforms) |
| `projects/11-terraform-backend` | D2/D4 (IaC for stores + permissions) |
| `labs/m4-serverless`, `m5-orchestration` | D1/D3 (Lambda triggers, Step Functions pipelines) |
| Your Parquet + partitioning work in `db_polars_app` | D1 (file formats, partitioning, columnar) |

**New things to add for this cert:** Glue (ETL + Catalog + crawlers), Athena, Kinesis/Firehose, EMR, Redshift, Lake Formation, MWAA.

## Exam-day wrong-answer tells
- "serverless SQL over S3, pay per scan" → **Athena**. "petabyte warehouse, complex joins" → **Redshift**.
- "streaming, sub-second, replay" → **Kinesis Data Streams**; "stream → land in S3/Redshift, no code" → **Data Firehose**.
- "serverless Spark ETL + catalog" → **Glue**; "big custom Spark/Hadoop clusters" → **EMR**.
- "orchestrate steps with retries/branching" → **Step Functions**; "complex DAGs, Airflow" → **MWAA**.
- "fine-grained (row/column) lake permissions" → **Lake Formation**; "find PII in S3" → **Macie**.
- Performance fix on S3 queries → **partition + columnar (Parquet) + compress**.
