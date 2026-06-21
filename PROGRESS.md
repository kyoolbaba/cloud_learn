---
tags: [moc, progress, tracker]
aliases: [Progress, Tracker]
---
> [[HOME|🏠 Home]] · [[START-HERE|Start here]] · [[STUDY_PLAN|Plan]] · [[CERT_ROADMAP|Certs]]

# Progress Tracker — Cloud & Infrastructure Study Plan

Companion to `STUDY_PLAN.md`. Tick items as you finish the labs. Each module's
hands-on guide lives in `labs/<module>/README.md`.

**Current position:** ⚠️ Set up a **personal AWS account** first
(`projects/SETUP-personal-aws.md`) — the current `default` profile is a **shared
company account** (857810275001, Healthium prod data), unsafe for create/destroy labs.
After the `learn` profile points at a personal account → **Project 00 (budget alarm)**.
WSL/Linux is optional; the AWS projects run from Windows.

## Project track (build one thing per service — see `projects/`)
- [ ] 00 — Lock the account + budget alarm  ← **do first**
- [ ] 01 — S3 file vault
- [ ] 02 — EC2 disposable dev box + benchmark
- [ ] 03 — Self-configuring web server (user-data)
- [ ] 04 — Least-privilege IAM key
- [ ] 05 — Serverless API (Lambda + API Gateway)
- [ ] 06 — Auto-process uploads (S3 → Lambda)
- [ ] 07 — Container in the cloud (ECR + Fargate)
- [ ] 08 — Parallel job queue (SQS)
- [ ] 09 — Fan-out & aggregate (Step Functions Map)
- [ ] 10 — Cost guardian (CloudWatch + autostop)
- [ ] 11 — One-command backend (Terraform)
- [ ] 12 — 🏁 Capstone: cloud forecast toggle

## Certification track (AWS now, Azure later — see `CERT_ROADMAP.md`)
Focus: **AWS Cloud Practitioner (CLF-C02)** first → then ML Engineer Assoc. (MLA-C01) or Data Engineer Assoc. (DEA-C01).
- [ ] CLF-C02 Domain 1 — Cloud Concepts (notes + practice Qs)
- [ ] CLF-C02 Domain 2 — Security & Compliance
- [ ] CLF-C02 Domain 3 — Technology & Services
- [ ] CLF-C02 Domain 4 — Billing, Pricing & Support
- [ ] CLF-C02 mock exam ≥ 18/25
- [ ] CLF-C02 readiness checklist all ticked → **book exam**
Track lives in `certs/aws-cloud-practitioner-clf-c02/`. The projects above double as cert hands-on.

**Cert tracks built (2026-06-21):** [[CLF-C02|CLF-C02]] · [[AIF-C01|AIF-C01]] · [[DEA-C01|DEA-C01]] · [[MLA-C01|MLA-C01 🎯]] — hub: [[CERTS-MOC]]. After CLF-C02, the data-science ladder is AIF → DEA → MLA.

### 🔵 AWS path (core — do in order)
- [ ] **CLF-C02** — Cloud Practitioner (foundation)
- [ ] **AIF-C01** — AI Practitioner
- [ ] **DEA-C01** — Data Engineer Associate 🛠️ (S3, Glue, Athena, Redshift, Step Functions, pipelines)
- [ ] **MLA-C01** — ML Engineer Associate 🎯 (your bullseye)

### 🟡 Optional later (AWS depth — pick at most one; see [[OPTIONAL-CERTS]])
- [ ] SAA-C03 (Solutions Architect Associate)
- [ ] SCS-C03 (Security Specialty)
- [ ] Terraform Associate
- [ ] Databricks (Data Engineer Associate / ML Professional)
- [ ] AIP-C01 (GenAI Developer Professional)

### 🟦 Azure later (only after the AWS core)
- [ ] AZ-900 · DP-900 · **AI-901** (replaces AI-900) · DP-700 · DP-600 · PL-300 · Azure Databricks Data Engineer

> Retired / avoid: ~~MLS-C01~~ (AWS ML Specialty — retired 2026-03-31), ~~DP-100~~ (Azure Data Scientist — retired 2026-06-01), AI-102 (retires 2026-06-30 — not a long-term path). Details in [[CERT_ROADMAP]] § 2026 corrections.

---

## Environment baseline (checked 2026-06-20)

| Component | Status | Notes |
|---|---|---|
| WSL2 engine | ✅ | v2.5.10, kernel 6.6.87, default version 2 |
| Ubuntu distro | ⬜ | install with `wsl --install -d Ubuntu` |
| Docker Desktop | ✅ | CLI present; verify it runs in Module 2 |
| Python | ✅ | Anaconda on Windows; we use Linux python3 in WSL |
| Git | ✅ | |
| Cursor / VS Code | ✅ | `code .` opens this folder |

