#!/usr/bin/env python3
"""orchestrate_run.py — drive a full remote forecast run from your laptop.

THIS SCRIPT IS ~80% OF THE FINAL "RUN IN CLOUD" TOGGLE. It ties S3 + EC2 +
user-data + polling together:

  1. make a job_id and a job.json (what to forecast)
  2. upload job.json + worker.py to s3://bucket/jobs/<job_id>/
  3. launch an EC2 instance whose user-data downloads & runs worker.py
  4. POLL s3://.../progress.json until stage == "done"  (this is the progress bar)
  5. download forecast.parquet
  6. terminate the instance (stop paying)

Later, db_polars_app.py calls this same flow from a web route instead of main().

Setup:  source config.sh   (needs FORECAST_BUCKET, KEY_NAME, SECURITY_GROUP_ID,
        IAM_INSTANCE_PROFILE with S3 access, AWS_REGION)
Usage:  python orchestrate_run.py --n-series 50 --horizon 6
        python orchestrate_run.py --keep      # don't terminate (to SSH in & debug)
"""
import argparse
import json
import os
import time
import uuid
from pathlib import Path

import boto3

REGION = os.environ.get("AWS_REGION", "ap-south-1")
BUCKET = os.environ["FORECAST_BUCKET"]
KEY_NAME = os.environ.get("KEY_NAME")
SG_ID = os.environ.get("SECURITY_GROUP_ID")
PROFILE = os.environ.get("IAM_INSTANCE_PROFILE")
INSTANCE_TYPE = os.environ.get("INSTANCE_TYPE", "t3.micro")
PROJECT = os.environ.get("PROJECT_TAG", "forecast")
HERE = Path(__file__).parent

s3 = boto3.client("s3", region_name=REGION)
ec2 = boto3.client("ec2", region_name=REGION)
ssm = boto3.client("ssm", region_name=REGION)
UBUNTU_SSM = "/aws/service/canonical/ubuntu/server/24.04/stable/current/amd64/hvm/ebs-gp3/ami-id"


def upload_job(job_id, n_series, horizon):
    prefix = f"jobs/{job_id}"
    job = {"job_id": job_id, "n_series": n_series, "horizon": horizon}
    s3.put_object(Bucket=BUCKET, Key=f"{prefix}/job.json", Body=json.dumps(job).encode())
    s3.upload_file(str(HERE / "worker.py"), BUCKET, f"{prefix}/worker.py")
    print(f"[1-2] uploaded job.json + worker.py to s3://{BUCKET}/{prefix}/")


def render_userdata(job_id):
    ud = (HERE / "worker_userdata.sh").read_text(encoding="utf-8")
    return ud.replace("__BUCKET__", BUCKET).replace("__JOB_ID__", job_id)


def launch(job_id):
    ami = ssm.get_parameter(Name=UBUNTU_SSM)["Parameter"]["Value"]
    kwargs = dict(
        ImageId=ami, InstanceType=INSTANCE_TYPE, MinCount=1, MaxCount=1,
        KeyName=KEY_NAME,
        SecurityGroupIds=[SG_ID] if SG_ID else None,
        UserData=render_userdata(job_id),
        IamInstanceProfile={"Name": PROFILE} if PROFILE else None,
        InstanceInitiatedShutdownBehavior="terminate",   # `shutdown -h` in user-data => terminates
        TagSpecifications=[{"ResourceType": "instance",
                            "Tags": [{"Key": "project", "Value": PROJECT},
                                     {"Key": "job_id", "Value": job_id}]}],
    )
    kwargs = {k: v for k, v in kwargs.items() if v is not None}
    iid = ec2.run_instances(**kwargs)["Instances"][0]["InstanceId"]
    print(f"[3] launched {iid}; user-data will bootstrap & run worker.py")
    return iid


def poll(job_id, timeout=1800):
    key = f"jobs/{job_id}/progress.json"
    print("[4] polling progress (Ctrl-C is safe; instance self-terminates):")
    start = time.time()
    last = None
    while time.time() - start < timeout:
        try:
            p = json.loads(s3.get_object(Bucket=BUCKET, Key=key)["Body"].read())
        except s3.exceptions.NoSuchKey:
            p = None
        if p and p != last:
            done, total, stage = p["done"], p["total"], p["stage"]
            eta = p.get("eta_seconds")
            bar = "#" * int(20 * done / max(total, 1))
            print(f"    [{bar:<20}] {done}/{total}  {stage}" + (f"  eta {eta}s" if eta else ""))
            last = p
            if stage == "done":
                return True
        time.sleep(5)
    print("    timed out."); return False


def download_result(job_id):
    key = f"jobs/{job_id}/forecast.parquet"
    out = HERE / f"result-{job_id}.parquet"
    s3.download_file(BUCKET, key, str(out))
    print(f"[5] downloaded -> {out}")


def terminate(iid):
    ec2.terminate_instances(InstanceIds=[iid])
    print(f"[6] terminated {iid}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--n-series", type=int, default=50)
    ap.add_argument("--horizon", type=int, default=6)
    ap.add_argument("--keep", action="store_true", help="don't terminate at the end")
    a = ap.parse_args()

    job_id = uuid.uuid4().hex[:8]
    print(f"=== job {job_id} ===")
    upload_job(job_id, a.n_series, a.horizon)
    iid = launch(job_id)
    try:
        if poll(job_id):
            download_result(job_id)
    finally:
        if not a.keep:
            terminate(iid)
        else:
            print(f"--keep set; remember to: python ec2_lab.py terminate {iid}")


if __name__ == "__main__":
    main()
