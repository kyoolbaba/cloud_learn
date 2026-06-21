---
tags: [portfolio, moc, hands-on]
aliases: [Portfolio, Proof of Work, Portfolio Index]
---
> [[HOME|🏠 Home]] · [[STUDY_PLAN|Study plan (briefs)]] · [[PROGRESS|Tracker]] · [[CERTS-MOC|Certs]]

# 🗂️ Portfolio — proof of work

This folder is where your **mini-project proofs** live. The full brief for each project (what to build,
tools, skills, completion proof) is in [[STUDY_PLAN]] → *Mini-project portfolio*; the tickable checklist
is in [[PROGRESS]]. **Here is where the actual evidence goes** — so by project 18 you have an
end-to-end "laptop → cloud forecasting" showcase to show a recruiter.

## How to use this folder
1. Finish a mini-project in [[STUDY_PLAN]].
2. Open that project's subfolder — **already created** (`01-linux/` … `18-capstone/`), each with a pre-seeded `README.md`.
3. Drop the **proof artifacts** in it (script, screenshot, `.parquet`, exported result, a short note).
4. **Fill in** that subfolder's `README.md` — what you built, the date, and links to your artifacts.
5. Flip its row to ✅ in the table below **and** tick it in [[PROGRESS]].

> 🔒 **Never commit secrets.** No access keys, `.env`, `config.sh`, account IDs, or customer data — this may become a *public* repo. Screenshots only; blur any account numbers. Everything is **personal `learn` account or local** — never the company account.

## Project index
| # | Mini-project | Suggested subfolder | Proof to capture | Done |
|---|---|---|---|---|
| 1 | Linux — Worker bootstrap kit | `01-linux/` | `setup_worker.sh` + `systemctl status` screenshot | ⬜ |
| 2 | Networking — Reverse-proxied API | `02-networking/` | `nginx.conf` + saved `curl -v` trace | ⬜ |
| 3 | Docker — Containerized app | `03-docker/` | Docker Hub URL + UI screenshot | ⬜ |
| 4 | Git + CI/CD — Auto-tested repo | `04-git-cicd/` | repo link + green Actions badge + merged PR | ⬜ |
| 5 | AWS Core — Remote run (boto3) | `05-aws-core/` | `result.parquet` + the boto3 script | ⬜ |
| 6 | S3 Data Lake — Partitioned Parquet | `06-s3-data-lake/` | S3 listing screenshot + CSV-vs-Parquet note | ⬜ |
| 7 | EC2 — Disposable benchmark box | `07-ec2/` | `benchmark.md` + "terminated" screenshot | ⬜ |
| 8 | Lambda/API GW — Trigger API | `08-lambda-apigw/` | saved `curl …/run` → `job_id` | ⬜ |
| 9 | ECR/Fargate — Serverless run | `09-ecr-fargate/` | Fargate CloudWatch log + S3 output | ⬜ |
| 10 | SQS — Parallel shard queue | `10-sqs/` | run log + DLQ message | ⬜ |
| 11 | Step Functions — Fan-out/aggregate | `11-step-functions/` | green execution graph + `forecast.parquet` | ⬜ |
| 12 | SageMaker/MLOps — Train→register→score | `12-sagemaker-mlops/` | registered model screenshot + `metrics.parquet` | ⬜ |
| 13 | Lakehouse — Glue + Athena | `13-lakehouse/` | Athena result CSV + Delta/Iceberg/Hudi note | ⬜ |
| 14 | Terraform — One-command backend | `14-terraform/` | `main.tf` + `plan` output + clean `destroy` | ⬜ |
| 15 | Security — Least-privilege + KMS | `15-security/` | policy JSON + denied-action screenshot | ⬜ |
| 16 | FinOps — Cost guardrails | `16-finops/` | budget-alarm screenshot + `TEARDOWN.md` | ⬜ |
| 17 | Kubernetes — Local deploy | `17-kubernetes/` | `kubectl get pods` (×3) + manifests | ⬜ |
| 18 | 🏁 Capstone — Cloud toggle | `18-capstone/` | screen-recording: toggle → progress → tables | ⬜ |

**Progress: 0 / 18.** Update the count as you go.

## 📋 Per-project writeup template (already seeded into each subfolder's `README.md`)
```markdown
---
tags: [portfolio, <domain>]
---
# <NN> · <Mini-project name>

- **Domain:** <e.g. Docker>
- **What I built:** <one or two sentences>
- **Tools used:** <list>
- **Skills learned:** <list>
- **Completion proof:** <link/screenshot/file in this folder>
- **Date completed:** <YYYY-MM-DD>

## Notes
<what was hard, what I'd do differently, links to the STUDY_PLAN brief>
```

---
Back to: [[HOME]] · [[STUDY_PLAN]] · [[PROGRESS]]
