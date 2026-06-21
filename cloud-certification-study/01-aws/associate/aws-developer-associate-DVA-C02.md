# AWS Certified Developer – Associate

> 🍼 **Beginner explanation:** Teaches how to *build and deploy* applications on AWS — especially serverless apps with Lambda, APIs, and DynamoDB, plus CI/CD and debugging.
>
> 🌍 **Real-world example:** Build a serverless REST API that stores form submissions in DynamoDB and notifies a queue — no servers to manage.

| Field | Value |
|---|---|
| **1. Certification name** | AWS Certified Developer – Associate |
| **2. Exam code** | DVA-C02 |
| **3. Level** | Associate |
| **4. Best for role** | Developers building/deploying apps on AWS |
| **5. Prerequisites** | ~1 year dev experience + AWS basics; CLF-C02 helpful |

---

## 6. Core topics
- Serverless development (Lambda, API Gateway)
- DynamoDB (data modeling, capacity, indexes)
- Messaging/eventing (SQS, SNS, EventBridge, Kinesis basics)
- CI/CD (CodeCommit, CodeBuild, CodeDeploy, CodePipeline)
- IAM roles for apps, Cognito (auth), encryption (KMS)
- Observability (CloudWatch logs/metrics, X-Ray), SDK/CLI usage

## 7. AWS services to learn
| Category | Services |
|---|---|
| Compute | Lambda, Elastic Beanstalk, ECS/Fargate basics |
| API/Integration | API Gateway, SQS, SNS, EventBridge, Step Functions |
| Data | DynamoDB, S3, ElastiCache |
| CI/CD | CodeBuild, CodeDeploy, CodePipeline, SAM/CloudFormation |
| Security | IAM, Cognito, KMS, Secrets Manager, Parameter Store |
| Observability | CloudWatch, X-Ray |

## 8. Hands-on labs
1. **Serverless API:** API Gateway → Lambda → return JSON. *(Cleanup: delete API, Lambda.)*
2. **Lambda + DynamoDB CRUD app.** *(Cleanup: delete table, Lambda.)*
3. **SQS workflow:** producer Lambda → SQS → consumer Lambda. *(Cleanup: delete queue, Lambdas.)*
4. **CI/CD pipeline:** CodePipeline deploying a Lambda via SAM. *(Cleanup: delete pipeline + stack.)*
5. **X-Ray tracing** on the serverless API. *(Cleanup: delete resources.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–2 | Lambda fundamentals; Lab 1 |
| 3–4 | DynamoDB modeling + indexes; Lab 2 |
| 5–6 | SQS/SNS/EventBridge; Lab 3 |
| 7 | API Gateway depth |
| 8–9 | CI/CD (Code* services + SAM); Lab 4 |
| 10 | Security (IAM/Cognito/KMS/Secrets) |
| 11 | Observability (CloudWatch/X-Ray); Lab 5 |
| 12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 80%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Lambda + API Gateway + DynamoDB (Labs 1–2) |
| 2 | Messaging + Step Functions (Lab 3) |
| 3 | CI/CD + security + observability (Labs 4–5) |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | Lambda + serverless patterns (Lab 1) |
| 3 | DynamoDB (Lab 2) |
| 4 | Messaging/eventing (Lab 3) |
| 5 | API Gateway + auth (Cognito) |
| 6 | CI/CD (Lab 4) |
| 7 | Security + observability (Lab 5) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **80%+**. Many questions test exact service behavior (DynamoDB capacity, Lambda limits, deployment types).
- Memorize CodeDeploy deployment configs (in-place vs blue/green; canary/linear).
- 4 timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] Lambda limits (timeout, memory, /tmp, concurrency)
- [ ] DynamoDB: partition key design, LSI vs GSI, RCU/WCU
- [ ] SQS standard vs FIFO; visibility timeout; DLQ
- [ ] CodeDeploy deployment strategies
- [ ] Cognito user pools vs identity pools
- [ ] Parameter Store vs Secrets Manager
- [ ] Flashcards reviewed twice

## 14. Notes template
```
### Topic: <name>
- Beginner explanation:
- Real-world use:
- AWS service(s):
- Azure equivalent:
- Common exam trap:
- My example:
```

## 15. Mistake log template
| Date | Topic | What I got wrong | Correct concept | Revisit date |
|---|---|---|---|---|

## 16. Flashcards (starter set)
| Q | A |
|---|---|
| FIFO queue use case? | Order-sensitive, exactly-once processing |
| GSI vs LSI? | GSI: different partition key, any time; LSI: same partition key, create at table creation |
| Lambda max timeout? | 15 minutes |
| Store DB password securely with rotation? | Secrets Manager |
| Blue/green on Lambda gradual shift? | CodeDeploy canary/linear |
| Trace a request across services? | AWS X-Ray |

→ More in `05-flashcards/aws-flashcards.md`.

## 17. Official docs / resources
- [ ] DVA-C02 exam guide: _add link_
- [ ] AWS Serverless / SAM docs: _add link_
- [ ] DynamoDB developer guide: _add link_
- [ ] Official practice exam: _add link_
