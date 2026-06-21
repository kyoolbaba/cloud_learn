---
tags: [project, 09-stepfunctions-fanout]
aliases: [09-stepfunctions-fanout]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]] | [[PROGRESS|Tracker]]

# Project 09 — Fan-out & aggregate  🕸️

**Service:** Step Functions (`Map`) + Fargate · **Time:** 2–3h · **Cost:** pennies

## Goal
Run a state machine that splits a forecast into **N shards, runs them in parallel**
on Fargate, then aggregates the per-shard parquet files into one result. Watch it on
the visual execution graph. **This is the "2-hour job in 10 minutes" pattern.**

## Why (ties to capstone)
The capstone's big-job path. After this, you can articulate (and build) real parallel scale.

## Prereq
Project 07 done (image in ECR, cluster, task def, task role).

## Learn from
`../../labs/m5-orchestration/statemachine.asl.json` (the `Map` definition) +
`README.md` Lab 2–3.

## Build it
1. Make sure `forecast_engine.py` honors `SHARD` (the capstone version does — it
   writes `shard{i}.parquet`). Register a second task def `forecast-aggregate` whose
   command concatenates `shard*.parquet` → `forecast.parquet` (write a tiny
   `aggregate.py`, or reuse the engine with a flag).
2. Create a Step Functions role allowing `ecs:RunTask` + `iam:PassRole`, then:
   ```powershell
   cd ..\..\labs\m5-orchestration
   # edit statemachine.asl.json: cluster, subnets, sg, account/region
   aws stepfunctions create-state-machine --name forecast-fanout `
     --definition file://statemachine.asl.json `
     --role-arn arn:aws:iam::857810275001:role/forecast-sfn-role
   ```
3. Seed a job, then start an execution with a shard list:
   ```powershell
   aws stepfunctions start-execution `
     --state-machine-arn arn:aws:states:ap-south-1:857810275001:stateMachine:forecast-fanout `
     --input '{\"shards\":[{\"shard\":0},{\"shard\":1},{\"shard\":2},{\"shard\":3},{\"shard\":4}]}'
   ```
4. Open the execution in the console → **watch the graph**: 5 parallel branches, then
   Aggregate. Confirm one `forecast.parquet` in S3.

## ✅ Done when
- [ ] The visual graph shows N shards running concurrently, then an aggregate step
- [ ] N `shard*.parquet` files appear, then a single merged `forecast.parquet`
- [ ] You can explain `Map`, `MaxConcurrency`, and `runTask.sync` (wait-for-finish)
- [ ] You can compare this to the SQS approach (Project 08) and AWS Batch

## 🧹 Teardown
```powershell
aws stepfunctions delete-state-machine --state-machine-arn <arn>
aws s3 rm "s3://$env:FORECAST_BUCKET/jobs/" --recursive
# + tear down the ECS cluster/ECR if you're done with Project 07 too
```

## 🚀 Stretch
Add `Retry`/`Catch` to a shard and force one to fail — watch Step Functions retry it
automatically, then route to a "failed" branch. Free resilience.
