# AWS Certified DevOps Engineer – Professional

> 🍼 **Beginner explanation:** Advanced cert for automating everything — CI/CD pipelines, infrastructure as code, monitoring, and automated incident response. Do after a Developer or SysOps associate.
>
> 🌍 **Real-world example:** Every code push auto-builds, tests, and deploys with blue/green, auto-rolls-back on errors, and alerts the team. This cert builds that platform.

| Field | Value |
|---|---|
| **1. Certification name** | AWS Certified DevOps Engineer – Professional |
| **2. Exam code** | DOP-C02 |
| **3. Level** | Professional |
| **4. Best for role** | DevOps & platform engineers |
| **5. Prerequisites** | DVA-C02 or SOA-C03 + experience recommended |

---

## 6. Core topics
- CI/CD pipelines & deployment strategies (blue/green, canary, rolling)
- Infrastructure as Code (CloudFormation, CDK)
- Monitoring, logging, observability, automated remediation
- Incident & event response, automation
- Security, compliance, and governance automation

## 7. AWS services to learn
| Category | Services |
|---|---|
| CI/CD | CodePipeline, CodeBuild, CodeDeploy, CodeArtifact |
| IaC | CloudFormation, CDK, SAM |
| Observability | CloudWatch, X-Ray, EventBridge, CloudTrail |
| Automation | Systems Manager, Lambda, Step Functions |
| Containers | ECS/EKS/Fargate, ECR |
| Security | IAM, Config, Secrets Manager, Inspector |

## 8. Hands-on labs
1. **CI/CD pipeline** (CodePipeline + CodeBuild + CodeDeploy). *(Cleanup: delete pipeline + artifacts bucket.)*
2. **Blue/green deployment** on ECS or Lambda via CodeDeploy. *(Cleanup: delete services/stacks.)*
3. **IaC with CloudFormation/CDK** (deploy + update + rollback). *(Cleanup: delete stack.)*
4. **Automated rollback** on CloudWatch alarm. *(Cleanup: delete alarms + pipeline.)*
5. **Auto-remediation:** Config rule → EventBridge → Lambda fix. *(Cleanup: delete rule + function.)*

## 9. Two-week plan (refresher)
| Day | Focus |
|---|---|
| 1–2 | CI/CD pipeline design; Lab 1 |
| 3–4 | Deployment strategies; Lab 2 |
| 5–6 | IaC (CFN/CDK); Lab 3 |
| 7 | Observability + EventBridge |
| 8 | Automated rollback; Lab 4 |
| 9 | Auto-remediation + compliance; Lab 5 |
| 10 | Security automation + secrets |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 75%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | CI/CD + deployment strategies (Labs 1–2) |
| 2 | IaC + rollback (Labs 3–4) |
| 3 | Monitoring + auto-remediation + security (Lab 5) |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | CI/CD pipelines (Lab 1) |
| 3 | Deployment strategies (Lab 2) |
| 4 | IaC deeply (Lab 3) |
| 5 | Observability + EventBridge |
| 6 | Automated rollback + remediation (Labs 4–5) |
| 7 | Security/compliance automation |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- ~75 Q / 180 min. Target **75%+**.
- Heavy on choosing deployment strategy + rollback automation + multi-account CI/CD.
- 3+ long timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] CodeDeploy strategies (in-place/blue-green; canary/linear/all-at-once)
- [ ] CloudFormation change sets, drift, nested stacks, StackSets
- [ ] EventBridge rules for event-driven automation
- [ ] Auto-rollback triggers (alarms, deployment hooks)
- [ ] Cross-account/multi-region pipelines
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
| Deploy to subset, then expand? | Canary / linear (CodeDeploy) |
| Deploy multi-account IaC? | CloudFormation StackSets |
| React to any AWS event? | EventBridge rule → target |
| Roll back on error automatically? | CodeDeploy + CloudWatch alarm |
| Preview infra changes before apply? | CloudFormation change set |

→ More in `05-flashcards/aws-flashcards.md`.

## 17. Official docs / resources
- [ ] DOP-C02 exam guide: _add link_
- [ ] AWS CodePipeline/CodeDeploy docs: _add link_
- [ ] CloudFormation + CDK docs: _add link_
- [ ] Official practice exam: _add link_
