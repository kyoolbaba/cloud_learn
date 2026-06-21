---
tags: [project, 05-lambda-api]
aliases: [05-lambda-api]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]] | [[PROGRESS|Tracker]]

# Project 05 — Serverless API endpoint  ⚡

**Service:** Lambda + API Gateway · **Time:** 1–2h · **Cost:** free (1M calls/mo)

## Goal
Deploy a Lambda function behind a public **HTTPS URL** (API Gateway) that returns
JSON. Start with a "forecasting tip of the day", then make it take a `?name=` query
param. `curl` it from your laptop.

## Why (ties to capstone)
The "Run in cloud" toggle POSTs to an API Gateway URL that triggers a Lambda. This is
that entry point in miniature — once you can build one, wiring the real trigger is the same.

## Learn from
`../../labs/m4-serverless/lambda_start_fargate.py` (a real Lambda handler) and
`lambda_policies.md` (the execution role).

## Build it
1. Write `tip_lambda.py`:
   ```python
   import json, random
   TIPS = ["Theta is great for seasonal series.", "Always backtest with rolling CV.",
           "Intermittent demand? Try Croston/ADIDA.", "Scale features per series, not globally."]
   def handler(event, context):
       params = (event.get("queryStringParameters") or {})
       name = params.get("name", "forecaster")
       return {"statusCode": 200, "headers": {"Content-Type": "application/json"},
               "body": json.dumps({"hello": name, "tip": random.choice(TIPS)})}
   ```
2. Create an execution role (basic logging) and the function:
   ```powershell
   # trust policy file: { "Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}] }
   aws iam create-role --role-name tip-lambda-role --assume-role-policy-document file://trust.json
   aws iam attach-role-policy --role-name tip-lambda-role --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
   Compress-Archive tip_lambda.py lambda.zip -Force
   aws lambda create-function --function-name tip --runtime python3.12 --handler tip_lambda.handler `
     --role arn:aws:iam::857810275001:role/tip-lambda-role --zip-file fileb://lambda.zip
   ```
3. Add an **HTTP API** trigger (console is fastest: API Gateway → Create HTTP API →
   add integration = `tip` Lambda → route `GET /tip` → deploy). You get a URL.
4. Test:
   ```powershell
   curl "https://<api-id>.execute-api.ap-south-1.amazonaws.com/tip?name=milan"
   ```

## ✅ Done when
- [ ] `curl`ing the public URL returns your JSON
- [ ] The `?name=` param changes the response
- [ ] You can find the invocation logs in CloudWatch (`/aws/lambda/tip`)
- [ ] You can explain: Lambda = event-driven function; API Gateway = HTTPS → Lambda

## 🧹 Teardown
```powershell
aws lambda delete-function --function-name tip
# delete the HTTP API in the API Gateway console; delete the role when done
```

## 🚀 Stretch
Make the Lambda read the tips from a file in your S3 vault (Project 01) — now it
needs an extra IAM statement (`s3:GetObject`). Add it and watch a denied call start working.
