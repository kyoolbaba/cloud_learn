# 🛠️ Project: AWS ML Deployment (Train → Endpoint → Monitor)

> **Goal:** Take a model from notebook to a monitored production endpoint on AWS. Reinforces MLA-C01 + AIF-C01.
>
> 🌍 **Real-world story:** You trained a churn/price model. Now serve it as an API, monitor it, and add a batch-scoring path.

## What you'll build
```
S3 (training data) → SageMaker training job → Model artifact (S3)
        ↓                                          ↓
   Real-time endpoint  ←──────────────  Deploy  ──→  Batch Transform (offline scoring)
        ↓
   Model Monitor + CloudWatch (drift/metrics)
```

## Skills practiced
- SageMaker training + model artifacts
- Real-time endpoint vs Batch Transform (cost/latency trade-off)
- Model Monitor / CloudWatch for drift
- IAM roles, KMS, endpoint security
- MLOps basics (optional SageMaker Pipeline)

## Steps
1. Put a small training dataset in S3.
2. Train with a **built-in algorithm** (e.g., XGBoost) or a script.
3. Deploy a **real-time endpoint**; invoke with test data.
4. Run **Batch Transform** on a larger file; compare cost.
5. Enable **Model Monitor** + a CloudWatch alarm on latency/errors.
6. (Bonus) Wrap train→deploy in a **SageMaker Pipeline**.

## ✅ Success criteria
- [ ] Endpoint returns predictions
- [ ] Batch job writes results to S3
- [ ] Monitoring/alarm configured
- [ ] You can articulate when to use real-time vs batch

## 💸 Cleanup (do it!)
- [ ] **DELETE the real-time endpoint** (bills per hour!)
- [ ] Delete Model Monitor schedule
- [ ] Stop/delete Studio apps + domain
- [ ] Delete S3 data + model artifacts
- [ ] Delete CloudWatch alarms; check Cost Explorer

## 📝 Reflection / write-up
- Which metric did you optimize and why?
- Cost difference real-time vs batch?
- AWS↔Azure: same flow on Azure ML → see [[azure-ai-project]]

🔗 Related: [[../03-shared-cloud-concepts/ai-ml]] · [[../01-aws/associate/aws-machine-learning-engineer-associate-MLA-C01]]
