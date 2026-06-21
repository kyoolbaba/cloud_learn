---
tags: [cert/mla-c01, aws/ml, sagemaker, data-prep, feature-engineering]
cert: MLA-C01
domain: 1
aliases: [MLA-C01 Domain 1, Data Preparation for ML]
---
> [[MLA-C01|⬅ MLA-C01 Home]] · Next: [[domain-2-model-development|Domain 2 · Model Development ▶]]

# Domain 1 — Data Preparation for ML (28%)

The biggest domain — "garbage in, garbage out." Cleaning, feature engineering, labeling,
splitting, and the SageMaker tools that do each.

## 1.1 Where ML data lives & how it's fed
- **S3** = default training data store. **FSx for Lustre** = high-throughput for big training (caches S3). **EFS** for shared file access.
- **Input modes:** **File mode** (download whole dataset first) vs **Pipe mode** / **FastFile** (stream from S3 — start training without full download; good for huge data).
- **Efficient formats:** **RecordIO-protobuf** (optimal for many built-in algos), Parquet, CSV. Convert for speed.

## 1.2 SageMaker data-prep tools (match tool → job)
| Need | Tool |
|---|---|
| Visual, low-code data prep + 300+ transforms + quick model preview | **SageMaker Data Wrangler** |
| Scalable batch preprocessing/feature jobs (your own script, Spark/sklearn) | **SageMaker Processing** |
| Store/share/serve features (online + offline), avoid train/serve skew | **SageMaker Feature Store** |
| Label raw data (human + auto-labeling) | **SageMaker Ground Truth** |
| Big SQL/ETL upstream | Glue, Athena, EMR (see [[domain-1-ingestion-transformation|DEA-C01 D1]]) |

## 1.3 Feature engineering (heavily tested — know the technique names)
- **Scaling/normalization:** standardization (z-score), min-max — needed for distance/gradient models (not trees).
- **Encoding categoricals:** **one-hot** (low cardinality), **label/ordinal**, target/embedding (high cardinality).
- **Missing values:** drop, or **impute** (mean/median/mode, model-based). Document the choice.
- **Outliers:** cap/clip, winsorize, or robust scaling.
- **Binning/discretization**, **log transform** for skew, **polynomial/interaction** features.
- **Datetime/time-series features** (your bread and butter): **lags**, **rolling means**, day-of-week, holidays, Fourier/seasonality terms.
- **Text:** tokenization, TF-IDF, embeddings. **Dimensionality reduction:** PCA.

## 1.4 Class imbalance (classic exam trap)
Accuracy lies on imbalanced data (99% "no fraud"). Fix with: **resampling** (oversample minority / **SMOTE**, undersample majority), **class weights**, and **better metrics** (precision/recall/F1/AUC, not accuracy).

## 1.5 Splitting data right (avoid leakage)
- **Train / validation / test** split; tune on validation, report on untouched test.
- **Stratify** to keep class ratios across splits.
- **Time-series:** split **chronologically** (train on past, validate on future) — never random-shuffle time data, and never let future info leak into features. **Data leakage** = the #1 cause of "too good to be true" results.
- Fit scalers/encoders on **train only**, then apply to val/test (Feature Store helps keep this consistent).

## 1.6 Bias & quality checks before training
- **SageMaker Clarify** — pre-training **bias metrics** (e.g. class imbalance, label imbalance across groups) on the dataset.
- **Data Wrangler / Glue Data Quality** — profiling, null/outlier detection, validation rules.

## 1.7 Train/serve skew & Feature Store
If features are computed one way in training and another in production, predictions degrade.
**Feature Store** serves the **same** feature definitions to both (offline store for training, online store for low-latency inference).

## Hands-on (`$env:AWS_PROFILE="learn"` — cleanup included)
```powershell
$env:AWS_PROFILE = "learn"
# Run a Processing job that builds lag/rolling features from your sales Parquet
# (script-mode sklearn/Spark container reading s3://.../raw, writing s3://.../features)
aws sagemaker create-processing-job --processing-job-name feat-lab `
  --app-specification ImageUri=<sklearn-image> --role-arn <SageMakerRole> ...
# CLEANUP: Processing jobs stop on their own; just remove the S3 outputs.
aws s3 rm s3://yourname-ml-lab/features/ --recursive
```

## Flashcards
- Data Wrangler = visual prep; Processing = batch feature jobs; Feature Store = share features (no skew); Ground Truth = labeling.
- One-hot (low cardinality) vs label encoding; scale for gradient/distance models, not trees.
- Imbalance → SMOTE / class weights + precision/recall/F1 (not accuracy).
- Time-series → split chronologically; fit transforms on train only; beware leakage.
- Pipe/FastFile mode streams big data from S3 without full download.

## Practice questions
**Q1.** Forecasting model trained with a **random** train/test split looks amazing, then fails live. Likely cause?
- A) Too few epochs  B) **Temporal data leakage (must split chronologically)** ✅  C) Wrong instance type  D) No GPU

**Q2.** Reuse the exact same feature definitions in training and real-time inference to avoid skew:
- A) Two scripts  B) **SageMaker Feature Store** ✅  C) DynamoDB only  D) Data Wrangler export

**Q3.** Fraud data is 99.5% negatives. Best handling?
- A) Optimize accuracy  B) **Resample/SMOTE + class weights + use precision/recall/F1** ✅  C) Drop the positives  D) One-hot the label

**Q4.** Low-code, visual data prep with 300+ transforms and a quick model preview:
- A) Processing job  B) **SageMaker Data Wrangler** ✅  C) Ground Truth  D) Clarify

**Q5.** Stream a very large S3 training set without downloading it all first:
- A) File mode  B) **Pipe / FastFile mode** ✅  C) EFS only  D) Batch Transform
