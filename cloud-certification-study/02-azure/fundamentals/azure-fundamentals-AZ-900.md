# Microsoft Certified: Azure Fundamentals

> 🍼 **Beginner explanation:** The Azure "driver's license." Proves you understand cloud concepts and core Azure services, pricing, and governance — no technical depth required. Best Azure starting point.
>
> 🌍 **Real-world example:** Your company evaluates Azure. This cert lets you understand resource groups, regions, what Blob Storage and VMs are, and how billing/governance work.

| Field | Value |
|---|---|
| **1. Certification name** | Microsoft Certified: Azure Fundamentals |
| **2. Exam code** | AZ-900 |
| **3. Level** | Fundamentals |
| **4. Best for role** | Beginners, business users, anyone starting Azure |
| **5. Prerequisites** | None |

---

## 6. Core topics
- Cloud concepts (IaaS/PaaS/SaaS, public/private/hybrid, benefits)
- Azure architecture (Regions, Availability Zones, resource groups, subscriptions, management groups)
- Core services (compute, storage, networking, databases)
- Management & governance (RBAC, Policy, Locks, Cost Management, tags)
- Pricing (TCO calculator, pricing calculator, support plans)

## 7. Azure services to learn
| Category | Services |
|---|---|
| Compute | Virtual Machines, App Service, Functions, Container Instances |
| Storage | Blob Storage, Files, Disks |
| Networking | Virtual Network, Load Balancer, VPN Gateway |
| Database | Azure SQL, Cosmos DB (overview) |
| Identity/Mgmt | Microsoft Entra ID, Azure Monitor, Cost Management, Policy |

## 8. Hands-on labs
> Every lab ends with **Cleanup → delete the resource group**. Log in `04-trackers/lab-completion-tracker.md`.

1. **Azure portal tour** + create a **resource group**. *(Cleanup: delete RG.)*
2. **Storage account + Blob container**; upload a file. *(Cleanup: delete RG.)*
3. **Create a VM** (B-series) and view it. *(Cleanup: delete RG — stops all charges.)*
4. **Pricing & TCO calculator** estimate. *(No cost.)*
5. **Apply a tag + an Azure Policy** (e.g., allowed locations). *(Cleanup: remove policy assignment.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–2 | Cloud concepts (IaaS/PaaS/SaaS); Lab 1 |
| 3–4 | Azure architecture + hierarchy |
| 5–6 | Core compute + storage; Labs 2–3 |
| 7 | Networking + databases overview |
| 8 | Identity (Entra ID) + RBAC |
| 9 | Governance (Policy/Locks/tags); Lab 5 |
| 10 | Pricing + support; Lab 4 |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 85%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Cloud concepts + architecture (Lab 1) |
| 2 | Core services (Labs 2–3) |
| 3 | Identity + governance + pricing (Labs 4–5) |
| 4 | 2–3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | Cloud concepts |
| 3–4 | Azure architecture + hierarchy (Lab 1) |
| 5 | Compute + storage (Labs 2–3) |
| 6 | Networking + identity |
| 7 | Governance + pricing (Labs 4–5) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **85%+**. Mostly conceptual; ~40–60 questions / 45–60 min.
- Watch IaaS vs PaaS vs SaaS responsibility questions.
- 3 timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] IaaS vs PaaS vs SaaS (who manages what)
- [ ] Management group → subscription → RG → resource hierarchy
- [ ] Regions vs Availability Zones
- [ ] RBAC vs Azure Policy vs Locks (different jobs)
- [ ] CapEx vs OpEx, TCO calculator
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
| Object storage in Azure? | Blob Storage |
| AWS S3 equivalent? | Blob Storage |
| Group resources for lifecycle/billing? | Resource Group |
| Enforce org rules on resources? | Azure Policy |
| Grant permissions to users? | RBAC (Entra ID) |
| Prevent accidental deletion? | Resource Lock |
| PaaS web hosting? | App Service |

→ More in `05-flashcards/azure-flashcards.md`.

## 17. Official docs / resources
- [ ] AZ-900 exam page (Microsoft Learn): _add link_
- [ ] Microsoft Learn AZ-900 free path: _add link_
- [ ] Azure pricing + TCO calculator: _add link_
- [ ] Practice assessment: _add link_
