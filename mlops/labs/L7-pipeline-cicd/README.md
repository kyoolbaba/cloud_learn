---
tags: [mlops, hands-on, cloud-only, sagemaker, lab/l7]
aliases: [L7 Pipeline CICD]
cert: MLA-C01
---
> [[mlops/labs/L6-model-monitor/README|◀ L6]] · [[mlops/README|MLOps track]] · [[mlops/labs/capstone/README|🏁 Capstone ▶]] · [[MLA-C01|🎯 D2/D4]]

# L7 · SageMaker Pipelines — automate the whole loop

## 🎯 Goal
Stop running cells by hand. Define the lifecycle as a **pipeline** (process → train → evaluate →
**conditionally register**) that runs as one reproducible, parameterized DAG in the cloud.

## 💡 Why it matters (career + exam)
This is **MLOps maturity level 1→2** (read the Google CD/automation guide in
[[mlops/resources]]). A pipeline = "press one button (or one event) and the whole thing runs the
same way every time." **MLA-C01 Domain 2** (CI/CD for ML) + Domain 4 (automation).

## 🧱 What you build
A `Pipeline` with 4 steps: **ProcessingStep** (prep) → **TrainingStep** (XGBoost) →
**ProcessingStep** (evaluate accuracy) → **ConditionStep** (if accuracy ≥ threshold →
**RegisterModel**, else stop). Connect it to [[mlops/labs/L6-model-monitor/README|L6]] drift later
for full auto-retraining (that's the capstone).

## ☁️ Run it (in the cloud)
```python
# Cell 1 — pipeline parameters (so one definition runs many ways)
import sagemaker
from sagemaker.workflow.parameters import ParameterFloat, ParameterString
sess = sagemaker.Session(); role = sagemaker.get_execution_role(); bucket = sess.default_bucket()

acc_threshold = ParameterFloat(name="MinAccuracy", default_value=0.90)
input_data    = ParameterString(name="InputData",
                  default_value=f"s3://{bucket}/l3-train/train/train.csv")
```

```python
# Cell 2 — define steps (train + the approval condition shown; processing/eval analogous)
from sagemaker.workflow.steps import TrainingStep
from sagemaker.workflow.condition_step import ConditionStep
from sagemaker.workflow.conditions import ConditionGreaterThanOrEqualTo
from sagemaker.workflow.step_collections import RegisterModel
from sagemaker.estimator import Estimator
from sagemaker.inputs import TrainingInput

image = sagemaker.image_uris.retrieve("xgboost", sess.boto_region_name, version="1.7-1")
xgb = Estimator(image_uri=image, role=role, instance_count=1, instance_type="ml.m5.large",
                output_path=f"s3://{bucket}/l7-pipeline/output", sagemaker_session=sess)
xgb.set_hyperparameters(objective="binary:logistic", num_round=100, max_depth=4)

train_step = TrainingStep(name="Train",
    estimator=xgb, inputs={"train": TrainingInput(input_data, content_type="text/csv")})

register = RegisterModel(name="RegisterIfGoodEnough", estimator=xgb,
    model_data=train_step.properties.ModelArtifacts.S3ModelArtifacts,
    content_types=["text/csv"], response_types=["text/csv"],
    inference_instances=["ml.m5.large"], transform_instances=["ml.m5.large"],
    model_package_group_name="l7-pipeline-models", approval_status="PendingManualApproval")

# (an evaluation ProcessingStep would emit accuracy into a PropertyFile; condition reads it)
gate = ConditionStep(name="AccuracyGate",
    conditions=[ConditionGreaterThanOrEqualTo(left=acc_threshold, right=0.0)],  # wire to eval output
    if_steps=[register], else_steps=[])
```

```python
# Cell 3 — assemble + run the pipeline (executes in the cloud, not the notebook)
from sagemaker.workflow.pipeline import Pipeline
pipeline = Pipeline(name="l7-train-register-pipeline",
                    parameters=[acc_threshold, input_data],
                    steps=[train_step, gate], sagemaker_session=sess)
pipeline.upsert(role_arn=role)          # register/update the definition
execution = pipeline.start()            # kick it off
print("running — watch it in Studio → Pipelines")
execution.wait()
```

4. Watch the **DAG light up** in Studio → **Pipelines → l7-train-register-pipeline** (visual graph).

## ✅ Done when
- [ ] Studio → **Pipelines** shows `l7-train-register-pipeline` with a visual DAG.
- [ ] An execution reaches *Succeeded*.
- [ ] A model lands in registry `l7-pipeline-models` (when the accuracy gate passes).
- [ ] You can explain MLOps maturity 0→1→2 in your own words.

## 🧹 Teardown
- Pipeline definitions cost nothing at rest; executions only bill for the jobs they run (they self-stop).
- **Shut down the Studio kernel.**

## 📚 awesome-mlops links
*Infrastructure & Tooling* (Airflow, Kubeflow Pipelines) + the Google CD/automation guide.

## 🔁 Azure ML equivalent
SageMaker Pipelines ≈ **Azure ML pipelines** (component-based DAGs).

---
Next: [[mlops/labs/capstone/README|🏁 Capstone ▶]] · Back: [[mlops/README]]
