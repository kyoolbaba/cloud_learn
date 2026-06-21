---
tags: [project, 10-cloudwatch-autostop]
aliases: [10-cloudwatch-autostop]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]] | [[PROGRESS|Tracker]]

# Project 10 — Cost guardian  🛡️

**Service:** CloudWatch alarms + EventBridge-scheduled Lambda · **Time:** 1h · **Cost:** $0

## Goal
Build the safety net: (a) a CPU alarm that emails you, and (b) a scheduled Lambda
that **auto-terminates** any `project=forecast` instance running longer than a limit.
Test it by watching a box get killed.

## Why (ties to capstone)
The "hard max-runtime kill switch" — runaway-cost insurance so a hung forecast can't
quietly bill you for days.

## Learn from
`../../labs/m6-hardening/autostop_lambda.py` and `../../labs/m3-aws/cloudwatch_alarm.py`.

## Build it
1. **CPU alarm** on a running instance:
   ```powershell
   cd ..\..\labs\m3-aws
   python cloudwatch_alarm.py cpu <instance-id>
   ```
2. **Auto-stop Lambda:** deploy `autostop_lambda.py` with role allowing
   `ec2:DescribeInstances` + `ec2:TerminateInstances`. Set env `MAX_HOURS=2`.
   ```powershell
   cd ..\..\labs\m6-hardening
   Compress-Archive autostop_lambda.py autostop.zip -Force
   aws lambda create-function --function-name forecast-autostop --runtime python3.12 `
     --handler autostop_lambda.handler --role arn:aws:iam::857810275001:role/forecast-autostop-role `
     --zip-file fileb://autostop.zip --environment "Variables={MAX_HOURS=2}"
   ```
3. **Schedule it** every 15 min:
   ```powershell
   aws events put-rule --name forecast-autostop-15m --schedule-expression "rate(15 minutes)"
   # add the Lambda as the target + grant events.amazonaws.com permission to invoke it
   ```
4. **Test it fast:** set `MAX_HOURS=0` temporarily, launch a tagged instance, invoke
   the Lambda manually (`aws lambda invoke`), and watch the instance terminate.

## ✅ Done when
- [ ] CPU alarm exists and would email via SNS
- [ ] The autostop Lambda terminates an over-age `project=forecast` instance
- [ ] It's on a 15-minute schedule
- [ ] You can explain why this matters (forgotten/hung resources = the #1 bill cause)

## 🧹 Teardown
Leave the autostop + alarms ON — they're protective. Reset `MAX_HOURS=2` after testing.
```powershell
# only if you want them gone:
aws lambda delete-function --function-name forecast-autostop
aws events delete-rule --name forecast-autostop-15m
```

## 🚀 Stretch
Have the Lambda also delete S3 objects older than 7 days under `jobs/`, and post a
summary of what it cleaned to an SNS topic.
