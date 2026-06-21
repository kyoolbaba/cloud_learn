# 🔐 IAM & Security (Concept + AWS↔Azure)

> **Concept note:** IAM answers two questions: **who are you** (authentication) and **what can you do** (authorization). Security layers protect identities, data, networks, and apps.

## Core ideas
| Idea | Plain meaning |
|---|---|
| User / group | A person / a set of people |
| Role | A set of permissions that can be assumed (by a user/service) |
| Policy | The document that grants/denies actions |
| Least privilege | Give only the permissions needed |
| MFA | A second login factor |
| Encryption at rest/in transit | Scramble data on disk / on the wire |
| Secrets management | Safe storage for keys/passwords |

## AWS ↔ Azure service mapping
| Capability | AWS | Azure |
|---|---|---|
| Identity provider | IAM / IAM Identity Center | Microsoft Entra ID |
| Permissions model | IAM policies (JSON) | RBAC role assignments |
| Temporary credentials | STS | Managed identities |
| Keys / encryption | KMS / CloudHSM | Key Vault / Managed HSM |
| Secrets | Secrets Manager / Parameter Store | Key Vault / App Configuration |
| Threat detection | GuardDuty | Microsoft Defender for Cloud |
| SIEM | Security Hub | Microsoft Sentinel |
| Sensitive data discovery | Macie | Microsoft Purview |
| Conditional sign-in | (via IAM conditions) | Conditional Access |

## Hands-on lab
- Create a least-privilege user/role that can only read one bucket/container.
- Enable MFA. Store a secret in KMS/Key Vault and read it from a service via role/managed identity.
- **Cleanup:** delete users/roles/secrets.

## ⚠️ Common exam traps
- **Explicit deny always wins** in AWS IAM evaluation.
- Prefer **roles / managed identities** over long-lived access keys.
- Encryption "at rest" ≠ "in transit" — exams test both.
- In Azure, RBAC scope inherits down (management group → subscription → RG → resource).

## 🃏 Flashcards
| Q | A |
|---|---|
| AWS identity service? | IAM |
| Azure identity service? | Microsoft Entra ID |
| Give EC2 access to S3 safely? | IAM role |
| Azure equivalent of IAM role? | Managed identity + RBAC |
| What wins in IAM eval? | Explicit deny |
| Block risky logins (Azure)? | Conditional Access |

🔗 Related: [[networking]] · [[monitoring-logging]]
