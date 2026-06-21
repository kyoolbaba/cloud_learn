---
tags: [mlops, hands-on, cloud-only, sagemaker, lab/l5]
aliases: [L5 Realtime Endpoint]
cert: MLA-C01
---
> [[mlops/labs/L4-batch-inference/README|◀ L4]] · [[mlops/README|MLOps track]] · [[mlops/labs/L6-model-monitor/README|L6 ▶]] · [[MLA-C01|🎯 D3]]

# L5 · Real-time endpoint — live, low-latency predictions

## 🎯 Goal
Deploy the L3 model as a **live HTTPS endpoint**, send it a request, get a prediction back in
milliseconds — then **delete it immediately** so it stops billing.

## ⚠️ READ THIS FIRST — endpoints bill 24/7
A real-time endpoint is a server that **runs continuously** until you delete it. This is the
**#1 way beginners get a surprise SageMaker bill.** Do the whole lab in one sitting and run the
teardown. A forgotten `ml.m5.large` endpoint is ~**$60–70/month**.

## 💡 Why it matters (career + exam)
Use real-time only when you need **instant** answers (fraud check at checkout, live
recommendation). **MLA-C01 Domain 3** tests choosing endpoint type + the cost trade-off vs batch
(L4). Also note **Serverless Inference** (scales to zero) as the cheaper live option.

## 🧱 What you build
A deployed endpoint from the approved L3 model, one inference call, then a clean delete.

## ☁️ Run it (in the cloud)
```python
# Cell 1 — deploy the approved model as a live endpoint
import sagemaker
from sagemaker import ModelPackage
sess = sagemaker.Session(); role = sagemaker.get_execution_role()
sm = sess.boto_session.client("sagemaker")
pkg_arn = sm.list_model_packages(ModelPackageGroupName="l3-cancer-models",
            ModelApprovalStatus="Approved", SortBy="CreationTime"
          )["ModelPackageSummaryList"][0]["ModelPackageArn"]

model = ModelPackage(role=role, model_package_arn=pkg_arn, sagemaker_session=sess)
predictor = model.deploy(initial_instance_count=1, instance_type="ml.m5.large",
                         endpoint_name="l5-cancer-endpoint")   # <- now billing starts
```

```python
# Cell 2 — call the live endpoint
from sagemaker.serializers import CSVSerializer
from sagemaker.deserializers import CSVDeserializer
import pandas as pd
from sklearn.datasets import load_breast_cancer

predictor.serializer = CSVSerializer(); predictor.deserializer = CSVDeserializer()
X, _ = load_breast_cancer(return_X_y=True, as_frame=True)
print("prediction:", predictor.predict(X.iloc[[0]].values))   # one row → probability
```

```python
# Cell 3 — 🧹 DELETE IT NOW (stops the 24/7 bill)
predictor.delete_endpoint()
print("endpoint + config deleted — billing stopped")
```

> 💡 Cheaper alternative: deploy with `serverless_inference_config=ServerlessInferenceConfig()`
> — it **scales to zero** between requests, so idle time is free. Great for low-traffic demos.

## ✅ Done when
- [ ] You got a live prediction back from `l5-cancer-endpoint`.
- [ ] **`delete_endpoint()` ran** and Studio → **Endpoints** shows *nothing* live.
- [ ] You can explain real-time vs batch vs serverless and their cost shapes.

## 🧹 Teardown (verify — this one matters)
1. Cell 3 ran (`delete_endpoint()`).
2. Studio → **Deployments → Endpoints** = empty. If anything is *InService*, select → **Delete**.
3. **Shut down the Studio kernel.**

## 📚 awesome-mlops links
*Model Deployment and Serving* — online serving (Seldon, BentoML, KServe) concepts.

## 🔁 Azure ML equivalent
Endpoint ≈ **Azure ML online endpoint** (managed vs Kubernetes).

---
Next: [[mlops/labs/L6-model-monitor/README|L6 · Model Monitor ▶]] · Back: [[mlops/README]]
