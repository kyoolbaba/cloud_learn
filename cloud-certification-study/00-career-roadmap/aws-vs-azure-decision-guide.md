# ⚖️ AWS vs Azure — Decision Guide

You don't have to pick *forever*. But for any given month, focus on one. This guide helps you choose.

---

## Quick decision

| If... | Lean toward |
|---|---|
| Your target companies/job ads mostly say "AWS" | **AWS** |
| Your company already runs Microsoft (Office 365, Windows, Active Directory) | **Azure** |
| You want the largest market share / most tutorials | **AWS** |
| You want strong enterprise + hybrid + Microsoft integration | **Azure** |
| You're in data science and want best GenAI tooling today | Both strong — AWS **Bedrock** vs Azure **OpenAI Service** |
| You genuinely don't know | Start **AWS** (bigger ecosystem), add Azure fundamentals alongside |

---

## Service equivalents (the cheat sheet)

| Capability | AWS | Azure |
|---|---|---|
| Virtual machines | EC2 | Virtual Machines |
| Serverless functions | Lambda | Azure Functions |
| Object storage | S3 | Blob Storage |
| Block storage | EBS | Managed Disks |
| File storage | EFS | Azure Files |
| Virtual network | VPC | Virtual Network (VNet) |
| Identity / access | IAM | Microsoft Entra ID + RBAC |
| Relational DB (managed) | RDS / Aurora | Azure SQL Database |
| NoSQL | DynamoDB | Cosmos DB |
| Data warehouse | Redshift | Synapse / Microsoft Fabric |
| ETL / data integration | Glue | Data Factory / Synapse Pipelines |
| Query data in place | Athena | Synapse Serverless SQL |
| Streaming | Kinesis | Event Hubs |
| ML platform | SageMaker | Azure Machine Learning |
| Generative AI | Bedrock | Azure OpenAI Service |
| Monitoring | CloudWatch | Azure Monitor |
| Audit logging | CloudTrail | Activity Log / Azure Monitor |
| Secrets/keys | KMS / Secrets Manager | Key Vault |
| Infra as code | CloudFormation / CDK | ARM / Bicep |
| CI/CD | CodePipeline | Azure DevOps / GitHub Actions |
| Container orchestration | EKS / ECS | AKS |
| Threat detection | GuardDuty | Microsoft Defender for Cloud |
| SIEM | Security Hub | Microsoft Sentinel |

> 📌 Memorize this table. Many interviews and both certs reward knowing the mapping. Full detail lives in `03-shared-cloud-concepts/`.

---

## Cost & learning notes
- **AWS Free Tier:** 12 months of limited free usage + always-free amounts.
- **Azure Free:** $200 credit for 30 days + 12 months free on popular services + always-free services.
- Both will charge for anything beyond free limits — **set billing alerts**.

🔗 Related: [[recommended-path-for-data-scientist]] · [[certification-priority-matrix]]
