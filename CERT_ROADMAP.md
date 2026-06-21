---
tags: [moc, certs, roadmap, aws, azure]
aliases: [Cert Roadmap, Certification Roadmap]
---
> **Built tracks:** [[CLF-C02|CLF-C02]] · [[AIF-C01|AIF-C01]] · [[DEA-C01|DEA-C01]] · [[MLA-C01|MLA-C01 🎯]] · [[OPTIONAL-CERTS|Optional/future]] · hub: [[CERTS-MOC]] · [[HOME|🏠 Home]]

# Cloud Certification Roadmap — for Data roles

**Rule #1: pick one lane and go deep.** Don't chase every cert on both clouds — you'll burn out and
pass none. Choose one cloud + one role-cert, earn it, *then* branch. ~80% of concepts transfer
between AWS and Azure, so the second cloud is fast once you know one.

**Strategy: AWS first, Azure later.** Your work (forecasting with statsforecast/mlforecast) is the
Data Scientist / ML Engineer lane, and that lives best on AWS for you right now.

---

## 🗓️ 2026 certification corrections (read this first)
Exam codes rotate. These changed recently — the roadmap below already reflects them:

| Change | Status | What we do |
|---|---|---|
| **AWS ML Specialty (MLS-C01)** | ❌ **Retired 2026-03-31** | Removed. Use **[[MLA-C01\|MLA-C01]]** (ML Engineer Associate) instead. |
| **Azure DP-100 (Azure Data Scientist)** | ❌ **Retired 2026-06-01** | Removed from the Azure path. |
| **Azure AI-102 (Azure AI Engineer)** | ⚠️ **Retires 2026-06-30** | Not recommended as a long-term path. |
| **Azure AI-900 (AI Fundamentals)** | ♻️ **Replaced by AI-901 after 2026-06-30** | Use **AI-901** for future Azure AI fundamentals. |
| **Azure DP-203 (Data Engineer)** | ❌ Retired earlier → **Fabric** | Use **DP-700** (Fabric DE) + **DP-600** (Fabric Analytics). |

> Always confirm current codes before booking: AWS → aws.amazon.com/certification · Azure → learn.microsoft.com/credentials.

---

## 🔵 AWS-first ladder (your main path)
Do these in order. Steps 1–4 are the core; 5–9 are **optional, later** (see [[OPTIONAL-CERTS]]).

1. **AWS Cloud Practitioner — [[CLF-C02]]** · foundation (IAM, S3, EC2, VPC, pricing, Well-Architected)
2. **AWS AI Practitioner — [[AIF-C01]]** · AI/GenAI foundation (Bedrock, RAG, responsible AI)
3. **AWS Data Engineer – Associate — [[DEA-C01]]** 🛠️ · pipelines (ingestion, S3, Glue, Athena, Redshift, Step Functions)
4. **AWS ML Engineer – Associate — [[MLA-C01]]** 🎯 · **your bullseye** (SageMaker train/deploy/monitor/retrain — your forecasting/ML/MLOps work)
5. *Optional:* **AWS Solutions Architect – Associate (SAA-C03)** · architecture depth
6. *Optional later:* **AWS Security – Specialty (SCS-C03)** · security depth
7. *Optional later:* **AWS Generative AI Developer – Professional (AIP-C01)** · GenAI depth
8. *Optional later:* **HashiCorp Terraform – Associate** · Infrastructure-as-Code
9. *Optional later:* **Databricks** certs · lakehouse/ML on Databricks

→ details on 5–9 in [[OPTIONAL-CERTS]].

## 🟦 Azure-later ladder (only after AWS, or if your org is Azure)
1. **AZ-900** — Azure Fundamentals
2. **DP-900** — Azure Data Fundamentals
3. **AI-901** — Azure AI Fundamentals *(replaces AI-900 after 2026-06-30)*
4. **DP-700** — Fabric Data Engineer Associate
5. **DP-600** — Fabric Analytics Engineer Associate
6. **PL-300** — Power BI Data Analyst Associate
7. **Azure Databricks Data Engineer Associate**
8. **Azure AI Apps and Agents Developer Associate** *(the modern Azure AI path — replaces the retiring AI-102 direction)*

---

