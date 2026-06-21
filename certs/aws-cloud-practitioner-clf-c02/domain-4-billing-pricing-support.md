---
tags: [cert/clf-c02, aws/foundational, billing]
cert: CLF-C02
domain: 4
aliases: [CLF-C02 Domain 4, Billing Pricing and Support]
---
> [[domain-3-technology-services|◀ Domain 3]] · [[CLF-C02|CLF-C02 Home]] · [[CLF-C02-practice|Practice Exam ▶]]

# Domain 4 — Billing, Pricing & Support (12%)

Smallest domain, easy points. Pricing models, cost tools, and support plans.

## 4.1 Pricing fundamentals
- **Pay-as-you-go** — pay for what you use, no long-term contracts (default).
- **Pay less by using more** — volume tiers (e.g., S3 storage gets cheaper per GB at scale).
- **Save when you reserve / commit** — Reserved Instances & Savings Plans.
- **3 cost drivers**: **compute**, **storage**, **data transfer OUT** (in is usually free; out costs).

## 4.2 EC2 purchasing options (know when to use each)
| Option | Use when |
|---|---|
| **On-Demand** | short-term, unpredictable, no commitment (most expensive/flexible) |
| **Reserved Instances (RI)** | steady-state, 1- or 3-yr commit → up to ~72% off |
| **Savings Plans** | commit to $/hour of compute for 1–3 yrs → flexible discount across EC2/Fargate/Lambda |
| **Spot Instances** | fault-tolerant/batch/flexible workloads → up to ~90% off, can be interrupted |
| **Dedicated Hosts** | licensing/compliance needs physical isolation |

Tells: "cheapest for interruption-tolerant batch" → **Spot**; "steady 24/7 server for a year" →
**Reserved/Savings Plan**; "spiky, unknown" → **On-Demand**.

## 4.3 Free Tier (3 types)
- **12-month free** (new accounts): e.g., 750 hrs/mo `t2/t3.micro` EC2, 5 GB S3.
- **Always free**: e.g., 1M Lambda requests/mo, 25 GB DynamoDB.
- **Trials**: short-term (e.g., some SageMaker, Redshift).

## 4.4 Cost-management tools (know which does what)
| Tool | Does |
|---|---|
| **AWS Pricing Calculator** | **Estimate** costs *before* you build. |
| **AWS Billing Dashboard** | Current charges + invoices. |
| **AWS Cost Explorer** | **Visualize & analyze** past/forecast spend with filters. |
| **AWS Budgets** | **Alerts** when cost/usage crosses a threshold (you used this in Project 00). |
| **Cost & Usage Report (CUR)** | Most detailed line-item billing data → S3. |
| **Cost Allocation Tags** | Tag resources (e.g., `project=forecast`) to break down spend. |
| **AWS Organizations** | **Consolidated billing** across accounts → volume discounts + one bill. |

Tells: "estimate before building" → **Pricing Calculator**; "alert at $X" → **Budgets**;
"analyze where money went" → **Cost Explorer"; "one bill for many accounts" → **Organizations/Consolidated billing**.

## 4.5 Support plans (know the ladder)
| Plan | Key inclusions |
|---|---|
| **Basic** (free) | Docs, whitepapers, forums (re:Post), core Trusted Advisor checks, Health Dashboard |
| **Developer** | Business-hours **email** to Cloud Support Associates |
| **Business** | **24/7** phone/chat/email, **full Trusted Advisor**, prod-system-down <1 hr |
| **Enterprise On-Ramp** | + pool of Technical Account Managers, faster response |
| **Enterprise** | **Dedicated TAM**, Concierge, <15-min critical response, IEM |

Tells: "dedicated **Technical Account Manager (TAM)**" → **Enterprise** (pool at On-Ramp);
"full Trusted Advisor + 24/7" → **Business** and up.

## 4.6 Other resources
- **Trusted Advisor** — checks across cost / performance / security / fault tolerance / service limits
  (full set needs Business+).
- **AWS Health Dashboard** — service health + personalized events.
- **re:Post** (Q&A), **Knowledge Center**, **AWS Partner Network (APN)**, **Professional Services**,
  **Marketplace** (buy 3rd-party software).

## Hands-on
```powershell
$env:AWS_PROFILE = "learn"
# In the console: Billing → Cost Explorer (enable it), Budgets (your Project 00 alarm), Pricing Calculator (web).
aws budgets describe-budgets --account-id <your-personal-acct-id> --query "Budgets[].BudgetName"
aws ce get-cost-and-usage --time-period Start=2026-06-01,End=2026-06-20 --granularity MONTHLY --metrics "UnblendedCost" 2>$null
```
Build a mock estimate in the **Pricing Calculator** for "1 t3.micro + 50 GB S3" — see the cost drivers.

## Practice questions
**Q1.** Cheapest option for a fault-tolerant batch job that can handle interruptions:
- A) On-Demand  B) Reserved  C) **Spot** ✅  D) Dedicated Host

**Q2.** Estimate the cost of a planned architecture *before* deploying:
- A) Cost Explorer  B) Budgets  C) **AWS Pricing Calculator** ✅  D) CUR

**Q3.** Get alerted when monthly spend exceeds $50:
- A) **AWS Budgets** ✅  B) Cost Explorer  C) Trusted Advisor  D) CloudWatch only

**Q4.** Which support plan includes a **dedicated** Technical Account Manager?
- A) Business  B) Developer  C) **Enterprise** ✅  D) Basic

**Q5.** One consolidated bill and volume discounts across many accounts:
- A) Cost Explorer  B) **AWS Organizations (consolidated billing)** ✅  C) Budgets  D) Savings Plans

**Q6.** Steady production server running 24/7 for a year — cheapest:
- A) On-Demand  B) Spot  C) **Reserved Instance / Savings Plan** ✅  D) Dedicated Host

**Q7.** (multi) Free-tier types include: (choose 2)
- A) **12-month free** ✅  B) Lifetime hardware  C) **Always free** ✅  D) Refundable
