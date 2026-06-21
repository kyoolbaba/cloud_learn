# AWS Certified Generative AI Developer – Professional

> 🍼 **Beginner explanation:** Advanced cert for building *production* generative-AI apps on AWS — RAG systems, agents, prompt engineering, guardrails, vector search, plus cost & security. The capstone for a GenAI-focused data scientist.
>
> 🌍 **Real-world example:** A production assistant that answers from your company's documents (RAG), uses tools/agents to take actions, blocks unsafe content (Guardrails), and stays within budget. This cert is exactly that.

> ⚠️ Verify the current exam code/availability before booking — newer GenAI exams evolve quickly.

| Field | Value |
|---|---|
| **1. Certification name** | AWS Certified Generative AI Developer – Professional |
| **2. Exam code** | AIP-C01 |
| **3. Level** | Professional |
| **4. Best for role** | Developers/data scientists building production GenAI apps |
| **5. Prerequisites** | AIF-C01 + dev experience; Bedrock familiarity |

---

## 6. Core topics
- Foundation models & model selection
- Retrieval-Augmented Generation (RAG) + vector databases + embeddings
- Prompt engineering & evaluation
- Agents & tool use / orchestration
- Bedrock (Knowledge Bases, Agents, Guardrails)
- Security, responsible AI, cost & performance optimization

## 7. AWS services to learn
| Category | Services |
|---|---|
| GenAI | Bedrock (FMs, Knowledge Bases, Agents, Guardrails), SageMaker JumpStart |
| Vector/search | OpenSearch (vector), Kendra, Aurora pgvector |
| Supporting | Lambda, Step Functions, S3, API Gateway |
| Security/cost | IAM, KMS, CloudWatch, Bedrock model invocation logging |

## 8. Hands-on labs (design + light build)
1. **RAG app design** — embeddings → vector store → retrieval → FM. *(Cleanup: delete vector index/collection.)*
2. **Bedrock prompt workflow** + parameter tuning (temperature/top-p). *(No persistent cost.)*
3. **Vector search concept** with OpenSearch Serverless. *(Cleanup: delete collection — billed!)*
4. **Guardrails** config to block topics/PII. *(Cleanup: delete guardrail.)*
5. **Monitoring** Bedrock invocations + cost. *(Cleanup: delete log group.)*

## 9. Two-week plan (refresher)
| Day | Focus |
|---|---|
| 1–2 | FMs + model selection + tokens/embeddings |
| 3–4 | RAG architecture; Lab 1 |
| 5 | Vector databases; Lab 3 |
| 6–7 | Prompt engineering + evaluation; Lab 2 |
| 8 | Agents + tool use |
| 9 | Guardrails + responsible AI; Lab 4 |
| 10 | Security + cost + monitoring; Lab 5 |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 75%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | FMs + RAG + embeddings (Labs 1, 3) |
| 2 | Prompts + agents (Lab 2) |
| 3 | Guardrails + security + cost (Labs 4–5) |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1 | GenAI fundamentals + FMs |
| 2 | Embeddings + vector stores (Lab 3) |
| 3 | RAG architecture (Lab 1) |
| 4 | Prompt engineering + evaluation (Lab 2) |
| 5 | Agents + orchestration |
| 6 | Guardrails + responsible AI (Lab 4) |
| 7 | Security + cost + monitoring (Lab 5) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **75%+**. Scenario-heavy: choose RAG vs fine-tune, pick vector store, design guardrails, control cost.
- Practice prompt-engineering and evaluation reasoning questions.
- 3+ timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] RAG vs fine-tuning vs prompt engineering — when to use each
- [ ] Embeddings + vector similarity basics
- [ ] Bedrock Knowledge Bases vs Agents vs Guardrails
- [ ] Vector store options + trade-offs
- [ ] Cost levers (model choice, caching, token limits)
- [ ] Responsible AI + PII protection
- [ ] Flashcards reviewed twice

## 14. Notes template
```
### Topic: <name>
- Concept:
- Real-world use:
- AWS service(s):
- Azure equivalent (Azure OpenAI):
- Common exam trap:
- Trade-off notes:
```

## 15. Mistake log template
| Date | Topic | What I got wrong | Correct concept | Revisit date |
|---|---|---|---|---|

## 16. Flashcards (starter set)
| Q | A |
|---|---|
| Ground an LLM in private docs? | RAG (retrieval + FM) |
| Store/search embeddings? | Vector database (OpenSearch/pgvector) |
| Block unsafe topics/PII in Bedrock? | Guardrails |
| Let an FM call tools/APIs? | Bedrock Agents |
| Reduce hallucinations cheaply? | RAG + better prompts (before fine-tuning) |
| Control randomness of output? | temperature / top-p |

→ More in `05-flashcards/aws-flashcards.md`.

## 17. Official docs / resources
- [ ] AIP-C01 exam guide (verify code): _add link_
- [ ] Amazon Bedrock docs (KB/Agents/Guardrails): _add link_
- [ ] OpenSearch vector search docs: _add link_
- [ ] Official practice exam: _add link_
