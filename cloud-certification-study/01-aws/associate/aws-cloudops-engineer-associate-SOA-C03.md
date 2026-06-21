# AWS Certified CloudOps Engineer – Associate

> 🍼 **Beginner explanation:** Teaches how to *operate* AWS day-to-day — deploy, monitor, automate, back up, patch, and keep systems reliable. The "keep the lights on" cert.
>
> 🌍 **Real-world example:** Production is live. You build dashboards, set alarms, automate patching with Systems Manager, and create backup plans so outages are caught and recovered fast.

| Field | Value |
|---|---|
| **1. Certification name** | AWS Certified CloudOps Engineer – Associate |
| **2. Exam code** | SOA-C03 |
| **3. Level** | Associate |
| **4. Best for role** | Cloud operations, sysadmins, DevOps operations |
| **5. Prerequisites** | ~1 year AWS ops; CLF-C02/SAA helpful |

---

## 6. Core topics
- Monitoring, logging, metrics, alarms, dashboards
- Deployment + automation (Systems Manager, CloudFormation basics)
- Reliability, backup & recovery, patching
- Networking operations, security/compliance ops
- Cost & performance operations

## 7. AWS services to learn
| Category | Services |
|---|---|
| Observability | CloudWatch (metrics/logs/alarms/dashboards), CloudTrail, X-Ray |
| Automation | Systems Manager (Patch/Run/State Manager), CloudFormation |
| Compute/scale | EC2, Auto Scaling, ELB |
| Networking | VPC, Route 53 |
| Resilience | AWS Backup, snapshots |
| Security/Mgmt | IAM, Config, Trusted Advisor |

## 8. Hands-on labs
1. **CloudWatch dashboard** with EC2 + custom metrics. *(Cleanup: delete dashboard.)*
2. **Alarms + SNS** notifications on CPU. *(Cleanup: delete alarms + topic.)*
3. **Systems Manager Patch Manager** baseline + patch an EC2. *(Cleanup: deregister, terminate EC2.)*
4. **AWS Backup plan** for an EBS volume / RDS. *(Cleanup: delete backup plan + recovery points.)*
5. **AWS Config** rule to flag non-compliant resources. *(Cleanup: delete rule + recorder.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–2 | CloudWatch metrics/logs; Lab 1 |
| 3 | Alarms + dashboards; Lab 2 |
| 4–5 | Systems Manager; Lab 3 |
| 6 | Auto Scaling + ELB ops |
| 7 | Backup & recovery; Lab 4 |
| 8 | CloudTrail + Config + compliance; Lab 5 |
| 9 | Networking ops (Route 53, VPC) |
| 10 | Cost + Trusted Advisor |
| 11 | Mock #1 + gaps |
| 12–13 | Revise weak areas |
| 14 | Mock #2 → book if 80%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Monitoring + logging (Labs 1–2) |
| 2 | Automation + Systems Manager (Lab 3) |
| 3 | Backup/recovery + compliance (Labs 4–5) |
| 4 | Networking + cost + 3 mocks |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | CloudWatch deeply (Labs 1–2) |
| 3 | Systems Manager (Lab 3) |
| 4 | Auto Scaling + ELB ops |
| 5 | Backup & DR (Lab 4) |
| 6 | CloudTrail + Config (Lab 5) |
| 7 | Networking + cost ops |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **80%+**. SOA historically may include hands-on style/scenario questions — practice console flows.
- Know CloudWatch vs CloudTrail vs Config distinctions cold.
- 4 timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] CloudWatch (metrics/logs/alarms) vs CloudTrail (API audit) vs Config (compliance)
- [ ] Systems Manager: Patch/Run/State/Session/Parameter
- [ ] Auto Scaling policies (target tracking/step/scheduled)
- [ ] AWS Backup vs manual snapshots
- [ ] Cross-region/cross-account DR basics
- [ ] Flashcards reviewed twice

## 14. Notes template
```
### Topic: <name>
- Beginner explanation:
- Real-world use:
- AWS service(s):
- Azure equivalent:
- Common exam trap:
- My example:
```

## 15. Mistake log template
| Date | Topic | What I got wrong | Correct concept | Revisit date |
|---|---|---|---|---|

## 16. Flashcards (starter set)
| Q | A |
|---|---|
| Who called this API and when? | CloudTrail |
| Is this resource compliant? | AWS Config |
| Centralized patching? | Systems Manager Patch Manager |
| Centralized backups across services? | AWS Backup |
| Scale based on a metric target? | Target tracking scaling policy |
| Secure shell to EC2 without SSH keys/ports? | SSM Session Manager |

→ More in `05-flashcards/aws-flashcards.md`.

## 17. Official docs / resources
- [ ] SOA-C03 exam guide: _add link_
- [ ] Systems Manager docs: _add link_
- [ ] CloudWatch + Config docs: _add link_
- [ ] Official practice exam: _add link_
