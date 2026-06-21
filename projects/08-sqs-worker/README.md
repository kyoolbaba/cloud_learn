---
tags: [project, 08-sqs-worker]
aliases: [08-sqs-worker]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]] | [[PROGRESS|Tracker]]

# Project 08 — Parallel job queue  📨

**Service:** SQS (+ dead-letter queue) · **Time:** 1–2h · **Cost:** free (1M req/mo)

## Goal
Enqueue 100 "shard" jobs, run **multiple consumer processes** that split the work,
then add a **dead-letter queue** and watch a poison message get parked after retries.

## Why (ties to capstone)
Queues decouple "create work" from "do work" and let many workers run in parallel —
the foundation of fanning a big forecast across machines.

## Learn from
`../../labs/m5-orchestration/sqs_producer.py` and `sqs_consumer.py`.

## Build it
1. Set env + enqueue:
   ```powershell
   $env:QUEUE_NAME="forecast-shards"
   cd ..\..\labs\m5-orchestration
   python sqs_producer.py 100
   ```
2. **Run 3 consumers in parallel** (3 separate PowerShell windows, or):
   ```powershell
   1..3 | ForEach-Object { Start-Process python -ArgumentList "sqs_consumer.py" }
   ```
   Watch them split the 100 messages — that's horizontal scaling.
3. **Dead-letter queue:** create a DLQ and attach a redrive policy
   (`maxReceiveCount: 3`) to the main queue (console: SQS → queue → Dead-letter queue).
4. **Force a failure:** edit `process()` in a copy of the consumer to `raise` on
   `shard == 7`. Run it. After 3 receives, message 7 lands in the DLQ instead of
   looping forever. Inspect it there.

## ✅ Done when
- [ ] 100 messages enqueued; 3 consumers drained them in parallel
- [ ] You can explain **visibility timeout** (why a pulled msg isn't deleted until you delete it)
- [ ] A poison message ends up in the DLQ after `maxReceiveCount` tries
- [ ] You understand at-least-once delivery (delete only after success)

## 🧹 Teardown
```powershell
aws sqs get-queue-url --queue-name forecast-shards    # then:
aws sqs delete-queue --queue-url <url>
aws sqs delete-queue --queue-url <dlq-url>
```

## 🚀 Stretch
Make each consumer actually write a `shard{i}.parquet` to S3, then a final script
concatenates them — you've now built fan-out + aggregate by hand (Project 09 does it
with Step Functions instead).
