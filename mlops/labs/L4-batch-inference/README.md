---
tags: [mlops, hands-on, cloud-only, sagemaker, lab/l4]
aliases: [L4 Batch Inference]
cert: MLA-C01
---
> [[mlops/labs/L3-train-and-register/README|◀ L3]] · [[mlops/README|MLOps track]] · [[mlops/labs/L5-realtime-endpoint/README|L5 ▶]] · [[MLA-C01|🎯 D3]]

# L4 · Batch inference — score a whole dataset, no server to babysit

## 🎯 Goal
Use **Batch Transform** to score a CSV of records in one shot. A cloud instance spins up,
reads input from S3, writes predictions to S3, and **shuts itself off** — so there's nothing
billing 24/7. This is the **cheapest, safest** way to serve when you don't need instant answers.

## 💡 Why it matters (career + exam)
Most real scoring (nightly forecasts, lead scoring, your SKU forecasting) is **batch**, not
live. Knowing batch-vs-realtime trade-offs is a core **MLA-C01 Domain 3** topic — and batch is
the deploy mode that won't surprise you with a bill.

## 🧱 What you build
A `Transformer` that takes the model from **L3**, scores `val.csv`, and drops `val.csv.out`
(predictions) in S3 — instance auto-terminates when done.

## ☁️ Run it (in the cloud)
```python
# Cell 1 — get the approved model from L3's registry into a deployable Model
import sagemaker
sess = sagemaker.Session(); role = sagemaker.get_execution_role()
sm = sess.boto_session.client("sagemaker")
bucket = sess.default_bucket()

pkgs = sm.list_model_packages(ModelPackageGroupName="l3-cancer-models",
                              ModelApprovalStatus="Approved", SortBy="CreationTime")
pkg_arn = pkgs["ModelPackageSummaryList"][0]["ModelPackageArn"]

from sagemaker import ModelPackage
model = ModelPackage(role=role, model_package_arn=pkg_arn, sagemaker_session=sess)
```

```python
# Cell 2 — prepare INPUT (features only, no label column for scoring)
import pandas as pd
from sklearn.datasets import load_breast_cancer
X, _ = load_breast_cancer(return_X_y=True, as_frame=True)
X.tail(50).to_csv("score_me.csv", index=False, header=False)
input_s3 = sess.upload_data("score_me.csv", bucket, "l4-batch/input")
```

```python
# Cell 3 — Batch Transform: spins up, scores, writes to S3, SHUTS DOWN
transformer = model.transformer(
    instance_count=1, instance_type="ml.m5.large",       # billed only for the minutes it runs
    output_path=f"s3://{bucket}/l4-batch/output",
    accept="text/csv",
)
transformer.transform(input_s3, content_type="text/csv", split_type="Line")
transformer.wait()
print("predictions written to:", transformer.output_path)
```

```python
# Cell 4 — read predictions back
import pandas as pd
preds = pd.read_csv(f"{transformer.output_path}/score_me.csv.out", header=None)
preds.head()
```

## ✅ Done when
- [ ] Studio → **Batch transform jobs** shows a *Completed* job.
- [ ] `s3://<bucket>/l4-batch/output/score_me.csv.out` exists with one prediction per row.
- [ ] You confirmed **no instance is still running** (batch self-terminates).
- [ ] You can state when to pick batch over a real-time endpoint.

## 🧹 Teardown
- Batch Transform **auto-terminates** — nothing to delete, no 24/7 bill. (This is the point.)
- **Shut down the Studio kernel.**

## 📚 awesome-mlops links
*Model Deployment and Serving* — offline/batch scoring patterns.

## 🔁 Azure ML equivalent
Batch Transform ≈ **Azure ML batch endpoints**.

---
Next: [[mlops/labs/L5-realtime-endpoint/README|L5 · Real-time endpoint ▶]] · Back: [[mlops/README]]
