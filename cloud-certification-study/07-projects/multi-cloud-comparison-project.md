# 🛠️ Project: Multi-Cloud Comparison (AWS vs Azure, Same Workload)

> **Goal:** Build the *same* simple workload on both clouds and document the differences. This is the single best exercise for cementing the AWS↔Azure mapping that pays off in exams **and** interviews.
>
> 🌍 **Real-world story:** "We might switch clouds / we're multi-cloud." You can speak fluently about both because you've built on both.

## Pick ONE workload to mirror
| Option | AWS | Azure |
|---|---|---|
| **A. Static site + CDN** | S3 + CloudFront | Blob static site + Front Door |
| **B. Serverless API** | API Gateway + Lambda + DynamoDB | API Mgmt/HTTP + Functions + Cosmos DB |
| **C. Mini data pipeline** | S3 + Glue + Athena | Data Lake + Data Factory + Synapse |
| **D. Tiny RAG app** | Bedrock + OpenSearch | Azure OpenAI + AI Search |

> Recommended for you (data scientist): **C** or **D**.

## Deliverable: a comparison table you fill in
| Dimension | AWS | Azure | Notes |
|---|---|---|---|
| Services used | | | |
| Setup difficulty (1–5) | | | |
| Time to build | | | |
| Cost (est.) | | | |
| IAM/identity model | | | |
| Monitoring tools | | | |
| What I preferred | | | |

## Steps
1. Build the chosen workload on **AWS**; note each service + friction.
2. Build the **same** workload on **Azure**; note the equivalent service.
3. Fill the comparison table above.
4. Draw **two architecture diagrams** side by side.
5. Write 5 bullet "lessons learned."

## ✅ Success criteria
- [ ] Same workload works on both clouds
- [ ] Comparison table complete
- [ ] You can explain each service's equivalent without notes

## 💸 Cleanup (do it on BOTH!)
- [ ] AWS: terminate/delete all resources; check Cost Explorer
- [ ] Azure: delete the resource group(s); check Cost Management
- [ ] Update `04-trackers/lab-completion-tracker.md` for both

## 📝 Reflection / write-up (great resume/LinkedIn material)
- 5 lessons learned:
- Which cloud felt better for data/AI work, and why?
- Link this to the mapping deck → [[../05-flashcards/shared-cloud-flashcards]]

🔗 Related: [[../00-career-roadmap/aws-vs-azure-decision-guide]] · [[aws-data-pipeline-project]] · [[azure-data-pipeline-project]] · [[azure-ai-project]]
