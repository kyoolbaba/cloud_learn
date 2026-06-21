# 🃏 Shared Cloud Flashcards (AWS ↔ Azure Mapping)

The most interview- and exam-valuable deck: knowing the **equivalent** service in the other cloud. Cover one column, name the other.

## Compute
| Capability | AWS | Azure |
|---|---|---|
| Virtual machines | EC2 | Virtual Machines |
| Serverless functions | Lambda | Azure Functions |
| PaaS web hosting | Elastic Beanstalk | App Service |
| Kubernetes | EKS | AKS |
| Auto scaling | Auto Scaling Groups | VM Scale Sets |

## Storage
| Capability | AWS | Azure |
|---|---|---|
| Object | S3 | Blob Storage |
| Block (VM disk) | EBS | Managed Disks |
| File share | EFS | Azure Files |
| Archive | Glacier | Blob Archive |

## Networking
| Capability | AWS | Azure |
|---|---|---|
| Private network | VPC | VNet |
| Instance firewall | Security Group | NSG |
| L7 load balancer | ALB | Application Gateway |
| L4 load balancer | NLB | Azure Load Balancer |
| Global delivery | CloudFront | Front Door |
| DNS | Route 53 | Azure DNS / Traffic Manager |
| Private link to on-prem | Direct Connect | ExpressRoute |
| Connect many networks | Transit Gateway | Virtual WAN |

## Databases & Data
| Capability | AWS | Azure |
|---|---|---|
| Managed relational | RDS / Aurora | Azure SQL |
| NoSQL | DynamoDB | Cosmos DB |
| Cache | ElastiCache | Azure Cache for Redis |
| Warehouse | Redshift | Synapse / Fabric |
| ETL | Glue | Data Factory |
| Query-in-place | Athena | Synapse Serverless SQL |
| Streaming | Kinesis | Event Hubs |
| Search | OpenSearch | Azure AI Search |

## Identity & Security
| Capability | AWS | Azure |
|---|---|---|
| Identity | IAM | Microsoft Entra ID |
| Keys/encryption | KMS | Key Vault |
| Secrets | Secrets Manager | Key Vault |
| Threat detection | GuardDuty | Defender for Cloud |
| SIEM | Security Hub | Microsoft Sentinel |
| Sensitive data discovery | Macie | Microsoft Purview |

## AI / ML
| Capability | AWS | Azure |
|---|---|---|
| ML platform | SageMaker | Azure Machine Learning |
| Foundation models | Bedrock | Azure OpenAI |
| Vision | Rekognition | Azure AI Vision |
| Language | Comprehend | Azure AI Language |
| Doc extraction | Textract | Document Intelligence |
| RAG/search | Kendra / OpenSearch | Azure AI Search |

## Management & DevOps
| Capability | AWS | Azure |
|---|---|---|
| Metrics/alarms | CloudWatch | Azure Monitor |
| Audit log | CloudTrail | Activity Log |
| Infra as code | CloudFormation / CDK | ARM / Bicep |
| CI/CD | CodePipeline | Azure Pipelines / GitHub Actions |
| Cost analysis | Cost Explorer | Cost Management |
| Recommendations | Trusted Advisor | Azure Advisor |

🔗 Related: [[aws-flashcards]] · [[azure-flashcards]] · [[../00-career-roadmap/aws-vs-azure-decision-guide]]
