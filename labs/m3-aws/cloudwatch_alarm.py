#!/usr/bin/env python3
"""cloudwatch_alarm.py — create CloudWatch alarms (your runaway-cost insurance).

Two alarms:
  billing  -> emails you if estimated charges cross a $ threshold (DO THIS DAY ONE)
  cpu      -> fires if an instance pegs CPU > 80% for 5 min

Both notify via an SNS topic (email). Run setup-topic first and CONFIRM the email
subscription link AWS sends you, or notifications go nowhere.

Setup:  source config.sh
Usage:
  python cloudwatch_alarm.py setup-topic you@example.com
  python cloudwatch_alarm.py billing 20        # alert at $20 estimated charges
  python cloudwatch_alarm.py cpu i-0abc123      # CPU>80% alarm for an instance
"""
import argparse
import os
import sys

import boto3

REGION = os.environ.get("AWS_REGION", "ap-south-1")
TOPIC_NAME = "forecast-alerts"


def sns(region=REGION):
    return boto3.client("sns", region_name=region)


def topic_arn(region=REGION):
    # create_topic is idempotent — returns the existing ARN if it already exists.
    return sns(region).create_topic(Name=TOPIC_NAME)["TopicArn"]


def setup_topic(email):
    arn = topic_arn()
    sns().subscribe(TopicArn=arn, Protocol="email", Endpoint=email)
    print(f"SNS topic: {arn}")
    print(f"Check {email} and CLICK the confirmation link, or alerts won't send.")


def billing_alarm(threshold_usd):
    # IMPORTANT: AWS/Billing EstimatedCharges only exists in us-east-1, so the
    # billing alarm + its SNS topic must live there too.
    cw = boto3.client("cloudwatch", region_name="us-east-1")
    arn = topic_arn(region="us-east-1")
    cw.put_metric_alarm(
        AlarmName=f"forecast-billing-over-{threshold_usd}usd",
        Namespace="AWS/Billing", MetricName="EstimatedCharges",
        Dimensions=[{"Name": "Currency", "Value": "USD"}],
        Statistic="Maximum", Period=21600, EvaluationPeriods=1,
        Threshold=float(threshold_usd), ComparisonOperator="GreaterThanThreshold",
        AlarmActions=[arn], ActionsEnabled=True,
        AlarmDescription="Estimated AWS charges exceeded threshold",
    )
    print(f"Billing alarm set at ${threshold_usd} (us-east-1). "
          f"Subscribe an email there too: python cloudwatch_alarm.py setup-topic <email>  (in us-east-1).")


def cpu_alarm(instance_id):
    cw = boto3.client("cloudwatch", region_name=REGION)
    cw.put_metric_alarm(
        AlarmName=f"forecast-cpu-high-{instance_id}",
        Namespace="AWS/EC2", MetricName="CPUUtilization",
        Dimensions=[{"Name": "InstanceId", "Value": instance_id}],
        Statistic="Average", Period=300, EvaluationPeriods=1,
        Threshold=80.0, ComparisonOperator="GreaterThanThreshold",
        AlarmActions=[topic_arn()], ActionsEnabled=True,
        AlarmDescription="EC2 CPU > 80% for 5 minutes",
    )
    print(f"CPU alarm set for {instance_id} (>80% for 5 min).")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    st = sub.add_parser("setup-topic"); st.add_argument("email")
    b = sub.add_parser("billing"); b.add_argument("threshold")
    c = sub.add_parser("cpu"); c.add_argument("instance_id")
    a = p.parse_args()
    if a.cmd == "setup-topic": setup_topic(a.email)
    elif a.cmd == "billing":   billing_alarm(a.threshold)
    elif a.cmd == "cpu":       cpu_alarm(a.instance_id)


if __name__ == "__main__":
    main()
