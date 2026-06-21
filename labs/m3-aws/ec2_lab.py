#!/usr/bin/env python3
"""ec2_lab.py — launch / inspect / stop / terminate an EC2 virtual machine.

EC2 = a rented Linux box. You pay while it RUNS. The cardinal rule of this whole
plan: **STOP or TERMINATE every instance after a lab.** stop = keep the disk, pause
billing for compute; terminate = delete it entirely.

Everything is tagged project=forecast so you can always find and kill it.

Setup:  source config.sh    (KEY_NAME, SECURITY_GROUP_ID, INSTANCE_TYPE, ...)

Usage:
  python ec2_lab.py latest-ami                 # newest Ubuntu 24.04 AMI id (no hardcoding)
  python ec2_lab.py launch [--userdata FILE]   # start one instance (optionally bootstrapped)
  python ec2_lab.py list                       # all project=forecast instances + states
  python ec2_lab.py stop  <instance-id>
  python ec2_lab.py start <instance-id>
  python ec2_lab.py terminate <instance-id>
  python ec2_lab.py terminate-all             # nuke every project=forecast instance (cleanup)
"""
import argparse
import os
import sys

import boto3

REGION = os.environ.get("AWS_REGION", "ap-south-1")
KEY_NAME = os.environ.get("KEY_NAME")
SG_ID = os.environ.get("SECURITY_GROUP_ID")
SUBNET_ID = os.environ.get("SUBNET_ID") or None
INSTANCE_TYPE = os.environ.get("INSTANCE_TYPE", "t3.micro")
PROFILE = os.environ.get("IAM_INSTANCE_PROFILE") or None
PROJECT = os.environ.get("PROJECT_TAG", "forecast")

ec2 = boto3.client("ec2", region_name=REGION)
ssm = boto3.client("ssm", region_name=REGION)

# Canonical's public SSM parameter that always points at the latest Ubuntu 24.04 AMI.
UBUNTU_SSM = "/aws/service/canonical/ubuntu/server/24.04/stable/current/amd64/hvm/ebs-gp3/ami-id"


def latest_ami():
    ami = ssm.get_parameter(Name=UBUNTU_SSM)["Parameter"]["Value"]
    print(ami)
    return ami


def launch(userdata_file=None):
    user_data = ""
    if userdata_file:
        with open(userdata_file, "r", encoding="utf-8") as f:
            user_data = f.read()        # cloud-init runs this as root on first boot

    kwargs = dict(
        ImageId=latest_ami_quiet(),
        InstanceType=INSTANCE_TYPE,
        MinCount=1, MaxCount=1,
        KeyName=KEY_NAME,
        SecurityGroupIds=[SG_ID] if SG_ID else None,
        SubnetId=SUBNET_ID,
        UserData=user_data,
        IamInstanceProfile={"Name": PROFILE} if PROFILE else None,
        TagSpecifications=[{
            "ResourceType": "instance",
            "Tags": [{"Key": "project", "Value": PROJECT}, {"Key": "Name", "Value": f"{PROJECT}-worker"}],
        }],
    )
    kwargs = {k: v for k, v in kwargs.items() if v is not None}   # drop blanks
    inst = ec2.run_instances(**kwargs)["Instances"][0]
    iid = inst["InstanceId"]
    print(f"Launched {iid} ({INSTANCE_TYPE}). Waiting for it to enter 'running'...")
    ec2.get_waiter("instance_running").wait(InstanceIds=[iid])
    ip = ec2.describe_instances(InstanceIds=[iid])["Reservations"][0]["Instances"][0].get("PublicIpAddress")
    print(f"Running. Public IP: {ip}")
    print(f"SSH:  ssh -i {KEY_NAME}.pem ubuntu@{ip}")
    print(f"!! Remember:  python ec2_lab.py terminate {iid}   when done.")
    return iid


def list_instances():
    resp = ec2.describe_instances(Filters=[{"Name": f"tag:project", "Values": [PROJECT]}])
    rows = []
    for r in resp["Reservations"]:
        for i in r["Instances"]:
            rows.append((i["InstanceId"], i["State"]["Name"],
                         i.get("PublicIpAddress", "-"), i["InstanceType"]))
    if not rows:
        print("(no project=forecast instances)")
    for iid, state, ip, itype in rows:
        print(f"{iid}  {state:<12} {ip:<16} {itype}")
    return rows


def _ids_for(state_filter=None):
    return [iid for iid, state, *_ in list_instances_quiet()
            if state_filter is None or state == state_filter]


def stop(iid):       ec2.stop_instances(InstanceIds=[iid]);      print(f"Stopping {iid}")
def start(iid):      ec2.start_instances(InstanceIds=[iid]);     print(f"Starting {iid}")
def terminate(iid):  ec2.terminate_instances(InstanceIds=[iid]); print(f"Terminating {iid}")


def terminate_all():
    ids = [iid for iid, state, *_ in list_instances_quiet() if state not in ("terminated", "shutting-down")]
    if not ids:
        print("Nothing to terminate."); return
    ec2.terminate_instances(InstanceIds=ids)
    print(f"Terminating: {', '.join(ids)}")


# --- quiet helpers (no printing) ---
def latest_ami_quiet():
    return ssm.get_parameter(Name=UBUNTU_SSM)["Parameter"]["Value"]


def list_instances_quiet():
    resp = ec2.describe_instances(Filters=[{"Name": "tag:project", "Values": [PROJECT]}])
    return [(i["InstanceId"], i["State"]["Name"], i.get("PublicIpAddress", "-"), i["InstanceType"])
            for r in resp["Reservations"] for i in r["Instances"]]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("latest-ami")
    lp = sub.add_parser("launch"); lp.add_argument("--userdata")
    sub.add_parser("list")
    for c in ("stop", "start", "terminate"):
        sp = sub.add_parser(c); sp.add_argument("instance_id")
    sub.add_parser("terminate-all")
    a = p.parse_args()
    if a.cmd == "latest-ami":   latest_ami()
    elif a.cmd == "launch":     launch(a.userdata)
    elif a.cmd == "list":       list_instances()
    elif a.cmd == "stop":       stop(a.instance_id)
    elif a.cmd == "start":      start(a.instance_id)
    elif a.cmd == "terminate":  terminate(a.instance_id)
    elif a.cmd == "terminate-all": terminate_all()


if __name__ == "__main__":
    main()
