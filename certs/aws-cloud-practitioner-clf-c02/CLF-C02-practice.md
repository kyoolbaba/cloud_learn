---
tags: [cert/clf-c02, aws/foundational, practice-exam]
cert: CLF-C02
aliases: [CLF-C02 Practice Exam, CLF-C02 Mock]
---
> [[CLF-C02|⬅ CLF-C02 Home]] · [[CLF-C02-readiness|Readiness Checklist ➡]]

# CLF-C02 — mixed mock exam (25 Q)

Roughly domain-weighted (Concepts 24% · Security 30% · Tech 34% · Billing 12%). Cover the
answer key, do all 25 in one ~30-min sitting, then review **every** miss. Target ≥ 70% (18/25)
before booking. Answers + explanations at the bottom.

1. Which is a benefit of cloud computing?
   A) Large upfront hardware purchase  B) Guessing capacity in advance
   C) **Trade capital expense for variable expense**  D) Manual scaling only

2. Under the shared responsibility model, the customer is responsible for:
   A) Physical security of data centers  B) **Configuring security groups & IAM**
   C) Hypervisor patching  D) Region hardware

3. Service that records all API calls for auditing:
   A) CloudWatch  B) Config  C) **CloudTrail**  D) GuardDuty

4. Run containers without managing any servers:
   A) EC2  B) **Fargate**  C) EBS  D) Lightsail

5. Deploy across multiple ___ for high availability within a Region:
   A) Edge locations  B) **Availability Zones**  C) Accounts  D) VPCs

6. Cheapest EC2 pricing for interruption-tolerant workloads:
   A) On-Demand  B) Reserved  C) **Spot**  D) Dedicated Host

7. Find personally identifiable information stored in S3:
   A) Inspector  B) GuardDuty  C) **Macie**  D) WAF

8. Estimate monthly cost before building:
   A) Cost Explorer  B) **Pricing Calculator**  C) Budgets  D) CUR

9. Which is serverless and event-driven, billed per invocation?
   A) EC2  B) **Lambda**  C) Beanstalk  D) ECS on EC2

10. The Well-Architected pillar about minimizing environmental impact:
    A) Reliability  B) **Sustainability**  C) Performance Efficiency  D) Security

11. Managed relational database service:
    A) DynamoDB  B) **RDS**  C) Redshift  D) ElastiCache

12. (multi) Two ways to follow least privilege / protect the root user: (choose 2)
    A) **Enable MFA on root**  B) Share root credentials  C) **Use IAM roles instead of long-lived keys**  D) Create root access keys

13. Petabyte-scale data warehouse for analytics:
    A) **Redshift**  B) DynamoDB  C) Aurora  D) Neptune

14. Get best-practice checks for cost, security, performance, fault tolerance, limits:
    A) **Trusted Advisor**  B) CloudTrail  C) Inspector  D) Artifact

15. DNS and domain registration service:
    A) CloudFront  B) **Route 53**  C) Direct Connect  D) API Gateway

16. Download a PCI-DSS compliance report:
    A) Security Hub  B) Config  C) **AWS Artifact**  D) Trusted Advisor

17. Which support plan gives 24/7 phone/chat and full Trusted Advisor (minimum)?
    A) Developer  B) **Business**  C) Basic  D) Free

18. Object storage with 11 nines of durability:
    A) EBS  B) EFS  C) **S3**  D) Instance store

19. Set an alert when spend crosses a threshold:
    A) Cost Explorer  B) **AWS Budgets**  C) CUR  D) Pricing Calculator

20. Intelligent threat detection from CloudTrail/VPC/DNS logs:
    A) Inspector  B) **GuardDuty**  C) Macie  D) Shield

21. IaC service that is AWS-native:
    A) Terraform  B) **CloudFormation**  C) Ansible  D) Jenkins

22. Which model is SaaS?
    A) EC2  B) Elastic Beanstalk  C) **Amazon QuickSight**  D) Lambda

23. One bill and volume pricing across many accounts:
    A) **AWS Organizations (consolidated billing)**  B) Budgets  C) Savings Plans  D) Cost Explorer

24. Stateful, instance-level virtual firewall:
    A) Network ACL  B) **Security group**  C) WAF  D) Shield

25. Performance metrics, logs, and alarms:
    A) CloudTrail  B) **CloudWatch**  C) Config  D) X-Ray

---

## Answer key
1-C, 2-B, 3-C, 4-B, 5-B, 6-C, 7-C, 8-B, 9-B, 10-B, 11-B, 12-A&C, 13-A, 14-A, 15-B,
16-C, 17-B, 18-C, 19-B, 20-B, 21-B, 22-C, 23-A, 24-B, 25-B

### Why (the ones people miss)
- **2:** customer = security *in* the cloud (IAM, SGs, data, OS on EC2); AWS = *of* the cloud.
- **3 vs 25:** CloudTrail = **API/audit** ("who did what"); CloudWatch = **metrics/logs/alarms**.
- **7/16/20:** Macie=PII in S3, Artifact=compliance docs, GuardDuty=threat detection. Don't swap them.
- **14 vs 16:** Trusted Advisor=best-practice checks; Artifact=downloadable compliance reports.
- **22:** SaaS = ready-to-use software (QuickSight). EC2=IaaS, Beanstalk/Lambda=PaaS-ish.
- **24:** Security group = stateful, instance level. NACL = stateless, subnet level.

**Scoring:** 18+/25 → you're ready; do the readiness checklist. <18 → re-read the weak domain and retake.
