---
tags: [foundations, beginner, finops, cost, aws]
aliases: [FinOps Basics, Cost Engineering, Cloud Cost Control]
---
> [[06-mlops-basics|◀ MLOps]] · [[HOME|🏠 Home]] · [[STUDY_PLAN|Plan (M6.5)]] · [[PROGRESS|Tracker]] · [[08-kubernetes-basics|Kubernetes ▶]]

# 07 · FinOps basics (don't get a surprise bill)

## In plain English
**FinOps** = treating cloud cost as something you **estimate, watch, and control** — not a scary
surprise at month-end. The cloud charges by the second for things that are *running*, so the #1
rule is: **know the cost before you start, and tear things down after.**

> Analogy: the cloud is a taxi with the meter always running. FinOps is checking the fare estimate
> before the ride, watching the meter, and remembering to **get out of the taxi** (terminate) when done.

## Why it matters for your career
A single forgotten resource (a NAT Gateway, a SageMaker endpoint) can quietly cost ₹3,000–₹10,000/month.
For a learner on a personal account this is *your money*. For a company it's a real engineering skill —
"cost-aware" data scientists and engineers are valued. It also keeps your hands-on labs **safe and free**.

## Key concepts
- **Pricing Calculator** — estimate cost *before* building.
- **Cost Explorer** — see where money already went (by service/tag).
- **Budgets + billing alarms** — get emailed when spend crosses ₹/$ thresholds. **Set one on day one.**
- **Free Tier traps** — "free" has limits (hours, GB, requests); over them you pay. Some services aren't free at all.
- **The classic surprise-bill culprits:**
  - **NAT Gateway** — ~$32+/mo just to exist, plus data charges. Easy to forget.
  - **SageMaker real-time endpoints** — bill **24/7** while "up." Delete after testing.
  - **CloudWatch Logs** — unbounded log ingestion/retention adds up.
  - **Unattached EBS volumes** + **old snapshots** — still billed after the EC2 is gone.
  - **Elastic IPs** not attached, idle load balancers, leftover S3 in Standard.
- **EC2 stop vs terminate** — **stop** keeps the disk (small cost, restartable); **terminate** deletes it (no cost).
- **S3 storage classes** — Standard → IA → Glacier; **lifecycle rules** auto-move/expire data.
- **Spot instances** — up to ~90% cheaper, interruptible (great for training).
- **Savings Plans / Reserved** — commit to steady usage for a discount (later, not for learners).
- **Tagging strategy** — tag everything `project=learn` so you can find + delete it.

## Tools
AWS Budgets · Cost Explorer · Pricing Calculator · CloudWatch · S3 lifecycle rules

## Mini lab (full version = [[STUDY_PLAN|STUDY_PLAN Module 6.5]])
1. **Estimate** a lab's cost in the Pricing Calculator *before* running it.
2. Create a **Budget alarm** (e.g. alert at $5 and $20) — this is **Project 00**.
3. Open **Cost Explorer** and read your spend by service.
4. **Tag** resources (`project=learn`).
5. Add an **S3 lifecycle rule** (transition to IA after 30 days, expire after 90).
6. List the **risky services** that can cause surprise bills (NAT, endpoints, EBS…).
7. Write a reusable **teardown checklist** for every lab.

> ✅ This whole note is "cost-safety" — there's nothing to tear down here, just habits to build. Personal `learn` account only.

## ✅ Checkpoint
I can **estimate, monitor, and control** cloud cost before running experiments, and I can name the
top surprise-bill culprits and how to avoid them.

---
Back to: [[HOME]] · [[START-HERE]] · [[STUDY_PLAN]] · [[PROGRESS]] · related project: [[projects/00-safety-budget/README|Project 00 — budget alarm]]
