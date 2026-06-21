# AWS Certified Machine Learning Engineer – Associate

> 🍼 **Beginner explanation:** Teaches the full ML lifecycle on AWS — preparing data, training, deploying models as endpoints, monitoring them, and MLOps. The "ship ML to production" cert.
>
> 🌍 **Real-world example:** You trained a churn model in a notebook. This cert teaches you to deploy it as a SageMaker endpoint, monitor drift, automate retraining, and do it securely + cheaply.

| Field | Value |
|---|---|
| **1. Certification name** | AWS Certified Machine Learning Engineer – Associate |
| **2. Exam code** | MLA-C01 |
| **3. Level** | Associate |
| **4. Best for role** | ML engineers, data scientists deploying ML workloads |
| **5. Prerequisites** | ML basics + Python; AIF-C01 / SAA helpful |

---

## 6. Core topics
- ML lifecycle (data prep → train → tune → deploy → monitor)
- Feature engineering & data preparation at scale
- Model training, hyperparameter tuning, evaluation metrics
- Deployment patterns (real-time endpoints, batch transform, async, serverless)
- Monitoring (data/model drift, Model Monitor), MLOps & CI/CD for ML
- Responsible AI, security, cost optimization

## 7. AWS services to learn
| Category | Services |
|---|---|
| ML platform | SageMaker (Studio, Training, Endpoints, Pipelines, Model Monitor, Feature Store, Clarify) |
| GenAI | Bedrock basics |
| Storage/compute | S3, ECR, Lambda, Step Functions |
| Security/Mgmt | IAM, KMS, CloudWatch |

## 8. Hands-on labs
1. **Train a simple model** in SageMaker (built-in algorithm or script). *(Cleanup: stop training jobs, delete Studio apps.)*
2. **Deploy a real-time endpoint**; invoke it. *(Cleanup: DELETE endpoint — it bills per hour!)*
3. **Monitor the endpoint** with Model Monitor / CloudWatch. *(Cleanup: delete monitor schedule + endpoint.)*
4. **Batch inference** with Batch Transform. *(Cleanup: delete transform job artifacts.)*
5. **(Bonus) SageMaker Pipeline** to automate train→deploy. *(Cleanup: delete pipeline + endpoints.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–2 | ML lifecycle + SageMaker overview; Lab 1 |
| 3 | Feature engineering / Feature Store |
| 4–5 | Training + tuning + metrics |
| 6–7 | Deployment patterns; Lab 2; Lab 4 |
| 8 | Monitoring + drift; Lab 3 |
| 9 | MLOps + Pipelines; Lab 5 |
| 10 | Security + cost + responsible AI |
| 11 | Mock #1 + gaps |
| 12 | Revise |
| 13 | Flashcards + service mapping |
| 14 | Mock #2 → book if 80%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Lifecycle + data prep + training (Lab 1) |
| 2 | Deployment + batch (Labs 2, 4) |
| 3 | Monitoring + MLOps + security (Labs 3, 5) |
| 4 | Cost + 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1 | ML concepts + metrics refresher |
| 2 | SageMaker components (Lab 1) |
| 3 | Feature engineering + Feature Store |
| 4 | Training + tuning |
| 5 | Deployment patterns (Labs 2, 4) |
| 6 | Monitoring + drift (Lab 3) |
| 7 | MLOps + Pipelines + security (Lab 5) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **80%+**. Expect scenarios choosing deployment type (real-time vs batch vs async vs serverless) by latency/cost.
- Know evaluation metrics (precision/recall/F1/AUC) and when each matters.
- 4 timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] Deployment options & cost trade-offs
- [ ] Model Monitor: data/quality/bias/drift types
- [ ] Hyperparameter tuning (Bayesian vs random)
- [ ] Feature Store online vs offline
- [ ] SageMaker Pipelines + CI/CD for ML
- [ ] Securing endpoints (IAM, VPC, KMS)
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
| Low-latency single predictions? | SageMaker real-time endpoint |
| Large offline scoring job? | Batch Transform |
| Detect data drift in production? | SageMaker Model Monitor |
| Reuse features across teams? | Feature Store |
| Automate train→deploy? | SageMaker Pipelines |
| Detect bias in models? | SageMaker Clarify |
| Metric for imbalanced classes? | Precision/Recall/F1 (not accuracy) |

→ More in `05-flashcards/aws-flashcards.md`.

## 17. Official docs / resources
- [ ] MLA-C01 exam guide: _add link_
- [ ] SageMaker developer guide: _add link_
- [ ] AWS MLOps best practices: _add link_
- [ ] Official practice exam: _add link_
