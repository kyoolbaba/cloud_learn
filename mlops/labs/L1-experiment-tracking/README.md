---
tags: [mlops, hands-on, cloud-only, sagemaker, lab/l1]
aliases: [L1 Experiment Tracking]
cert: MLA-C01
---
> [[mlops/README|◀ MLOps track]] · [[mlops/00-cloud-workspace|Setup]] · [[mlops/labs/L2-feature-store/README|L2 ▶]] · [[MLA-C01|🎯 MLA-C01 D2]]

# L1 · Experiment tracking — never lose a result again

## 🎯 Goal
Run the **same model 3 ways** (different params), and have SageMaker **record every run's
params + metrics** so you can compare them in a UI and answer *"which settings were best, and
can I reproduce them?"* All inside a cloud notebook.

## 💡 Why it matters (career + exam)
Untracked experiments = "I think the good model used 100 trees… maybe?" Tracking makes results
**reproducible**, which is the foundation everything else builds on. **MLA-C01 Domain 2** tests
exactly this. Concept reading: [[mlops/resources|awesome-mlops → Workflow Management]].

## 🧱 What you build
A SageMaker **Experiment** with 3 **runs**, each logging hyperparameters + an accuracy metric,
all viewable + sortable in **Studio → Experiments**.

## ☁️ Run it (in the cloud)
1. Open **SageMaker Studio** (from [[mlops/00-cloud-workspace|setup]]).
2. **File → New → Notebook**, kernel **Python 3 (ipykernel)**.
3. Paste the code below into cells and run. *Nothing here touches your laptop.*

```python
# Cell 1 — toy data + cloud session (runs on the Studio cloud instance)
import sagemaker
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

sess = sagemaker.Session()
print("Running in region:", sess.boto_region_name)   # proves we're in the cloud

X, y = load_breast_cancer(return_X_y=True, as_frame=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
```

```python
# Cell 2 — track 3 runs with different hyperparameters
from sagemaker.experiments.run import Run
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

EXPERIMENT = "l1-tracking-demo"

for n_estimators in [10, 100, 300]:           # 3 different settings
    run_name = f"rf-{n_estimators}-trees"
    with Run(experiment_name=EXPERIMENT, run_name=run_name, sagemaker_session=sess) as run:
        # 1) log what we chose
        run.log_parameter("model", "RandomForest")
        run.log_parameter("n_estimators", n_estimators)

        # 2) train
        clf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
        clf.fit(X_tr, y_tr)
        preds = clf.predict(X_te)

        # 3) log how it did
        run.log_metric("accuracy", accuracy_score(y_te, preds))
        run.log_metric("f1", f1_score(y_te, preds))
        print(f"logged {run_name}: acc={accuracy_score(y_te, preds):.4f}")
```

```python
# Cell 3 — read the results back programmatically (optional)
from sagemaker.analytics import ExperimentAnalytics
df = ExperimentAnalytics(experiment_name=EXPERIMENT,
                         sagemaker_session=sess).dataframe()
df[["TrialComponentName", "n_estimators", "accuracy - Last", "f1 - Last"]]
```

4. **See it in the UI:** Studio left nav → **Experiments** → `l1-tracking-demo` → sort by
   `accuracy`. That sortable table *is* the point of experiment tracking.

## ✅ Done when
- [ ] `Experiments` shows `l1-tracking-demo` with **3 runs**.
- [ ] Each run has `n_estimators` (param) and `accuracy` + `f1` (metrics).
- [ ] You can sort by accuracy and name the winning run.
- [ ] You can explain *why* tracking matters (reproducibility) in one sentence.

## 🧹 Teardown
- No endpoints or jobs were created → **$0 left running.**
- **Shut down the Studio kernel** (Running Terminals and Kernels → Shut Down) so the notebook instance stops billing.
- Experiment metadata is free to keep; delete later from the Experiments UI if you want.

## 📚 awesome-mlops links
*Workflow Management* section (MLflow Tracking, Weights & Biases) — the open-source tools this
managed feature replaces. See [[mlops/resources]].

## 🔁 Azure ML equivalent
`Run` + Experiments ≈ **Azure ML Jobs + MLflow tracking** (Azure ML uses MLflow natively).

---
Next: [[mlops/labs/L2-feature-store/README|L2 · Feature store ▶]] · Back: [[mlops/README]]
