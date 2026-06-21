#!/usr/bin/env python3
"""sqs_consumer.py — pull work off the queue and process it.

Key concepts shown:
  - long polling (WaitTimeSeconds) so you don't hammer the API
  - VISIBILITY TIMEOUT: a received message is hidden from other consumers for N
    seconds; you must DELETE it within that window or it reappears (at-least-once
    delivery). Delete only AFTER successful processing.
  - run several copies of this script at once to see parallel consumption.

Setup:  source ../m3-aws/config.sh
Usage:  python sqs_consumer.py          # drains the queue, then exits when empty
"""
import json
import os
import time

import boto3

REGION = os.environ.get("AWS_REGION", "ap-south-1")
QUEUE_NAME = os.environ.get("QUEUE_NAME", "forecast-shards")
sqs = boto3.client("sqs", region_name=REGION)


def process(msg_body):
    job = json.loads(msg_body)
    time.sleep(0.5)                         # pretend to forecast this shard
    print(f"  processed shard {job['shard']}")


def main():
    url = sqs.create_queue(QueueName=QUEUE_NAME)["QueueUrl"]
    empty_polls = 0
    while empty_polls < 2:                   # exit after two empty long-polls
        resp = sqs.receive_message(
            QueueUrl=url, MaxNumberOfMessages=10, WaitTimeSeconds=10,  # long poll
            VisibilityTimeout=30,
        )
        msgs = resp.get("Messages", [])
        if not msgs:
            empty_polls += 1
            continue
        empty_polls = 0
        for m in msgs:
            try:
                process(m["Body"])
                # delete ONLY on success, so failures get retried after the timeout
                sqs.delete_message(QueueUrl=url, ReceiptHandle=m["ReceiptHandle"])
            except Exception as e:           # noqa: BLE001 (lab: keep going)
                print(f"  FAILED (will reappear): {e}")
    print("Queue empty — exiting.")


if __name__ == "__main__":
    main()
