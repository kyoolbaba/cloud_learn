---
tags: [cert/mla-c01, aws/ml, sagemaker, moc, bullseye]
cert: MLA-C01
level: associate
aliases: [MLA-C01, AWS ML Engineer Associate, bullseye cert]
---
> **Track notes:** [[domain-1-data-preparation|1 · Data Prep]] · [[domain-2-model-development|2 · Model Dev]] · [[domain-3-deployment-orchestration|3 · Deploy & Orchestrate]] · [[domain-4-monitoring-maintenance-security|4 · Monitor & Secure]] · [[MLA-C01-practice|🧪 Practice]] · [[MLA-C01-readiness|✅ Readiness]]
> **Up:** [[CERTS-MOC|All certs]] · [[CERT_ROADMAP|Roadmap]]

# AWS Certified Machine Learning Engineer – Associate (MLA-C01) — study track

🎯 **Your bullseye.** This is the cert that matches what you actually do — build, train, deploy,
and monitor ML models. It's **SageMaker end-to-end** plus MLOps. Your `statsforecast`/`mlforecast`
work, RMSE/MAPE evaluation, and the "Run in cloud" capstone all live inside this exam.

> ✅ **Verified 2026-06-21** against [aws.amazon.com](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/) + the official **MLA-C01 Exam Guide** (docs.aws.amazon.com): 65 Q · **130 min** · pass **720/1000** · **$150** · domains **28/26/22/24**. Still re-skim the current Exam Guide PDF before booking.

## Exam facts (verified 2026-06-21)
| | |
|---|---|
| Code | **MLA-C01** |
| Level | Associate |
| Questions | **65** (incl. **new formats**: ordering, matching, case study) |
| Time | **130 minutes** |
| Pass | **720 / 1000** (scaled) |
| Cost | **$150 USD** |
| Prereqs | none (recommended: CLF-C02 and/or AIF-C01 + ~1 yr ML experience) |
| Validity | 3 years |

## The 4 domains (memorize the weightings)
| # | Domain | Weight | File |
|---|---|---|---|
| 1 | Data Preparation for ML | **28%** | [[domain-1-data-preparation\|open]] |
| 2 | ML Model Development | **26%** | [[domain-2-model-development\|open]] |
| 3 | Deployment & Orchestration of ML Workflows | **22%** | [[domain-3-deployment-orchestration\|open]] |
| 4 | ML Solution Monitoring, Maintenance & Security | **24%** | [[domain-4-monitoring-maintenance-security\|open]] |

Unusually flat weighting — **all four matter**. Domain 1 (data prep) edges it.

## 4–6 week study plan (~1 hr/day)
| Week | Do |
|---|---|
| 1–2 | Domain 1 (Data Wrangler, Processing, Feature Store, Ground Truth, leakage, imbalance) |
| 3 | Domain 2 (built-in algos incl. **DeepAR**, training, AMT tuning, Autopilot, metrics) |
| 4 | Domain 3 (endpoints: real-time/serverless/async/batch, Pipelines, model registry, CI/CD) |
| 5 | Domain 4 (Model Monitor + drift, cost optimization, security, retraining) |
| 6 | `practice-questions.md` + official practice exam → `exam-readiness-checklist.md` → **book** |

## How this maps to YOUR work (use it as the running example)
- **Forecasting = regression / time-series** → SageMaker **DeepAR** (built-in), or bring your own `statsforecast` container.
- **Metrics you already use** (RMSE, MAE, **MAPE**) are Domain 2's regression metrics.
- **Feature engineering** (lags, rolling means, calendar features) → Domain 1 + **Feature Store**.
- **Offline scoring of thousands of SKUs** → **Batch Transform** (no endpoint); the **capstone** = exactly this.
- **"Run in cloud" toggle** → Domain 3 (deploy/orchestrate) + Domain 4 (monitor/secure/cost).

## What you've already built that maps here
| Already done | Covers (MLA-C01) |
|---|---|
| `labs/m5-orchestration` (Step Functions, SQS) | D3 (orchestration, fan-out scoring) |
| `projects/07-ecr-fargate`, `12-capstone` | D2/D3 (BYO container in ECR, batch scoring) |
| `projects/04-iam-least-privilege`, `10-cloudwatch-autostop` | D4 (execution roles, monitoring, cost kill-switch) |
| Your Parquet/feature pipeline | D1 (data prep, feature engineering) |

**New to add:** SageMaker (Studio, Data Wrangler, Processing, Training, AMT, Pipelines, Model Registry, Model Monitor, Clarify, Feature Store).

## Exam-day wrong-answer tells
- "huge dataset, score offline, no always-on endpoint" → **Batch Transform**.
- "spiky/intermittent traffic, no infra mgmt" → **Serverless Inference**; "large payload / long-running" → **Async Inference**; "steady low-latency" → **Real-time endpoint**.
- "time-series forecasting, built-in" → **DeepAR**; "tabular classification/regression, built-in" → **XGBoost / Linear Learner**; "anomaly detection" → **Random Cut Forest**.
- "automatically find best hyperparameters" → **Automatic Model Tuning (AMT)**; "build a model with little code" → **Autopilot**.
- "detect drift on a deployed model" → **Model Monitor**; "explain/bias" → **Clarify**.
- "cheap training, interruptible" → **Managed Spot Training**; "reuse features across teams" → **Feature Store**.
- "CI/CD for ML / repeatable train→deploy" → **SageMaker Pipelines + Model Registry**.
