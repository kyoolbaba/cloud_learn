# Microsoft Certified: Azure Data Fundamentals

> 🍼 **Beginner explanation:** Covers data concepts on Azure — relational vs non-relational data, and analytics workloads. Core foundation for any data scientist/analyst on Azure.
>
> 🌍 **Real-world example:** Understand whether customer data belongs in Azure SQL (relational) or Cosmos DB (NoSQL), and how analytics flows through a data lake into Synapse/Fabric for dashboards.

| Field | Value |
|---|---|
| **1. Certification name** | Microsoft Certified: Azure Data Fundamentals |
| **2. Exam code** | DP-900 |
| **3. Level** | Fundamentals |
| **4. Best for role** | Data analysts, data engineers, data scientists |
| **5. Prerequisites** | None; basic data familiarity helps |

---

## 6. Core topics
- Core data concepts (relational vs non-relational, transactional vs analytical)
- Relational data on Azure (Azure SQL family)
- Non-relational data on Azure (Cosmos DB, tables, blobs)
- Analytics workloads (data lake, Synapse, Microsoft Fabric, Power BI)
- Data roles, ingestion, and visualization basics

## 7. Azure services to learn
| Category | Services |
|---|---|
| Relational | Azure SQL Database, SQL Managed Instance, Azure DB for PostgreSQL/MySQL |
| Non-relational | Cosmos DB, Table Storage, Blob Storage |
| Analytics | Azure Synapse Analytics, Microsoft Fabric, Data Lake Storage, Data Factory |
| Visualization | Power BI |

## 8. Hands-on labs
1. **Azure SQL Database** basics — create + run a query. *(Cleanup: delete RG.)*
2. **Cosmos DB** overview — create a container, add an item. *(Cleanup: delete RG.)*
3. **Data Lake / Blob** overview — upload sample data. *(Cleanup: delete RG.)*
4. **Analytics concept** — explore Synapse/Fabric + a Power BI sample. *(Cleanup: delete RG/workspace.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–2 | Core data concepts |
| 3–4 | Relational data + Azure SQL; Lab 1 |
| 5–6 | Non-relational + Cosmos DB; Lab 2 |
| 7 | Data lake + storage; Lab 3 |
| 8–9 | Analytics (Synapse/Fabric) + Power BI; Lab 4 |
| 10 | Data roles + flashcards |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 85%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Data concepts + relational (Lab 1) |
| 2 | Non-relational + storage (Labs 2–3) |
| 3 | Analytics + Power BI (Lab 4) |
| 4 | Mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | Core data concepts |
| 3 | Relational + Azure SQL (Lab 1) |
| 4 | Non-relational + Cosmos DB (Lab 2) |
| 5 | Data lake + storage (Lab 3) |
| 6 | Analytics (Synapse/Fabric) (Lab 4) |
| 7 | Power BI + data roles |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **85%+**. Conceptual; match data type/workload to service.
- Know OLTP vs OLAP, structured vs semi/unstructured.
- 3 timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] Relational vs non-relational vs analytical
- [ ] OLTP vs OLAP
- [ ] Azure SQL family differences (DB vs MI)
- [ ] Cosmos DB APIs (overview)
- [ ] Synapse vs Fabric vs Power BI roles
- [ ] Flashcards reviewed twice

## 14. Notes template
```
### Topic: <name>
- Beginner explanation:
- Real-world use:
- Azure service(s):
- AWS equivalent:
- Common exam trap:
- My example:
```

## 15. Mistake log template
| Date | Topic | What I got wrong | Correct concept | Revisit date |
|---|---|---|---|---|

## 16. Flashcards (starter set)
| Q | A |
|---|---|
| Managed relational DB? | Azure SQL Database |
| Globally distributed NoSQL? | Cosmos DB |
| AWS equivalent of Cosmos DB? | DynamoDB |
| Big-data analytics platform? | Synapse / Microsoft Fabric |
| Business dashboards? | Power BI |
| Cheap object/data lake storage? | Data Lake Storage (Blob) |
| OLTP vs OLAP? | OLTP = transactions; OLAP = analytics |

→ More in `05-flashcards/azure-flashcards.md`.

## 17. Official docs / resources
- [ ] DP-900 exam page: _add link_
- [ ] Microsoft Learn DP-900 path: _add link_
- [ ] Microsoft Fabric / Synapse docs: _add link_
- [ ] Practice assessment: _add link_
