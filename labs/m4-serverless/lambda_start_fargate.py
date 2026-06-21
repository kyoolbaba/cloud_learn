"""lambda_start_fargate.py — an AWS Lambda that launches a Fargate task on demand.

This is the cloud-side ENTRY POINT the app calls: "start a forecast for job X".
Lambda is for glue/triggering (short, event-driven) — NOT the heavy compute. It
just calls ecs.run_task and returns; Fargate does the actual forecasting.

Deploy: zip this file -> create a Lambda (Python 3.12) -> give its role permission
to ecs:RunTask + iam:PassRole (see lambda_policies.md). Set env vars CLUSTER,
TASKDEF, SUBNETS (comma-sep), SECURITY_GROUP.

Triggers that can invoke it: API Gateway (HTTP), an S3 "object created" event, or
a direct boto3 invoke. The `event` carries the job_id/bucket.
"""
import json
import os

import boto3

ecs = boto3.client("ecs")

CLUSTER = os.environ["CLUSTER"]
TASKDEF = os.environ["TASKDEF"]                 # e.g. "forecast-engine"
SUBNETS = os.environ["SUBNETS"].split(",")
SECURITY_GROUP = os.environ["SECURITY_GROUP"]


def handler(event, context):
    # event may come from API Gateway (body is a JSON string) or a direct invoke.
    body = event.get("body")
    payload = json.loads(body) if isinstance(body, str) else (body or event)
    job_id = payload.get("job_id", "adhoc")
    bucket = payload["bucket"]

    resp = ecs.run_task(
        cluster=CLUSTER,
        taskDefinition=TASKDEF,
        launchType="FARGATE",
        count=1,
        networkConfiguration={
            "awsvpcConfiguration": {
                "subnets": SUBNETS,
                "securityGroups": [SECURITY_GROUP],
                "assignPublicIp": "ENABLED",     # needed to pull the image / reach S3 w/o NAT
            }
        },
        overrides={
            "containerOverrides": [
                {
                    "name": "forecast-engine",
                    # pass the job to the container as env vars at launch time
                    "environment": [
                        {"name": "JOB_ID", "value": job_id},
                        {"name": "BUCKET", "value": bucket},
                    ],
                }
            ]
        },
    )
    task_arn = resp["tasks"][0]["taskArn"] if resp.get("tasks") else None
    return {
        "statusCode": 200,
        "body": json.dumps({"job_id": job_id, "task_arn": task_arn}),
    }
