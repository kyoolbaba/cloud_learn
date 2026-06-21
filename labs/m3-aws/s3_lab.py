#!/usr/bin/env python3
"""s3_lab.py — learn Amazon S3 (object storage) with boto3.

S3 stores OBJECTS (files) in BUCKETS (globally-unique namespaces), addressed by a
KEY (path-like string). It's where job.json, progress.json and results live so the
app and the cloud worker can hand data back and forth.

Setup:  pip install boto3   &&   source config.sh   (sets FORECAST_BUCKET, AWS_REGION)
Auth:   `aws configure` once (creates ~/.aws/credentials). NEVER hardcode keys.

Usage:
  python s3_lab.py create-bucket
  python s3_lab.py upload  ./local.txt   data/local.txt
  python s3_lab.py list    [prefix]
  python s3_lab.py download data/local.txt ./got.txt
  python s3_lab.py presign data/local.txt           # time-limited public URL
  python s3_lab.py delete  data/local.txt
"""
import argparse
import os
import sys

import boto3
from botocore.exceptions import ClientError

REGION = os.environ.get("AWS_REGION", "ap-south-1")
BUCKET = os.environ.get("FORECAST_BUCKET")


def s3():
    return boto3.client("s3", region_name=REGION)


def create_bucket():
    # Outside us-east-1 you MUST pass a LocationConstraint, or S3 rejects it.
    kwargs = {"Bucket": BUCKET}
    if REGION != "us-east-1":
        kwargs["CreateBucketConfiguration"] = {"LocationConstraint": REGION}
    try:
        s3().create_bucket(**kwargs)
        print(f"Created s3://{BUCKET} in {REGION}")
    except ClientError as e:
        code = e.response["Error"]["Code"]
        if code in ("BucketAlreadyOwnedByYou", "BucketAlreadyExists"):
            print(f"Bucket already exists: {BUCKET}")
        else:
            raise


def upload(local, key):
    s3().upload_file(local, BUCKET, key)        # multipart + retries handled for you
    print(f"Uploaded {local} -> s3://{BUCKET}/{key}")


def list_objects(prefix=""):
    resp = s3().list_objects_v2(Bucket=BUCKET, Prefix=prefix)
    for obj in resp.get("Contents", []):
        print(f"{obj['Size']:>10}  {obj['LastModified']:%Y-%m-%d %H:%M}  {obj['Key']}")
    if "Contents" not in resp:
        print("(empty)")


def download(key, local):
    s3().download_file(BUCKET, key, local)
    print(f"Downloaded s3://{BUCKET}/{key} -> {local}")


def presign(key, seconds=3600):
    # A presigned URL grants temporary access without giving away credentials —
    # how you'd let a browser download a finished forecast.parquet directly.
    url = s3().generate_presigned_url(
        "get_object", Params={"Bucket": BUCKET, "Key": key}, ExpiresIn=seconds
    )
    print(f"Valid for {seconds}s:\n{url}")


def delete(key):
    s3().delete_object(Bucket=BUCKET, Key=key)
    print(f"Deleted s3://{BUCKET}/{key}")


def main():
    if not BUCKET:
        sys.exit("Set FORECAST_BUCKET (source config.sh first).")
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("create-bucket")
    u = sub.add_parser("upload"); u.add_argument("local"); u.add_argument("key")
    l = sub.add_parser("list"); l.add_argument("prefix", nargs="?", default="")
    d = sub.add_parser("download"); d.add_argument("key"); d.add_argument("local")
    pr = sub.add_parser("presign"); pr.add_argument("key"); pr.add_argument("seconds", nargs="?", type=int, default=3600)
    de = sub.add_parser("delete"); de.add_argument("key")
    a = p.parse_args()
    {
        "create-bucket": create_bucket,
        "upload": lambda: upload(a.local, a.key),
        "list": lambda: list_objects(a.prefix),
        "download": lambda: download(a.key, a.local),
        "presign": lambda: presign(a.key, a.seconds),
        "delete": lambda: delete(a.key),
    }[a.cmd]()


if __name__ == "__main__":
    main()
