#!/bin/bash
# worker_userdata.sh — EC2 "user-data": cloud-init runs this AS ROOT on first boot.
# It self-configures the box, runs the forecast worker, then shuts down to stop billing.
#
# The app/orchestrator passes BUCKET and JOB_ID by rewriting the two lines below
# before launch (orchestrate_run.py does this automatically), OR you bake them in.
#
# Logs land in /var/log/cloud-init-output.log on the instance (SSH in to debug).
set -euxo pipefail

BUCKET="__BUCKET__"     # <- orchestrate_run.py replaces these placeholders
JOB_ID="__JOB_ID__"

# 1) install runtime (Ubuntu 24.04 ships python3; add pip + libs)
apt-get update -y
apt-get install -y python3-pip awscli
pip3 install --break-system-packages boto3 pandas pyarrow

# 2) fetch the worker code from S3 (uploaded by the orchestrator) and run it.
#    Auth is via the instance's IAM ROLE — no keys on the box.
cd /tmp
aws s3 cp "s3://${BUCKET}/jobs/${JOB_ID}/worker.py" worker.py
BUCKET="${BUCKET}" JOB_ID="${JOB_ID}" python3 worker.py

# 3) all done -> power off so you stop paying. (Use 'terminate' from the
#    orchestrator if you want the instance deleted, not just stopped.)
shutdown -h now
