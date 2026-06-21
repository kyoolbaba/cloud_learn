---
tags: [cert/aif-c01, aws/ai-ml, security]
cert: AIF-C01
domain: 5
aliases: [AIF-C01 Domain 5, AI Security Compliance Governance]
---
> [[domain-4-responsible-ai|◀ Domain 4]] · [[AIF-C01|AIF-C01 Home]] · [[AIF-C01-practice|Practice Exam ▶]]

# Domain 5 — Security, Compliance & Governance for AI (14%)

Securing AI/ML systems and the data in them. Most of this is "normal AWS security applied to AI,"
plus a few AI-specific governance points. Big overlap with CLF-C02 Domain 2 — reuse that.

## 5.1 Secure the data and the model
- **IAM least privilege** — scope who can invoke models, read training data, deploy endpoints.
- **Encryption** — at rest (**KMS** on S3, EBS, SageMaker volumes) and in transit (**TLS**).
- **Network isolation** — keep traffic private with **VPC** + **PrivateLink / VPC endpoints** so calls to Bedrock/SageMaker don't traverse the public internet.
- **Secrets** — keys/tokens in **Secrets Manager / SSM**, never in prompts or code.
- **Data minimization** — don't send more sensitive data to a model than needed; mask/redact PII first.

## 5.2 Data privacy & ownership (AI-specific, often tested)
- On **Amazon Bedrock**, your prompts and data are **not used to train the base FMs**, and your fine-tuned model is **private to you** (kept in your account, encrypted). Know this — it's a common scenario ("can we use Bedrock with sensitive data?").
- Watch **data residency / sovereignty** — pick Regions that meet legal requirements; some models/features are Region-limited.
- Beware leaking sensitive data **into prompts** (it may be logged) — govern what goes in.

## 5.3 Governance & compliance
- **Shared responsibility model** still applies: AWS secures the infrastructure/managed service; **you** secure your data, access, prompts, and use case.
- **AWS Artifact** — download compliance reports (SOC, ISO, PCI, HIPAA eligibility).
- **Governance practices:** data lineage/cataloging, model versioning, approval workflows, documented intended use, and **model/data cards**.
- **Regulations to recognize:** GDPR (privacy), HIPAA (health), plus emerging AI-specific rules (e.g. EU AI Act) — the exam wants awareness, not legal depth.

## 5.4 Monitor & audit (who did what, and is it behaving)
| Service | Role |
|---|---|
| **CloudTrail** | audit log of **API calls** (who invoked which model, changed config). |
| **CloudWatch** | metrics, logs, alarms (latency, errors, invocation counts). |
| **Bedrock model invocation logging** | capture prompts/responses to S3/CloudWatch for audit + evaluation. |
| **SageMaker Model Monitor** | drift/quality monitoring of deployed models. |

## 5.5 AI-specific threats to recognize
- **Prompt injection / jailbreaking** — malicious input subverts instructions → mitigate with **Guardrails**, input validation, least privilege on any tools the model can call.
- **Data poisoning** — bad training data corrupts the model → vet/validate data sources.
- **Model/data exfiltration & sensitive-data leakage** → encryption, access control, output filtering.
- **Hallucinated/false output** → RAG grounding + human review (ties to Domain 4 veracity).

## 5.6 Governed AI lifecycle (tie it together)
Secure data (IAM/KMS/VPC) → govern what goes into prompts/training → log + monitor (CloudTrail/CloudWatch/Model Monitor) → guardrail outputs → document (Model Cards) → review high-stakes decisions (A2I).

## How this is real for you
Your `default` profile touches **Healthium prod (PHI-adjacent) data**. Rule of thumb for any AI feature: keep that data in your account, use **Bedrock** (not a public model), enable **VPC endpoints + KMS**, and never paste real patient/customer data into a prompt without redaction.

## Flashcards
- Bedrock: your data **not** used to train base models; fine-tuned model stays private to you.
- CloudTrail = who-did-what (API audit); CloudWatch = metrics/logs/alarms.
- Private connectivity to AI services = **VPC endpoints / PrivateLink**.
- Compliance reports = **AWS Artifact**; shared responsibility still applies.
- Threats: prompt injection, data poisoning, data leakage.

## Hands-on (`$env:AWS_PROFILE="learn"` — verify the security posture, read-only)
```powershell
$env:AWS_PROFILE = "learn"
# Who am I acting as? (least privilege starts with knowing your identity)
aws sts get-caller-identity
# Audit trail: recent Bedrock API calls — who invoked which model:
aws cloudtrail lookup-events `
  --lookup-attributes AttributeKey=EventSource,AttributeValue=bedrock.amazonaws.com --max-results 5
# Is private connectivity in place? (VPC endpoints in your account):
aws ec2 describe-vpc-endpoints --query "VpcEndpoints[].ServiceName" --output table
```
**Cleanup:** none — all read-only checks.

## Practice questions
**Q1.** How do you keep traffic to Amazon Bedrock off the public internet?
- A) Public IP + security group  B) **VPC endpoints / PrivateLink** ✅  C) CloudFront  D) NAT gateway only

**Q2.** Which service tells you **who invoked which model** (audit trail)?
- A) CloudWatch  B) **CloudTrail** ✅  C) Macie  D) Config

**Q3.** A team worries sensitive prompts will be used to train the base model. On Bedrock:
- A) That always happens  B) **Your data isn't used to train base FMs; your fine-tuned model stays private** ✅  C) Only if you opt out  D) Only in us-east-1

**Q4.** Where do you download a SOC 2 / ISO compliance report?
- A) Trusted Advisor  B) GuardDuty  C) **AWS Artifact** ✅  D) Inspector

**Q5.** Best first mitigation against prompt-injection attacks on a customer-facing FM app?
- A) Bigger model  B) **Bedrock Guardrails + input validation + least privilege** ✅  C) Higher temperature  D) Disable logging
