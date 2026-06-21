"""forecast_engine.py — the worker that runs inside the container (capstone version).

Production-flavored evolution of m3-aws/worker.py:
  - supports BOTH a single job and a SHARD of a fan-out (Step Functions Map)
  - writes progress.json frequently so the app's progress bar is smooth
  - writes forecast.parquet (single) or shard{i}.parquet (fan-out)
  - self-contained: gets everything from env (BUCKET, JOB_ID, optional SHARD)

Swap the `_forecast_series` body for your real statsforecast/mlforecast call.

Run in the container:  BUCKET=... JOB_ID=... [SHARD=3] python3 forecast_engine.py
"""
from __future__ import annotations

import json
import os
import time

import boto3
import pandas as pd

BUCKET = os.environ["BUCKET"]
JOB_ID = os.environ["JOB_ID"]
SHARD = os.environ.get("SHARD")            # set by the Map fan-out; None for single runs
PREFIX = f"jobs/{JOB_ID}"
s3 = boto3.client("s3")


def _put_json(key, obj):
    s3.put_object(Bucket=BUCKET, Key=key, Body=json.dumps(obj).encode(),
                  ContentType="application/json")


def _progress(done, total, stage, started):
    elapsed = time.time() - started
    rate = done / elapsed if elapsed else 0
    eta = (total - done) / rate if rate else None
    # shard runs report to their own progress file; the aggregator merges them
    name = f"progress-shard{SHARD}.json" if SHARD is not None else "progress.json"
    _put_json(f"{PREFIX}/{name}",
              {"done": done, "total": total, "stage": stage,
               "eta_seconds": round(eta, 1) if eta else None})


def _forecast_series(series_id: str, horizon: int) -> list[dict]:
    # >>> replace this stub with the real engine (statsforecast/mlforecast/etc.) <<<
    base = 100 + (hash(series_id) % 50)
    return [{"series_id": series_id, "h": h, "yhat": base + h} for h in range(1, horizon + 1)]


def main():
    started = time.time()
    job = json.loads(s3.get_object(Bucket=BUCKET, Key=f"{PREFIX}/job.json")["Body"].read())
    horizon = int(job.get("horizon", 6))
    n_series = int(job.get("n_series", 50))

    # which series this process is responsible for
    if SHARD is not None:
        total_shards = int(job.get("shards", 1))
        ids = [f"sku_{i}" for i in range(n_series) if i % total_shards == int(SHARD)]
        out_key = f"{PREFIX}/shard{SHARD}.parquet"
    else:
        ids = [f"sku_{i}" for i in range(n_series)]
        out_key = f"{PREFIX}/forecast.parquet"

    rows = []
    for idx, sid in enumerate(ids):
        rows.extend(_forecast_series(sid, horizon))
        if idx % 5 == 0 or idx == len(ids) - 1:
            _progress(idx + 1, len(ids), "forecasting", started)

    local = "/tmp/out.parquet"
    pd.DataFrame(rows).to_parquet(local, index=False)
    s3.upload_file(local, BUCKET, out_key)
    _progress(len(ids), len(ids), "done", started)
    print(f"done -> s3://{BUCKET}/{out_key}")


if __name__ == "__main__":
    main()
