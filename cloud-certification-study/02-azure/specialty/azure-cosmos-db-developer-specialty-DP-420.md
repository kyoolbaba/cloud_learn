# Microsoft Certified: Azure Cosmos DB Developer Specialty

> 🍼 **Beginner explanation:** Deep cert on Cosmos DB — Azure's globally distributed NoSQL database. You learn data modeling, partitioning, indexing, queries, and performance tuning. Genuinely useful for data engineers/scientists.
>
> 🌍 **Real-world example:** Build a high-scale app storing millions of events with a smart partition key so reads/writes stay fast and cheap worldwide.

| Field | Value |
|---|---|
| **1. Certification name** | Microsoft Certified: Azure Cosmos DB Developer Specialty |
| **2. Exam code** | DP-420 |
| **3. Level** | Specialty |
| **4. Best for role** | Developers & data engineers using Cosmos DB |
| **5. Prerequisites** | Programming + database basics; DP-900 helpful |

---

## 6. Core topics
- Data modeling for NoSQL (embedding vs referencing)
- Partitioning (partition keys, logical/physical partitions)
- Indexing policies & query optimization
- Throughput (RU/s), autoscale, consistency levels
- Integration (change feed, Functions, analytics), security, monitoring

## 7. Azure services to learn
| Category | Services |
|---|---|
| Core | Azure Cosmos DB (NoSQL API), change feed |
| Integration | Azure Functions, Synapse Link, Event Hubs |
| Security/Ops | Entra ID/RBAC, Key Vault, Azure Monitor |

## 8. Hands-on labs
1. **Cosmos DB data model** — embed vs reference design. *(Cleanup: delete RG.)*
2. **Partition strategy** — choose + test a partition key. *(Cleanup: delete RG.)*
3. **Query optimization** — review RU charge per query. *(Cleanup: delete RG.)*
4. **Indexing checklist** — custom indexing policy. *(Cleanup: delete RG.)*
5. **Change feed** → Azure Function trigger. *(Cleanup: delete RG.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–2 | Cosmos basics + APIs + RU/s |
| 3–4 | Data modeling; Lab 1 |
| 5–6 | Partitioning; Lab 2 |
| 7–8 | Indexing + queries; Labs 3–4 |
| 9 | Change feed + integration; Lab 5 |
| 10 | Consistency + security + monitoring |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 75%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Modeling + partitioning (Labs 1–2) |
| 2 | Indexing + queries (Labs 3–4) |
| 3 | Change feed + consistency + security (Lab 5) |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1 | Cosmos fundamentals + RU/s |
| 2 | Data modeling (Lab 1) |
| 3 | Partitioning (Lab 2) |
| 4 | Indexing (Lab 4) |
| 5 | Query optimization (Lab 3) |
| 6 | Change feed + integration (Lab 5) |
| 7 | Consistency + security + monitoring |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **75%+**. Code + design detail: partition keys, RU costs, consistency trade-offs.
- 3+ timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] Embedding vs referencing
- [ ] Partition key selection + hot partition avoidance
- [ ] 5 consistency levels + trade-offs
- [ ] RU/s, autoscale, query RU cost
- [ ] Indexing policies + change feed uses
- [ ] Flashcards reviewed twice

## 14. Notes template
```
### Topic: <name>
- Concept:
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
| Throughput unit in Cosmos? | Request Unit (RU/s) |
| AWS equivalent of Cosmos DB? | DynamoDB |
| Avoid hot partitions by? | High-cardinality, even-access partition key |
| Strongest consistency? | Strong (highest cost/latency) |
| React to data changes? | Change feed |
| Run analytics without hurting OLTP? | Synapse Link (analytical store) |

→ More in `05-flashcards/azure-flashcards.md`.

## 17. Official docs / resources
- [ ] DP-420 exam page: _add link_
- [ ] Cosmos DB developer docs: _add link_
- [ ] Partitioning + indexing guides: _add link_
- [ ] Practice assessment: _add link_
