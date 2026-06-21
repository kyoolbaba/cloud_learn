---
tags: [mlops, hands-on, cloud-only, sagemaker, lab/l2]
aliases: [L2 Feature Store]
cert: MLA-C01
---
> [[mlops/labs/L1-experiment-tracking/README|◀ L1]] · [[mlops/README|MLOps track]] · [[mlops/labs/L3-train-and-register/README|L3 ▶]] · [[MLA-C01|🎯 D1]]

# L2 · Feature store — compute features once, use them everywhere

## 🎯 Goal
Store engineered features in **SageMaker Feature Store** so the *exact same* feature values
feed both **training** and **serving** — killing "train/serve skew" (the #1 silent ML bug).

## 💡 Why it matters (career + exam)
If training uses `avg_sales_30d` computed one way and production computes it slightly
differently, your live model quietly rots. A feature store is the single source of truth.
**MLA-C01 Domain 1** (data prep). Concepts: [[mlops/resources|awesome-mlops → Feature Stores]].

## 🧱 What you build
A **Feature Group** (online + offline) holding rows of features keyed by a record id, written
from a Studio notebook and queryable for both batch (offline → S3) and low-latency (online) reads.

## ☁️ Run it (in the cloud)
Studio → new notebook (Python 3). Uses the bucket from [[mlops/00-cloud-workspace|setup]].

```python
# Cell 1 — build a small feature dataframe (needs an id + event-time column)
import sagemaker, pandas as pd, time
from sklearn.datasets import load_breast_cancer

sess = sagemaker.Session(); role = sagemaker.get_execution_role()
X, y = load_breast_cancer(return_X_y=True, as_frame=True)
df = X.copy()
df["target"] = y
df["record_id"] = df.index.astype("string")          # required: unique key
df["event_time"] = pd.Series([time.time()] * len(df), dtype="float64")  # required: timestamp
df = df.rename(columns=lambda c: c.replace(" ", "_"))  # feature names: no spaces
```

```python
# Cell 2 — create + populate the Feature Group (online + offline store in S3)
from sagemaker.feature_store.feature_group import FeatureGroup

fg = FeatureGroup(name="l2-cancer-features", sagemaker_session=sess)
fg.load_feature_definitions(data_frame=df)
fg.create(
    s3_uri=f"s3://{sess.default_bucket()}/feature-store",  # offline store
    record_identifier_name="record_id",
    event_time_feature_name="event_time",
    role_arn=role,
    enable_online_store=True,                              # low-latency serving reads
)
# wait until ACTIVE, then ingest the rows
while fg.describe().get("FeatureGroupStatus") != "Created":
    time.sleep(10)
fg.ingest(data_frame=df, max_workers=3, wait=True)
print("ingested", len(df), "records")
```

```python
# Cell 3 — read one record back from the ONLINE store (serving path)
rt = sess.boto_session.client("sagemaker-featurestore-runtime")
rec = rt.get_record(FeatureGroupName="l2-cancer-features", RecordIdentifierValueAsString="0")
print(rec["Record"][:3])   # the same features training will see — no skew
```

## ✅ Done when
- [ ] Studio → **Feature Store** lists `l2-cancer-features` as *Active*.
- [ ] `get_record` returns features for `record_id = "0"` from the online store.
- [ ] Offline copy exists under `s3://<bucket>/feature-store/`.
- [ ] You can explain train/serve skew in one sentence.

## 🧹 Teardown
- Online store bills a little while it exists → delete when done: `fg.delete()`.
- Offline S3 data is cheap; remove with `aws s3 rm` later if you like.
- **Shut down the Studio kernel.**

## 📚 awesome-mlops links
*Feature Stores* section — **Feast**, **Hopsworks** (the OSS tools behind this concept).

## 🔁 Azure ML equivalent
SageMaker Feature Store ≈ **Azure ML Managed Feature Store** (same online/offline split).

---
Next: [[mlops/labs/L3-train-and-register/README|L3 · Train + register ▶]] · Back: [[mlops/README]]
