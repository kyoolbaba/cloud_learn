---
tags: [projects, moc, hands-on]
aliases: [Projects, Projects MOC]
---
> [[HOME|🏠 Home]] · [[labs/README|◀ Labs]] · [[CERT_ROADMAP|Certs]] · [[PROGRESS|Tracker]]
>
> **Build track:** [[projects/00-safety-budget/README|00 Budget]] · [[projects/01-s3-file-vault/README|01 S3 vault]] · [[projects/02-ec2-devbox/README|02 EC2]] · [[projects/03-userdata-webserver/README|03 user-data]] · [[projects/04-iam-least-privilege/README|04 IAM]] · [[projects/05-lambda-api/README|05 Lambda API]] · [[projects/06-s3-trigger-pipeline/README|06 S3→Lambda]] · [[projects/07-ecr-fargate/README|07 Fargate]] · [[projects/08-sqs-worker/README|08 SQS]] · [[projects/09-stepfunctions-fanout/README|09 Step Fns]] · [[projects/10-cloudwatch-autostop/README|10 Autostop]] · [[projects/11-terraform-backend/README|11 Terraform]] · [[projects/12-capstone-cloud-toggle/README|🏁 12 Capstone]] · [[projects/SETUP-personal-aws|⚙️ Setup]]

# Cloud Projects — learn each AWS service by building something small

One **small project per service**. Each is concrete (you build a thing), short
(~1–2 hrs), free-tier friendly, and ends with a teardown so the bill stays ~$0.
They build on each other and ladder into the capstone (the "Run in cloud" toggle).

**Each project follows the same shape:** Goal → Why → Learn-from (the `labs/` file) →
Build it → ✅ Done-when → 🧹 Teardown → 🚀 Stretch.

## ⚠️ Prerequisite — use a separate personal account
Your `default` CLI profile points at a **shared company account** (`857810275001`,
Healthium production data). **Do not run these projects there.** First do
**[`SETUP-personal-aws.md`](SETUP-personal-aws.md)**: create a free personal account,
an admin IAM user, and a `learn` CLI profile.

**Every session, set the profile and confirm the account before any command:**
```powershell
$env:AWS_PROFILE = "learn"
aws sts get-caller-identity --query Account --output text   # must be your PERSONAL account id
```
With `AWS_PROFILE=learn` set, the CLI + boto3 use the personal account automatically.

## Your setup
- AWS CLI 2.17 + boto3 1.43 ready — **all projects run from Windows/PowerShell** (no WSL needed)
- Region `ap-south-1`; reference code in `../labs/`; fill in `../labs/m3-aws/config.sh` once (Project 01)

## 💸 The three cost rules (non-negotiable)
1. **Budget alarm first** — Project 00, before you launch anything.
2. **Tear down after every project** — each has a 🧹 section. The #1 bill cause is forgotten running resources.
3. **Free tier:** `t3.micro` EC2 (750h/mo yr-1), 5GB S3, 1M Lambda calls/mo. Fargate/Step Functions cost pennies for short runs — still tear down.

## The track

| # | Project | Service(s) | Time | Cost |
|---|---|---|---|---|
| **00** | Lock the account + budget alarm | Budgets, IAM, CloudWatch | 30m | $0 |
| **01** | S3 file vault (backup + share links) | **S3** | 1–2h | free |
| **02** | Disposable dev box + benchmark | **EC2**, security groups, SSH | 1–2h | free-tier |
| **03** | Self-configuring web server | **user-data**, security groups | 1h | free-tier |
| **04** | Least-privilege key (prove it can't escape) | **IAM** | 1–2h | $0 |
| **05** | Serverless API endpoint | **Lambda + API Gateway** | 1–2h | free |
| **06** | Auto-process uploads | **S3 events → Lambda** | 1–2h | free |
| **07** | Run your container in the cloud | **ECR + Fargate**, CloudWatch logs | 2–3h | pennies |
| **08** | Parallel job queue | **SQS** (+ DLQ) | 1–2h | free |
| **09** | Fan-out & aggregate | **Step Functions** `Map` + Fargate | 2–3h | pennies |
| **10** | Cost guardian | **CloudWatch** alarms + scheduled Lambda | 1h | $0 |
| **11** | One-command backend | **Terraform** (IaC) | 2–3h | free |
| **12** | 🏁 Capstone: the cloud forecast toggle | everything | project | pennies |

Work them in order — each assumes the previous. Tick them off in `../PROGRESS.md`.

## How to use a project
1. Open its `README.md`.
2. Skim the **Learn-from** lab file (the reference implementation).
3. Do **Build it** yourself (don't just copy the lab — type/modify it).
4. Verify against **✅ Done when**.
5. Run **🧹 Teardown**.
6. Ping me if something errors — I can run boto3/CLI from here to debug with you.
