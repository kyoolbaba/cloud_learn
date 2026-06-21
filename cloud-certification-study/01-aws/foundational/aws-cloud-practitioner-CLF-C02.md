# AWS Certified Cloud Practitioner

> 🍼 **Beginner explanation:** This is the "driver's license" of AWS. It proves you understand what the cloud is, what AWS offers, how billing works, and basic security — without needing to be technical. Perfect first cert.
>
> 🌍 **Real-world example:** A company is moving from its own servers to AWS. You're the analyst in the meeting. This cert lets you understand the conversation — what S3 is, why they'd use Auto Scaling, how they'll be billed.

| Field | Value |
|---|---|
| **1. Certification name** | AWS Certified Cloud Practitioner |
| **2. Exam code** | CLF-C02 |
| **3. Level** | Foundational |
| **4. Best for role** | Beginners, business/non-technical stakeholders, anyone starting AWS |
| **5. Prerequisites** | None. ~6 months general AWS exposure helps but not required |

---

## 6. Core topics
- AWS global infrastructure (Regions, Availability Zones, Edge locations)
- Shared Responsibility Model (what AWS secures vs what you secure)
- IAM basics (users, groups, roles, MFA, least privilege)
- Core services overview (compute, storage, networking, databases)
- Pricing & billing (pay-as-you-go, Free Tier, Cost Explorer, Budgets)
- Support plans (Basic, Developer, Business, Enterprise)
- Well-Architected Framework (intro), cloud value proposition

## 7. AWS services to learn
| Category | Services |
|---|---|
| Compute | EC2, Lambda, Elastic Beanstalk (overview) |
| Storage | S3, EBS, EFS, Glacier |
| Database | RDS, DynamoDB (overview) |
| Networking | VPC, CloudFront, Route 53 (overview) |
| Security | IAM, KMS, Shield, WAF (overview) |
| Management | CloudWatch, CloudTrail, Cost Explorer, Budgets, Trusted Advisor |

## 8. Hands-on labs
> Every lab ends with **Cleanup**. Log each in `04-trackers/lab-completion-tracker.md`.

1. **Create an AWS account safely** → enable **MFA** on the root user. *(Cleanup: none, keep account)*
2. **Set a billing alarm** ($5 threshold via Budgets + CloudWatch). *(Cleanup: keep — it protects you)*
3. **Create an IAM user + group** with limited permissions; stop using root for daily work. *(Cleanup: keep IAM user)*
4. **Create an S3 bucket**, upload a file, view it, set it private. *(Cleanup: delete object + bucket)*
5. **Launch & terminate an EC2 instance** (t2.micro free tier) just to see it. *(Cleanup: TERMINATE the instance.)*
6. **Explore Cost Explorer** and the Free Tier dashboard. *(Cleanup: none)*

## 9. Two-week plan (fast track)
| Day | Focus |
|---|---|
| 1–2 | Cloud concepts, global infrastructure, Free Tier; do Labs 1–2 |
| 3–4 | IAM + shared responsibility; Lab 3 |
| 5–6 | Compute + storage core services; Labs 4–5 |
| 7 | Databases + networking overview |
| 8–9 | Pricing, billing, support plans; Lab 6 |
| 10 | Well-Architected intro + flashcards |
| 11–12 | Mock exam #1, log weak topics |
| 13 | Revise weak topics + flashcards |
| 14 | Mock exam #2 → if 85%+, book exam |

## 10. Four-week plan (comfortable)
| Week | Focus |
|---|---|
| 1 | Concepts + infrastructure + IAM (Labs 1–3) |
| 2 | Compute, storage, databases, networking (Labs 4–5) |
| 3 | Pricing, billing, support, security (Lab 6) + flashcards daily |
| 4 | 2–3 mock exams, weak-topic revision, last-3-days checklist |

## 11. Eight-week plan (slow & steady / busy schedule)
| Weeks | Focus |
|---|---|
| 1–2 | Cloud concepts + global infrastructure |
| 3–4 | IAM, security, shared responsibility (Labs 1–3) |
| 5 | Compute + storage (Labs 4–5) |
| 6 | Databases, networking, management tools (Lab 6) |
| 7 | Pricing, billing, support, Well-Architected |
| 8 | Mocks + revision + book exam |

## 12. Mock exam strategy
- Take your first mock **after ~60% of topics** to find gaps early.
- Aim for **85%+ consistently** (it's a foundational exam, target high).
- Review **every** wrong answer; log it in section 15 and `04-trackers/weak-topic-log.md`.
- Do at least **3 full mocks** under timed conditions (90 min, 65 questions).

## 13. Final revision checklist (last 3 days)
- [ ] Can explain Regions vs AZs vs Edge locations
- [ ] Can draw the Shared Responsibility Model line
- [ ] Know the 4 support plans and who needs each
- [ ] Know Free Tier vs pay-as-you-go vs Savings Plans/Reserved
- [ ] Know IAM users/groups/roles/MFA + least privilege
- [ ] Can match 10 core services to compute/storage/db/networking
- [ ] Reviewed all flashcards twice
- [ ] No new topics — review only

## 14. Notes template
```
### Topic: <name>
- Beginner explanation:
- Why it matters / real-world use:
- AWS service(s):
- Azure equivalent:
- Common exam trap:
- My own example:
```

## 15. Mistake log template
| Date | Question/Topic | What I got wrong | Correct concept | Revisit date |
|---|---|---|---|---|
| | | | | |

## 16. Flashcards (starter set)
| Q | A |
|---|---|
| What is a Region? | A geographic area with multiple isolated data centers (AZs) |
| What is an Availability Zone? | One or more discrete data centers within a Region |
| Shared Responsibility: who secures the cloud? | AWS secures *of* the cloud; you secure *in* the cloud |
| Cheapest support plan with 24/7 phone? | Business |
| Service for object storage? | S3 |
| Service for running VMs? | EC2 |
| Tool to set a spending alert? | AWS Budgets |
| Best practice for root account? | Enable MFA, don't use for daily tasks |

→ More in `05-flashcards/aws-flashcards.md`.

## 17. Official docs / resources
- [ ] AWS Cloud Practitioner exam guide (official): _add link_
- [ ] AWS Skill Builder free digital course: _add link_
- [ ] AWS Well-Architected Framework: _add link_
- [ ] AWS Free Tier page: _add link_
- [ ] Practice exam (official): _add link_
