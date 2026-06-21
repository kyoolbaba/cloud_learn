# Microsoft Certified: Azure for SAP Workloads Specialty

> 🍼 **Beginner explanation:** Very specialized — running SAP (enterprise ERP software) on Azure: migration, SAP HANA databases, high availability/DR, monitoring, storage, and networking. Only relevant if you work with SAP.
>
> 🌍 **Real-world example:** Migrate a company's SAP S/4HANA from on-prem to Azure with HA/DR and proper sizing.

| Field | Value |
|---|---|
| **1. Certification name** | Microsoft Certified: Azure for SAP Workloads Specialty |
| **2. Exam code** | AZ-120 |
| **3. Level** | Specialty |
| **4. Best for role** | SAP architects/engineers |
| **5. Prerequisites** | SAP Basis/admin background + AZ-104/305 helpful |

---

## 6. Core topics
- SAP on Azure architecture & sizing
- Migration to Azure (greenfield/lift-and-shift)
- SAP HANA on Azure (certified VMs / large instances)
- HA/DR for SAP, storage & networking design
- Monitoring & operations

## 7. Azure services to learn
| Category | Services |
|---|---|
| Compute | Azure VMs (SAP-certified), HANA Large Instances |
| Storage | Premium/Ultra Disks, Azure NetApp Files |
| Networking | VNets, ExpressRoute, load balancers |
| Resilience | Availability zones/sets, Site Recovery, backup |
| Ops | Azure Monitor for SAP solutions |

## 8. Hands-on labs (design-focused)
1. **SAP on Azure architecture** diagram. *(Design.)*
2. **HA/DR plan** for SAP (zones + replication). *(Design.)*
3. **Migration checklist** (assessment → cutover). *(Design.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–3 | SAP on Azure architecture + sizing; Lab 1 |
| 4–5 | SAP HANA on Azure |
| 6–7 | HA/DR; Lab 2 |
| 8–9 | Storage + networking |
| 10 | Migration; Lab 3 |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 75%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Architecture + sizing (Lab 1) |
| 2 | HANA + HA/DR (Lab 2) |
| 3 | Storage + networking + migration (Lab 3) |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | SAP on Azure architecture (Lab 1) |
| 3 | SAP HANA specifics |
| 4 | HA/DR (Lab 2) |
| 5 | Storage design |
| 6 | Networking (ExpressRoute) |
| 7 | Migration (Lab 3) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **75%+**. Sizing + HA/DR + migration scenarios.
- 3 timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] SAP-certified VM SKUs + sizing approach
- [ ] HANA storage (Ultra Disk / ANF) requirements
- [ ] HA (zones, clustering) vs DR (Site Recovery)
- [ ] ExpressRoute for SAP connectivity
- [ ] Migration phases
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
| High-perf storage for HANA? | Ultra Disk / Azure NetApp Files |
| Private dedicated connectivity? | ExpressRoute |
| DR for SAP VMs? | Azure Site Recovery |
| AWS equivalent program? | SAP on AWS |

→ More in `05-flashcards/azure-flashcards.md`.

## 17. Official docs / resources
- [ ] AZ-120 exam page: _add link_
- [ ] SAP on Azure docs: _add link_
- [ ] Azure Monitor for SAP: _add link_
- [ ] Practice assessment: _add link_
