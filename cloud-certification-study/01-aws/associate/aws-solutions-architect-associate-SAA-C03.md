# AWS Certified Solutions Architect – Associate

> 🍼 **Beginner explanation:** Teaches you to *design* systems on AWS — how to pick compute, storage, networking, and databases so apps are reliable, secure, and cost-effective. The single most-valued associate cert.
>
> 🌍 **Real-world example:** "Build a web app that handles traffic spikes, never loses data, and stays cheap." This cert is exactly how you'd architect that (Auto Scaling + ALB + RDS Multi-AZ + S3 + CloudFront).

| Field | Value |
|---|---|
| **1. Certification name** | AWS Certified Solutions Architect – Associate |
| **2. Exam code** | SAA-C03 |
| **3. Level** | Associate |
| **4. Best for role** | Cloud/solution architects, system designers, data scientists wanting architecture skills |
| **5. Prerequisites** | ~1 year AWS exposure recommended; CLF-C02 helpful, not required |

---

## 6. Core topics
- Compute, storage, networking, databases (in depth)
- High availability, fault tolerance, elasticity, decoupling
- Cost optimization (right-sizing, Reserved/Savings/Spot, S3 tiers)
- Security & IAM (roles, policies, encryption)
- **Well-Architected Framework** (6 pillars)
- Designing resilient, performant, secure, cost-optimized architectures

## 7. AWS services to learn
| Category | Services |
|---|---|
| Compute | EC2, Auto Scaling, Lambda, ECS/Fargate (overview) |
| Networking | VPC, subnets, route tables, NAT/IGW, ALB/NLB, Route 53, CloudFront |
| Storage | S3 (+ classes), EBS, EFS, Storage Gateway |
| Database | RDS (Multi-AZ/read replicas), Aurora, DynamoDB, ElastiCache |
| Integration | SQS, SNS, EventBridge |
| Security/Mgmt | IAM, KMS, CloudWatch, CloudTrail |

## 8. Hands-on labs
1. **Build a VPC** (public+private subnets, IGW, NAT, route tables). *(Cleanup: delete NAT GW first — it costs hourly, then VPC.)*
2. **Launch EC2 behind an ALB with Auto Scaling.** *(Cleanup: delete ASG, ALB, EC2.)*
3. **RDS Multi-AZ** + connect from EC2. *(Cleanup: delete RDS, skip final snapshot.)*
4. **S3 static website hosting** + **CloudFront** distribution. *(Cleanup: disable/delete distribution, then bucket.)*
5. **IAM roles** for EC2 to read S3 (no keys). *(Cleanup: delete role/policy.)*
6. **CloudWatch alarm** + SNS notification. *(Cleanup: delete alarm + topic.)*

## 9. Two-week plan (intensive)
| Day | Focus |
|---|---|
| 1–2 | VPC + networking; Lab 1 |
| 3–4 | EC2, Auto Scaling, ELB; Lab 2 |
| 5–6 | Storage (S3 classes, EBS, EFS); Lab 4 |
| 7–8 | Databases (RDS, Aurora, DynamoDB); Lab 3 |
| 9 | Decoupling (SQS/SNS/EventBridge) |
| 10 | Security/IAM/KMS; Lab 5; Lab 6 |
| 11 | Well-Architected + cost optimization |
| 12 | Mock #1 + gaps |
| 13 | Revise weak areas |
| 14 | Mock #2 → book if 80%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Networking + compute (Labs 1–2) |
| 2 | Storage + databases (Labs 3–4) |
| 3 | Security, decoupling, monitoring, cost (Labs 5–6) |
| 4 | Well-Architected + 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | VPC + networking deeply (Lab 1) |
| 3 | Compute + Auto Scaling (Lab 2) |
| 4 | Storage (Lab 4) |
| 5 | Databases (Lab 3) |
| 6 | Security + decoupling (Labs 5–6) |
| 7 | Cost + Well-Architected |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- 65 questions / 130 min. Target **80%+** before booking.
- Practice **scenario** questions — they describe a need; you pick the best-fit architecture.
- Watch keywords: "most cost-effective", "highly available", "least operational overhead", "decouple".
- 4+ timed mocks; log every miss.

## 13. Final revision checklist (last 3 days)
- [ ] VPC components + when to use NAT vs IGW
- [ ] ALB vs NLB vs Gateway LB
- [ ] RDS Multi-AZ (HA) vs Read Replicas (scale reads)
- [ ] S3 storage classes + lifecycle
- [ ] SQS vs SNS vs EventBridge
- [ ] EC2 pricing models (On-Demand/Reserved/Spot/Savings)
- [ ] 6 Well-Architected pillars
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
| HA database setup? | RDS Multi-AZ |
| Scale read traffic on RDS? | Read replicas |
| Decouple app components? | SQS (queue) / SNS (pub-sub) |
| Cheapest for fault-tolerant, interruptible compute? | Spot Instances |
| Serve static content globally with low latency? | CloudFront |
| Give EC2 access to S3 securely? | IAM role (not access keys) |
| Storage for infrequent access, ms retrieval? | S3 Standard-IA |

→ More in `05-flashcards/aws-flashcards.md`.

## 17. Official docs / resources
- [ ] SAA-C03 exam guide: _add link_
- [ ] AWS Well-Architected Framework: _add link_
- [ ] AWS Architecture Center: _add link_
- [ ] Official practice exam: _add link_
