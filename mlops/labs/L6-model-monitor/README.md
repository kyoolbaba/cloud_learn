---
tags: [mlops, hands-on, cloud-only, sagemaker, lab/l6]
aliases: [L6 Model Monitor]
cert: MLA-C01
---
> [[mlops/labs/L5-realtime-endpoint/README|◀ L5]] · [[mlops/README|MLOps track]] · [[mlops/labs/L7-pipeline-cicd/README|L7 ▶]] · [[MLA-C01|🎯 D4]]

# L6 · Model Monitor — catch drift before it hurts

## 🎯 Goal
Capture an endpoint's live traffic, **baseline** what "normal" input looks like, then run a
**Model Monitor** job that flags **data drift** (inputs changed vs baseline) and writes violations
to S3 + CloudWatch.

## 💡 Why it matters (career + exam)
A model silently decays as the world changes (your forecasting drifts hard around
promotions/seasonality — exactly this). Monitoring is what turns "trained once" into "trusted in
production." **MLA-C01 Domain 4** (monitoring + maintenance). Concepts:
[[mlops/resources|awesome-mlops → Testing, Monitoring and Maintenance]].

## 🧱 What you build
1. An endpoint with **data capture** on (logs requests/responses to S3).
2. A **baseline** (statistics + constraints) from training data.
3. A **monitoring schedule** that compares captured traffic to the baseline and reports drift.

## ☁️ Run it (in the cloud)
```python
# Cell 1 — deploy WITH data capture enabled
import sagemaker
from sagemaker import ModelPackage
from sagemaker.model_monitor import DataCaptureConfig
sess = sagemaker.Session(); role = sagemaker.get_execution_role(); bucket = sess.default_bucket()
sm = sess.boto_session.client("sagemaker")
pkg_arn = sm.list_model_packages(ModelPackageGroupName="l3-cancer-models",
            ModelApprovalStatus="Approved", SortBy="CreationTime"
          )["ModelPackageSummaryList"][0]["ModelPackageArn"]

capture = DataCaptureConfig(enable_capture=True, sampling_percentage=100,
                            destination_s3_uri=f"s3://{bucket}/l6-monitor/captured")
predictor = ModelPackage(role=role, model_package_arn=pkg_arn, sagemaker_session=sess
            ).deploy(1, "ml.m5.large", endpoint_name="l6-endpoint",
                     data_capture_config=capture)   # <- billing starts
```

```python
# Cell 2 — send traffic so there's something to monitor
from sagemaker.serializers import CSVSerializer
import pandas as pd
from sklearn.datasets import load_breast_cancer
predictor.serializer = CSVSerializer()
X, _ = load_breast_cancer(return_X_y=True, as_frame=True)
for i in range(200):
    predictor.predict(X.iloc[[i % len(X)]].values)
print("sent 200 requests — captured to S3")
```

```python
# Cell 3 — baseline "normal" inputs (a one-off processing job)
from sagemaker.model_monitor import DefaultModelMonitor
from sagemaker.model_monitor.dataset_format import DatasetFormat
X.to_csv("baseline.csv", index=False)
base_s3 = sess.upload_data("baseline.csv", bucket, "l6-monitor/baseline-in")

mon = DefaultModelMonitor(role=role, instance_count=1, instance_type="ml.m5.large")
mon.suggest_baseline(baseline_dataset=base_s3, dataset_format=DatasetFormat.csv(header=True),
                     output_s3_uri=f"s3://{bucket}/l6-monitor/baseline-out")
# -> writes statistics.json + constraints.json (what "normal" means)
```

```python
# Cell 4 — schedule hourly drift checks (captured traffic vs baseline)
from sagemaker.model_monitor import CronExpressionGenerator
mon.create_monitoring_schedule(
    monitor_schedule_name="l6-drift-schedule",
    endpoint_input=predictor.endpoint_name,
    output_s3_uri=f"s3://{bucket}/l6-monitor/reports",
    statistics=mon.baseline_statistics(), constraints=mon.suggested_constraints(),
    schedule_cron_expression=CronExpressionGenerator.hourly(),
)
print("monitoring scheduled — violations land in S3 + CloudWatch")
```

> First monitoring run starts at the top of the next hour. Drift violations appear under
> `.../reports/` as `constraint_violations.json` and as CloudWatch metrics.

## ✅ Done when
- [ ] `s3://<bucket>/l6-monitor/captured/...` has captured request/response JSONL.
- [ ] `statistics.json` + `constraints.json` exist under `baseline-out/`.
- [ ] Studio → endpoint → **Monitoring** shows schedule `l6-drift-schedule`.
- [ ] You can explain data drift vs model/concept drift.

## 🧹 Teardown (important — endpoint + schedule both bill)
```python
mon.delete_monitoring_schedule()     # stop the recurring job
predictor.delete_endpoint()          # stop the 24/7 endpoint
```
Then **shut down the Studio kernel** and confirm Endpoints + Schedules are empty.

## 📚 awesome-mlops links
*Testing, Monitoring and Maintenance* — Evidently, whylogs, drift detection.

## 🔁 Azure ML equivalent
Model Monitor ≈ **Azure ML model monitoring** (data drift + data quality monitors).

---
Next: [[mlops/labs/L7-pipeline-cicd/README|L7 · Pipeline + CI/CD ▶]] · Back: [[mlops/README]]
