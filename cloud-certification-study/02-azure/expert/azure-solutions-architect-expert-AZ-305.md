# Microsoft Certified: Azure Solutions Architect Expert

> 🍼 **Beginner explanation:** The advanced Azure design cert. You architect complete solutions — identity/governance, data storage, business continuity, and infrastructure — balancing cost, security, and resilience. Azure's equivalent of AWS SAP.
>
> 🌍 **Real-world example:** Design a secure landing zone for an enterprise: governance hierarchy, hybrid identity, HA/DR strategy, data platform, and a migration plan.

| Field | Value |
|---|---|
| **1. Certification name** | Microsoft Certified: Azure Solutions Architect Expert |
| **2. Exam code** | AZ-305 |
| **3. Level** | Expert |
| **4. Best for role** | Experienced cloud architects |
| **5. Prerequisites** | AZ-104 knowledge + real Azure experience strongly recommended |

---

## 6. Core topics
- Design identity, governance & monitoring solutions
- Design data storage solutions (relational + non-relational)
- Design business continuity solutions (backup, HA, DR)
- Design infrastructure solutions (compute, networking, app architecture, migration)

## 7. Azure services to learn
| Category | Services |
|---|---|
| Governance | Management Groups, Policy, RBAC, Entra ID, Blueprints/landing zones |
| Data | Azure SQL, Cosmos DB, Storage, Synapse/Fabric, Data Lake |
| Continuity | Backup, Site Recovery, availability zones/sets, geo-replication |
| Infra | VMs, AKS, App Service, VNets, Front Door, App Gateway |

## 8. Hands-on labs (design-focused)
1. **Architecture Decision Records** for a sample workload. *(Design.)*
2. **HA/DR design** (RTO/RPO targets → services). *(Design.)*
3. **Secure landing zone design** (management groups + policy + identity). *(Design.)*
4. **Migration strategy** (rehost/refactor/rearchitect mapping). *(Design.)*

## 9. Two-week plan (refresher)
| Day | Focus |
|---|---|
| 1–3 | Identity/governance/monitoring; Lab 3 |
| 4–6 | Data storage design; |
| 7–8 | Business continuity; Lab 2 |
| 9–10 | Infrastructure + migration; Labs 1, 4 |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 75%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Identity + governance (Lab 3) |
| 2 | Data storage design |
| 3 | Continuity + infra + migration (Labs 1–2, 4) |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | Identity/governance/monitoring (Lab 3) |
| 3–4 | Data storage solutions |
| 5 | Business continuity (Lab 2) |
| 6 | Infrastructure design (Lab 1) |
| 7 | Migration (Lab 4) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **75%+**. Case-study heavy — pick the *best-fit* service given constraints.
- Practice mapping requirements (cost/RTO/compliance) → services.
- 3+ timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] Governance hierarchy + landing zones
- [ ] Choosing data store (SQL vs Cosmos vs Storage) by requirement
- [ ] HA vs DR vs backup; RTO/RPO mapping
- [ ] Compute choice (VM vs AKS vs App Service vs Functions)
- [ ] Migration strategies (the "Rs")
- [ ] Flashcards reviewed twice

## 14. Notes template
```
### Topic: <name>
- Concept:
- Real-world use:
- Azure service(s):
- AWS equivalent:
- Common exam trap:
- Trade-off notes:
```

## 15. Mistake log template
| Date | Topic | What I got wrong | Correct concept | Revisit date |
|---|---|---|---|---|

## 16. Flashcards (starter set)
| Q | A |
|---|---|
| Enforce org-wide standards? | Azure Policy + Management Groups |
| Lowest RTO multi-region data? | Geo-replication / active-active |
| Choose for global low-latency NoSQL? | Cosmos DB |
| Best for containerized microservices? | AKS |
| AWS equivalent of this cert? | Solutions Architect – Professional |

→ More in `05-flashcards/azure-flashcards.md`.

## 17. Official docs / resources
- [ ] AZ-305 exam page: _add link_
- [ ] Azure Architecture Center + Well-Architected: _add link_
- [ ] Cloud Adoption Framework / landing zones: _add link_
- [ ] Practice assessment: _add link_
