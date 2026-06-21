---
tags: [cert/clf-c02, aws/foundational]
cert: CLF-C02
domain: 3
aliases: [CLF-C02 Domain 3, Cloud Technology and Services]
---
> [[domain-2-security-compliance|◀ Domain 2]] · [[CLF-C02|CLF-C02 Home]] · [[domain-4-billing-pricing-support|Domain 4 · Billing ▶]]

# Domain 3 — Cloud Technology & Services (34%)

The largest domain. It's breadth, not depth: **recognize what each service does** and pick
the right one for a scenario. Flashcard the one-liners.

## 3.1 Ways to interact with AWS
- **Management Console** (web UI) · **CLI** (`aws ...`) · **SDKs** (boto3 etc.) ·
  **Infrastructure as Code** (**CloudFormation** — AWS-native templates; CDK; Terraform is 3rd-party).
- Exam tip: "repeatable, version-controlled infrastructure" → **CloudFormation/IaC**.

## 3.2 Global infrastructure (high-yield)
- **Region** = a geographic area (e.g., `ap-south-1` Mumbai). Pick by: **latency** (close to users),
  **compliance/data residency**, **price**, **service availability**.
- **Availability Zone (AZ)** = 1+ isolated data centers in a Region. Deploy across **multiple AZs**
  for high availability.
- **Edge Locations / PoPs** = CloudFront CDN caches + Route 53, close to users for low latency.
- **Local Zones / Outposts / Wavelength** = AWS closer to you / on-prem / 5G edge.

