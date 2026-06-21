---
tags: [foundations, beginner, mlops, ml]
aliases: [MLOps Basics, ML Lifecycle, MLOps]
---
> [[05-lakehouse-basics|◀ Lakehouse]] · [[HOME|🏠 Home]] · [[STUDY_PLAN|Plan (M5.6)]] · [[PROGRESS|Tracker]] · [[07-finops-basics|FinOps ▶]]

# 06 · MLOps basics (from notebook to production)

## In plain English
**MLOps** = DevOps for machine learning. It's the discipline of taking a model from a notebook
to a **reliable, monitored, automatically-retrained production system**. A model isn't "done"
when it trains well — it's done when it's deployed, watched, and re-trained as the world changes.

> Analogy: training a model is *baking one cake*. MLOps is running the *bakery* — recipes (versioned),
> ovens (pipelines), quality checks (monitoring), and re-baking when ingredients change (retraining).

## Why it matters for your career
This is the **ML Engineer / MLOps Engineer** lane and your **bullseye** ([[MLA-C01]]). Your
forecasting work drifts hard around promotions/seasonality, so monitoring + retraining is exactly
what keeps it accurate. This is the difference between "I trained a model" and "I run a model in production."

## Key concepts (the lifecycle)
1. **Experiment tracking** — record every run's data, params, code, and metrics (so results are reproducible). Tools: **MLflow**, SageMaker Experiments.
2. **Feature store** — compute features once, reuse them in training *and* serving (kills train/serve skew). SageMaker Feature Store.
3. **Model registry** — versioned models with an **approval gate** before deploy. SageMaker Model Registry.
4. **Deployment options** — **batch inference** (score a whole dataset, no server), **real-time endpoint** (live low-latency), serverless/async (see [[MLA-C01]] Domain 3).
5. **Monitoring** — watch a live model for **data drift** (inputs changed) and **model drift** (accuracy decayed). SageMaker Model Monitor + CloudWatch.
6. **Retraining pipeline** — drift detected → trigger retrain → register → approve → redeploy. SageMaker Pipelines + Step Functions/EventBridge.
7. **Rollback** — instantly revert to the last good model if a new one misbehaves.
8. **CI/CD for ML** — the same pipeline idea as [[04-git-cicd-basics]], applied to models.

## Tools
SageMaker (Pipelines, Model Registry, Batch Transform, Endpoints, Model Monitor) · MLflow · GitHub Actions · Docker · ECR · S3 · CloudWatch · Step Functions

## Mini lab (full version = [[STUDY_PLAN|STUDY_PLAN Module 5.6]])
1. Train a **small model locally** (even sklearn on toy data).
2. **Track** the run's params + metrics (MLflow or a JSON log).
3. Save the **model artifact** to S3.
4. **Register** a model version (note its metrics + status).
5. Run **batch inference** over a dataset.
6. Deploy a **simple endpoint**; send one request.
7. **Log predictions** (input + output) for later monitoring.
8. Write **drift-monitoring** notes: what you'd watch and the alarm threshold.
9. Sketch a **retraining pipeline**: drift → retrain → register → approve → redeploy.

> 💸 Cost/safety: real-time **endpoints bill 24/7 — delete them after testing.** Prefer **Batch Transform** for offline scoring. Personal `learn` account only.

## ✅ Checkpoint
I can explain the **full ML lifecycle** — data → training → deployment → monitoring → retraining —
and which AWS service handles each stage.

---
Back to: [[HOME]] · [[START-HERE]] · [[STUDY_PLAN]] · [[PROGRESS]] · related cert: [[MLA-C01]]
