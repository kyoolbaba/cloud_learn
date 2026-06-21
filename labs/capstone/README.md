---
tags: [lab, capstone]
aliases: [capstone lab]
---
> [[labs/README|⬅ Labs]] | [[HOME|Home]] | [[STUDY_PLAN|Plan]]

# 🏁 Capstone — the real "Run in cloud" toggle

Everything from M0–M6 assembles here. You flip a toggle in the dashboard, watch a
live progress bar while thousands of SKUs forecast on cloud hardware, and get the
results back as registered tables — on a backend you can `apply`/`destroy` in one
command.

## Architecture

```
┌───────────────────────── db_polars_app.py (your app) ─────────────────────────┐
│  "Run in cloud" toggle                                                          │
│     POST /api/ts/run?target=cloud   ── app_cloud_routes.py ──┐                  │
│     GET  /api/ts/status/{job_id}  (polls progress bar) ◄──┐  │                  │
│     GET  /api/ts/result/{job_id}  (presigned -> _register)│  │                  │
└───────────────────────────────────────────────────────────┼──┼─────────────────┘
                                                            │  │ 1. upload job.json
                            4. progress.json / forecast.parquet│  ▼
                                          ┌──────────────────  S3 bucket  ─────────┐
                                          │ jobs/<id>/{job.json,progress.json,...}  │
                                          └─────────────────────────────────────────┘
                                                            │  │ 2. trigger
                                                            │  ▼
                                   API Gateway ──► Lambda ──► Fargate task(s)
                                                 (start)     forecast_engine.py  (M4)
                                                              │  big job? Step Functions
                                                              │  Map fans out N shards (M5)
                                                              ▼  3. write results to S3
                                          (IaC: Terraform builds all of this — M6)
```

## How the pieces map to modules

| Piece | File | Module |
|---|---|---|
| Container/image | `Dockerfile`, `forecast_engine.py` | M2 + M4 |
| App toggle + status | `app_cloud_routes.py` | M1 (HTTP) + M3 (S3) |
| Trigger | API Gateway → `lambda_start_fargate.py` | M4 |
| Worker | `forecast_engine.py` writing `progress.json`/`forecast.parquet` | M3 + M4 |
| Big-job fan-out | `statemachine.asl.json` (Map) | M5 |
| Guardrails | least-priv IAM, budget alarm, `autostop_lambda.py` | M3 + M6 |
| IaC | `m6-hardening/terraform/` | M6 |

## Assemble it

1. **Container:** build `forecast-engine` and push to ECR.
   ```bash
   docker build -t forecast-engine:0.1 .
   ../m4-serverless/push_to_ecr.sh        # retag/push to ECR
   ```
2. **Backend (IaC):** `terraform apply` the bucket + ECR + roles (M6), then register
   the Fargate task def (M4) and wire API Gateway → Lambda.
3. **App side:** add to `db_polars_app.py`:
   ```python
   from app_cloud_routes import router as cloud_router
   app.include_router(cloud_router)
   # set env: FORECAST_BUCKET, AWS_REGION, TRIGGER=api, CLOUD_API_URL=<api-gw-url>
   ```
4. **Progress UI:** the front-end polls `GET /api/ts/status/{job_id}` every ~2s →
   progress bar + ETA; on `done_flag`, calls `/api/ts/result/{job_id}` and
   `_register()`s the parquet as a table (flows into charts/export/dashboard).
5. **Guardrails:** confirm budget alarm, least-privilege roles, and
   `forecast-autostop` schedule are live before real runs.

## Test the flow locally first (no cloud)

Run `forecast_engine.py` against a local S3 stand-in or just verify the progress
contract end-to-end with the M3 `orchestrate_run.py` (EC2 path) — it already does
upload → run → poll → download. The capstone just moves the trigger to
API Gateway/Fargate and the `main()` driver into FastAPI routes.

## Done =
Flip the toggle → "provisioning…" → live progress bar → results as tables, with a
backend you `terraform destroy` when idle and a bill you control. ✅

**Tick the final box in `../../PROGRESS.md`.**

---

### Definition-of-done checklist
- [ ] `forecast-engine` image in ECR
- [ ] `POST /api/ts/run?target=cloud` uploads job.json + triggers a run
- [ ] Fargate task runs `forecast_engine.py`, writes progress.json + forecast.parquet
- [ ] `GET /api/ts/status/{job_id}` drives a live progress bar
- [ ] results download via presigned URL and `_register()` as tables
- [ ] big jobs fan out via Step Functions `Map` and aggregate
- [ ] least-priv IAM, budget alarm, autostop kill switch all on
- [ ] whole backend is `terraform apply` / `terraform destroy`