---

## Fundamentals
- [ ] WSL2 Ubuntu installed; comfortable in bash
- [ ] Permissions (octal + rwx) instant-readable
- [ ] Background processes, nohup, tmux
- [ ] systemd service created; cron job scheduled
- [ ] OverTheWire Bandit 0→15
- [ ] Identify listening ports; explain TCP vs UDP, public vs private IP
- [ ] curl a service and read headers/status; SSH tunnel works
- [ ] TLS cert inspected; nginx reverse proxy in front of the app

## Docker
- [ ] Containerized `db_polars_app.py` with deps; runs with port mapped + volume
- [ ] `.dockerignore` + layer caching understood
- [ ] Image pushed to a registry

## AWS core
- [ ] Root MFA + IAM admin user + **budget alarm**
- [ ] S3 via CLI and boto3 (incl. presigned URL)
- [ ] EC2 launch → SSH → run → stop → terminate
- [ ] user-data bootstrap works
- [ ] Least-privilege IAM policy written & tested
- [ ] CloudWatch alarm created
- [ ] boto3 script drives a full remote run (job→start→poll→result→stop)

## Serverless & scale
- [ ] Image in ECR; runs on Fargate
- [ ] Lambda starts a Fargate task; API Gateway / S3 trigger wired
- [ ] SQS producer/consumer
- [ ] Step Functions Map fan-out + aggregation
- [ ] (opt) AWS Batch array job; SageMaker Processing job

## Hardening
- [ ] Terraform apply/destroy the backend
- [ ] Secrets in Secrets Manager/SSM (zero hardcoded creds)
- [ ] VPC private subnet + tight security groups
- [ ] Auto-stop / max-runtime kill switch

## Capstone
- [ ] "Run in cloud" toggle → cloud forecast → live progress bar → results registered as tables

---

## Git + CI/CD
> Learn: [[04-git-cicd-basics]] · [[STUDY_PLAN|Module 2.5]]
- [ ] Git repo created
- [ ] Branching and pull request practiced
- [ ] Merge conflict resolved
- [ ] pytest workflow created
- [ ] Docker image built in CI
- [ ] Image pushed to ECR
- [ ] ECS/Fargate deployment triggered from CI/CD

## Lakehouse
> Learn: [[05-lakehouse-basics]] · [[STUDY_PLAN|Module 5.5]] · cert [[DEA-C01]]
- [ ] CSV vs Parquet comparison completed
- [ ] S3 partitioning lab completed
- [ ] Glue table created
- [ ] Athena query tested
- [ ] Schema evolution note written
- [ ] Delta/Iceberg/Hudi comparison note written
- [ ] Lake Formation / Unity Catalog governance notes written

## MLOps
> Learn: [[06-mlops-basics]] · **hands-on: [[mlops/README|☁️ MLOps track (cloud-only)]]** · cert [[MLA-C01]] 🎯
> Setup once: [[mlops/00-cloud-workspace|SageMaker Studio workspace]] · craft layer: [[mlops/code-craft]]
- [ ] 00 — Cloud workspace (Studio + CloudShell + S3 bucket) set up
- [ ] L1 — Experiment tracking (SageMaker Experiments)
- [ ] L2 — Feature store (online + offline)
- [ ] L3 — Training job → model registry + approval gate
- [ ] L4 — Batch inference (Batch Transform)
- [ ] L5 — Real-time endpoint (deployed **and deleted**)
- [ ] L6 — Model Monitor + drift alarm
- [ ] L7 — SageMaker Pipeline (train→eval→register)
- [ ] 🏁 Capstone — drift→retrain loop (EventBridge)
- [ ] Code-craft self-check passed (src modules, config, tests, logging) → [[mlops/code-craft]]

## FinOps
> Learn: [[07-finops-basics]] · [[STUDY_PLAN|Module 6.5]]
- [ ] Pricing estimate created before lab
- [ ] Budget alarm active
- [ ] Cost Explorer checked
- [ ] NAT Gateway cost warning understood
- [ ] SageMaker endpoint cleanup checklist created
- [ ] CloudWatch logs cost warning understood
- [ ] S3 lifecycle rule tested

## Kubernetes basics
> Learn: [[08-kubernetes-basics]] · [[STUDY_PLAN|Module 6.6]]
- [ ] Local cluster created
- [ ] Pod deployed
- [ ] Service exposed
- [ ] Deployment scaled
- [ ] Logs checked
- [ ] ConfigMap and Secret tested
- [ ] ECS vs Kubernetes comparison note written

