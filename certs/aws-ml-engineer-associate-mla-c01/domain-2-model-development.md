---
tags: [cert/mla-c01, aws/ml, sagemaker, training, evaluation]
cert: MLA-C01
domain: 2
aliases: [MLA-C01 Domain 2, ML Model Development]
---
> [[domain-1-data-preparation|◀ Domain 1]] · [[MLA-C01|MLA-C01 Home]] · [[domain-3-deployment-orchestration|Domain 3 · Deploy ▶]]

# Domain 2 — ML Model Development (26%)

Choosing an approach, training it, tuning it, and **evaluating** it correctly.

## 2.1 Choose the modeling approach
| Situation | Approach |
|---|---|
| Tabular classification/regression | **XGBoost** (built-in, the workhorse) or **Linear Learner** |
| **Time-series forecasting** | **DeepAR** (built-in) — *your domain*; or BYO `statsforecast`/`mlforecast` container |
| Anomaly detection | **Random Cut Forest**, IP Insights |
| Clustering | **K-Means** |
| NLP / text classification | **BlazingText**, or fine-tune an FM |
| Want it built for you (AutoML) | **SageMaker Autopilot** |
| Pre-built/open models to deploy or fine-tune | **SageMaker JumpStart** |
| Generative AI | **Amazon Bedrock** (see [[domain-2-generative-ai-fundamentals|AIF-C01]]) |

**Build vs buy ladder:** AI service → JumpStart/Autopilot → built-in algorithm → bring-your-own-script → bring-your-own-container. Escalate only for more control.

## 2.2 Training on SageMaker
- **Training job** = container + algorithm + hyperparameters + S3 data + instance(s) → model artifact to S3.
- **Managed Spot Training** — up to ~90% cheaper, interruptible; use **checkpointing** to resume. (Great for your big forecasting runs.)
- **Distributed training** — data-parallel (split data) or model-parallel (split model) for large jobs.
- **Script mode / BYOC** — run your own code (`statsforecast`) in a SageMaker-managed container; push image to **ECR**.
- **SageMaker Experiments** — track runs, params, metrics; **Debugger** — catch vanishing gradients/overfitting/bottlenecks.

## 2.3 Hyperparameter tuning
- **Automatic Model Tuning (AMT)** — searches hyperparameters (**Bayesian**, random, grid, Hyperband) to optimize an objective metric (e.g. minimize validation RMSE). Set ranges + max jobs + parallelism.
- **Hyperparameter** = set *before* training (learning rate, depth, #trees); **parameter** = learned *during* training (weights).

## 2.4 Evaluation metrics (know which fits the problem — exam-critical)
**Regression / forecasting (your world):**
- **RMSE** (penalizes big errors), **MAE** (robust, same units), **MAPE** (percentage error — what you report), **R²**.

**Classification:**
- **Confusion matrix** → Precision = TP/(TP+FP) ("of predicted-positive, how many right"), Recall/Sensitivity = TP/(TP+FN) ("of actual-positive, how many caught"), **F1** = harmonic mean, **AUC-ROC** (ranking quality, threshold-independent).
- **When to favor:** **Recall** when missing a positive is costly (disease, fraud); **Precision** when false alarms are costly. **Accuracy** only on balanced data.

## 2.5 Fit problems (diagnose + fix)
- **Overfitting** (great train, poor val) → more data, **regularization** (L1/L2, dropout), simpler model, early stopping, cross-validation.
- **Underfitting** (poor train) → bigger/more complex model, more features, train longer.
- **Bias–variance trade-off**: underfit = high bias; overfit = high variance.
- **Cross-validation** = robust estimate on limited data (use time-series CV for temporal data).

## 2.6 Reproducibility & governance (sets up Domain 3)
Track datasets, code, hyperparameters, and metrics (Experiments) → register the winning model in the **Model Registry** with its metrics + lineage → approve → deploy. This is the MLOps spine.

## Hands-on (cleanup included)
```powershell
$env:AWS_PROFILE = "learn"
# Tune DeepAR (or XGBoost) to minimize validation RMSE with Automatic Model Tuning
aws sagemaker create-hyper-parameter-tuning-job --hyper-parameter-tuning-job-name fc-tune `
  --hyper-parameter-tuning-job-config file://amt.json --training-job-definition file://train.json
# Use Managed Spot (MaxWaitTimeInSeconds + checkpointing) to slash cost.
# CLEANUP: tuning/training jobs end themselves; delete model artifacts + any leftover endpoints.
aws s3 rm s3://yourname-ml-lab/models/ --recursive
```

## Flashcards
- DeepAR = built-in time-series forecasting; XGBoost = tabular workhorse; RCF = anomaly; K-Means = clustering.
- AMT = automatic hyperparameter tuning (Bayesian); Autopilot = AutoML.
- Regression: RMSE/MAE/MAPE/R². Classification: precision/recall/F1/AUC + confusion matrix.
- Recall for "don't miss positives"; precision for "avoid false alarms"; accuracy only if balanced.
- Overfit → regularize/more data/early stop; Managed Spot + checkpointing = cheap training.

## Practice questions
**Q1.** Built-in SageMaker algorithm for **time-series forecasting**:
- A) XGBoost  B) **DeepAR** ✅  C) K-Means  D) BlazingText

**Q2.** Automatically search for the best hyperparameters to minimize validation RMSE:
- A) Autopilot only  B) **Automatic Model Tuning (AMT)** ✅  C) Model Monitor  D) Clarify

**Q3.** Fraud detection: missing a real fraud is far worse than a false alarm. Optimize:
- A) Precision  B) Accuracy  C) **Recall** ✅  D) RMSE

**Q4.** Model scores 0.98 on training but 0.61 on validation. This is:
- A) Underfitting  B) **Overfitting (regularize / more data / early stop)** ✅  C) Data leakage fixed  D) Good generalization

**Q5.** Cut training cost ~90% for a long, interruption-tolerant job:
- A) Bigger instance  B) **Managed Spot Training + checkpointing** ✅  C) Real-time endpoint  D) Multi-model endpoint
