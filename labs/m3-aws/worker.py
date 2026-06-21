#!/usr/bin/env python3
"""worker.py — runs ON the cloud instance. The "forecast engine" stand-in.

Lifecycle (this is exactly what the real forecast_engine.py will do):
  1. read job.json from S3            (what to forecast)
  2. loop over series, "forecasting"  (replace with real statsforecast/mlforecast)
  3. write progress.json every few series  -> the app's progress bar reads this
  4. on finish, write forecast.parquet + a final progress.json {stage:"done"}

It gets BUCKET + JOB_ID from environment variables set by the user-data bootstrap.
Auth comes from the instance's IAM ROLE (no keys on the box — the secure pattern).

Run on the instance:  BUCKET=... JOB_ID=... python3 worker.py
"""
import json
import os
import time

import boto3
import pandas as pd

BUCKET = os.environ["BUCKET"]
JOB_ID = os.environ["JOB_ID"]
PREFIX = f"jobs/{JOB_ID}"
s3 = boto3.client("s3")


def put_json(key, obj):
    s3.put_object(Bucket=BUCKET, Key=key, Body=json.dumps(obj).encode(), ContentType="application/json")


def write_progress(done, total, stage, started):
    elapsed = time.time() - started
    rate = done / elapsed if elapsed > 0 else 0
    eta = (total - done) / rate if rate > 0 else None
    put_json(f"{PREFIX}/progress.json",
             {"done": done, "total": total, "stage": stage,
              "eta_seconds": round(eta, 1) if eta else None})


def main():
    started = time.time()
    write_progress(0, 1, "starting", started)

    # 1) read the job spec
    job = json.loads(s3.get_object(Bucket=BUCKET, Key=f"{PREFIX}/job.json")["Body"].read())
    n_series = int(job.get("n_series", 50))
    horizon = int(job.get("horizon", 6))
    print(f"job {JOB_ID}: {n_series} series, horizon {horizon}")

    # 2) "forecast" each series (swap this block for the real engine)
    rows = []
    for i in range(n_series):
        time.sleep(0.1)                       # pretend each series takes work
        base = 100 + i
        for h in range(1, horizon + 1):
            rows.append({"series_id": f"sku_{i}", "h": h, "yhat": base + h})
        if i % 5 == 0 or i == n_series - 1:   # 3) report progress periodically
            write_progress(i + 1, n_series, "forecasting", started)
            print(f"  {i + 1}/{n_series}")

    # 4) write the result and mark done
    df = pd.DataFrame(rows)
    local = "/tmp/forecast.parquet"
    df.to_parquet(local, index=False)
    s3.upload_file(local, BUCKET, f"{PREFIX}/forecast.parquet")
    write_progress(n_series, n_series, "done", started)
    print(f"done -> s3://{BUCKET}/{PREFIX}/forecast.parquet")


if __name__ == "__main__":
    main()
