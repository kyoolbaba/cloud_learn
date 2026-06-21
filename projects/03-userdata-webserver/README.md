---
tags: [project, 03-userdata-webserver]
aliases: [03-userdata-webserver]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]] | [[PROGRESS|Tracker]]

# Project 03 — Self-configuring web server  🌐

**Service:** EC2 user-data (cloud-init), security groups · **Time:** 1h · **Cost:** free-tier

## Goal
Launch an instance that **configures itself on boot** — installs nginx and serves a
page showing its own instance id — with zero manual SSH. Open it in your browser.

## Why (ties to capstone)
This is exactly how the cloud worker self-configures: user-data installs Python +
deps and runs the forecast engine automatically when the box boots. No hand-holding.

## Learn from
`../../labs/m3-aws/worker_userdata.sh` — the bootstrap pattern. `ec2_lab.py launch --userdata`.

## Build it
1. Write `web_userdata.sh` (runs as root on first boot):
   ```bash
   #!/bin/bash
   set -eux
   apt-get update -y && apt-get install -y nginx
   TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 60")
   IID=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-id)
   echo "<h1>Hello from $IID</h1>" > /var/www/html/index.html
   systemctl enable --now nginx
   ```
   (That `169.254.169.254` address is the **instance metadata service** — how a box
   learns about itself.)
2. Open **port 80** in the security group, from your IP:
   ```powershell
   $myip = (Invoke-RestMethod https://checkip.amazonaws.com).Trim()
   aws ec2 authorize-security-group-ingress --group-name forecast-sg --protocol tcp --port 80 --cidr "$myip/32"
   ```
3. Launch with the user-data:
   ```powershell
   cd ..\..\labs\m3-aws
   python ec2_lab.py launch --userdata ..\..\projects\03-userdata-webserver\web_userdata.sh
   ```
4. Wait ~90s (cloud-init runs), then open `http://<public-ip>/` in your browser.
   Debug by SSHing in and reading `/var/log/cloud-init-output.log`.

## ✅ Done when
- [ ] Browsing the public IP shows "Hello from i-xxxx" — and you never SSH'd to set it up
- [ ] You can explain what user-data is and when it runs (first boot, as root)
- [ ] You understand why port 80 had to be opened in the security group
- [ ] Instance **terminated** after

## 🧹 Teardown
```powershell
python ec2_lab.py terminate-all
# optional: revoke port 80 again
aws ec2 revoke-security-group-ingress --group-name forecast-sg --protocol tcp --port 80 --cidr "$myip/32"
```

## 🚀 Stretch
Make user-data pull a page from your S3 vault (Project 01) and serve that — now the
box's content is decoupled from its config.
