---
tags: [project, 12-capstone-cloud-toggle]
aliases: [12-capstone-cloud-toggle]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]] | [[PROGRESS|Tracker]]

# Project 12 — 🏁 Capstone: the cloud forecast toggle

**Service:** everything · **Time:** a real project · **Cost:** pennies (tear down)

## Goal
Assemble Projects 01–11 into the actual feature: a **"Run in cloud" toggle** that
uploads a job, runs the forecast on cloud hardware, streams a **live progress bar**,
and returns results as tables.

## You've already built every piece
| Piece | From project |
|---|---|
| S3 data exchange + presigned download | 01 |
| Compute (EC2 path / Fargate path) | 02–03 / 07 |
| Least-privilege IAM + roles | 04 |
| API Gateway → Lambda trigger | 05 |
| Event-driven auto-start | 06 |
| Container in ECR on Fargate | 07 |
| Parallel fan-out for big jobs | 08–09 |
| Budget alarm + autostop kill switch | 00, 10 |
| One-command backend | 11 |

## Build it
Follow **`../../labs/capstone/README.md`** — it has the full architecture diagram and
the assembly steps. The key files:
- `app_cloud_routes.py` → graft into `db_polars_app.py`: `POST /api/ts/run?target=cloud`,
  `GET /api/ts/status/{job_id}`, `GET /api/ts/result/{job_id}`
- `forecast_engine.py` → the worker (swap the stub for your real statsforecast/mlforecast engine)
- `Dockerfile`, `job.example.json`

Flow: toggle → upload `job.json` → API Gateway/Lambda starts Fargate (or Step
Functions `Map` for big jobs) → engine writes `progress.json` + `forecast.parquet` →
app polls `/status` for the bar → on done, presigned download → `_register()` as tables.

## ✅ Done (the whole plan) when
- [ ] Flipping the toggle runs a forecast on cloud hardware
- [ ] A live progress bar + ETA updates from `progress.json`
- [ ] Results download and register as tables (flow into charts/export/dashboard)
- [ ] Big jobs fan out in parallel and aggregate
- [ ] Least-priv IAM, budget alarm, autostop all on
- [ ] The backend is `terraform apply` / `terraform destroy`

## 🧹 Teardown
`terraform destroy` the backend; delete ECR images, Lambdas, APIs, state machines;
empty the bucket. Stand it back up only when you need it.

## 🎓 You're done
You flip a toggle, watch thousands of SKUs forecast on cloud hardware with a live
progress bar, and get results back as tables — on a backend you control end to end,
with a bill you control. That was the whole point.
