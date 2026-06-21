"""app_cloud_routes.py — the "Run in cloud" toggle, as a FastAPI router.

Graft this into db_polars_app.py:
    from app_cloud_routes import router as cloud_router
    app.include_router(cloud_router)

It implements the app side of the capstone:
  POST /api/ts/run?target=cloud   -> upload job.json to S3, trigger the cloud run,
                                     return {job_id}
  GET  /api/ts/status/{job_id}    -> read progress.json from S3 -> {done,total,stage,eta}
  GET  /api/ts/result/{job_id}    -> presigned URL to forecast.parquet (for _register())

Two ways to trigger the run (pick via TRIGGER env):
  - "api"      : POST to your API Gateway URL (Module 4)  [recommended for Fargate]
  - "ec2"      : call orchestrate_run-style EC2 launch     [Module 3 path]
The status/result endpoints are identical either way (both read S3).

Env:  FORECAST_BUCKET, AWS_REGION, TRIGGER (api|ec2), CLOUD_API_URL (if api)
"""
from __future__ import annotations

import json
import os
import uuid

import boto3
import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

REGION = os.environ.get("AWS_REGION", "ap-south-1")
BUCKET = os.environ.get("FORECAST_BUCKET", "milan-forecast-lab")
TRIGGER = os.environ.get("TRIGGER", "api")
CLOUD_API_URL = os.environ.get("CLOUD_API_URL", "")

s3 = boto3.client("s3", region_name=REGION)
router = APIRouter(prefix="/api/ts", tags=["cloud-forecast"])


class RunRequest(BaseModel):
    mapping: dict = {}          # your column mapping (date/target/keys)
    models: list[str] = ["trend"]
    horizon: int = 6
    n_series: int = 50
    cv: dict = {}               # cross-validation settings
    shards: int = 1             # >1 => fan-out path (Step Functions Map)


@router.post("/run")
def run(req: RunRequest, target: str = "local"):
    if target != "cloud":
        raise HTTPException(400, "this route handles target=cloud; local stays in-process")

    job_id = uuid.uuid4().hex[:8]
    prefix = f"jobs/{job_id}"

    # 1) upload the job spec to S3
    s3.put_object(
        Bucket=BUCKET, Key=f"{prefix}/job.json",
        Body=json.dumps({"job_id": job_id, **req.model_dump()}).encode(),
        ContentType="application/json",
    )
    # seed an initial progress so the UI shows "provisioning..." immediately
    s3.put_object(
        Bucket=BUCKET, Key=f"{prefix}/progress.json",
        Body=json.dumps({"done": 0, "total": req.n_series, "stage": "provisioning",
                         "eta_seconds": None}).encode(),
    )

    # 2) trigger the cloud run
    if TRIGGER == "api":
        if not CLOUD_API_URL:
            raise HTTPException(500, "CLOUD_API_URL not set")
        r = httpx.post(CLOUD_API_URL, json={"job_id": job_id, "bucket": BUCKET}, timeout=15)
        r.raise_for_status()
    else:
        raise HTTPException(501, "ec2 trigger: call your orchestrate_run launch here")

    return {"job_id": job_id, "status_url": f"/api/ts/status/{job_id}"}


@router.get("/status/{job_id}")
def status(job_id: str):
    key = f"jobs/{job_id}/progress.json"
    try:
        p = json.loads(s3.get_object(Bucket=BUCKET, Key=key)["Body"].read())
    except s3.exceptions.NoSuchKey:
        raise HTTPException(404, "unknown job_id (or not started yet)")
    pct = round(100 * p["done"] / max(p["total"], 1), 1)
    return {**p, "percent": pct, "done_flag": p["stage"] == "done"}


@router.get("/result/{job_id}")
def result(job_id: str):
    # presigned URL the front-end can fetch, then _register() as a table
    key = f"jobs/{job_id}/forecast.parquet"
    try:
        s3.head_object(Bucket=BUCKET, Key=key)
    except Exception:
        raise HTTPException(409, "result not ready")
    url = s3.generate_presigned_url("get_object",
        Params={"Bucket": BUCKET, "Key": key}, ExpiresIn=3600)
    return {"job_id": job_id, "download_url": url}
