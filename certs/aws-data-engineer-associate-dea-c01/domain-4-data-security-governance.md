---
tags: [cert/dea-c01, aws/data-engineering, security, governance]
cert: DEA-C01
domain: 4
aliases: [DEA-C01 Domain 4, Data Security and Governance]
---
> [[domain-3-data-operations-support|◀ Domain 3]] · [[DEA-C01|DEA-C01 Home]] · [[DEA-C01-practice|Practice Exam ▶]]

# Domain 4 — Data Security & Governance (18%)

Protecting data and controlling **who can see which rows/columns**. Heavy reuse of CLF-C02
security + [[domain-5-security-compliance-governance|AIF-C01 Domain 5]].

## 4.1 Access control (the data-engineering twist = fine-grained)
- **IAM** — identity + coarse resource permissions (who can call Glue/Athena/S3).
- **AWS Lake Formation** — the key DEA service: **fine-grained** lake permissions at **database / table / column / row / cell** level, centrally, over the Glue Catalog + S3.
- **LF-Tags (tag-based access control)** — attach tags to catalog resources, grant by tag → scales to many tables without per-table grants.
- **Cross-account sharing** via Lake Formation / Redshift data sharing without copying data.

**Trap:** "let analysts see all columns except `salary`" or "only rows for their region" → **Lake Formation column/row-level security**, not a bucket policy.

## 4.2 Encryption
- **At rest:** **KMS** keys — S3 **SSE-KMS** (auditable, customer-managed CMKs) vs SSE-S3 (AWS-managed); Redshift, RDS, EBS, Glue all support KMS. **In transit:** TLS everywhere.
- **Key management:** customer-managed CMK when you need key rotation control, grants, and CloudTrail on key use.

## 4.3 Sensitive data: find, mask, anonymize
- **Amazon Macie** — ML-based discovery of **PII/sensitive data in S3** (then you can quarantine/encrypt).
- **Masking/redaction** — Glue transforms, **Redshift dynamic data masking**, tokenization; anonymize before sharing for analytics.
- Classify data (public/internal/restricted) and apply controls per class.

## 4.4 Network protection
- **VPC** + **VPC endpoints (Gateway for S3/DynamoDB, Interface/PrivateLink for Glue/Athena/etc.)** keep data traffic off the public internet.
- Keep stores in **private subnets**; tight security groups; no public S3 (Block Public Access on).

## 4.5 Auditing & monitoring
- **CloudTrail** — every API call (who queried/changed/exported data).
- **S3 server access logs / CloudWatch** — access + operational logs.
- **AWS Config** — track resource configuration/compliance over time.

## 4.6 Governance, lineage & retention
- **Glue Data Catalog** + **Lake Formation** = governed, discoverable metadata.
- **Amazon DataZone** — business catalog, data products, discovery + governance across teams; supports **data lineage**.
- **Retention/immutability:** S3 **Versioning** + **Object Lock** (WORM/compliance mode), lifecycle to archive; RDS/Redshift snapshots.
- **Compliance:** download reports via **AWS Artifact**; shared responsibility still applies.

## How this is real for you
Healthium prod data is PHI-adjacent. A compliant DEA design: S3 with **Block Public Access + SSE-KMS**, **Lake Formation** so analysts see only permitted columns/rows, **Macie** scanning for stray PII, **VPC endpoints** for private access, and **CloudTrail** auditing every query.

## Hands-on (`$env:AWS_PROFILE="learn"` — lock a bucket down)
```powershell
$env:AWS_PROFILE = "learn"
$b = "yourname-dea-sec-lab"
aws s3api create-bucket --bucket $b --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1
# 1) Block ALL public access (governance baseline):
aws s3api put-public-access-block --bucket $b --public-access-block-configuration `
  BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
# 2) Default encryption at rest (SSE-KMS via the AWS-managed aws/s3 key = no key cost):
'{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"aws:kms"}}]}' | Out-File -Encoding ascii enc.json
aws s3api put-bucket-encryption --bucket $b --server-side-encryption-configuration file://enc.json
aws s3api get-bucket-encryption --bucket $b   # prove encryption is on
```
**Cleanup:** `aws s3 rb s3://$b --force; Remove-Item enc.json`. (Macie + Lake Formation are console-driven — try them on this bucket, then disable.)

## Flashcards
- Lake Formation = fine-grained (column/row/cell) lake permissions + LF-Tags.
- Macie = find PII in S3; KMS/SSE-KMS = encryption at rest; TLS = in transit.
- VPC endpoints/PrivateLink = private access to data services.
- CloudTrail = audit; Config = config/compliance tracking; Artifact = compliance reports.
- S3 Object Lock = WORM/immutability for retention.

## Practice questions
**Q1.** Analysts may query a table but must **not** see the `ssn` column. Best mechanism?
- A) Bucket policy  B) **Lake Formation column-level permissions** ✅  C) KMS key policy  D) Security group

**Q2.** Automatically discover credit-card numbers sitting in S3:
- A) GuardDuty  B) Inspector  C) **Macie** ✅  D) Config

**Q3.** Keep Athena/Glue traffic off the public internet:
- A) NAT only  B) **VPC endpoints / PrivateLink** ✅  C) CloudFront  D) Public subnet

**Q4.** Need auditable, customer-controlled encryption keys with usage logged in CloudTrail:
- A) SSE-S3  B) **SSE-KMS with a customer-managed CMK** ✅  C) Client gzip  D) No encryption

**Q5.** Make objects immutable for a 7-year retention requirement:
- A) Versioning only  B) Lifecycle expire  C) **S3 Object Lock (compliance mode)** ✅  D) Glacier without lock