## 3.3 Compute
| Service | One-liner |
|---|---|
| **EC2** | Virtual machines. Families: General (t/m), Compute (c), Memory (r/x), Storage (i/d), Accelerated (p/g GPU). |
| **AWS Lambda** | **Serverless** functions, event-driven, pay per ms, ≤15 min. "No servers to manage." |
| **ECS / EKS** | Run containers (ECS = AWS's, EKS = Kubernetes). |
| **AWS Fargate** | **Serverless containers** (no EC2 to manage) for ECS/EKS. |
| **Elastic Beanstalk** | PaaS: upload code, it provisions everything. |
| **EC2 Auto Scaling** | Add/remove instances to match demand (elasticity). |
| **Elastic Load Balancing (ELB)** | Distributes traffic across targets (ALB/NLB/GWLB). |

Tells: "no servers to manage / event-driven / per-request" → **Lambda**; "run containers without
managing servers" → **Fargate**; "just deploy my app, handle the rest" → **Beanstalk**.

## 3.4 Storage
| Service | One-liner |
|---|---|
| **Amazon S3** | Object storage, 11 9's durability. Classes: Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, **Glacier Instant/Flexible/Deep Archive**. |
| **Amazon EBS** | Block storage volumes for **one** EC2 (like a virtual disk). |
| **Amazon EFS** | Shared **file** storage (NFS) for many Linux EC2s. |
| **Amazon FSx** | Managed file systems (Windows, Lustre). |
| **S3 Glacier** | Cheap **archival** storage (retrieval minutes→hours). |
| **AWS Backup** | Centralized backups across services. |
| **Storage Gateway** | Hybrid on-prem ↔ AWS storage. |

Tells: "store any amount of objects/files, web-scale" → **S3**; "disk for one EC2" → **EBS**;
"shared filesystem across instances" → **EFS**; "cheapest long-term archive" → **Glacier Deep Archive**.

## 3.5 Databases
| Service | One-liner |
|---|---|
| **Amazon RDS** | Managed **relational** DB (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server). |
| **Amazon Aurora** | AWS's high-performance MySQL/PostgreSQL-compatible engine. |
| **Amazon DynamoDB** | Managed **NoSQL** key-value, serverless, single-digit-ms. |
| **Amazon Redshift** | **Data warehouse** (analytics/OLAP on petabytes). |
| **Amazon ElastiCache** | In-memory cache (Redis/Memcached). |
| **DocumentDB / Neptune / Keyspaces / Timestream / MemoryDB** | document / graph / Cassandra / time-series / in-memory. |

Tells: "relational + managed" → **RDS**; "NoSQL, serverless, massive scale" → **DynamoDB**;
"analytics/data warehouse" → **Redshift**; "speed up reads with a cache" → **ElastiCache**.

## 3.6 Networking & content delivery
| Service | One-liner |
|---|---|
| **Amazon VPC** | Your private virtual network (subnets, route tables, gateways). |
| **Security Group** | Stateful instance-level firewall (allow rules). **NACL** = subnet-level, stateless. |
| **Amazon Route 53** | DNS + domain registration + health checks. |
| **Amazon CloudFront** | CDN — caches content at edge locations. |
| **API Gateway** | Managed front door for APIs (→ Lambda/HTTP). |
| **Direct Connect** | Dedicated private link on-prem ↔ AWS. **VPN** = encrypted over internet. |

Tells: "DNS / route users to the nearest endpoint" → **Route 53**; "cache static content near users" →
**CloudFront**; "dedicated private connection to AWS" → **Direct Connect".

## 3.7 App integration, analytics, ML (recognize)
- **SQS** (queue), **SNS** (pub/sub notifications), **EventBridge** (event bus), **Step Functions** (workflows).
- **Athena** (SQL on S3), **Glue** (ETL/serverless data integration), **Kinesis** (streaming),
  **EMR** (managed Hadoop/Spark), **QuickSight** (BI dashboards), **Lake Formation** (data lakes).
- **SageMaker** (build/train/deploy ML), **Comprehend** (NLP), **Rekognition** (vision),
  **Textract** (OCR), **Polly** (TTS), **Transcribe** (STT), **Translate**, **Bedrock** (GenAI foundation models).

## 3.8 Management & monitoring
| Service | One-liner |
|---|---|
| **Amazon CloudWatch** | **Metrics, logs, alarms, dashboards** (performance monitoring). |
| **AWS CloudTrail** | **API audit** log (who did what). |
| **AWS Trusted Advisor** | Best-practice checks: cost, performance, security, fault tolerance, limits. |
| **AWS Systems Manager** | Operate fleets (patching, Parameter Store, run commands). |
| **AWS CloudFormation** | IaC templates. **AWS Organizations** = manage many accounts. |
| **AWS Health Dashboard** | Status of AWS services + events affecting you. |

> Don't confuse: **CloudWatch** = performance/metrics & logs; **CloudTrail** = API/audit history; **Config** = resource configuration/compliance.

## Hands-on
```powershell
$env:AWS_PROFILE = "learn"
aws ec2 describe-regions --output table                # global infra
aws ec2 describe-availability-zones --region ap-south-1 --query "AvailabilityZones[].ZoneName"
aws s3 ls                                              # storage
aws cloudwatch list-metrics --namespace AWS/EC2 --query "Metrics[0]"
```
You've already touched EC2, S3, Lambda, Fargate, VPC, Step Functions, SQS in `projects/`. For
each service above, say its one-liner out loud — that recognition *is* the exam.

## Practice questions
**Q1.** Run code with no servers to manage, billed per request, triggered by events:
- A) EC2  B) **Lambda** ✅  C) Lightsail  D) Batch

**Q2.** Petabyte-scale SQL analytics / data warehouse:
- A) DynamoDB  B) RDS  C) **Redshift** ✅  D) ElastiCache

**Q3.** Cache static content at edge locations close to users:
- A) Global Accelerator  B) **CloudFront** ✅  C) Route 53  D) Direct Connect

**Q4.** Shared file system mounted by many Linux EC2 instances at once:
- A) EBS  B) S3  C) **EFS** ✅  D) FSx for Windows

**Q5.** Highly available web app — deploy across what?
- A) Multiple Regions only  B) **Multiple Availability Zones** ✅  C) One large instance  D) Edge locations

**Q6.** Service for monitoring metrics and setting alarms:
- A) CloudTrail  B) Config  C) **CloudWatch** ✅  D) Inspector

**Q7.** Provision repeatable infrastructure from version-controlled templates (AWS-native):
- A) **CloudFormation** ✅  B) OpsWorks  C) CodeDeploy  D) Systems Manager

**Q8.** Serverless way to run Docker containers (no EC2 to manage):
- A) EKS on EC2  B) **Fargate** ✅  C) Lightsail  D) Batch on EC2
