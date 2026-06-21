# Microsoft Certified: Azure Security Engineer Associate

> 🍼 **Beginner explanation:** Teaches securing Azure — identity protection, platform/network security, data/app security, and security operations. A strong security capstone alongside your data work.
>
> 🌍 **Real-world example:** Harden a data platform: enforce MFA + Conditional Access, protect VMs/networks with NSGs + Defender, store secrets in Key Vault, and monitor threats with Sentinel.

| Field | Value |
|---|---|
| **1. Certification name** | Microsoft Certified: Azure Security Engineer Associate |
| **2. Exam code** | AZ-500 |
| **3. Level** | Associate |
| **4. Best for role** | Security engineers |
| **5. Prerequisites** | AZ-104 / security fundamentals recommended |

---

## 6. Core topics
- Identity & access security (Entra ID, Conditional Access, PIM, MFA)
- Platform protection (network security, firewalls, NSGs, Bastion)
- Security operations (Defender for Cloud, Sentinel, monitoring)
- Data & application security (Key Vault, encryption, app security)

## 7. Azure services to learn
| Category | Services |
|---|---|
| Identity | Microsoft Entra ID, Conditional Access, PIM, Identity Protection |
| Network | NSG, Azure Firewall, Bastion, DDoS Protection, Private Link |
| Sec Ops | Microsoft Defender for Cloud, Microsoft Sentinel |
| Data/App | Key Vault, encryption, Application security |

## 8. Hands-on labs
1. **RBAC + PIM** eligible role assignment. *(Cleanup: remove assignment.)*
2. **Key Vault** store + access a secret via managed identity. *(Cleanup: delete RG.)*
3. **Defender for Cloud** review secure score + recommendation. *(Cleanup: none.)*
4. **NSG + Azure Firewall** rule (concept/build). *(Cleanup: delete RG.)*
5. **Sentinel** concept — connect a data source. *(Cleanup: delete workspace.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–3 | Identity security (Entra/CA/PIM/MFA); Lab 1 |
| 4–6 | Platform/network protection; Lab 4 |
| 7–8 | Defender for Cloud; Lab 3 |
| 9 | Sentinel; Lab 5 |
| 10 | Data/app security + Key Vault; Lab 2 |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 80%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Identity security (Lab 1) |
| 2 | Platform/network protection (Lab 4) |
| 3 | Sec ops + data security (Labs 2–3, 5) |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | Identity security (Lab 1) |
| 3 | Network protection (Lab 4) |
| 4 | Firewalls + Bastion + Private Link |
| 5 | Defender for Cloud (Lab 3) |
| 6 | Sentinel (Lab 5) |
| 7 | Key Vault + data/app security (Lab 2) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **80%+**. Scenario + config detail (CA policies, NSG rules, Key Vault access).
- 4 timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] Conditional Access components + PIM
- [ ] NSG vs Azure Firewall vs App Gateway WAF
- [ ] Defender for Cloud vs Sentinel roles
- [ ] Key Vault access models (RBAC vs access policy)
- [ ] Encryption at rest/in transit options
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
| Just-in-time admin access? | PIM |
| AWS equivalent of Key Vault? | KMS / Secrets Manager |
| Cloud security posture + recommendations? | Defender for Cloud |
| SIEM/SOAR in Azure? | Microsoft Sentinel |
| Block risky sign-in scenarios? | Conditional Access |
| Secure RDP/SSH without public IP? | Azure Bastion |

→ More in `05-flashcards/azure-flashcards.md`.

## 17. Official docs / resources
- [ ] AZ-500 exam page: _add link_
- [ ] Microsoft Learn AZ-500 path: _add link_
- [ ] Defender + Sentinel docs: _add link_
- [ ] Practice assessment: _add link_
