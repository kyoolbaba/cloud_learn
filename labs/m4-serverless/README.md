---
tags: [lab, m4-serverless]
aliases: [m4-serverless lab]
---
> [[labs/README|⬅ Labs]] | [[HOME|Home]] | [[STUDY_PLAN|Plan]]

# Module 4 — Serverless & containers in the cloud (hands-on lab)

Goal: run your container with **no VM to babysit**. Push the image to **ECR**, run
it on **Fargate**, and trigger that run from a **Lambda** (called by API Gateway or
an S3 upload). This replaces the "launch & manage an EC2 box" approach from M3.

```
S3 upload (job.json)  ─┐
API Gateway (HTTPS)   ─┼─►  Lambda  ──ecs.run_task──►  Fargate task (your container)
                       ┘     (glue)                      pulls image from ECR, runs worker.py
```

---

## Lab 1 — Push the image to ECR

```bash
source ../m3-aws/config.sh
# build the image first if you haven't (from labs/m2-docker): docker build -t forecast-app:0.1 .
./push_to_ecr.sh           # creates repo, logs in, tags, pushes; prints the image URI
```

## Lab 2 — Run it on Fargate

```bash
# one-time: a cluster + the task-execution role
aws ecs create-cluster --cluster-name forecast-cluster
# (create ecsTaskExecutionRole via console wizard, or the AWS-managed setup)

# register the task definition (edit ACCOUNT_ID/REGION + image URI first):
aws ecs register-task-definition --cli-input-json file://ecs_taskdef.json

# run it once, passing the job via env overrides:
export CLUSTER=forecast-cluster SUBNETS=subnet-xxx,subnet-yyy SECURITY_GROUP=sg-zzz
python run_fargate_task.py --job-id test1
# watch it: CloudWatch Logs -> /ecs/forecast-engine
```
(Use default-VPC public subnets + a security group with no inbound needed; the task
only makes *outbound* calls to S3/ECR.)

## Lab 3 — Lambda that starts the task

1. Set up the role from `lambda_policies.md` (`ecs:RunTask` + `iam:PassRole`).
2. Create the function:
```bash
zip lambda.zip lambda_start_fargate.py
aws lambda create-function --function-name start-forecast \
  --runtime python3.12 --handler lambda_start_fargate.handler \
  --role arn:aws:iam::ACCOUNT_ID:role/forecast-lambda-role \
  --zip-file fileb://lambda.zip \
  --environment "Variables={CLUSTER=forecast-cluster,TASKDEF=forecast-engine,SUBNETS=subnet-xxx,SECURITY_GROUP=sg-zzz}"
# test it:
aws lambda invoke --function-name start-forecast \
  --payload '{"job_id":"test2","bucket":"'"$FORECAST_BUCKET"'"}' out.json && cat out.json
```

## Lab 4 — API Gateway → Lambda (HTTPS entry the app calls)

Console: API Gateway → **HTTP API** → integrate with `start-forecast` Lambda →
route `POST /run`. You get an HTTPS URL. Then:
```bash
curl -X POST https://<api-id>.execute-api.$AWS_REGION.amazonaws.com/run \
  -H 'Content-Type: application/json' \
  -d '{"job_id":"viaapi","bucket":"'"$FORECAST_BUCKET"'"}'
```
This URL is exactly what the "Run in cloud" toggle will POST to.

## Lab 5 — S3 trigger (drop a file → auto-start)

Console: S3 bucket → Properties → Event notifications → prefix `jobs/`, suffix
`job.json`, destination = `start-forecast` Lambda. Now uploading a `job.json`
auto-launches a Fargate run — no API call needed.

---

**Checkpoint (M4 done):** image in ECR, runs on Fargate, triggered by a Lambda via
API call *and* by an S3 upload — zero servers managed. Tick the **Serverless** boxes
in `../../PROGRESS.md`.  → **Module 5 — Orchestration & scale.**

> 🧹 Cleanup: deregister task defs, delete the cluster, empty the bucket, delete the
> Lambda/API when done. Fargate only bills while tasks run, but tidy up anyway.
