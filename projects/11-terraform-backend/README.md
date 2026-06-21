---
tags: [project, 11-terraform-backend]
aliases: [11-terraform-backend]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]] | [[PROGRESS|Tracker]]

# Project 11 — One-command backend (IaC)  🏗️

**Service:** Terraform · **Time:** 2–3h · **Cost:** free

## Goal
Define your whole forecast backend (S3 bucket + ECR repo + IAM task role) as code,
build it with `terraform apply`, and wipe it with `terraform destroy`. Then re-create
it in one command and *feel* the reproducibility.

## Why (ties to capstone)
"Stand up and tear down the backend in one command, bill you control" — that promise
is Terraform. Click-ops doesn't scale or reproduce; code does.

## Prereq
Install Terraform on Windows: `winget install HashiCorp.Terraform`, then `terraform -version`.

## Learn from
`../../labs/m6-hardening/terraform/` — `main.tf`, `variables.tf`, `outputs.tf` (ready to run).

## Build it
1. Copy the Terraform into this project (so your IaC lives with the project):
   ```powershell
   Copy-Item ..\..\labs\m6-hardening\terraform\*.tf .
   ```
2. Init, preview, apply:
   ```powershell
   terraform init
   terraform plan  -var "bucket_name=milan-forecast-tf-857"     # READ the plan
   terraform apply -var "bucket_name=milan-forecast-tf-857"
   terraform output                                              # bucket, ECR url, role arn
   ```
3. Look in the console — the bucket/ECR/role exist, created from text.
4. **Destroy and re-create** to feel it:
   ```powershell
   terraform destroy -var "bucket_name=milan-forecast-tf-857"
   terraform apply   -var "bucket_name=milan-forecast-tf-857"    # back in ~20s
   ```

## ✅ Done when
- [ ] `apply` created S3 + ECR + IAM role; `terraform output` shows them
- [ ] `destroy` removed everything; a second `apply` recreated it
- [ ] You can explain `plan` vs `apply` vs `destroy`, and what `terraform.tfstate` is
- [ ] You understand why state must never be committed (it can hold secrets) — it's gitignored

## 🧹 Teardown
```powershell
terraform destroy -var "bucket_name=milan-forecast-tf-857"
```

## 🚀 Stretch
Extend `main.tf` with the ECS cluster + task definition (Project 07) so the *compute*
backend is also code. Now `terraform apply` stands up the entire system.
