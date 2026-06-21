#!/usr/bin/env python3
"""run_fargate_task.py — run the Fargate task directly from your laptop (no Lambda).

Useful to test the container on Fargate before wiring up Lambda/API Gateway. Same
run_task call the Lambda makes. Watch logs in CloudWatch (/ecs/forecast-engine).

Setup:  source ../m3-aws/config.sh
        export CLUSTER=forecast-cluster SUBNETS=subnet-aaa,subnet-bbb SECURITY_GROUP=sg-xxx
Usage:  python run_fargate_task.py --job-id test1
"""
import argparse
import os

import boto3

ecs = boto3.client("ecs", region_name=os.environ.get("AWS_REGION", "ap-south-1"))
BUCKET = os.environ["FORECAST_BUCKET"]
CLUSTER = os.environ.get("CLUSTER", "forecast-cluster")
TASKDEF = os.environ.get("TASKDEF", "forecast-engine")
SUBNETS = os.environ["SUBNETS"].split(",")
SG = os.environ["SECURITY_GROUP"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--job-id", default="adhoc")
    a = ap.parse_args()
    resp = ecs.run_task(
        cluster=CLUSTER, taskDefinition=TASKDEF, launchType="FARGATE", count=1,
        networkConfiguration={"awsvpcConfiguration": {
            "subnets": SUBNETS, "securityGroups": [SG], "assignPublicIp": "ENABLED"}},
        overrides={"containerOverrides": [{
            "name": "forecast-engine",
            "environment": [{"name": "JOB_ID", "value": a.job_id},
                            {"name": "BUCKET", "value": BUCKET}]}]},
    )
    if resp.get("failures"):
        print("FAILURES:", resp["failures"]); return
    print("Started task:", resp["tasks"][0]["taskArn"])
    print("Logs: CloudWatch -> /ecs/forecast-engine")


if __name__ == "__main__":
    main()
