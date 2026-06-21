# AWS Certified Solutions Architect – Professional

> 🍼 **Beginner explanation:** The advanced architecture cert. You design *complex, enterprise* systems — many AWS accounts, hybrid (on-prem + cloud) networks, migrations, and disaster recovery. Do this after SAA-C03 + real experience.
>
> 🌍 **Real-world example:** A bank with 50 AWS accounts wants centralized security, a hybrid network to its data center, and a migration plan for 200 apps. This cert is that level.

| Field | Value |
|---|---|
| **1. Certification name** | AWS Certified Solutions Architect – Professional |
| **2. Exam code** | SAP-C02 |
| **3. Level** | Professional |
| **4. Best for role** | Experienced architects designing complex enterprise systems |
| **5. Prerequisites** | SAA-C03 + ~2 years hands-on AWS strongly recommended |

---

## 6. Core topics
- Multi-account strategy (Organizations, Control Tower, SCPs)
- Hybrid & advanced networking (Direct Connect, Transit Gateway, VPN)
- Migration strategies (7 Rs, MGN, DMS, Snow family)
- Cost optimization at scale, resilience & DR strategies
- Security & governance across accounts
- Continuous improvement of existing architectures

## 7. AWS services to learn
| Category | Services |
|---|---|
| Governance | Organizations, Control Tower, SCPs, IAM Identity Center |
| Networking | Transit Gateway, Direct Connect, VPC peering, PrivateLink, Route 53 |
| Migration | Application Migration Service (MGN), DMS, DataSync, Snow family |
| Resilience/DR | Route 53 failover, multi-Region, AWS Backup, pilot light/warm standby |
| Cost | Cost Explorer, Savings Plans, Compute Optimizer |

## 8. Hands-on labs (mostly design + diagrams)
1. **Multi-account architecture** diagram with Organizations + SCPs. *(No cost — design.)*
2. **Advanced VPC + Transit Gateway** connectivity design. *(If built: delete TGW attachments — billed hourly.)*
3. **Disaster recovery plan** (pilot light vs warm standby vs multi-site). *(Design.)*
4. **Migration plan** mapping 7 Rs to sample workloads. *(Design.)*

## 9. Two-week plan (refresher only — not for first-timers)
| Day | Focus |
|---|---|
| 1–2 | Multi-account + Organizations + SCPs |
| 3–4 | Advanced networking (TGW/DX/PrivateLink) |
| 5–6 | Migrations (7 Rs, MGN, DMS) |
| 7–8 | DR strategies + resilience |
| 9 | Cost optimization at scale |
| 10 | Security/governance |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 75%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Governance + multi-account (Lab 1) |
| 2 | Advanced networking + migration (Labs 2, 4) |
| 3 | DR + resilience + cost (Lab 3) |
| 4 | 3 long mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | Multi-account governance (Lab 1) |
| 3–4 | Advanced/hybrid networking (Lab 2) |
| 5 | Migration strategies (Lab 4) |
| 6 | DR + resilience (Lab 3) |
| 7 | Cost + security + continuous improvement |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Long, complex scenario questions; ~75 Q / 180 min. Target **75%+** (hard exam).
- Practice elimination on multi-correct, lengthy answers; manage time (~2 min/question).
- Focus on "best" not just "correct" — cost + ops overhead + resilience trade-offs.

## 13. Final revision checklist (last 3 days)
- [ ] Organizations + SCP inheritance/precedence
- [ ] Transit Gateway vs peering vs PrivateLink
- [ ] Direct Connect vs VPN vs DX + VPN
- [ ] 7 Rs migration strategies + tooling
- [ ] DR patterns + RTO/RPO trade-offs
- [ ] Cross-account access patterns (roles, RAM)
- [ ] Flashcards reviewed twice

## 14. Notes template
```
### Topic: <name>
- Concept:
- Real-world use:
- AWS service(s):
- Azure equivalent:
- Common exam trap:
- Trade-off notes:
```

## 15. Mistake log template
| Date | Topic | What I got wrong | Correct concept | Revisit date |
|---|---|---|---|---|

## 16. Flashcards (starter set)
| Q | A |
|---|---|
| Connect 100s of VPCs at scale? | Transit Gateway |
| Dedicated private link to on-prem? | Direct Connect |
| Enforce guardrails across accounts? | SCPs (Organizations) |
| Lowest RTO/RPO DR? | Multi-site active/active |
| Cheapest DR with minimal running infra? | Pilot light |
| Migrate databases with minimal downtime? | DMS |

→ More in `05-flashcards/aws-flashcards.md`.

## 17. Official docs / resources
- [ ] SAP-C02 exam guide: _add link_
- [ ] AWS Organizations + Control Tower docs: _add link_
- [ ] AWS DR whitepaper: _add link_
- [ ] Official practice exam: _add link_
