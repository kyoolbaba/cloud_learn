# Microsoft Certified: Azure Virtual Desktop Specialty

> 🍼 **Beginner explanation:** For delivering Windows desktops/apps from Azure (Azure Virtual Desktop) — host pools, session hosts, user profiles (FSLogix), security, and monitoring. Niche for a data scientist.
>
> 🌍 **Real-world example:** A company gives 500 remote workers a secure cloud Windows desktop. This cert covers designing and operating that.

| Field | Value |
|---|---|
| **1. Certification name** | Microsoft Certified: Azure Virtual Desktop Specialty |
| **2. Exam code** | AZ-140 |
| **3. Level** | Specialty |
| **4. Best for role** | Desktop/server admins |
| **5. Prerequisites** | AZ-104 + Windows/VDI background |

---

## 6. Core topics
- AVD architecture (host pools, workspaces, app groups, session hosts)
- User profiles (FSLogix), images & golden images
- Security & access (Conditional Access, RBAC)
- Networking, scaling, monitoring & maintenance

## 7. Azure services to learn
| Category | Services |
|---|---|
| AVD | Host pools, session hosts, app groups, workspaces |
| Profiles | FSLogix, Azure Files / NetApp Files |
| Identity/Security | Entra ID, Conditional Access, RBAC |
| Ops | Azure Monitor, autoscale, image management |

## 8. Hands-on labs (design + concept)
1. **AVD architecture design** (pooled vs personal). *(Design.)*
2. **Host pool notes** + session host sizing. *(Cleanup: delete RG if built.)*
3. **FSLogix checklist** for profile containers. *(Design.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–3 | AVD architecture; Lab 1 |
| 4–5 | Session hosts + images; Lab 2 |
| 6–7 | FSLogix profiles; Lab 3 |
| 8 | Security + access |
| 9 | Networking + scaling + monitoring |
| 10 | Flashcards |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 75%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Architecture + host pools (Labs 1–2) |
| 2 | FSLogix + images (Lab 3) |
| 3 | Security + networking + monitoring |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | AVD architecture (Lab 1) |
| 3 | Session hosts + sizing (Lab 2) |
| 4 | Images / golden image |
| 5 | FSLogix (Lab 3) |
| 6 | Security + access |
| 7 | Networking + scaling + monitoring |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **75%+**. Config + design detail (host pool types, FSLogix, scaling).
- 3 timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] Pooled vs personal host pools
- [ ] FSLogix profile containers + storage choice
- [ ] Autoscale + scaling plans
- [ ] Conditional Access for AVD
- [ ] Image management
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
| Roaming Windows profiles in AVD? | FSLogix |
| Shared desktop for many users? | Pooled host pool |
| AWS equivalent of AVD? | Amazon WorkSpaces |
| Scale session hosts by schedule/demand? | Scaling plans / autoscale |

→ More in `05-flashcards/azure-flashcards.md`.

## 17. Official docs / resources
- [ ] AZ-140 exam page: _add link_
- [ ] Azure Virtual Desktop docs: _add link_
- [ ] FSLogix docs: _add link_
- [ ] Practice assessment: _add link_
