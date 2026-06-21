---
tags: [cert/mla-c01, aws/ml, sagemaker, monitoring, security, cost]
cert: MLA-C01
domain: 4
aliases: [MLA-C01 Domain 4, ML Monitoring Maintenance and Security]
---
> [[domain-3-deployment-orchestration|◀ Domain 3]] · [[MLA-C01|MLA-C01 Home]] · [[MLA-C01-practice|Practice Exam ▶]]

# Domain 4 — ML Solution Monitoring, Maintenance & Security (24%)

Keeping a deployed model healthy, cheap, and secure — plus when/how to retrain.

## 4.1 Monitoring with SageMaker Model Monitor (know the 4 types)
| Monitor type | Catches |
|---|---|
| **Data quality** | input drift — live feature stats vs a **baseline** (nulls, ranges, distribution) |
| **Model quality** | prediction accuracy decay vs ground-truth labels |
| **Bias drift** | fairness shifting over time (with Clarify) |
| **Feature attribution drift** | which features drive predictions changing (with Clarify) |

It captures live data (**Data Capture**), compares to a baseline on a schedule, and emits **CloudWatch** metrics → **alarms**. **Clarify** provides bias + explainability in production.

## 4.2 Drift → retrain loop (the maintenance pattern)
Data/concept **drift** (the world changed; e.g. demand pattern shifts) degrades models. Pattern:
**Model Monitor detects drift → CloudWatch alarm → EventBridge → trigger a SageMaker Pipeline to retrain → register → approve → redeploy.** Automate retraining instead of waiting for complaints.

## 4.3 Safe rollout & testing in production
- **A/B testing** via **production variants** (split traffic between model v1/v2, compare metrics).
- **Shadow testing** — send a copy of live traffic to the new model **without** serving its responses; compare safely.
- **Blue/green** + **canary** — shift traffic gradually; **roll back** instantly if metrics drop.

## 4.4 Cost optimization (explicitly tested)
- **Right-size** instances; **auto-scale** to demand; **scale to zero** with Serverless/Async when idle.
- **Multi-Model Endpoints** to share infra across many models.
- **Managed Spot Training** for training; **Savings Plans** for steady inference.
- **Batch Transform** instead of an always-on endpoint for offline scoring.
- Delete idle endpoints; alarm on spend (ties to your `projects/10-cloudwatch-autostop`).

## 4.5 Security (reuses CLF-C02 D2 + [[domain-5-security-compliance-governance|AIF-C01 D5]])
- **IAM execution role** — the role SageMaker assumes; scope it **least privilege** (only the S3 prefixes/ECR/KMS it needs). **SageMaker Role Manager** helps build these.
- **Network isolation** — run training/endpoints in a **VPC** (no internet), use **VPC endpoints/PrivateLink**; `EnableNetworkIsolation` blocks outbound from the container.
- **Encryption** — **KMS** for S3 data, EBS volumes, model artifacts; TLS in transit.
- **Secrets** in Secrets Manager; never hardcode. **Macie** to find PII in training data.

## 4.6 Governance & lineage
- **Model Registry** approval gates; **Model Cards** document intended use/metrics/limits; **ML lineage tracking** records which data+code+params produced a model (audit + reproducibility).

## How this is real for you
Your forecasts drift hard around promotions/seasonality. The MLA design: **Model Monitor** on input + accuracy, **EventBridge → Pipeline** auto-retrain when MAPE degrades, **Batch Transform** for nightly scoring, a tight **execution role** over only the Healthium S3 prefix, **KMS** on the data, and a **CloudWatch budget alarm** kill-switch.

## Hands-on (`$env:AWS_PROFILE="learn"` — monitoring + a cost kill-switch)
```powershell
$env:AWS_PROFILE = "learn"
# A CloudWatch alarm on endpoint invocations = runaway-cost guard (ties to projects/10):
aws cloudwatch put-metric-alarm --alarm-name ml-endpoint-invocations-high `
  --namespace AWS/SageMaker --metric-name Invocations --statistic Sum `
  --period 300 --threshold 100000 --comparison-operator GreaterThanThreshold `
  --evaluation-periods 1 --alarm-description "Alert if an endpoint is hammered"
# Least-privilege check: what can a SageMaker execution role actually do?
aws iam list-attached-role-policies --role-name <YourSageMakerExecutionRole>
```
**Cleanup:** `aws cloudwatch delete-alarms --alarm-names ml-endpoint-invocations-high`. (For drift: enable **Data Capture** on the endpoint config + a Model Monitor schedule in the console — then delete the endpoint; it bills 24/7.)

## Flashcards
- Model Monitor types: data quality, model quality, bias drift, feature attribution drift (needs a baseline + Data Capture).
- Drift → CloudWatch alarm → EventBridge → retrain Pipeline.
- A/B = production variants; shadow = mirror traffic, don't serve; blue/green+canary = safe rollout + rollback.
- Cost: right-size, auto-scale/scale-to-zero, MME, Spot training, Batch over endpoint, delete idle endpoints.
- Security: least-privilege execution role, VPC isolation, KMS, Macie, Secrets Manager.

## Practice questions
**Q1.** Detect that live input feature distributions have drifted from training:
- A) Clarify only  B) **SageMaker Model Monitor (data quality)** ✅  C) CloudTrail  D) Autopilot

**Q2.** Test a new model on real traffic **without** exposing its responses to users:
- A) A/B variants  B) **Shadow testing** ✅  C) Batch Transform  D) Canary at 100%

**Q3.** Automatically retrain when accuracy decays. Best wiring?
- A) Manual monthly  B) **Model Monitor → CloudWatch alarm → EventBridge → SageMaker Pipeline** ✅  C) Bigger instance  D) Delete endpoint

**Q4.** Cheapest way to keep many rarely-used models servable:
- A) One endpoint each  B) **Multi-Model Endpoint** ✅  C) Real-time per model  D) EC2 fleet

**Q5.** Restrict a training job to only its S3 prefix and block internet egress:
- A) Admin role + public subnet  B) **Least-privilege execution role + VPC + network isolation** ✅  C) Root keys  D) Open security group
