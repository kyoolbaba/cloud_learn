---
tags: [mlops, hands-on, cloud-only, sagemaker, lab/l3]
aliases: [L3 Train and Register]
cert: MLA-C01
---
> [[mlops/labs/L2-feature-store/README|◀ L2]] · [[mlops/README|MLOps track]] · [[mlops/labs/L4-batch-inference/README|L4 ▶]] · [[MLA-C01|🎯 D2]]

# L3 · Training job + model registry — the approval gate

## 🎯 Goal
Run training as a **managed SageMaker Training Job** (not in the notebook process — on a
*separate* cloud instance that spins up, trains, saves the model to S3, and disappears), then
**register** the resulting model as a versioned, approvable artifact.

## 💡 Why it matters (career + exam)
A training *job* is reproducible infra (logged, sized, isolated) — unlike "I ran `.fit()` in a
cell." The **Model Registry** adds versioning + an **approval status** gate, so only blessed
models reach production. **MLA-C01 Domain 2**. This artifact feeds L4 and L5.

## 🧱 What you build
A training job using SageMaker's built-in **XGBoost**, producing `model.tar.gz` in S3,
registered as version 1 in a **Model Package Group** with status `PendingManualApproval` → `Approved`.

## ☁️ Run it (in the cloud)
```python
# Cell 1 — upload training data to S3 (XGBoost wants: label in column 0, no header)
import sagemaker, pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

sess = sagemaker.Session(); role = sagemaker.get_execution_role()
bucket = sess.default_bucket(); prefix = "l3-train"
X, y = load_breast_cancer(return_X_y=True, as_frame=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
pd.concat([ytr, Xtr], axis=1).to_csv("train.csv", index=False, header=False)
pd.concat([yte, Xte], axis=1).to_csv("val.csv",   index=False, header=False)
train_s3 = sess.upload_data("train.csv", bucket, f"{prefix}/train")
val_s3   = sess.upload_data("val.csv",   bucket, f"{prefix}/val")
```

```python
# Cell 2 — launch a managed Training Job (runs on its OWN cloud instance, then stops)
from sagemaker.estimator import Estimator
from sagemaker.inputs import TrainingInput

image = sagemaker.image_uris.retrieve("xgboost", sess.boto_region_name, version="1.7-1")
xgb = Estimator(image_uri=image, role=role, instance_count=1,
                instance_type="ml.m5.large",          # billed per second, only while training
                output_path=f"s3://{bucket}/{prefix}/output",
                sagemaker_session=sess)
xgb.set_hyperparameters(objective="binary:logistic", num_round=100, max_depth=4)
xgb.fit({"train": TrainingInput(train_s3, content_type="text/csv"),
         "validation": TrainingInput(val_s3, content_type="text/csv")})
print("model artifact:", xgb.model_data)               # model.tar.gz in S3
```

```python
# Cell 3 — register the model (versioned + approval gate)
mp = xgb.register(
    content_types=["text/csv"], response_types=["text/csv"],
    inference_instances=["ml.m5.large"], transform_instances=["ml.m5.large"],
    model_package_group_name="l3-cancer-models",
    approval_status="PendingManualApproval",           # <- the gate
)
# ...after you've reviewed metrics, approve it:
sm = sess.boto_session.client("sagemaker")
sm.update_model_package(ModelPackageArn=mp.model_package_arn,
                        ModelApprovalStatus="Approved")
print("approved:", mp.model_package_arn)
```

## ✅ Done when
- [ ] Studio → **Training jobs** shows a *Completed* job.
- [ ] A `model.tar.gz` exists under `s3://<bucket>/l3-train/output/`.
- [ ] **Model Registry** → `l3-cancer-models` → version 1, status **Approved**.
- [ ] You can explain why a registry + approval gate matters.

## 🧹 Teardown
- Training jobs auto-stop — **nothing keeps running.** No endpoint yet.
- **Shut down the Studio kernel.** Keep the registered model — L4/L5 need it.

## 📚 awesome-mlops links
*Model Deployment and Serving* (registry concepts) + *MLOps Core*.

## 🔁 Azure ML equivalent
Training Job ≈ **Azure ML command job**; Model Registry ≈ **Azure ML registered models** with stages.

---
Next: [[mlops/labs/L4-batch-inference/README|L4 · Batch inference ▶]] · Back: [[mlops/README]]
