---
tags: [cert/mla-c01, aws/ml, sagemaker, readiness]
cert: MLA-C01
aliases: [MLA-C01 Readiness Checklist]
---
> [[MLA-C01|⬅ MLA-C01 Home]] · [[MLA-C01-practice|🧪 Practice Exam]]

# MLA-C01 — exam-readiness checklist

Book only when you can tick **every** box. This is your bullseye — aim to *understand*, not memorize.

## Domain 1 — Data preparation
- [ ] Data Wrangler vs Processing vs Feature Store vs Ground Truth — when each
- [ ] Feature engineering: scaling, encoding, missing values, outliers, datetime/lag features
- [ ] Class imbalance fixes (SMOTE/weights) + why accuracy misleads
- [ ] Correct splitting; **chronological** split for time-series; avoid data leakage
- [ ] Pipe/FastFile input modes; efficient formats (RecordIO/Parquet)

## Domain 2 — Model development
- [ ] Pick built-in algo: DeepAR (forecasting), XGBoost/Linear Learner (tabular), RCF (anomaly), K-Means
- [ ] Training: Managed Spot + checkpointing, script mode / BYOC, distributed training
- [ ] AMT (hyperparameter tuning) vs Autopilot (AutoML); hyperparameter vs parameter
- [ ] Metrics: RMSE/MAE/MAPE/R² (regression) and precision/recall/F1/AUC + confusion matrix
- [ ] Diagnose over/underfitting; regularization; cross-validation

## Domain 3 — Deployment & orchestration
- [ ] The 4 inference options (real-time / serverless / async / batch) — pick from a scenario
- [ ] MME, inference pipelines, production variants, auto-scaling
- [ ] BYO container → ECR; model artifact in S3
- [ ] SageMaker Pipelines + Model Registry + Projects (CI/CD); approval gates
- [ ] Step Functions / MWAA / EventBridge orchestration; CFN/CDK IaC

## Domain 4 — Monitoring, maintenance & security
- [ ] Model Monitor 4 types + baseline + Data Capture → CloudWatch alarms
- [ ] Drift → EventBridge → retrain Pipeline loop
- [ ] A/B (variants) vs shadow vs blue/green/canary
- [ ] Cost: right-size, auto-scale/scale-to-zero, MME, Spot, Batch, delete idle endpoints
- [ ] Security: least-privilege execution role, VPC isolation, KMS, Macie, Secrets Manager
- [ ] Governance: Model Registry approval, Model Cards, lineage

## Practice gate
- [ ] Scored **≥ 18/25** on [[MLA-C01-practice|the mock]]
- [ ] Took the official AWS Skill Builder **MLA-C01 practice exam**
- [ ] Ran one real SageMaker flow end-to-end (train → register → Batch Transform) in `learn`
- [ ] Comfortable with the **new question formats** (ordering, matching, case study)

## Logistics
- [ ] Confirmed format on the **official MLA-C01 Exam Guide PDF**
- [ ] Registered (Pearson VUE); know cost ($150), pass (720/1000), **130 min** (verified 2026-06-21)

## Free official resources
- **AWS Skill Builder** — "Machine Learning Engineer – Associate" learning plan + official practice set
- **Amazon SageMaker Developer Guide** — Data Wrangler, Training, AMT, Pipelines, Model Monitor, Clarify
- **AWS Workshops** (workshops.aws) — SageMaker Immersion Day, MLOps workshops
- **Machine Learning Lens** (Well-Architected) + **MLA-C01 Exam Guide** PDF

When every box is ticked → **book it.** This completes the core data-science ladder
([[AIF-C01|AIF-C01]] → [[DEA-C01|DEA-C01]] → **MLA-C01**). See [[CERT_ROADMAP]] for optional depth → [[OPTIONAL-CERTS]] (SAA-C03 / Terraform / Databricks). Note: MLS-C01 and DP-100 are retired.
