---
tags: [project, 00-safety-budget]
aliases: [00-safety-budget]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]] | [[PROGRESS|Tracker]]

# Project 00 — Lock the account + budget alarm  🔒

**Service:** AWS Budgets, IAM, CloudWatch · **Time:** 30 min · **Cost:** $0

> Do this **before** any other project. It's the seatbelt.

## Goal
Guarantee you'll be emailed long before any surprise bill, and confirm you're not
flying as root.

## Build it

**1. Confirm you're an IAM user, not root** (already true for you — `user/milan`):
```powershell
aws sts get-caller-identity      # Arn should say :user/...  NOT :root
```
If you ever see `root`, stop and create an IAM admin user instead.

**2. Enable MFA on the root user** (console, one-time): IAM → root user → "Assign MFA".
Then lock the root credentials away and never use them daily.

**3. Set an AWS Budget at $5 and $10** (console is easiest):
Billing → **Budgets** → Create budget → *Zero spend* or *Monthly cost* →
amount `5` → alert email = yours. Repeat for `10`. You'll get an email if you cross them.

**4. Set a CloudWatch billing alarm too** (belt + suspenders), using the lab script:
```powershell
cd ..\..\labs\m3-aws
python cloudwatch_alarm.py setup-topic your-email@example.com   # CONFIRM the email link!
python cloudwatch_alarm.py billing 5
python cloudwatch_alarm.py billing 10
```
> Billing metrics live in `us-east-1` — the script handles that automatically.
> You must also enable "Receive Billing Alerts" once: Billing → Billing Preferences.

## ✅ Done when
- [ ] `get-caller-identity` shows an IAM user (✅ already)
- [ ] Root has MFA; root keys are not in use
- [ ] AWS Budget(s) created at $5 / $10 with your email
- [ ] You received + **confirmed** the SNS subscription email
- [ ] A billing alarm shows in CloudWatch (us-east-1)

## 🧹 Teardown
Nothing to tear down — leave these on forever.

## 🚀 Stretch
Add a $20 budget scoped to tag `project=forecast` so you can see exactly what this
learning is costing.
