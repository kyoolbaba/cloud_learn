---
tags: [project, 07-ecr-fargate]
aliases: [07-ecr-fargate]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]] | [[PROGRESS|Tracker]]

# Project 07 — Run your container in the cloud  📦☁️

**Service:** ECR + ECS/Fargate + CloudWatch Logs · **Time:** 2–3h · **Cost:** pennies (tear down)

## Goal
Take the forecast container, push it to **ECR**, and run it on **Fargate** (no server
to manage). It writes a result to your S3 bucket; you read its logs in CloudWatch.

## Why (ties to capstone)
This IS the capstone's compute: a container running `forecast_engine.py` on Fargate,
triggered on demand. After this project, the worker is "real".

## Prereq
Docker Desktop running. The sample image from `../../labs/m2-docker` (or build the
capstone engine in `../../labs/capstone`).

## Learn from
`../../labs/m4-serverless/` — `push_to_ecr.sh`, `ecs_taskdef.json`, `run_fargate_task.py`.
`../../labs/capstone/forecast_engine.py` + its `Dockerfile`.

## Build it
1. **Build + push the engine image to ECR:**
   ```powershell
   cd ..\..\labs\capstone
   docker build -t forecast-engine:0.1 .
   $acct = aws sts get-caller-identity --query Account --output text
   $reg = "$acct.dkr.ecr.ap-south-1.amazonaws.com"
   aws ecr create-repository --repository-name forecast-engine 2>$null
   aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin $reg
   docker tag forecast-engine:0.1 "$reg/forecast-engine:0.1"
   docker push "$reg/forecast-engine:0.1"
   ```
2. **Task role + execution role:** create `forecast-task-role` (S3 access to your
   bucket — reuse Project 04's policy) and the standard `ecsTaskExecutionRole`
   (console wizard creates it). 
3. **Register the task def** (`ecs_taskdef.json`, with ACCOUNT_ID/REGION/image filled in)
   and create a cluster:
   ```powershell
   aws ecs create-cluster --cluster-name forecast-cluster
   aws ecs register-task-definition --cli-input-json file://..\m4-serverless\ecs_taskdef.json
   ```
4. **Run the task**, passing a job id + bucket (need default-VPC subnet ids + a SG):
   ```powershell
   cd ..\m4-serverless
   $env:CLUSTER="forecast-cluster"; $env:SUBNETS="subnet-xxx,subnet-yyy"; $env:SECURITY_GROUP="sg-zzz"
   # seed a job first (so the engine has something to read):
   python ..\m3-aws\s3_lab.py upload ..\capstone\job.example.json jobs/test1/job.json
   python run_fargate_task.py --job-id test1
   ```
5. Watch **CloudWatch Logs → /ecs/forecast-engine**; confirm `forecast.parquet`
   landed in `s3://bucket/jobs/test1/`.

## ✅ Done when
- [ ] Your image is in ECR (`aws ecr list-images --repository-name forecast-engine`)
- [ ] A Fargate task ran to completion (no EC2 you manage)
- [ ] Its logs are visible in CloudWatch
- [ ] `forecast.parquet` is in S3
- [ ] You can explain ECR vs Docker Hub, and Fargate vs EC2

## 🧹 Teardown
```powershell
aws ecs delete-cluster --cluster forecast-cluster
aws ecr delete-repository --repository-name forecast-engine --force
aws s3 rm "s3://$env:FORECAST_BUCKET/jobs/" --recursive
```

## 🚀 Stretch
Give the task role **no S3 keys** — it already uses the role, not keys. Confirm the
container reaches S3 purely via the task role (the secure pattern).
