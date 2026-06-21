# AWS Certified Data Engineer – Associate

> 🍼 **Beginner explanation:** Teaches how to move, clean, store, and query data at scale on AWS — building data lakes, warehouses, and pipelines. Core cert for your data-science career.
>
> 🌍 **Real-world example:** Sales data lands in S3 hourly. You build a Glue job to clean it, catalog it, query it with Athena, and load it into Redshift for dashboards. This cert is exactly that.

| Field | Value |
|---|---|
| **1. Certification name** | AWS Certified Data Engineer – Associate |
| **2. Exam code** | DEA-C01 |
| **3. Level** | Associate |
| **4. Best for role** | Data engineers, analytics engineers, data scientists moving into pipelines |
| **5. Prerequisites** | SQL + data basics; CLF-C02/SAA helpful |

---

## 6. Core topics
- Data ingestion (batch + streaming)
- Transformation & ETL/ELT, orchestration
- Data lakes vs data warehouses
- Data modeling, partitioning, file formats (Parquet/ORC)
- Governance, security, data quality, cataloging
- Cost & performance optimization

## 7. AWS services to learn
| Category | Services |
|---|---|
| Storage / lake | S3, Lake Formation |
| ETL / catalog | Glue (jobs, crawlers, Data Catalog), Glue DataBrew |
| Query | Athena |
| Warehouse | Redshift (+ Spectrum) |
| Streaming | Kinesis (Data Streams/Firehose), MSK basics |
| Orchestration | Step Functions, MWAA (Airflow), EventBridge |
| Security/Mgmt | IAM, KMS, CloudWatch, Lake Formation permissions |

## 8. Hands-on labs
1. **S3 data lake** with raw/clean/curated prefixes. *(Cleanup: empty + delete bucket.)*
2. **Glue crawler** → build Data Catalog table from S3. *(Cleanup: delete crawler, database, catalog tables.)*
3. **Athena query** over the cataloged data; convert CSV→Parquet. *(Cleanup: delete query results bucket data.)*
4. **Redshift Serverless** small warehouse; load from S3; query. *(Cleanup: delete workgroup/namespace — billed while active!)*
5. **Streaming:** Kinesis Firehose → S3 with simple transform. *(Cleanup: delete delivery stream.)*
6. **Simple ETL pipeline:** EventBridge → Glue job → Athena. *(Cleanup: delete all components.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–2 | Data lake on S3, formats, partitioning; Lab 1 |
| 3–4 | Glue crawlers + Data Catalog; Lab 2 |
| 5 | Athena + Parquet optimization; Lab 3 |
| 6–7 | Redshift architecture + loading; Lab 4 |
| 8 | Streaming (Kinesis/Firehose); Lab 5 |
| 9 | Orchestration (Step Functions/MWAA); Lab 6 |
| 10 | Governance + Lake Formation + security |
| 11 | Cost/performance optimization |
| 12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 80%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | S3 lake + Glue + Athena (Labs 1–3) |
| 2 | Redshift + streaming (Labs 4–5) |
| 3 | Orchestration + governance + security (Lab 6) |
| 4 | Cost/perf + 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1 | Data concepts, lakes vs warehouses, formats |
| 2 | S3 lake design (Lab 1) |
| 3 | Glue + Catalog (Lab 2) |
| 4 | Athena (Lab 3) |
| 5 | Redshift (Lab 4) |
| 6 | Streaming (Lab 5) |
| 7 | Orchestration + governance (Lab 6) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **80%+**. Expect scenario questions: choose the right ingestion/transform/store tool for cost + latency.
- Know when **Athena vs Redshift vs EMR**, **Kinesis vs MSK**, **Glue vs EMR**.
- 4 timed mocks; log misses to `04-trackers/weak-topic-log.md`.

## 13. Final revision checklist (last 3 days)
- [ ] When to use Athena vs Redshift vs EMR
- [ ] Partitioning + columnar formats reduce cost/scan
- [ ] Kinesis Data Streams vs Firehose vs MSK
- [ ] Glue crawler vs job vs Data Catalog roles
- [ ] Lake Formation permissions model
- [ ] Redshift distribution & sort keys (basics)
- [ ] Flashcards reviewed twice

## 14. Notes template
```
### Topic: <name>
- Beginner explanation:
- Real-world use:
- AWS service(s):
- Azure equivalent:
- Common exam trap:
- My example:
```

## 15. Mistake log template
| Date | Topic | What I got wrong | Correct concept | Revisit date |
|---|---|---|---|---|

## 16. Flashcards (starter set)
| Q | A |
|---|---|
| Query S3 with SQL, no servers? | Athena |
| Best file format for analytics cost? | Parquet (columnar) |
| Stream data to S3 with buffering, fully managed? | Kinesis Data Firehose |
| Central metadata catalog? | AWS Glue Data Catalog |
| Fine-grained lake permissions? | Lake Formation |
| Petabyte-scale warehouse? | Redshift |
| Reduce Athena scan cost? | Partition + compress + columnar |

→ More in `05-flashcards/aws-flashcards.md`.

## 17. Official docs / resources
- [ ] DEA-C01 exam guide: _add link_
- [ ] AWS Glue + Lake Formation docs: _add link_
- [ ] Redshift best practices: _add link_
- [ ] Official practice exam: _add link_