## 🎯 Role → cert map (which cert for which job)
| Role | Start | Core cert(s) | Also helpful | Azure (later) |
|---|---|---|---|---|
| **Data Analyst** | CLF-C02 | DEA-C01 (light) + QuickSight | SQL, [[05-lakehouse-basics\|lakehouse]] | DP-900 → PL-300 |
| **Data Scientist** | CLF-C02 + AIF-C01 | **MLA-C01** 🎯 | [[06-mlops-basics\|MLOps]] | AI-901 |
| **ML Engineer** | CLF-C02 + AIF-C01 | **MLA-C01** 🎯 | Terraform, [[04-git-cicd-basics\|CI/CD]] | — |
| **MLOps Engineer** | MLA-C01 | **MLA-C01** + Terraform Assoc. | [[04-git-cicd-basics\|CI/CD]], [[06-mlops-basics\|MLOps]], SAA-C03 | — |
| **Data Engineer** | CLF-C02 | **DEA-C01** 🛠️ | [[05-lakehouse-basics\|lakehouse]], Databricks DE | DP-900 → DP-700/DP-600 |
| **Cloud Data Engineer** | DEA-C01 | DEA-C01 + **SAA-C03** | Terraform, SCS-C03 | DP-700 + Azure Databricks |
| **DevOps-aware Data Scientist** | MLA-C01 | MLA-C01 + Terraform | [[04-git-cicd-basics\|CI/CD]], [[08-kubernetes-basics\|K8s basics]], [[07-finops-basics\|FinOps]] | — |

**Two anchors for you:**
- **[[MLA-C01]]** 🎯 is the **bullseye** — it maps directly to your forecasting / ML / MLOps work (SageMaker build→train→deploy→monitor→retrain).
- **[[DEA-C01]]** 🛠️ is **important** — it's the data-pipeline backbone: ingestion, **S3**, **Glue**, **Athena**, **Redshift**, **Step Functions**, Kinesis/EMR, Lake Formation. Everything ML consumes comes through here.

---

## ⚠️ Do NOT chase everything
- **Finish the core 4 (CLF → AIF → DEA → MLA) before touching anything optional.** One lane, deep.
- **Skip retired exams** (MLS-C01, DP-100) and don't start a path that's about to retire (AI-102).
- **One cloud first.** Don't add Azure *or* GCP until the AWS core is done — concepts transfer, so the 2nd cloud is fast later.
- **A cert is a checkpoint, not the goal** — the hands-on ([[STUDY_PLAN]] + projects) is what makes you employable; the cert just proves it.

## 🧭 Optional / future certs (the "not now" list)
Full detail — what each is, when to take it, why not now, which role it helps — lives in **[[OPTIONAL-CERTS]]**:

| Cert | When | Helps role |
|---|---|---|
| SAA-C03 (Solutions Architect Assoc.) | after MLA-C01 | Cloud Data Engineer / generalist |
| SCS-C03 (Security Specialty) | much later | Cloud DE / MLOps (regulated) |
| Terraform Associate | after Module 6 | MLOps / Cloud DE / DevOps-aware DS |
| Databricks Data Engineer Assoc. | if job uses Databricks | Data / Cloud Data Engineer |
| Databricks ML Professional | much later | ML / MLOps (Databricks) |
| AWS AIP-C01 (GenAI Dev Pro) | later | DS/ML → GenAI |
| GCP Pro Data Engineer / ML Engineer | **not now** (only if on GCP) | DE / ML Engineer (GCP) |

---

## How each cert track is built (Learn → Hands-on → Checkpoint)
Each `certs/<cert>/` track has:
1. **Domain breakdown** — official exam domains + weightings (the theory spine).
2. **Per-domain notes** — concise theory, only what the exam tests, with a runnable **Hands-on** code block.
3. **Practice questions** — a 25-Q mock with explained answers.
4. **Readiness checklist** — "can you do/explain X" gate before booking.

Existing leverage:
- **CLF-C02:** `labs/m1`–`m3`, `projects/00–05, 11` already cover IAM/S3/EC2/VPC/IaC hands-on.
- **DEA-C01:** add Glue, Athena, Redshift, Kinesis, EMR on top of our S3/Step Functions/SQS work + [[05-lakehouse-basics|lakehouse]].
- **MLA-C01:** SageMaker end-to-end (train/tune/deploy/monitor/pipelines) — ties straight into your forecasting engine + [[06-mlops-basics|MLOps]].

---
See also: [[STUDY_PLAN]] (the hands-on plan) · [[PROGRESS]] (tracker) · [[CERTS-MOC]] (cert hub) · [[OPTIONAL-CERTS]]
