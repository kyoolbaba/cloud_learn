---
tags: [project, 02-ec2-devbox]
aliases: [02-ec2-devbox]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]] | [[PROGRESS|Tracker]]

# Project 02 — Disposable dev box + benchmark  🖥️

**Service:** EC2, security groups, SSH key pairs · **Time:** 1–2h · **Cost:** free-tier (t3.micro)

## Goal
Launch a real Linux server in the cloud, SSH in, run a CPU benchmark, capture the
result, then **terminate it**. Feel the full lifecycle: launch → use → destroy.

## Why (ties to capstone)
The cloud worker is an EC2 (or Fargate) box. You must be fluent at standing one up
and — critically — tearing it down, or the bill runs.

## Learn from
`../../labs/m3-aws/ec2_lab.py` — launch/list/stop/terminate + auto AMI lookup.

## Build it
1. **Key pair** (for SSH): 
   ```powershell
   aws ec2 create-key-pair --key-name forecast-key --query KeyMaterial --output text > forecast-key.pem
   icacls forecast-key.pem /inheritance:r /grant:r "$($env:USERNAME):(R)"   # lock perms
   ```
2. **Security group** allowing SSH **from your IP only**:
   ```powershell
   $myip = (Invoke-RestMethod https://checkip.amazonaws.com).Trim()
   aws ec2 create-security-group --group-name forecast-sg --description "ssh from me" 
   # grab the GroupId it returns, then:
   aws ec2 authorize-security-group-ingress --group-name forecast-sg --protocol tcp --port 22 --cidr "$myip/32"
   ```
3. Put `KEY_NAME=forecast-key` and `SECURITY_GROUP_ID=sg-...` into your env/config.
4. Launch + SSH (use the lab script):
   ```powershell
   cd ..\..\labs\m3-aws
   python ec2_lab.py launch        # prints the public IP + ssh command
   ssh -i forecast-key.pem ubuntu@<IP>
   ```
5. On the box, benchmark and save the result:
   ```bash
   sudo apt update && sudo apt install -y sysbench
   sysbench cpu --cpu-max-prime=20000 run | tee ~/bench.txt
   ```
6. Copy the result back, then **terminate**:
   ```powershell
   scp -i forecast-key.pem ubuntu@<IP>:~/bench.txt .
   python ec2_lab.py terminate <instance-id>
   ```

## ✅ Done when
- [ ] You SSH'd into a cloud box you launched
- [ ] `bench.txt` is on your laptop
- [ ] The instance is **terminated** (`python ec2_lab.py list` shows none running)
- [ ] You can explain: key pair vs security group, stop vs terminate, public vs private IP

## 🧹 Teardown
```powershell
python ec2_lab.py terminate-all     # nuke any leftover project=forecast instances
```
(Keep the key pair + security group for later projects.)

## 🚀 Stretch
Launch with `--userdata` pointing at a script that installs sysbench and runs the
benchmark automatically on boot — then you never SSH in. (That's Project 03.)
