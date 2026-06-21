---
tags: [project, 04-iam-least-privilege]
aliases: [04-iam-least-privilege]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]] | [[PROGRESS|Tracker]]

# Project 04 — Least-privilege key (prove it can't escape)  🔑

**Service:** IAM (users, policies, profiles) · **Time:** 1–2h · **Cost:** $0

## Goal
Create a `forecast-worker` IAM user that can touch **only** your one bucket and
start/stop **only** `project=forecast` instances. Then **prove** it's locked down by
trying — and failing — to do anything else.

## Why (ties to capstone)
The worker and the app must run with minimum permissions, so a leaked key can't nuke
your account. Writing and *testing* a tight policy is a core cloud skill.

## Learn from
`../../labs/m3-aws/iam_forecast_worker_policy.json` — the ready-made least-privilege policy.

## Build it
1. Create the user + the policy (replace the bucket name):
   ```powershell
   cd ..\..\labs\m3-aws
   (Get-Content iam_forecast_worker_policy.json) -replace 'BUCKET_NAME', $env:FORECAST_BUCKET | Set-Content pol.json
   aws iam create-user --user-name forecast-worker
   aws iam put-user-policy --user-name forecast-worker --policy-name forecast-min --policy-document file://pol.json
   ```
2. Give it access keys and make a **second CLI profile**:
   ```powershell
   aws iam create-access-key --user-name forecast-worker     # note AccessKeyId + SecretAccessKey
   aws configure --profile worker                            # paste them; region ap-south-1
   ```
3. **Prove the allow-list works** (these should SUCCEED):
   ```powershell
   aws s3 ls "s3://$env:FORECAST_BUCKET" --profile worker
   ```
4. **Prove the deny works** (these should FAIL with AccessDenied):
   ```powershell
   aws s3 ls --profile worker                                # list ALL buckets -> denied
   aws ec2 describe-instances --profile worker               # not in policy -> denied
   aws iam list-users --profile worker                       # definitely denied
   ```

## ✅ Done when
- [ ] `forecast-worker` can read/write its one bucket
- [ ] It is **denied** on other buckets, EC2 describe (untagged), and IAM
- [ ] You can read the policy JSON and explain each statement (Effect/Action/Resource/Condition)
- [ ] You understand the `aws:ResourceTag/project` condition that scopes EC2 access

## 🧹 Teardown
Keep the user for later projects, **but rotate/disable the key when idle**:
```powershell
aws iam list-access-keys --user-name forecast-worker
aws iam update-access-key --user-name forecast-worker --access-key-id <id> --status Inactive
```

## 🚀 Stretch
Convert the user into a **role** the EC2 instance assumes (an *instance profile*), so
the worker needs **no keys at all** — the gold-standard pattern. (You'll use this in Project 07.)
