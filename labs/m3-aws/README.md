---
tags: [lab, m3-aws]
aliases: [m3-aws lab]
---
> [[labs/README|⬅ Labs]] | [[HOME|Home]] | [[STUDY_PLAN|Plan]]

# Module 3 — Cloud 101 + AWS core (hands-on lab)

> 💸 **Before anything:** set a **budget alarm** and never use the root account.
> Stop/terminate every instance after a lab. Tag everything `project=forecast`.

The mini-capstone here (`orchestrate_run.py`) is **80% of the final cloud toggle**.

**Install:** `pip install boto3` · install the AWS CLI · then `source config.sh`
(after `cp config.example.sh config.sh` and filling it in).

---

## Lab 1 — Account, MFA, IAM user, budget (console + script)

In the **AWS Console** (one-time, can't be fully scripted):
1. Create an account. **Enable MFA on the root user.** Then stop using root.
2. IAM → create an **admin user** (`milan-admin`), give it `AdministratorAccess`,
   enable MFA, log in as that user from now on.
3. Create an **access key** for it → you'll feed it to `aws configure`.

Then set the **budget alarm** (do it today):
```bash
python cloudwatch_alarm.py setup-topic you@example.com   # confirm the email link!
python cloudwatch_alarm.py billing 5                       # alert at $5
python cloudwatch_alarm.py billing 20                      # and $20
```

---

## Lab 2 — AWS CLI

```bash
aws configure            # paste access key + secret, region (ap-south-1), output json
aws sts get-caller-identity   # proves who you are -> your account + user ARN
```

---

## Lab 3 — S3 from CLI *and* boto3

```bash
# CLI:
aws s3 mb "s3://$FORECAST_BUCKET"
echo "hello cloud" > hello.txt
aws s3 cp hello.txt "s3://$FORECAST_BUCKET/data/hello.txt"
aws s3 ls "s3://$FORECAST_BUCKET/data/"

# boto3 (same operations, from Python — this is what the app uses):
python s3_lab.py create-bucket
python s3_lab.py upload hello.txt data/hello.txt
python s3_lab.py list data/
python s3_lab.py presign data/hello.txt 600     # open the URL in a browser
python s3_lab.py download data/hello.txt got.txt
```

---

## Lab 4 — EC2: launch → SSH → run → **stop → terminate**

First create (console or CLI) a **key pair** (`forecast-key`) and a **security
group** allowing SSH (22) **from your IP only**; put their names/ids in `config.sh`.
```bash
python ec2_lab.py latest-ami           # newest Ubuntu AMI (auto-looked-up)
python ec2_lab.py launch               # prints the public IP + SSH command
ssh -i forecast-key.pem ubuntu@<IP>    # log in; run `python3 --version`, poke around
python ec2_lab.py list                 # see its state
python ec2_lab.py stop  <id>           # pause billing (keeps disk)
python ec2_lab.py terminate <id>       # delete it entirely  <-- DO THIS
```
Watch Billing → Free Tier usage afterward so you trust the lifecycle.

---

## Lab 5 — user-data bootstrap

An instance that self-configures on boot (installs Python + deps, runs a script):
```bash
python ec2_lab.py launch --userdata worker_userdata.sh
# SSH in and watch:  tail -f /var/log/cloud-init-output.log
```
This is how the cloud worker configures itself with zero manual steps.

---

## Lab 6 — Least-privilege IAM policy

Create a dedicated `forecast-worker` user/role that can touch **only** your bucket
and start/stop **only** `project=forecast` instances — nothing else:
```bash
sed "s/BUCKET_NAME/$FORECAST_BUCKET/g" iam_forecast_worker_policy.json > /tmp/pol.json
aws iam create-user --user-name forecast-worker
aws iam put-user-policy --user-name forecast-worker \
    --policy-name forecast-min --policy-document file:///tmp/pol.json
```
Test that it **can't** do anything else (e.g. `aws s3 ls` on another bucket → denied).
**Also create an instance role/profile** (`forecast-worker-profile`) with S3 access so
the worker box needs no keys — put its name in `config.sh` as `IAM_INSTANCE_PROFILE`.

---

## Lab 7 — CloudWatch

```bash
python cloudwatch_alarm.py cpu <instance-id>     # CPU>80%/5min -> email
```
Then in the console: EC2 → Monitoring tab to see CPU/network metrics; Logs for
cloud-init output if you ship it.

---

## Lab 8 — 🏁 Mini-capstone: drive a full remote run from Python

This is the whole loop, end to end:
```bash
python orchestrate_run.py --n-series 50 --horizon 6
#   [1-2] upload job.json + worker.py
#   [3]   launch instance (user-data runs worker.py)
#   [4]   live progress bar from progress.json in S3
#   [5]   download result-<job>.parquet
#   [6]   terminate the instance
```
Read all four files together: `orchestrate_run.py` (laptop driver),
`worker_userdata.sh` (bootstrap), `worker.py` (the engine), `s3_lab.py`/`ec2_lab.py`
(the primitives). **The capstone replaces `main()` with a FastAPI route and
`worker.py` with your real forecast engine — that's it.**

---

**Checkpoint (M3 done):** stand up & tear down EC2, move data via S3 (CLI + boto3),
write/test a least-privilege policy, set alarms, and run `orchestrate_run.py`
green start-to-finish. Tick the **AWS core** boxes in `../../PROGRESS.md`.
→ **Module 4 — Serverless (ECR + Fargate + Lambda).**
