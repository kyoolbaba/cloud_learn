---
tags: [lab, m6-hardening]
aliases: [m6-hardening lab]
---
> [[labs/README|⬅ Labs]] | [[HOME|Home]] | [[STUDY_PLAN|Plan]]

# Module 6 — Production hardening & Infrastructure as Code (hands-on lab)

Goal: the whole backend defined as code (`apply`/`destroy`), zero hardcoded
secrets, tight networking, and a kill switch so nothing runs away.

**Install Terraform** (in WSL): follow HashiCorp's apt repo steps, then `terraform -version`.

---

## Lab 1 — Terraform basics: build & destroy the backend

```bash
cd terraform
terraform init                                  # download the AWS provider
terraform plan  -var bucket_name=$FORECAST_BUCKET   # PREVIEW (always read this)
terraform apply -var bucket_name=$FORECAST_BUCKET   # creates S3 + ECR + IAM task role
terraform output                                # bucket name, ECR URL, role ARN
# ... use it ...
terraform destroy -var bucket_name=$FORECAST_BUCKET # wipe it all in one command
```
Re-run `apply` and feel it: your entire backend reproducible from text files. Wire
the outputs into `../m3-aws/config.sh` so the boto3 scripts use these resources.

## Lab 2 — Terraform the worker stack

Extend `main.tf` with the ECS cluster, task definition, and (optional) Step
Functions state machine — so the *compute* backend is `apply`/`destroy`-able too,
not just storage. (Add `aws_ecs_cluster`, `aws_ecs_task_definition`,
`aws_sfn_state_machine` resources; reference the ECR repo + task role already defined.)

## Lab 3 — Secrets: no plaintext credentials, ever

```bash
python ../m6-hardening/secrets_demo.py put-ssm /forecast/api-key "demo-12345"
python ../m6-hardening/secrets_demo.py get-ssm /forecast/api-key   # fetched at runtime
```
Replace any hardcoded key in your code with a `get-ssm` call. The worker reads
secrets via its IAM role — nothing sensitive ships with the image.

## Lab 4 — VPC: put the worker in a private subnet

Concept lab (console or Terraform): a **private subnet** (no public IP) + a **NAT
gateway** for outbound-only internet (to reach S3/ECR), and a security group that
allows **nothing inbound**. The worker can call out; nobody can call in. Understand
why production isolates compute this way. (NAT gateways cost money — tear down after.)

## Lab 5 — Auto-stop / max-runtime kill switch

Deploy `autostop_lambda.py` on a schedule:
```bash
zip autostop.zip autostop_lambda.py
aws lambda create-function --function-name forecast-autostop \
  --runtime python3.12 --handler autostop_lambda.handler \
  --role arn:aws:iam::ACCOUNT_ID:role/forecast-autostop-role \
  --zip-file fileb://autostop.zip --environment "Variables={MAX_HOURS=2}"
# schedule it every 15 min:
aws events put-rule --name forecast-autostop-15m --schedule-expression "rate(15 minutes)"
# (then add the Lambda as the rule's target + grant events permission to invoke it)
```
Now any `project=forecast` instance running > 2h is terminated automatically.

---

**Checkpoint (M6 done):** `terraform apply` stands up the backend; `destroy` removes
it; no secret is hardcoded; a runaway job auto-dies. Tick the **Hardening** boxes in
`../../PROGRESS.md`.  → **🏁 Capstone.**
