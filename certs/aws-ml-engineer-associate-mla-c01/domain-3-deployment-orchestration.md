---
tags: [cert/mla-c01, aws/ml, sagemaker, deployment, mlops]
cert: MLA-C01
domain: 3
aliases: [MLA-C01 Domain 3, Deployment and Orchestration of ML Workflows]
---
> [[domain-2-model-development|◀ Domain 2]] · [[MLA-C01|MLA-C01 Home]] · [[domain-4-monitoring-maintenance-security|Domain 4 · Monitor & Secure ▶]]

# Domain 3 — Deployment & Orchestration of ML Workflows (22%)

Getting a trained model into production the **right way**, and wiring repeatable train→deploy
pipelines. The deployment-option decision is the most-tested thing here.

## 3.1 The four inference options (memorize the decision)
| Option | Use when | Latency / shape |
|---|---|---|
| **Real-time endpoint** | steady traffic, low-latency online predictions | always-on, ms; you pay 24/7 |
| **Serverless Inference** | **intermittent/spiky** traffic, idle gaps, no infra mgmt | scales to zero; cold starts |
| **Asynchronous Inference** | **large payloads** (up to GB) or **long** processing; queue requests | near-real-time, autoscale to zero |
| **Batch Transform** | **score a whole dataset offline**, no persistent endpoint | bulk, cheapest for offline |

**For your forecasting:** scoring thousands of SKUs nightly = **Batch Transform** (this is the capstone). A live "forecast this one series now" call = real-time or serverless.

## 3.2 Endpoint capabilities
- **Auto-scaling** — scale instance count on a target metric (e.g. `InvocationsPerInstance`).
- **Multi-Model Endpoint (MME)** — many models behind one endpoint, loaded on demand → cheap when you have *many* models (e.g. one per region/SKU).
- **Multi-container / Inference Pipeline** — chain preprocessing → model → postprocessing in one endpoint (reuses your Feature transforms; kills train/serve skew).
- **Production variants** — multiple model versions on one endpoint with weighted traffic → **A/B testing** (see D4).

## 3.3 Infrastructure choices
- Pick instances by need: **CPU** (small/tabular), **GPU** (deep learning), **AWS Inferentia** (cheap high-throughput inference), **Graviton** (price/perf).
- Right-size and **auto-scale** rather than over-provision (Domain 4 cost theme).

## 3.4 Containers & artifacts
- **BYOC** — package your code (`statsforecast`) as a container in **Amazon ECR**; SageMaker runs it for training and/or inference.
- **Model artifact** (`model.tar.gz`) in S3 + image in ECR = a deployable model.

## 3.5 MLOps: pipelines, registry, CI/CD (the orchestration half)
| Need | Service |
|---|---|
| Repeatable **ML pipeline** (process → train → eval → register → deploy) | **SageMaker Pipelines** |
| Version + approve models before deploy | **SageMaker Model Registry** |
| Templated MLOps project + CI/CD (CodePipeline/CodeBuild) | **SageMaker Projects** |
| General workflow orchestration / triggers | **Step Functions**, **MWAA**, **EventBridge** |
| Infra as code | **CloudFormation / CDK** |

Pattern: **Pipelines** builds the model → registers a version in **Model Registry** (status *PendingManualApproval*) → on **approval**, CI/CD deploys to a real-time/batch endpoint. Re-runnable and auditable.

## 3.6 Deployment safety (intro; expanded in D4)
**Blue/green**, **canary**, and **shadow** deployments roll out new models gradually and let you roll back — never hard-swap a model in prod.

## Hands-on (cleanup included — endpoints bill 24/7!)
```powershell
$env:AWS_PROFILE = "learn"
# Batch-score a dataset with NO standing endpoint (cheapest for offline forecasting)
aws sagemaker create-transform-job --transform-job-name fc-batch `
  --model-name <model> --transform-input file://in.json --transform-output file://out.json `
  --transform-resources InstanceType=ml.m5.large,InstanceCount=1
# If you DO create a real-time endpoint, DELETE IT after testing — it charges while running:
aws sagemaker delete-endpoint --endpoint-name <ep>
aws sagemaker delete-endpoint-config --endpoint-config-name <cfg>
```

## Flashcards
- Batch Transform = offline whole-dataset scoring (no endpoint); Serverless = spiky/idle; Async = big payload/long; Real-time = steady low-latency.
- MME = many models, one endpoint (cost); Inference Pipeline = preprocess+model+postprocess in one.
- Production variants = A/B traffic split.
- Pipelines + Model Registry + Projects = CI/CD for ML; approve before deploy.
- ⚠️ Real-time endpoints bill 24/7 — delete them after labs.

## Practice questions
**Q1.** Score 5 million records once per night, no need for an always-on endpoint:
- A) Real-time endpoint  B) **Batch Transform** ✅  C) Async inference  D) MME

**Q2.** Traffic is rare and bursty; you don't want to manage or pay for idle servers:
- A) Real-time endpoint  B) **Serverless Inference** ✅  C) Batch Transform  D) EC2

**Q3.** Host hundreds of per-region models cost-effectively behind one endpoint:
- A) One endpoint each  B) **Multi-Model Endpoint** ✅  C) Batch Transform  D) Lambda each

**Q4.** Build a repeatable process→train→evaluate→register→deploy flow with approvals:
- A) Cron + scripts  B) **SageMaker Pipelines + Model Registry** ✅  C) Manual console  D) Athena

**Q5.** Requests carry 500 MB payloads and take minutes each:
- A) Real-time endpoint  B) **Asynchronous Inference** ✅  C) Serverless  D) Batch Transform only
