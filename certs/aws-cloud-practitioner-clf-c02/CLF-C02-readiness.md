---
tags: [cert/clf-c02, aws/foundational, readiness]
cert: CLF-C02
aliases: [CLF-C02 Readiness Checklist]
---
> [[CLF-C02|⬅ CLF-C02 Home]] · [[CLF-C02-practice|🧪 Practice Exam]]

# CLF-C02 — exam-readiness checklist

Book the exam only when you can tick **every** box. These are the recall + skills the exam expects.

## Domain 1 — Cloud Concepts
- [ ] List the 6 advantages of cloud (CapEx→OpEx, economies of scale, stop guessing capacity, agility, no data centers, go global)
- [ ] Name the 6 Well-Architected pillars (incl. Sustainability)
- [ ] Distinguish IaaS / PaaS / SaaS with an example each
- [ ] Explain elasticity vs scalability vs high availability
- [ ] Explain CapEx vs OpEx and TCO

## Domain 2 — Security & Compliance
- [ ] Explain the shared responsibility model + how it shifts for managed services
- [ ] Root user best practices (MFA, don't use daily, no root keys)
- [ ] IAM users vs groups vs roles vs policies; least privilege
- [ ] Match: GuardDuty (threats), Macie (PII), Inspector (vulns), CloudTrail (audit), KMS (keys), Artifact (compliance)
- [ ] Encryption at rest vs in transit

## Domain 3 — Technology & Services
- [ ] Region vs AZ vs Edge location; how to choose a Region
- [ ] One-liner for each compute service (EC2, Lambda, ECS/EKS, Fargate, Beanstalk)
- [ ] Storage: S3 vs EBS vs EFS vs Glacier — when each
- [ ] Databases: RDS/Aurora vs DynamoDB vs Redshift vs ElastiCache
- [ ] Networking: VPC, security group vs NACL, Route 53, CloudFront
- [ ] CloudWatch vs CloudTrail vs Config (don't confuse)
- [ ] 4 ways to interact (Console, CLI, SDK, CloudFormation/IaC)

## Domain 4 — Billing, Pricing & Support
- [ ] EC2 pricing: On-Demand / Reserved / Savings Plans / Spot / Dedicated — when each
- [ ] 3 free-tier types
- [ ] Tool for each: Pricing Calculator (estimate), Cost Explorer (analyze), Budgets (alert), CUR (detail)
- [ ] Support plans ladder; which has a dedicated TAM (Enterprise)
- [ ] Consolidated billing via Organizations

## Practice gate
- [ ] Scored **≥ 18/25** on `practice-questions.md`
- [ ] Scored **≥ 70%** on each domain's questions
- [ ] Took at least one **timed** full practice set (AWS Skill Builder official practice exam recommended)

## Logistics
- [ ] Account: created at aws.amazon.com/certification (uses your Amazon/personal account)
- [ ] Chosen test center **or** online-proctored (quiet room, webcam, valid ID, clear desk)
- [ ] Know the cost ($100) + that results are usually instant (pass/fail) with the score email later

## Free official resources to round out prep
- **AWS Skill Builder** — "AWS Cloud Practitioner Essentials" (free course) + official practice question set
- **AWS Cloud Quest: Cloud Practitioner** (gamified hands-on)
- **CLF-C02 Exam Guide + sample questions** (PDF on the certification page) — read the official guide once

When every box is ticked → **book it.** Then we move to your next cert
(ML Engineer Associate MLA-C01 or Data Engineer Associate DEA-C01) per `../../CERT_ROADMAP.md`.
