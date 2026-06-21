---
tags: [cert/clf-c02, aws/foundational]
cert: CLF-C02
domain: 1
aliases: [CLF-C02 Domain 1, Cloud Concepts]
---
> [[CLF-C02|⬅ CLF-C02 Home]] · Next: [[domain-2-security-compliance|Domain 2 · Security ▶]]

# Domain 1 — Cloud Concepts (24%)

What the AWS Cloud is and why people use it. Mostly definitions and frameworks.

## 1.1 Benefits of the AWS Cloud (high-yield)
**The 6 advantages of cloud** (memorize — frequently tested):
1. **Trade capital expense for variable expense** (CapEx → OpEx; pay only for what you use).
2. **Benefit from massive economies of scale** (AWS's scale = lower prices).
3. **Stop guessing capacity** (scale up/down on demand).
4. **Increase speed and agility** (resources in minutes, not weeks).
5. **Stop spending money running/maintaining data centers**.
6. **Go global in minutes** (deploy to multiple Regions easily).

Other benefits to recognize: **elasticity** (auto scale with demand), **high availability**,
**fault tolerance**, **agility**, **reliability**.

## 1.2 Cloud economics
- **CapEx** = upfront purchase (own servers). **OpEx** = ongoing pay-per-use (cloud).
- **TCO (Total Cost of Ownership)** — cloud usually lowers it vs on-prem (no hardware, power, cooling, staff).
- **Economies of scale** — AWS buys compute in bulk; you get the discount.
- **Right-sizing** — match instance size to actual need (cost optimization).

## 1.3 Cloud computing models (IaaS / PaaS / SaaS)
| Model | You manage | Example |
|---|---|---|
| **IaaS** (Infrastructure) | OS, apps, data | **EC2**, VPC |
| **PaaS** (Platform) | just your app + data | **Elastic Beanstalk**, RDS, Lambda |
| **SaaS** (Software) | nothing — just use it | **Amazon WorkMail**, Chime, QuickSight |

## 1.4 Deployment models
- **Cloud** (all-in on AWS) · **Hybrid** (cloud + on-prem, e.g. via Direct Connect / Outposts) ·
  **On-premises / private** (your own data center).

## 1.5 AWS Well-Architected Framework — **6 pillars** (memorize)
1. **Operational Excellence** — run & monitor, improve processes.
2. **Security** — protect data & systems.
3. **Reliability** — recover from failure, scale.
4. **Performance Efficiency** — use resources efficiently.
5. **Cost Optimization** — avoid unnecessary spend.
6. **Sustainability** — minimize environmental impact.

Mnemonic: **"OSR-PCS"** or remember *"Our Servers Run Pretty Cost-effectively & Sustainably."*

## 1.6 AWS Cloud Adoption Framework (CAF) — 6 perspectives
**Business, People, Governance** (business capabilities) + **Platform, Security, Operations**
(technical capabilities). Used to plan a cloud migration.

## Hands-on (cement it)
You already see these in action — connect the vocabulary:
```powershell
$env:AWS_PROFILE = "learn"
# Elasticity/agility: you launched + killed an EC2 in minutes (Project 02) = "stop guessing capacity"
# Global infra: pick a region with --region; that's "go global in minutes"
aws ec2 describe-regions --query "Regions[].RegionName" --output table
```
Open the **AWS Well-Architected Tool** in the console and start a (free) review of any
workload — see the 6 pillars turned into real questions.

## Cheat facts
- 6 advantages of cloud; 6 Well-Architected pillars; IaaS/PaaS/SaaS; CapEx vs OpEx; TCO.
- "Elasticity" = scale with demand; "Agility" = move fast; "Economies of scale" = cheaper at scale.

## Practice questions
**Q1.** A company wants to stop buying servers upfront and pay only for what it uses. Which
cloud benefit is this?
- A) Economies of scale  B) **Trade capital expense for variable expense** ✅  C) Go global in minutes  D) Elasticity

**Q2.** Which Well-Architected pillar focuses on minimizing environmental impact?
- A) Reliability  B) Cost Optimization  C) **Sustainability** ✅  D) Operational Excellence

**Q3.** Running an app on EC2 where AWS manages only the physical hardware is which model?
- A) SaaS  B) PaaS  C) **IaaS** ✅  D) FaaS

**Q4.** A solution that scales out when traffic spikes and scales in when it drops demonstrates:
- A) Fault tolerance  B) **Elasticity** ✅  C) Durability  D) Economies of scale

**Q5.** (multi) Which are technical perspectives of the AWS CAF? (choose 2)
- A) Business  B) **Platform** ✅  C) People  D) **Operations** ✅
