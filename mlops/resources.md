---
tags: [mlops, reference, resources]
aliases: [MLOps Resources, awesome-mlops map]
---
> [[mlops/README|◀ MLOps track]] · [[HOME|🏠 Home]] · [[MLA-C01|🎯 MLA-C01]]

# 📚 MLOps resources — awesome-mlops, mapped to this track

The big curated directory is **[visenger/awesome-mlops](https://github.com/visenger/awesome-mlops)** —
a link library, *not* a course. Below it's filtered down to **only what helps you**, in the
right order, and mapped to the labs in [[mlops/README]]. Use it for the *why* behind each
cloud service you wire up.

## 🟢 Start here (beginner, read in this order)
1. **Google — *Practitioners Guide to MLOps* (whitepaper)** — the single best free overview of the lifecycle. Read before L1.
2. **MLOps Zoomcamp** (DataTalksClub, free) — structured course covering tracking → deployment → monitoring. Pairs with L1–L6.
3. **"MLOps: Continuous delivery and automation pipelines in ML"** (Google Cloud) — the famous **MLOps maturity levels 0→1→2**. Read before L7.
4. **Full Stack Deep Learning** — broader ML-systems course; skim the deployment + monitoring lectures.

## 🗂️ awesome-mlops sections → your labs
| awesome-mlops section | Reinforces | When |
|---|---|---|
| **MLOps Core** | the whole picture | before L1 |
| **Workflow Management** (experiment tracking) | [[mlops/labs/L1-experiment-tracking/README\|L1]] | L1 |
| **Feature Stores** (Feast, Hopsworks) | [[mlops/labs/L2-feature-store/README\|L2]] — concepts behind SageMaker Feature Store | L2 |
| **Model Deployment and Serving** | [[mlops/labs/L4-batch-inference/README\|L4]] + [[mlops/labs/L5-realtime-endpoint/README\|L5]] | L4–L5 |
| **Testing, Monitoring and Maintenance** | [[mlops/labs/L6-model-monitor/README\|L6]] — drift detection | L6 |
| **Infrastructure & Tooling** | [[mlops/labs/L7-pipeline-cicd/README\|L7]] — CI/CD for ML | L7 |
| **Model Governance, Ethics, Responsible AI** | heavily tested on **[[AIF-C01]]** + Azure AI | anytime |
| **Existing ML Systems** (case studies) | how Uber/Netflix/etc. actually do it | after capstone |

## ⚠️ How to use this without drowning
- awesome-mlops is **cloud-agnostic and not exam-aligned** — it explains *concepts*, not AWS click-paths.
- Your **primary** sources stay: the [[MLA-C01]] track + these hands-on labs. awesome-mlops is the *background reading* that makes the services make sense.
- Don't try to read it all. Read the 4 "start here" items; dip into a section only when you reach its lab.

## 🔧 Tools you'll meet (and the AWS service that replaces each)
| Open-source tool (in awesome-mlops) | AWS managed equivalent (what you'll actually use) |
|---|---|
| MLflow Tracking | **SageMaker Experiments** (or managed MLflow in SageMaker) |
| Feast | **SageMaker Feature Store** |
| Seldon / BentoML / KServe | **SageMaker Endpoints** |
| Evidently / whylogs (drift) | **SageMaker Model Monitor** |
| Airflow / Kubeflow Pipelines | **SageMaker Pipelines** (+ Step Functions / EventBridge) |
| DVC (data versioning) | **S3 versioning** + Feature Store |

> Saved in memory as [[awesome-mlops-reference]]. The link directory lives at
> https://github.com/visenger/awesome-mlops.

---
Back to: [[mlops/README]] · [[foundations/06-mlops-basics]]
