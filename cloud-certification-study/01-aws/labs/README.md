# 🧪 AWS Labs — Reusable Guides & Cleanup

Hands-on labs live inside each certification file (section 8). This folder holds **reusable lab guidance** and the **golden cleanup rules** so you never get a surprise bill.

## 🔑 Golden lab rules
1. **Always set a billing alarm before any lab.**
2. **Use Free Tier eligible options** (t2.micro/t3.micro, Serverless small).
3. **Tag everything** with `project=cert-study` so you can find leftovers.
4. **Clean up the same day** and log it in `04-trackers/lab-completion-tracker.md`.

## 💸 "These cost money even when idle" — delete first
| Resource | Why it bills | Cleanup |
|---|---|---|
| NAT Gateway | Hourly + data | Delete before the VPC |
| Elastic IP (unattached) | Hourly when not attached | Release it |
| RDS / Redshift / OpenSearch | Running hourly | Delete instance/cluster/collection |
| SageMaker endpoints | Per-hour instance | Delete endpoint |
| Load Balancers (ALB/NLB) | Hourly | Delete |
| Transit Gateway attachments | Hourly | Delete attachments + TGW |
| EBS volumes / snapshots | Storage | Delete unused |

## 🧹 End-of-session cleanup checklist
- [ ] Terminated all EC2 instances
- [ ] Deleted RDS/Redshift/OpenSearch/SageMaker endpoints
- [ ] Deleted NAT GWs, released unused Elastic IPs
- [ ] Emptied + deleted temporary S3 buckets
- [ ] Deleted Load Balancers + Auto Scaling groups
- [ ] Disabled paid security services (Macie, GuardDuty) if only for a lab
- [ ] Checked **Billing → Free Tier** + **Cost Explorer** for surprises
- [ ] Logged the lab + cleanup in the lab tracker

## 🛠️ Lab environment tips
- Prefer the **AWS Management Console** for learning; CLI/CDK later.
- Work in **one region** (e.g., us-east-1) to avoid orphaned resources elsewhere.
- Take a screenshot as evidence and note it in the lab tracker.
