#!/usr/bin/env python3
"""secrets_demo.py — read secrets at runtime instead of hardcoding them.

NEVER put API keys/passwords in code or files. Store them in SSM Parameter Store
(free, great for config) or Secrets Manager (paid, adds rotation), and fetch at
runtime with the instance/task IAM role — no credentials travel with your code.

Setup:  source ../m3-aws/config.sh
Usage:
  python secrets_demo.py put-ssm /forecast/api-key  "super-secret-value"
  python secrets_demo.py get-ssm /forecast/api-key
  python secrets_demo.py get-secret forecast/db-creds     # Secrets Manager
"""
import os
import sys

import boto3

REGION = os.environ.get("AWS_REGION", "ap-south-1")


def put_ssm(name, value):
    ssm = boto3.client("ssm", region_name=REGION)
    # SecureString encrypts the value with KMS at rest.
    ssm.put_parameter(Name=name, Value=value, Type="SecureString", Overwrite=True)
    print(f"Stored {name} (SecureString).")


def get_ssm(name):
    ssm = boto3.client("ssm", region_name=REGION)
    val = ssm.get_parameter(Name=name, WithDecryption=True)["Parameter"]["Value"]
    print(val)


def get_secret(name):
    sm = boto3.client("secretsmanager", region_name=REGION)
    print(sm.get_secret_value(SecretId=name)["SecretString"])


def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "put-ssm":     put_ssm(sys.argv[2], sys.argv[3])
    elif cmd == "get-ssm":   get_ssm(sys.argv[2])
    elif cmd == "get-secret": get_secret(sys.argv[2])
    else:                    print(__doc__)


if __name__ == "__main__":
    main()
