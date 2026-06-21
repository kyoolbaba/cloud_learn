# Microsoft Certified: Azure Administrator Associate

> 🍼 **Beginner explanation:** Hands-on cert for running Azure day to day — identities, storage, VMs, networking, and monitoring. The core "Azure operator" cert.
>
> 🌍 **Real-world example:** Manage a company's Azure: create users/groups, set up VNets, deploy VMs, configure storage, set RBAC, and monitor + back up resources.

| Field | Value |
|---|---|
| **1. Certification name** | Microsoft Certified: Azure Administrator Associate |
| **2. Exam code** | AZ-104 |
| **3. Level** | Associate |
| **4. Best for role** | Azure admins, cloud engineers |
| **5. Prerequisites** | AZ-900 helpful; 6 months Azure admin experience recommended |

---

## 6. Core topics
- Identities & governance (Entra ID, RBAC, subscriptions, Policy)
- Storage (accounts, blob, files, security, lifecycle)
- Compute (VMs, scale sets, App Service, containers)
- Networking (VNets, NSGs, load balancing, DNS, peering)
- Monitoring & backup (Azure Monitor, Backup, Site Recovery)

## 7. Azure services to learn
| Category | Services |
|---|---|
| Identity/Governance | Microsoft Entra ID, RBAC, Azure Policy, Management Groups |
| Storage | Storage Accounts, Blob, Files, Azure Backup |
| Compute | Virtual Machines, VM Scale Sets, App Service |
| Networking | Virtual Network, NSG, Load Balancer, App Gateway, DNS, VNet Peering |
| Monitoring | Azure Monitor, Log Analytics, Alerts |

## 8. Hands-on labs
1. **VNet + subnets + NSG**. *(Cleanup: delete RG.)*
2. **Storage account** + blob + lifecycle rule. *(Cleanup: delete RG.)*
3. **Deploy a VM** + connect; resize. *(Cleanup: delete RG.)*
4. **RBAC** assignment at RG scope. *(Cleanup: remove assignment.)*
5. **Azure Monitor alert** + **Backup** for the VM. *(Cleanup: delete RG + Recovery Services vault.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–2 | Identity + RBAC + governance; Lab 4 |
| 3–4 | Storage; Lab 2 |
| 5–7 | Compute (VMs, scale sets); Lab 3 |
| 8–10 | Networking; Lab 1 |
| 11 | Monitoring + backup; Lab 5 |
| 12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 80%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Identity + governance + storage (Labs 2, 4) |
| 2 | Compute (Lab 3) |
| 3 | Networking + monitoring/backup (Labs 1, 5) |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1 | Identity + Entra ID |
| 2 | Governance + RBAC + Policy (Lab 4) |
| 3 | Storage (Lab 2) |
| 4–5 | Compute (Lab 3) |
| 6 | Networking (Lab 1) |
| 7 | Monitoring + backup (Lab 5) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **80%+**. May include **case studies + hands-on lab** style tasks — practice the portal.
- 4 timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] RBAC roles + scope inheritance
- [ ] Storage redundancy (LRS/ZRS/GRS/GZRS)
- [ ] NSG rules + priorities + effective rules
- [ ] VNet peering vs VPN/Gateway
- [ ] Backup vs Site Recovery
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
| Geo-redundant storage code? | GRS |
| Control inbound/outbound at subnet/NIC? | NSG |
| AWS equivalent of NSG? | Security Group / NACL |
| Backup VMs/files? | Azure Backup (Recovery Services vault) |
| DR/replication for VMs? | Azure Site Recovery |
| Layer-7 load balancing? | Application Gateway |

→ More in `05-flashcards/azure-flashcards.md`.

## 17. Official docs / resources
- [ ] AZ-104 exam page: _add link_
- [ ] Microsoft Learn AZ-104 path: _add link_
- [ ] Azure networking + storage docs: _add link_
- [ ] Practice assessment: _add link_
