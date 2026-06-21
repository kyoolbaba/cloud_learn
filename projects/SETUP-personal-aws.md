---
tags: [project, setup, aws]
aliases: [Setup Personal AWS, learn profile]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]]

# Setup — a separate personal AWS account for learning (do this first)

Your current `default` CLI profile points at a **shared company account** (account
`857810275001`, with Healthium production data + running instances). We will **not**
learn there. This guide creates an isolated personal account and a dedicated `learn`
CLI profile so every project runs safely, with zero chance of touching company resources.

> Why a separate account is the right call: the projects create *and delete* resources.
> In a shared/production account that's dangerous. In your own account you're admin,
> it's free-tier, and you literally cannot harm the company's data.

---

## Step 1 — Create the AWS account (browser, ~10 min)

1. Go to **https://signup.aws.amazon.com/**.
2. Use a **personal email** (different from your Healthium/work email).
3. Provide a payment method — **free-tier usage is ~$0**; the budget alarm in
   Project 00 is your guardrail. AWS requires a card on file even for free tier.
4. Verify your phone, choose the **Basic (free) support** plan.
5. You now have a brand-new account with its own 12-digit account id (**not** 857810275001).

## Step 2 — Secure the root user (one-time)

1. Sign in as **root** (the email you just used).
2. **IAM → enable MFA on root** (authenticator app). Then stop using root for daily work.

## Step 3 — Create an admin IAM user

The plan's design: your daily *learning* user is an admin; the *workloads* you build
run as least-privilege roles (that's what Project 04 teaches). The budget alarm +
autostop Lambda are the cost guardrails.

1. **IAM → Users → Create user**, name it `milan-learn`.
2. Attach policy **`AdministratorAccess`** directly.
3. Enable **MFA** for this user too.
4. **Create access key** → "Command Line Interface (CLI)" → copy the **Access key ID**
   and **Secret access key** (you see the secret only once).

## Step 4 — Configure a dedicated `learn` CLI profile

This adds a *separate* profile alongside your work `default` — it does not touch it.
```powershell
aws configure --profile learn
#   AWS Access Key ID     : <paste the milan-learn key>
#   AWS Secret Access Key : <paste the secret>
#   Default region name   : ap-south-1
#   Default output format : json
```

## Step 5 — Verify you're in the NEW account ✅

```powershell
aws sts get-caller-identity --profile learn
```
The `Account` must be your **new** id and the Arn must say `user/milan-learn`.
**If it shows 857810275001, stop** — the profile is wrong.

## Step 6 — The session habit that keeps you safe

At the start of **every** learning session, set the profile for the whole terminal
and confirm the account, before running any project command:
```powershell
$env:AWS_PROFILE = "learn"
aws sts get-caller-identity --query Account --output text   # must be the NEW account id
```
Every project brief assumes `AWS_PROFILE=learn` is set. With it set, the CLI and
boto3 both use the personal account automatically — no `--profile` flag needed each time.

---

## When you're done
Run `aws sts get-caller-identity --profile learn` and tell me the result (the account
id is fine to share; it's not a secret). I'll confirm it's isolated, then we do
**Project 00 (budget alarm)** live — safely — in your own account.
