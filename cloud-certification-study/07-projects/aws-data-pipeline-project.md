# 🛠️ Project: AWS Data Pipeline (S3 → Glue → Athena → Redshift)

> **Goal:** Build an end-to-end batch data pipeline on AWS. Reinforces DEA-C01 + SAA-C03 and gives you a portfolio piece.
>
> 🌍 **Real-world story:** Raw sales CSVs land daily; you clean + catalog them, query with SQL, and load curated data into a warehouse for dashboards.

## What you'll build
```
Sample CSV → S3 (raw) → Glue Crawler → Glue Catalog → Glue Job (CSV→Parquet) → S3 (curated)
                                                              ↓
                                          Athena (ad-hoc SQL)  +  Redshift Serverless (warehouse)
```

## Skills practiced
- Data lake zoning (raw/curated), Parquet + partitioning
- Glue crawlers/jobs + Data Catalog
- Athena querying + cost control
- Redshift load + simple star schema
- IAM least-privilege roles, CloudWatch monitoring

## Steps
1. Create S3 buckets: `raw/`, `curated/` (tag `project=cert-study`).
2. Upload a sample dataset (e.g., public sales/retail CSV).
3. Run a **Glue crawler** on `raw/` → catalog table.
4. Query raw data in **Athena**.
5. Write a **Glue job** to clean + convert to **Parquet**, partitioned, into `curated/`.
6. Crawl `curated/`; compare Athena scan cost vs raw.
7. Spin up **Redshift Serverless**; `COPY` curated data; run analytics queries.
8. Add a **CloudWatch** dashboard/alarm.
9. (Bonus) Trigger the job on new files with **EventBridge**.

## ✅ Success criteria
- [ ] Athena returns correct results on curated data
- [ ] Parquet + partition reduced bytes scanned vs CSV
- [ ] Redshift query returns aggregates
- [ ] IAM roles are least-privilege (no wildcards you don't need)

## 💸 Cleanup (do it!)
- [ ] Delete **Redshift Serverless** workgroup + namespace (bills while active)
- [ ] Delete Glue jobs, crawlers, catalog DB
- [ ] Empty + delete S3 buckets (incl. Athena query results)
- [ ] Delete CloudWatch dashboard/alarm + EventBridge rule
- [ ] Check Cost Explorer

## 📝 Reflection / write-up (for your portfolio)
- Architecture diagram:
- What cost-optimization did you apply?
- AWS↔Azure: how would this look on Azure? → see [[azure-data-pipeline-project]]

🔗 Related: [[../03-shared-cloud-concepts/data-engineering]] · [[../01-aws/associate/aws-data-engineer-associate-DEA-C01]]
