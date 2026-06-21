---
tags: [mlops, moc, hands-on, cloud-only]
aliases: [MLOps, MLOps Track, MLOps MOC]
cssclass: wide
---
> [[HOME|🏠 Home]] · [[foundations/06-mlops-basics|◀ MLOps basics (concepts)]] · [[MLA-C01|🎯 MLA-C01]] · [[mlops/resources|📚 Resources]] · [[PROGRESS|Tracker]]
>
> **Labs:** [[mlops/labs/L1-experiment-tracking/README|L1 Tracking]] · [[mlops/labs/L2-feature-store/README|L2 Features]] · [[mlops/labs/L3-train-and-register/README|L3 Train+Register]] · [[mlops/labs/L4-batch-inference/README|L4 Batch]] · [[mlops/labs/L5-realtime-endpoint/README|L5 Endpoint]] · [[mlops/labs/L6-model-monitor/README|L6 Monitor]] · [[mlops/labs/L7-pipeline-cicd/README|L7 Pipeline]] · [[mlops/labs/capstone/README|🏁 Capstone]]
>
> **Underneath it all:** [[mlops/code-craft|🧰 Code craft — notebook → production code]]

# ☁️ MLOps Track — learn the ML lifecycle, 100% in the cloud

This is your dedicated, **hands-on MLOps lane**. The *concepts* come from
[[foundations/06-mlops-basics|the MLOps basics note]] and [[mlops/resources|awesome-mlops]];
this folder is where you **build the lifecycle for real** — and every line of code
runs **on the cloud**, never on your laptop.

> One-line story: take a model from a notebook → to a **versioned, deployed, monitored,
> auto-retrained production system** — the difference between *"I trained a model"* and
> *"I run a model in production."* That's the [[MLA-C01|ML Engineer]] job.

## 🔑 The non-negotiable rule: nothing runs locally

| ❌ Not this | ✅ This (cloud-only) |
|---|---|
| `pip install` on your laptop | Packages installed **inside SageMaker Studio** (a cloud machine) |
| Notebook on Windows | **SageMaker Studio JupyterLab** (cloud notebook, code stored in cloud) |
| `aws ...` from PowerShell | **AWS CloudShell** (browser terminal, runs in AWS) |
| Model files on your disk | Artifacts in **S3** |
| A local `mlflow` server | **SageMaker Experiments / managed MLflow** |

**Why cloud-only?** (a) Your laptop never holds data or credentials. (b) The exact
environment that trains is the one that serves — no "works on my machine." (c) It mirrors
how real ML teams work, which is exactly what [[MLA-C01]] tests. **Set up the cloud
workbench once → [[mlops/00-cloud-workspace|00 · Cloud workspace setup]].**

## 🗺️ The track (each lab = one stage of the lifecycle)

Each lab maps to one concept from [[foundations/06-mlops-basics]] and one MLA-C01 domain.

| # | Lab | Lifecycle stage | Cloud service | Runs in | MLA domain |
|---|---|---|---|---|---|
| **00** | [[mlops/00-cloud-workspace|Cloud workspace setup]] | *(prereq)* | SageMaker Studio, CloudShell | — | — |
| **L1** | [[mlops/labs/L1-experiment-tracking/README|Experiment tracking]] | track every run | SageMaker Experiments | Studio notebook | D2 |
| **L2** | [[mlops/labs/L2-feature-store/README|Feature store]] | reuse features, kill skew | SageMaker Feature Store | Studio notebook | D1 |
| **L3** | [[mlops/labs/L3-train-and-register/README|Train + register]] | training job → model registry | Training Jobs, Model Registry | Studio notebook | D2 |
| **L4** | [[mlops/labs/L4-batch-inference/README|Batch inference]] | score a dataset, no server | Batch Transform | Studio notebook | D3 |
| **L5** | [[mlops/labs/L5-realtime-endpoint/README|Real-time endpoint]] | live low-latency serving | SageMaker Endpoints | Studio notebook | D3 |
| **L6** | [[mlops/labs/L6-model-monitor/README|Model Monitor]] | detect data/model drift | Model Monitor, CloudWatch | Studio notebook | D4 |
| **L7** | [[mlops/labs/L7-pipeline-cicd/README|Pipeline + CI/CD]] | automate the whole loop | SageMaker Pipelines, EventBridge | Studio notebook | D2/D4 |
| 🏁 | [[mlops/labs/capstone/README|Capstone]] | drift → retrain → redeploy, hands-off | everything above | Pipeline | all |

**Do them in order** — each lab produces an artifact (a model, a feature group, a
registered version) the next one consumes. The capstone wires them into one automated loop.

## 🧱 Each lab follows the same shape
**Goal** → **Why it matters** (career + exam) → **What you build** → **☁️ Run it (in the cloud)** →
**code** → **✅ Done when** → **🧹 Teardown** → **📚 awesome-mlops links** → **🔁 Azure ML equivalent**.

## 💸 Cost discipline (MLOps bills more than the core labs — read this)
SageMaker is **not** all free-tier. The big three money leaks:
1. **Real-time endpoints bill 24/7** while they exist — **delete them after every lab** (L5/L6). Prefer **Batch Transform** (L4) for offline scoring.
2. **Studio apps (the running kernel)** bill per hour — **Shut down** the instance from `Running Terminals and Kernels` when you stop for the day.
3. **Training jobs** bill per second of instance time — fine, but use small instances (`ml.m5.large`) on toy data.

> Free-tier softener: SageMaker has a **2-month free tier** (Studio notebook hours, training, batch transform on small instances). Stay on `ml.t3.medium`/`ml.m5.large`, toy datasets, and **tear down endpoints**, and this whole track costs a few dollars at most. Personal `learn` account **only** — never the company account.

## ✅ Track checkpoint
When you finish the capstone you can say: *"I can take a model from experiment to a
self-healing production pipeline — tracking, feature store, registry, batch + real-time
serving, drift monitoring, and automated retraining — entirely on AWS."* That sentence is
a portfolio piece → log it in [[portfolio/12-sagemaker-mlops/README|portfolio/12]].

---
Back to: [[HOME]] · [[foundations/06-mlops-basics]] · [[mlops/resources]] · cert: [[MLA-C01]]
