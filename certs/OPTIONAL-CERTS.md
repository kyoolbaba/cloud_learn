---
tags: [certs, optional, moc, roadmap]
aliases: [Optional Certs, Future Certs, Optional Certifications]
---
> [[CERTS-MOC|⬅ All certs]] · [[CERT_ROADMAP|Roadmap]] · [[HOME|🏠 Home]]

# 🧭 Optional / future certifications (the "not now" list)

These are **good later**, not now. **Rule #1 still holds: pick one lane and go deep.** Finish the
core AWS ladder first — [[CLF-C02]] → [[AIF-C01]] → [[DEA-C01]] → [[MLA-C01]] 🎯 — *then* pick
**at most one** of these based on the role you're aiming at. Chasing all of them = passing none.

> ⚠️ Codes/availability change — confirm on the official pages before booking
> (AWS → aws.amazon.com/certification · HashiCorp → developer.hashicorp.com/certifications ·
> Databricks → databricks.com/learn/certification · Google → cloud.google.com/learn/certification).

## AWS depth (after the core ladder)

### AWS Solutions Architect – Associate (SAA-C03)
- **What it is:** the most popular AWS cert — design well-architected systems (compute, storage, networking, security, cost) across the whole platform.
- **When to take:** after MLA-C01, if you want broad architecture credibility or a more general cloud role.
- **Why not now:** it's breadth, not your data/ML bullseye; your DEA/MLA work already covers the data slice.
- **Helps role:** Cloud Data Engineer, any cloud-generalist direction.

### AWS Security – Specialty (SCS-C03)
- **What it is:** deep AWS security — IAM, encryption/KMS, detection, incident response, data protection.
- **When to take:** much later, if security/compliance becomes part of your job (e.g. PHI/healthcare data).
- **Why not now:** specialty-level depth; you only need the security *basics* (in CLF-C02 / DEA-C01 D4) for now.
- **Helps role:** Cloud Data Engineer, MLOps in regulated environments.

### AWS Generative AI Developer – Professional (AIP-C01)
- **What it is:** professional-level GenAI development on AWS (Bedrock, RAG, agents, evaluation, guardrails at depth).
- **When to take:** later, if you build production GenAI features on top of your forecasting/data work.
- **Why not now:** professional tier; [[AIF-C01]] already gives you the GenAI foundation you need first.
- **Helps role:** Data Scientist / ML Engineer moving into GenAI products.

## Infrastructure as Code

### HashiCorp Terraform – Associate
- **What it is:** vendor-neutral Infrastructure-as-Code — define cloud infra in code, `plan`/`apply`/`destroy`.
- **When to take:** after MLA-C01, once you've done [[STUDY_PLAN|Module 6]] (Terraform) and want to prove IaC skill.
- **Why not now:** it's a tool cert; learn Terraform *in the labs* first — the cert can wait.
- **Helps role:** MLOps Engineer, Cloud Data Engineer, DevOps-aware Data Scientist.

## Databricks (lakehouse + ML)

### Databricks Certified Data Engineer – Associate
- **What it is:** data engineering on the Databricks lakehouse — Spark, Delta Lake, pipelines, Unity Catalog.
- **When to take:** if your company/target job uses Databricks (very common for data platforms).
- **Why not now:** platform-specific; master open lakehouse concepts first ([[05-lakehouse-basics]] + [[DEA-C01]]).
- **Helps role:** Data Engineer, Cloud Data Engineer.

### Databricks Certified Machine Learning – Professional
- **What it is:** production ML on Databricks — MLflow, feature store, model registry, monitoring at pro depth.
- **When to take:** much later, if you're doing MLOps on Databricks specifically.
- **Why not now:** professional-level + platform-specific; [[MLA-C01]] + [[06-mlops-basics]] come first.
- **Helps role:** ML Engineer, MLOps Engineer (Databricks shops).

## Google Cloud (only if your job moves to GCP)

### GCP Professional Data Engineer  ·  GCP Professional Machine Learning Engineer
- **What they are:** Google Cloud's data-engineering and ML-engineering professional certs (BigQuery, Dataflow, Vertex AI).
- **When to take:** **not now** — only if you actually land on GCP. Concepts transfer ~80% from AWS.
- **Why not now:** you're going **AWS first, Azure later**; adding a *third* cloud now is pure distraction.
- **Helps role:** Data Engineer / ML Engineer at GCP shops (future optionality only).

## Summary table
| Cert | Tier | When | Primary role it helps | Priority |
|---|---|---|---|---|
| **SAA-C03** | Associate | after MLA-C01 | Cloud Data Engineer / generalist | optional |
| **SCS-C03** | Specialty | much later | Cloud DE / MLOps (regulated) | optional later |
| **AIP-C01** | Professional | later | DS/ML → GenAI | optional later |
| **Terraform Associate** | Associate | after Module 6 | MLOps / Cloud DE / DevOps-aware DS | optional |
| **Databricks DE Associate** | Associate | if job uses Databricks | Data / Cloud Data Engineer | optional |
| **Databricks ML Professional** | Professional | much later | ML / MLOps (Databricks) | optional later |
| **GCP PDE / PMLE** | Professional | only if on GCP | DE / ML Engineer (GCP) | not now |

---
See the active ladder in [[CERT_ROADMAP]] · hub: [[CERTS-MOC]] · [[HOME|🏠 Home]]