## Mini-project portfolio (one shippable output per domain)
> Full briefs in [[STUDY_PLAN]] → *Mini-project portfolio*. Collect every proof in the [[portfolio/README|`portfolio/`]] folder (or a public GitHub repo). **Personal `learn` account only.**
- [ ] 1. Linux — `setup_worker.sh` + systemd service active (screenshot)
- [ ] 2. Networking — FastAPI behind nginx + saved `curl -v` lifecycle note
- [ ] 3. Docker — forecasting image on Docker Hub (public URL) + UI screenshot
- [ ] 4. Git + CI/CD — repo with **green GitHub Actions badge** + one merged PR
- [ ] 5. AWS Core — boto3 remote run → `result.parquet` downloaded
- [ ] 6. S3 Data Lake — partitioned Parquet lake + CSV-vs-Parquet size/scan note
- [ ] 7. EC2 Compute — `benchmark.md` + console shows instance terminated
- [ ] 8. Lambda/API Gateway — `curl .../run` returns a real `job_id` (saved)
- [ ] 9. ECR/Fargate — Fargate task CloudWatch log + S3 output
- [ ] 10. SQS — producer/consumer run log + a message in the DLQ
- [ ] 11. Step Functions — green execution graph + aggregated `forecast.parquet`
- [ ] 12. SageMaker/MLOps — registered model version + `metrics.parquet`
- [ ] 13. Lakehouse — Athena query result (CSV) + Delta/Iceberg/Hudi note
- [ ] 14. Terraform — `main.tf` + saved `plan` + clean `destroy` proof
- [ ] 15. Security — least-privilege IAM policy JSON + denied-action screenshot
- [ ] 16. FinOps — active budget alarm screenshot + `TEARDOWN.md`
- [ ] 17. Kubernetes — local `kubectl get pods` (3 replicas) + manifests (no cloud)
- [ ] 18. Capstone — screen-recording: toggle → progress bar → results as tables

---

## Session log
- 2026-06-20 — Set up lab workspace. WSL engine confirmed; installing Ubuntu next.
- 2026-06-20 — Built ALL ready-made code: M0–M2 (runnable now) + M3–M6 + capstone
  (cloud templates, need AWS account + `m3-aws/config.sh` filled in).
- 2026-06-20 — AWS verified (IAM user `milan`, acct 857810275001, ap-south-1, CLI
  2.17 + boto3 1.43). Added `projects/` — 13 small build-projects, one per service.
- 2026-06-20 — ⚠️ Discovered `default` account 857810275001 is a SHARED COMPANY account
  (Healthium prod buckets + 2 running EC2 instances; `milan` is a restricted dev user
  denied IAM/Budgets/CloudWatch/Lambda). Paused live setup. Plan: create a separate
  personal account + `learn` profile (`projects/SETUP-personal-aws.md`), wired all
  configs to `AWS_PROFILE=learn`. Resume Project 00 once `learn` profile is verified.
- 2026-06-20 — Direction set: certifications for data-science roles, **AWS now / Azure later**,
  **foundation first**. Added `CERT_ROADMAP.md` + full `certs/aws-cloud-practitioner-clf-c02/`
  track (4 domain study sheets + 25-Q mock + readiness checklist).
- 2026-06-21 — Built 3 more full cert tracks: **AIF-C01**, **DEA-C01**, **MLA-C01 🎯** (each = README +
  per-domain notes + 25-Q mock + readiness checklist). Made `certs/` an **Obsidian vault**: YAML
  frontmatter + tags + wiki-links on every note, plus `HOME.md` and `certs/CERTS-MOC.md` hubs.
- 2026-06-21 — Upgraded the vault into a full learning system. Rewrote `CERT_ROADMAP.md` with
  **2026 cert corrections** (MLS-C01 + DP-100 retired, AI-102 not long-term, AI-900→**AI-901**),
  AWS-first/Azure-later ladders, role→cert map, and an optional-cert table. Added STUDY_PLAN
  modules **M2.5 Git/CI-CD · M5.5 Lakehouse · M5.6 MLOps · M6.5 FinOps · M6.6 Kubernetes**, new
  beginner notes `foundations/04–08`, `certs/OPTIONAL-CERTS.md`, and the new checklists above.
- 2026-06-21 — Added a **mini-project portfolio**: one shippable, output-producing build per domain
  (18 total, Linux → Capstone) in `STUDY_PLAN.md`, with a matching proof-checklist here. Each leaves
  a concrete artifact (repo, screenshot, Parquet, CI badge) — all local or personal `learn` account.
