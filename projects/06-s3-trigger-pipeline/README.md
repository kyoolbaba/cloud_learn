---
tags: [project, 06-s3-trigger-pipeline]
aliases: [06-s3-trigger-pipeline]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]] | [[PROGRESS|Tracker]]

# Project 06 — Auto-process uploads  📥

**Service:** S3 event notifications → Lambda · **Time:** 1–2h · **Cost:** free

## Goal
Drop a CSV into `s3://bucket/incoming/` and have a Lambda **fire automatically**,
read the row count, and write a `summary.json` to `s3://bucket/processed/`. A real
event-driven pipeline — no polling, no servers.

## Why (ties to capstone)
"Drop a `job.json` → a forecast run auto-starts" is this exact pattern. Master the
S3→Lambda trigger here and the capstone's auto-start is trivial.

## Learn from
Project 05 (Lambda basics) + `../../labs/m4-serverless/README.md` Lab 5 (S3 trigger).

## Build it
1. Write `process_lambda.py`:
   ```python
   import json, boto3, urllib.parse
   s3 = boto3.client("s3")
   def handler(event, context):
       rec = event["Records"][0]["s3"]
       bucket = rec["bucket"]["name"]
       key = urllib.parse.unquote_plus(rec["object"]["key"])
       body = s3.get_object(Bucket=bucket, Key=key)["Body"].read().decode()
       rows = max(body.count("\n"), 1) - 1          # minus header
       out_key = key.replace("incoming/", "processed/") + ".summary.json"
       s3.put_object(Bucket=bucket, Key=out_key,
                     Body=json.dumps({"source": key, "rows": rows}).encode())
       return {"rows": rows, "wrote": out_key}
   ```
2. Deploy it (like Project 05) with a role that also allows `s3:GetObject`/`s3:PutObject`
   on your bucket.
3. Wire the trigger (console): S3 bucket → Properties → Event notifications →
   prefix `incoming/`, suffix `.csv`, destination = `process_lambda`.
4. Test:
   ```powershell
   "a,b`n1,2`n3,4`n5,6" | Set-Content sample.csv
   aws s3 cp sample.csv "s3://$env:FORECAST_BUCKET/incoming/sample.csv"
   Start-Sleep 5
   aws s3 ls "s3://$env:FORECAST_BUCKET/processed/"          # the summary appeared
   ```

## ✅ Done when
- [ ] Uploading a CSV to `incoming/` auto-creates a summary in `processed/`
- [ ] You can read the Lambda's CloudWatch logs showing it fired
- [ ] You understand the S3 event payload shape (`event["Records"][0]["s3"]`)
- [ ] You see why the Lambda needs both `GetObject` (read) and `PutObject` (write)

## 🧹 Teardown
```powershell
aws lambda delete-function --function-name process_lambda   # + remove the S3 event notification
aws s3 rm "s3://$env:FORECAST_BUCKET/incoming/" --recursive
aws s3 rm "s3://$env:FORECAST_BUCKET/processed/" --recursive
```

## 🚀 Stretch
Avoid infinite loops: what happens if the Lambda wrote back into `incoming/`? Explain
why prefix separation (`incoming/` vs `processed/`) matters for S3-triggered functions.
