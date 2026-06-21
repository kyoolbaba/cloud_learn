---
tags: [lab, m5-orchestration]
aliases: [m5-orchestration lab]
---
> [[labs/README|⬅ Labs]] | [[HOME|Home]] | [[STUDY_PLAN|Plan]]

# Module 5 — Orchestration & scale (hands-on lab)

Goal: turn one big forecast into **many parallel workers** and aggregate the
results — the "2 hours → 10 minutes" win. Three ways to do it; you'll feel the
trade-offs.

---

## Lab 1 — SQS: a decoupled job queue

```bash
source ../m3-aws/config.sh
python sqs_producer.py 100          # enqueue 100 shard messages
python sqs_consumer.py              # drains it; run 2-3 copies in parallel shells
                                    # and watch them split the work
```
Learn: **visibility timeout** (a pulled message is hidden, not deleted, until you
delete it → at-least-once delivery) and **dead-letter queues** (messages that fail
N times get parked for inspection). Add a DLQ in the console and force a failure.

---

## Lab 2 — Step Functions: a visual state machine

Deploy `statemachine.asl.json` (a **`Map`** state that fans N shards out to
parallel Fargate tasks, then an aggregate task):
```bash
# create a role that lets Step Functions call ecs:RunTask + iam:PassRole, then:
aws stepfunctions create-state-machine \
  --name forecast-fanout \
  --definition file://statemachine.asl.json \
  --role-arn arn:aws:iam::ACCOUNT_ID:role/forecast-sfn-role

aws stepfunctions start-execution \
  --state-machine-arn arn:aws:states:REGION:ACCOUNT_ID:stateMachine:forecast-fanout \
  --input '{"shards":[{"shard":0},{"shard":1},{"shard":2}]}'
```
Open the execution in the console → watch the **visual graph**: the Map branch
runs all shards concurrently (up to `MaxConcurrency`), each `runTask.sync` waits
for its Fargate task, then `Aggregate` runs. `Retry`/`Catch` give you free
resilience. **This is the cleanest expression of the fan-out pattern.**

---

## Lab 3 — Map fan-out, end to end

The conceptual core of the capstone's "big job" path:
```
split SKUs -> [shard0, shard1, ... shardN]   (the app builds this list)
   |  Step Functions Map (MaxConcurrency=10)
   v
shard0->Fargate  shard1->Fargate  ...  shardN->Fargate   (all at once)
   |
   v
Aggregate task: concat s3://.../shard*.parquet -> forecast.parquet
```
Each worker writes `shard{i}.parquet`; the aggregate task concatenates them.

---

## Lab 4 — AWS Batch (compare the effort)

```bash
# console one-time: Compute Environment (try Fargate Spot) + Job Queue + Job Definition
python batch_submit.py 100          # one 100-way ARRAY job
```
Each child reads `AWS_BATCH_JOB_ARRAY_INDEX` as its shard. Notice Batch manages the
fleet + Spot for you — less wiring than Step Functions, less visual control.

---

## Lab 5 — SageMaker Processing (the managed option)

Run `worker.py` as a SageMaker **Processing job** (input from S3, output to S3).
You get logging, autoscaling, and **Spot** (cheap, interruptible) for free. Good
when you want "managed run + track + autostop" without building orchestration.

---

## When to use what

| Tool | Best when |
|---|---|
| **Step Functions + Fargate Map** | you want a visual graph, retries/catch, modest fan-out, tight control |
| **AWS Batch** | pure "run N containers", large fleets, Spot, least wiring |
| **SageMaker Processing** | managed ML jobs, built-in tracking/autostop, don't want to manage infra |

**Checkpoint (M5 done):** fan a forecast across many parallel workers and aggregate
results; articulate Step Functions vs Batch vs SageMaker. Tick the **Serverless &
scale** boxes in `../../PROGRESS.md`.  → **Module 6 — Production hardening.**
