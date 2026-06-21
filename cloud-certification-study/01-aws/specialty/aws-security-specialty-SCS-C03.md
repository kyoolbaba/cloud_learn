# AWS Certified Security – Specialty

> 🍼 **Beginner explanation:** Deep security cert — identity, encryption, logging, threat detection, incident response, and data protection on AWS. Great capstone for a data scientist who handles sensitive data.
>
> 🌍 **Real-world example:** Lock down a data platform: least-privilege IAM, encrypt everything with KMS, detect threats with GuardDuty, investigate with CloudTrail, and respond to incidents automatically.

| Field | Value |
|---|---|
| **1. Certification name** | AWS Certified Security – Specialty |
| **2. Exam code** | SCS-C03 |
| **3. Level** | Specialty |
| **4. Best for role** | Security engineers, cloud admins, architects |
| **5. Prerequisites** | SAA + security fundamentals recommended |

---

## 6. Core topics
- Identity & access (IAM policies, roles, federation, permission boundaries)
- Data protection & encryption (KMS, envelope encryption, S3 encryption)
- Logging & monitoring (CloudTrail, Config, CloudWatch)
- Threat detection & response (GuardDuty, Security Hub, Detective)
- Infrastructure & network security (WAF, Shield, Network Firewall)
- Incident response & automation

## 7. AWS services to learn
| Category | Services |
|---|---|
| Identity | IAM, IAM Identity Center, STS, Organizations/SCPs |
| Data protection | KMS, CloudHSM, Secrets Manager, Macie |
| Detection | GuardDuty, Security Hub, Detective, Inspector |
| Logging | CloudTrail, Config, CloudWatch, VPC Flow Logs |
| Network | WAF, Shield, Network Firewall |

## 8. Hands-on labs
1. **Least-privilege IAM** policy + permission boundary. *(Cleanup: delete users/policies.)*
2. **KMS encryption** of an S3 bucket (SSE-KMS) + key policy. *(Cleanup: schedule key deletion, delete bucket.)*
3. **GuardDuty** enable + review sample findings. *(Cleanup: disable GuardDuty.)*
4. **CloudTrail investigation** — find who did an action. *(Cleanup: delete trail + log bucket.)*
5. **Macie** scan a bucket for sensitive data (sample). *(Cleanup: disable Macie — can be costly.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–2 | IAM deep dive; Lab 1 |
| 3 | STS, federation, Identity Center |
| 4–5 | KMS + encryption; Lab 2 |
| 6 | Secrets Manager + Macie; Lab 5 |
| 7 | Logging (CloudTrail/Config); Lab 4 |
| 8 | Threat detection (GuardDuty/Security Hub); Lab 3 |
| 9 | Network security (WAF/Shield/Firewall) |
| 10 | Incident response + automation |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 75%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | IAM + federation (Lab 1) |
| 2 | Encryption + data protection (Labs 2, 5) |
| 3 | Logging + detection + network (Labs 3–4) |
| 4 | Incident response + 3 mocks |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | IAM policies deeply (Lab 1) |
| 3 | KMS + envelope encryption (Lab 2) |
| 4 | Secrets + Macie (Lab 5) |
| 5 | Logging (Lab 4) |
| 6 | Threat detection (Lab 3) |
| 7 | Network security + incident response |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **75%+**. Heavy on IAM policy evaluation logic + KMS key policies + incident scenarios.
- Practice reading JSON policies and predicting allow/deny.
- 3+ timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] IAM policy evaluation (explicit deny > allow; boundaries; SCPs)
- [ ] KMS: key policies vs IAM, grants, envelope encryption
- [ ] CloudTrail vs Config vs GuardDuty vs Detective roles
- [ ] S3 encryption options (SSE-S3/SSE-KMS/SSE-C/DSSE)
- [ ] Cross-account access patterns
- [ ] Incident response automation (EventBridge + Lambda)
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
| Wins in IAM evaluation? | Explicit deny always wins |
| Detect threats from logs/behavior? | GuardDuty |
| Find sensitive data (PII) in S3? | Macie |
| Who did this API call? | CloudTrail |
| Control max permissions for a role? | Permission boundary |
| Encrypt with managed keys + audit? | KMS (SSE-KMS) |
| Visualize/investigate findings? | Detective |

→ More in `05-flashcards/aws-flashcards.md`.

## 17. Official docs / resources
- [ ] SCS-C03 exam guide: _add link_
- [ ] IAM + KMS docs: _add link_
- [ ] GuardDuty + Security Hub docs: _add link_
- [ ] Official practice exam: _add link_
