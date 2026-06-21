# 🃏 AWS Flashcards

Cover the answer column, recall, then check. Review ~10 min daily. Move misses to `04-trackers/weak-topic-log.md`.

## Core / Cloud Practitioner
| Q | A |
|---|---|
| Region vs AZ? | Region = geographic area; AZ = isolated data center(s) within it |
| Shared Responsibility: AWS vs you? | AWS secures *of* the cloud; you secure *in* the cloud |
| Object storage? | S3 |
| Run virtual machines? | EC2 |
| Serverless functions? | Lambda |
| Spending alert tool? | AWS Budgets |
| Cheapest 24/7-phone support plan? | Business |
| Root account best practice? | Enable MFA; don't use daily |

## Compute & Architecture
| Q | A |
|---|---|
| Interruptible cheap compute? | Spot |
| Steady workload discount? | Savings Plans / Reserved |
| HA database? | RDS Multi-AZ |
| Scale RDS reads? | Read replicas |
| Decouple components? | SQS (queue) / SNS (pub-sub) |
| Global low-latency content? | CloudFront |
| Kubernetes? | EKS |
| 6 Well-Architected pillars? | Ops, Security, Reliability, Performance, Cost, Sustainability |

## Storage & Data
| Q | A |
|---|---|
| Cheapest archive? | S3 Glacier Deep Archive |
| Query S3 with SQL, serverless? | Athena |
| Best analytics file format? | Parquet |
| ETL + catalog service? | Glue |
| Petabyte warehouse? | Redshift |
| Streaming ingest? | Kinesis |
| Fine-grained lake permissions? | Lake Formation |

## Networking
| Q | A |
|---|---|
| Private network? | VPC |
| Stateful instance firewall? | Security Group |
| Stateless subnet filter? | NACL |
| Connect many VPCs + on-prem? | Transit Gateway |
| Private link to on-prem? | Direct Connect |
| Private access to S3 (no internet)? | Gateway VPC endpoint |

## Security
| Q | A |
|---|---|
| Wins in IAM evaluation? | Explicit deny |
| Give EC2 access to S3? | IAM role |
| Threat detection from logs/behavior? | GuardDuty |
| Who called this API? | CloudTrail |
| Find PII in S3? | Macie |
| Managed encryption keys + audit? | KMS |
| Limit max permissions of a role? | Permission boundary |

## AI / ML
| Q | A |
|---|---|
| Managed foundation models? | Bedrock |
| Build/train/deploy your own ML? | SageMaker |
| Reduce hallucination cheaply? | RAG |
| Block unsafe LLM content? | Bedrock Guardrails |
| Real-time predictions? | SageMaker endpoint |
| Large offline scoring? | Batch Transform |
| Detect model drift? | SageMaker Model Monitor |
| Metric for imbalanced data? | Precision/Recall/F1 |

## Observability
| Q | A |
|---|---|
| Performance metrics/alarms? | CloudWatch |
| API audit log? | CloudTrail |
| Compliance/config state? | AWS Config |
| Distributed tracing? | X-Ray |

> Add your own cards as you study each cert file (section 16).
🔗 Related: [[shared-cloud-flashcards]] · [[azure-flashcards]]
