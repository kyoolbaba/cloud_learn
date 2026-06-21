# Microsoft Certified: Windows Server Hybrid Administrator Associate

> 🍼 **Beginner explanation:** For admins running Windows Server in hybrid setups — on-prem servers connected to Azure (via Azure Arc), with hybrid identity, migration, monitoring, and DR. Niche for a data scientist.
>
> 🌍 **Real-world example:** A company keeps Windows Servers on-prem but wants Azure management, hybrid Active Directory, and cloud backup/DR. This cert covers that bridge.

> ⚠️ **Exam-change flag:** Historically **AZ-800 + AZ-801**. Moving toward **AZ-802** after exam changes — confirm the current code/structure before booking.

| Field | Value |
|---|---|
| **1. Certification name** | Microsoft Certified: Windows Server Hybrid Administrator Associate |
| **2. Exam code** | AZ-800 + AZ-801 → AZ-802 (verify current) |
| **3. Level** | Associate |
| **4. Best for role** | Windows Server admins in Azure hybrid environments |
| **5. Prerequisites** | Windows Server admin experience; AZ-104 helpful |

---

## 6. Core topics
- Windows Server administration (AD DS, DNS, DHCP, file services)
- Hybrid identity (Entra Connect, hybrid AD)
- Azure Arc for servers, hybrid management
- Migration (Storage Migration Service, AD migration)
- Monitoring, troubleshooting, high availability & disaster recovery

## 7. Azure/Windows services to learn
| Category | Services |
|---|---|
| Identity | Active Directory DS, Microsoft Entra Connect |
| Hybrid mgmt | Azure Arc, Windows Admin Center, Azure Monitor |
| Storage/Files | File Services, Storage Migration Service, Azure File Sync |
| Resilience | Failover Clustering, Azure Site Recovery, Backup |

## 8. Hands-on labs (mostly concept + diagram)
1. **Azure Arc notes** — onboard a server (concept/lab). *(Cleanup: remove Arc resource/RG.)*
2. **Windows Server migration plan** (Storage Migration Service). *(Design.)*
3. **Hybrid architecture diagram** (on-prem AD + Entra Connect). *(Design.)*
4. **Azure File Sync** concept. *(Cleanup: delete RG if built.)*

## 9. Two-week plan (refresher)
| Day | Focus |
|---|---|
| 1–3 | Windows Server core (AD/DNS/DHCP) |
| 4–5 | Hybrid identity (Entra Connect); Lab 3 |
| 6–7 | Azure Arc + hybrid mgmt; Lab 1 |
| 8–9 | Migration; Lab 2 |
| 10 | HA/DR + monitoring; Lab 4 |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 80%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Windows Server core |
| 2 | Hybrid identity + Arc (Labs 1, 3) |
| 3 | Migration + HA/DR (Labs 2, 4) |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | Windows Server core (AD/DNS/DHCP) |
| 3 | File services + storage |
| 4 | Hybrid identity (Lab 3) |
| 5 | Azure Arc (Lab 1) |
| 6 | Migration (Lab 2) |
| 7 | HA/DR + monitoring (Lab 4) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **80%+**. Confirm whether you're sitting AZ-800/801 or AZ-802 and use matching mocks.
- 4 timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] AD DS roles + DNS/DHCP basics
- [ ] Entra Connect sync (hybrid identity)
- [ ] Azure Arc capabilities for servers
- [ ] Storage Migration Service + Azure File Sync
- [ ] Failover clustering + Site Recovery
- [ ] Flashcards reviewed twice

## 14. Notes template
```
### Topic: <name>
- Concept:
- Real-world use:
- Service(s):
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
| Manage on-prem servers from Azure? | Azure Arc |
| Sync on-prem AD to Entra ID? | Entra Connect |
| Tier file shares to cloud? | Azure File Sync |
| DR/replication for servers? | Azure Site Recovery |
| AWS equivalent of Arc (hybrid mgmt)? | Systems Manager (partly) |

→ More in `05-flashcards/azure-flashcards.md`.

## 17. Official docs / resources
- [ ] AZ-800/801/AZ-802 exam page (verify): _add link_
- [ ] Microsoft Learn Windows Server hybrid path: _add link_
- [ ] Azure Arc docs: _add link_
- [ ] Practice assessment: _add link_
