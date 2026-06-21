#!/usr/bin/env python3
"""sqs_producer.py — put work on a queue (SQS = a reliable to-do list for workers).

A queue DECOUPLES the thing creating work from the things doing it. Producer drops
N "shard" messages; any number of consumers pull and process them in parallel. If a
consumer dies mid-message, the message reappears after the visibility timeout — so
nothing is lost.

Setup:  source ../m3-aws/config.sh
Usage:  python sqs_producer.py 100        # enqueue 100 shard jobs
"""
import json
import os
import sys

import boto3

REGION = os.environ.get("AWS_REGION", "ap-south-1")
QUEUE_NAME = os.environ.get("QUEUE_NAME", "forecast-shards")
sqs = boto3.client("sqs", region_name=REGION)


def queue_url():
    # create_queue is idempotent; returns the URL whether or not it existed.
    return sqs.create_queue(QueueName=QUEUE_NAME)["QueueUrl"]


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    url = queue_url()
    for i in range(n):
        body = json.dumps({"shard": i, "n_series": 20, "horizon": 6})
        sqs.send_message(QueueUrl=url, MessageBody=body)
    print(f"Enqueued {n} messages to {QUEUE_NAME}")
    attrs = sqs.get_queue_attributes(QueueUrl=url,
        AttributeNames=["ApproximateNumberOfMessages"])["Attributes"]
    print(f"Queue depth ~ {attrs['ApproximateNumberOfMessages']}")


if __name__ == "__main__":
    main()
