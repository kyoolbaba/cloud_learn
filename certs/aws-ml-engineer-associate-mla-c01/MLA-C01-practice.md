---
tags: [cert/mla-c01, aws/ml, sagemaker, practice-exam]
cert: MLA-C01
aliases: [MLA-C01 Practice Exam, MLA-C01 Mock]
---
> [[MLA-C01|⬅ MLA-C01 Home]] · [[MLA-C01-readiness|Readiness Checklist ➡]]

# MLA-C01 — mixed mock exam (25 Q)

Domain-weighted (Data Prep 28% · Model Dev 26% · Deploy 22% · Monitor/Secure 24%).
One ~35-min sitting, then review every miss. Target ≥ 72% (18/25).

1. A forecasting model trained on a random split looks perfect but fails live. Cause?
   A) Too few epochs  B) **Temporal data leakage (split chronologically)**  C) Wrong region  D) No GPU

2. Avoid train/serve skew by reusing the same feature definitions in both:
   A) Two scripts  B) **SageMaker Feature Store**  C) DynamoDB  D) Athena

3. Fraud data is 99.5% negatives. Best handling?
   A) Optimize accuracy  B) **Resample/SMOTE + class weights + precision/recall/F1**  C) Drop positives  D) Label-encode target

4. Low-code visual data prep with 300+ transforms:
   A) Processing  B) **Data Wrangler**  C) Ground Truth  D) Clarify

5. Stream a huge S3 training set without downloading it all:
   A) File mode  B) **Pipe/FastFile mode**  C) EFS only  D) Batch Transform

6. Label a large set of raw images (human + auto-labeling):
   A) Clarify  B) **SageMaker Ground Truth**  C) Data Wrangler  D) Macie

7. Pre-training dataset bias metrics:
   A) Model Monitor  B) **SageMaker Clarify**  C) Debugger  D) Autopilot

8. Built-in algorithm for time-series forecasting:
   A) XGBoost  B) **DeepAR**  C) K-Means  D) BlazingText

9. Automatically find the best hyperparameters to minimize validation RMSE:
   A) Autopilot  B) **Automatic Model Tuning (AMT)**  C) Model Monitor  D) Clarify

10. Missing a true fraud is far worse than a false alarm. Optimize:
    A) Precision  B) Accuracy  C) **Recall**  D) RMSE

11. Train 0.98 / validation 0.61. This is:
    A) Underfitting  B) **Overfitting**  C) Leakage fixed  D) Good generalization

12. Cut cost ~90% on a long interruption-tolerant training job:
    A) Bigger instance  B) **Managed Spot Training + checkpointing**  C) Real-time endpoint  D) MME

13. Report forecast error as a percentage to stakeholders:
    A) AUC  B) **MAPE**  C) F1  D) Log loss

14. Score 5M records nightly, no always-on endpoint:
    A) Real-time  B) **Batch Transform**  C) Async  D) MME

15. Rare bursty traffic, no idle servers to manage/pay for:
    A) Real-time  B) **Serverless Inference**  C) Batch Transform  D) EC2

16. 500 MB payloads, minutes per request:
    A) Real-time  B) **Asynchronous Inference**  C) Serverless  D) Batch only

17. Hundreds of per-region models behind one cost-effective endpoint:
    A) One each  B) **Multi-Model Endpoint**  C) Batch  D) Lambda each

18. Repeatable process→train→eval→register→deploy with approvals:
    A) Cron scripts  B) **SageMaker Pipelines + Model Registry**  C) Console  D) Glue

19. Package your own `statsforecast` code for SageMaker:
    A) Lambda zip  B) **BYO container in ECR**  C) Layer  D) AMI

20. Detect input feature drift on a deployed model:
    A) Clarify only  B) **Model Monitor (data quality)**  C) CloudTrail  D) Autopilot

21. Test a new model on live traffic without serving its outputs:
    A) A/B variants  B) **Shadow testing**  C) Batch Transform  D) Canary 100%

22. Auto-retrain when accuracy decays — best wiring:
    A) Manual monthly  B) **Model Monitor → CloudWatch alarm → EventBridge → Pipeline**  C) Bigger instance  D) Delete endpoint

23. Split traffic 90/10 between model v1 and v2 to compare:
    A) Two endpoints  B) **Production variants (A/B)**  C) Shadow  D) MME

24. Restrict a training job to one S3 prefix and block internet egress:
    A) Admin + public subnet  B) **Least-privilege execution role + VPC + network isolation**  C) Root keys  D) Open SG

25. You finished testing a real-time endpoint. To stop charges you must:
    A) Nothing, it's free  B) **Delete the endpoint (and config)**  C) Stop the notebook  D) Lower temperature

---

## Answer key
1-B, 2-B, 3-B, 4-B, 5-B, 6-B, 7-B, 8-B, 9-B, 10-C, 11-B, 12-B, 13-B, 14-B, 15-B,
16-B, 17-B, 18-B, 19-B, 20-B, 21-B, 22-B, 23-B, 24-B, 25-B

### Why (the ones people miss)
- **1/2:** time-series must split chronologically; Feature Store kills train/serve skew.
- **8/13:** DeepAR = built-in forecasting; MAPE = percentage error metric you report.
- **14/15/16:** Batch (offline whole dataset) vs Serverless (spiky/idle) vs Async (big payload/long) vs Real-time (steady low-latency). This 4-way choice is the most-tested thing on the exam.
- **20 vs 7:** Model Monitor = drift on a *deployed* model; Clarify = bias/explainability (often at build).
- **21 vs 23:** shadow = mirror traffic, don't serve; A/B = production variants serving split traffic.
- **25:** real-time endpoints bill 24/7 — always delete them after labs.

**Scoring:** 18+/25 → ready; do the readiness checklist. <18 → re-read the weak domain and retake.
