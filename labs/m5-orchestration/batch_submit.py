#!/usr/bin/env python3
"""batch_submit.py — submit an AWS Batch ARRAY job (an alternative to Step Functions).

AWS Batch is purpose-built for "run N copies of this container across a fleet". An
ARRAY job of size N launches N children; each gets AWS_BATCH_JOB_ARRAY_INDEX (0..N-1)
as its shard id. Batch manages the compute fleet (incl. cheap Spot) for you.

Prereqs (console one-time): a Compute Environment (Fargate or EC2/Spot), a Job
Queue, and a Job Definition pointing at your ECR image. Put their names below.

Setup:  source ../m3-aws/config.sh
Usage:  python batch_submit.py 100        # 100-way array job
"""
import os
import sys

import boto3

batch = boto3.client("batch", region_name=os.environ.get("AWS_REGION", "ap-south-1"))
JOB_QUEUE = os.environ.get("BATCH_QUEUE", "forecast-queue")
JOB_DEF = os.environ.get("BATCH_JOBDEF", "forecast-engine")


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    resp = batch.submit_job(
        jobName="forecast-array",
        jobQueue=JOB_QUEUE,
        jobDefinition=JOB_DEF,
        arrayProperties={"size": n},          # <-- N parallel children
        containerOverrides={
            "environment": [{"name": "BUCKET", "value": os.environ["FORECAST_BUCKET"]}]
        },
    )
    print(f"Submitted array job {resp['jobId']} (size {n}).")
    print("Each child sees its shard via env AWS_BATCH_JOB_ARRAY_INDEX (0..N-1).")
    print("Track: aws batch describe-jobs --jobs", resp["jobId"])


if __name__ == "__main__":
    main()
