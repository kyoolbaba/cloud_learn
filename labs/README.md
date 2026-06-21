---
tags: [labs, moc, hands-on]
aliases: [Labs, Labs MOC]
---
> [[HOME|🏠 Home]] · [[STUDY_PLAN|Study plan]] · [[projects/README|Projects ▶]] · [[PROGRESS|Tracker]]
>
> **Modules:** [[labs/m0-linux/README|M0 Linux]] · [[labs/m1-networking/README|M1 Networking]] · [[labs/m2-docker/README|M2 Docker]] · [[labs/m3-aws/README|M3 AWS core]] · [[labs/m4-serverless/README|M4 Serverless]] · [[labs/m5-orchestration/README|M5 Orchestration]] · [[labs/m6-hardening/README|M6 Hardening]] · [[labs/capstone/README|🏁 Capstone]]

# Labs — ready-made code for the Cloud & Infrastructure plan

This folder holds **working, ready-to-run code** for every module in
`../STUDY_PLAN.md`. You learn by *running* and *reading* the code (the comments
explain the "why"), not by typing it from scratch.

## The one-line story of the whole plan

> Everything here builds toward **one feature**: a **"Run in cloud" toggle** in your
> forecasting dashboard. You flip it, thousands of SKUs forecast on rented cloud
> hardware while a live progress bar ticks, and the results come back as tables —
> on a backend you can stand up and tear down with one command.

Each module is a Lego brick for that feature:

| Module | You learn | Brick it adds to the capstone | Ready-made code |
|---|---|---|---|
| **M0 Linux** | the OS the cloud runs on | the worker is a Linux box | `m0-linux/scripts/` |
| **M1 Networking** | ports, HTTP, TLS, SSH, proxy | app ⇄ worker talk over the network | `m1-networking/` |
| **M2 Docker** | package app + deps into an image | the worker *is* a container | `m2-docker/` |
| **M3 AWS core** | IAM, S3, EC2, CloudWatch, boto3 | drive a remote run from Python | `m3-aws/` |
| **M4 Serverless** | ECR, Fargate, Lambda, API GW | run the container with no VM to babysit | `m4-serverless/` |
| **M5 Orchestration** | SQS, Step Functions, Batch | fan 1 big job into N parallel workers | `m5-orchestration/` |
| **M6 Hardening** | Terraform, secrets, VPC, auto-stop | one-command stand-up/tear-down, safe | `m6-hardening/` |
| **Capstone** | wire it all together | the actual toggle | `capstone/` |

**Do M0–M2 first:** they run entirely on your laptop (WSL2 + Docker) with **zero
cloud cost**. By the end of M2 you can containerize and run the forecasting app —
the "env-parity" win that makes the cloud step safe.

**M3–M6 + capstone are written as templates.** They're real, ready-made code, but
they read your account-specific values (bucket, region, key pair, security group,
account id) from `m3-aws/config.sh`. Before running any cloud lab:
1. Create an AWS account, enable root MFA, make an IAM admin user, **set a budget alarm.**
2. `cd m3-aws && cp config.example.sh config.sh`, fill in your values, `source config.sh`.
3. `pip install boto3` and install the AWS CLI; `aws configure`.
Then the boto3 scripts, Terraform, and Lambdas all run against *your* resources.
⚠️ **Cost discipline:** stop/terminate after every lab; the `autostop` Lambda in M6
is your safety net. Never commit `config.sh` or access keys.

## How to use this

1. Do the modules in order. Each has a `README.md` = the guided lab.
2. Run everything inside **WSL2 Ubuntu** (M0–M1) or with **Docker Desktop** (M2).
3. Tick boxes in `../PROGRESS.md` as you finish.

### ⚠️ One-time setup: fix line endings

These files live on the Windows filesystem, so shell scripts may have Windows
(`\r\n`) line endings that break bash. Normalize them once, from Ubuntu:

```bash
cd /mnt/c/Users/MilanGowdaJP/Documents/EXPERIMENTS/Learn/labs
sudo apt install -y dos2unix
find . -name "*.sh" -print0 | xargs -0 dos2unix
```
(If a script ever errors with `bad interpreter: ...^M`, that's the fix.)
