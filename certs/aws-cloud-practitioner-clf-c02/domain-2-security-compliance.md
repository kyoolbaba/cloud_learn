---
tags: [cert/clf-c02, aws/foundational, security]
cert: CLF-C02
domain: 2
aliases: [CLF-C02 Domain 2, Security and Compliance]
---
> [[domain-1-cloud-concepts|◀ Domain 1]] · [[CLF-C02|CLF-C02 Home]] · [[domain-3-technology-services|Domain 3 · Tech ▶]]

# Domain 2 — Security & Compliance (30%)

The biggest single domain. Centered on the **Shared Responsibility Model** and **IAM**.
You've already built most of this hands-on in Projects 00 & 04.

## 2.1 Shared Responsibility Model (THE most tested concept)
- **AWS = security OF the cloud** — hardware, the global infrastructure (Regions/AZs/edge),
  the hypervisor, managed-service internals.
- **You = security IN the cloud** — your data, IAM users/permissions, OS patching (on EC2),
  security-group rules, encryption settings, application code.

The line **shifts by service type:**
| Service | You patch the OS? | Example |
|---|---|---|
| IaaS (EC2) | **Yes** (you manage OS, firewall, patching) | EC2 |
| Managed (RDS, Lambda, S3) | **No** — AWS patches the OS/runtime; you manage data + access | RDS, Lambda |

> Always-yours no matter what: **your data, IAM/access management, client-side encryption.**

## 2.2 IAM (Identity and Access Management)
- **Root user** = the account owner; near-unlimited. **Lock it down**: enable MFA, don't use
  it daily, don't create root access keys. (You did this in setup.)
- **IAM user** = a person/app identity. **Group** = a set of users sharing permissions.
- **Role** = temporary credentials an identity/service *assumes* (e.g., EC2 → S3 with no keys).
  Prefer roles over long-lived access keys.
- **Policy** = JSON granting/denying actions on resources. **Least privilege** = grant only what's needed.
- **MFA** = second factor (authenticator app); protects against stolen passwords.
- **IAM Identity Center** (successor to AWS SSO) = central sign-in / federation to many accounts.
- IAM is **global** (not per-Region). Explicit **Deny** always beats Allow.

## 2.3 Security & monitoring services (recognize each)
| Service | One-liner |
|---|---|
| **AWS Shield** | DDoS protection (Standard free; Advanced paid) |
| **AWS WAF** | Web Application Firewall — filters HTTP (SQLi, XSS) |
| **Amazon GuardDuty** | Intelligent **threat detection** (analyzes logs for malicious activity) |
| **Amazon Inspector** | Automated **vulnerability** scanning (EC2, ECR images, Lambda) |
| **Amazon Macie** | Finds **sensitive data / PII** in S3 |
| **AWS KMS** | Managed **encryption keys** |
| **AWS CloudHSM** | Dedicated hardware security module |
| **AWS Secrets Manager** | Store/rotate secrets (DB passwords, API keys) |
| **AWS CloudTrail** | **Audit log of API calls** — "who did what, when" |
| **AWS Config** | Tracks **resource configuration** + compliance over time |
| **AWS Security Hub** | Central security-findings dashboard |
| **Amazon Detective** | Investigate/root-cause security findings |
| **AWS Artifact** | Self-service **compliance reports** (SOC, PCI, ISO) |
| **AWS Trusted Advisor** | Best-practice checks (incl. security) |

Tells: "detect threats" → **GuardDuty**; "find PII in S3" → **Macie**; "vulnerability scan" →
**Inspector**; "who made this API call" → **CloudTrail**; "download a PCI compliance report" → **Artifact**.

## 2.4 Compliance & encryption
- **AWS Compliance Programs**: PCI-DSS, HIPAA, SOC 1/2/3, ISO, FedRAMP, GDPR — proof via **Artifact**.
- **Encryption at rest** (KMS, SSE-S3, EBS encryption) and **in transit** (TLS/HTTPS).
- **AWS is responsible** for compliance OF the infrastructure; **you** configure your resources to be compliant.

## Hands-on (you've largely done this)
```powershell
$env:AWS_PROFILE = "learn"
aws iam list-users
aws iam list-roles --query "Roles[].RoleName" --output table
# CloudTrail: see your own API history (Event history is on by default)
aws cloudtrail lookup-events --max-results 5 --query "Events[].EventName"
```
Revisit `projects/04-iam-least-privilege` — creating a tight policy and proving it's denied
*is* this domain. Open **IAM Access Analyzer** and **Trusted Advisor** (security checks) in the console.

## Practice questions
**Q1.** Patching the guest OS on an EC2 instance is whose responsibility?
- A) AWS  B) **The customer** ✅  C) Shared equally  D) The AMI vendor

**Q2.** Which service provides an audit trail of all API calls in your account?
- A) Config  B) GuardDuty  C) **CloudTrail** ✅  D) CloudWatch

**Q3.** You need to discover credit-card numbers accidentally stored in S3. Use:
- A) Inspector  B) **Macie** ✅  C) GuardDuty  D) WAF

**Q4.** Best practice for the root user? (choose 2)
- A) **Enable MFA** ✅  B) Use it for daily admin  C) Create root access keys  D) **Don't use it for everyday tasks** ✅

**Q5.** Where do you download a SOC 2 compliance report?
- A) **AWS Artifact** ✅  B) Security Hub  C) Trusted Advisor  D) Config

**Q6.** An app on EC2 needs S3 access. Most secure approach?
- A) Hard-code access keys  B) Store keys in the AMI  C) **Attach an IAM role to the instance** ✅  D) Use the root keys

**Q7.** Which gives intelligent threat detection by analyzing CloudTrail/VPC/DNS logs?
- A) Inspector  B) Macie  C) **GuardDuty** ✅  D) Shield
