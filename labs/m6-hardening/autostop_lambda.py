"""autostop_lambda.py — runaway-cost insurance: kill forecast instances running too long.

Deploy as a Lambda on an EventBridge SCHEDULE (e.g. every 15 min). It terminates any
project=forecast EC2 instance that's been running longer than MAX_HOURS. This is the
hard "max-runtime kill switch" from the plan — the thing that saves you from a $$$
surprise if a job hangs.

Role needs: ec2:DescribeInstances, ec2:TerminateInstances (limited to the tag).
Env var:    MAX_HOURS (default 2)
"""
import datetime
import os

import boto3

ec2 = boto3.client("ec2")
MAX_HOURS = float(os.environ.get("MAX_HOURS", "2"))


def handler(event, context):
    now = datetime.datetime.now(datetime.timezone.utc)
    cutoff = now - datetime.timedelta(hours=MAX_HOURS)

    resp = ec2.describe_instances(Filters=[
        {"Name": "tag:project", "Values": ["forecast"]},
        {"Name": "instance-state-name", "Values": ["running"]},
    ])
    doomed = []
    for r in resp["Reservations"]:
        for i in r["Instances"]:
            if i["LaunchTime"] < cutoff:
                doomed.append(i["InstanceId"])

    if doomed:
        ec2.terminate_instances(InstanceIds=doomed)
        print(f"Terminated (ran > {MAX_HOURS}h): {doomed}")
    else:
        print("Nothing exceeded the max runtime.")
    return {"terminated": doomed}
