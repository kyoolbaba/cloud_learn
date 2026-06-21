# AWS Certified AI Practitioner

> 🍼 **Beginner explanation:** Proves you understand AI/ML and generative AI concepts and how AWS's AI services work — without heavy coding. Ideal as a data scientist's "AWS AI vocabulary" cert.
>
> 🌍 **Real-world example:** Your team wants a chatbot over company docs. This cert teaches the concepts (foundation models, RAG, responsible AI) and which AWS services (Bedrock, SageMaker) to reach for.

| Field | Value |
|---|---|
| **1. Certification name** | AWS Certified AI Practitioner |
| **2. Exam code** | AIF-C01 |
| **3. Level** | Foundational |
| **4. Best for role** | AI/ML beginners, data scientists, product/business users working with AI |
| **5. Prerequisites** | None; basic cloud (CLF-C02) helpful |

---

## 6. Core topics
- AI/ML/Deep Learning concepts and terminology
- Types of ML: supervised, unsupervised, reinforcement
- Generative AI & foundation models (FMs), tokens, embeddings, prompt engineering
- Amazon Bedrock basics (FMs as a service)
- Responsible AI (bias, fairness, transparency, guardrails)
- AWS AI service catalog and when to use each
- Model evaluation basics, cost/security considerations for AI

## 7. AWS services to learn
| Category | Services |
|---|---|
| GenAI | Amazon Bedrock, Bedrock Guardrails, Bedrock Knowledge Bases |
| ML platform | SageMaker (AI) overview, JumpStart |
| Vision | Rekognition |
| Language/NLP | Comprehend, Translate, Transcribe, Polly |
| Search/RAG | OpenSearch (vector), Kendra |
| Supporting | S3, IAM, CloudWatch |

## 8. Hands-on labs
1. **Explore Amazon Bedrock** console; try a text prompt with a foundation model. *(Cleanup: nothing persistent created)*
2. **SageMaker overview** — open Studio, note JumpStart models. *(Cleanup: stop/delete Studio apps + domain if created)*
3. **Rekognition demo** — upload an image, view labels. *(Cleanup: delete uploaded images)*
4. **Comprehend demo** — run sentiment/entity detection on sample text. *(Cleanup: none)*
5. **Responsible AI notes** — write how you'd add Guardrails to a chatbot. *(No cloud cost)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–2 | AI/ML basics + terminology |
| 3–4 | Generative AI + foundation models; Lab 1 |
| 5–6 | AWS AI services tour; Labs 3–4 |
| 7–8 | Bedrock + SageMaker concepts; Lab 2 |
| 9 | Responsible AI; Lab 5 |
| 10 | Flashcards + service mapping |
| 11–12 | Mock #1, log gaps |
| 13 | Revise weak topics |
| 14 | Mock #2 → book if 85%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | AI/ML fundamentals + terminology |
| 2 | Generative AI, FMs, Bedrock (Labs 1–2) |
| 3 | AI services catalog + responsible AI (Labs 3–5) |
| 4 | Mocks + revision + book |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | ML concepts + types of learning |
| 3–4 | Generative AI, prompts, embeddings, RAG concept |
| 5 | Bedrock + SageMaker (Labs 1–2) |
| 6 | AI services catalog (Labs 3–4) |
| 7 | Responsible AI + security/cost (Lab 5) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **85%+**. Foundational but with GenAI depth.
- Focus mocks on: choosing the right AWS AI service, responsible-AI scenarios, Bedrock vs SageMaker.
- 3 timed mocks; log every miss to `04-trackers/weak-topic-log.md`.

## 13. Final revision checklist (last 3 days)
- [ ] Can define FM, token, embedding, prompt, RAG, fine-tuning
- [ ] Know when to use Bedrock vs SageMaker
- [ ] Can match Rekognition/Comprehend/Transcribe/Polly/Translate to use cases
- [ ] Can list responsible-AI dimensions + Guardrails purpose
- [ ] Reviewed all flashcards twice

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
| | | | | |

## 16. Flashcards (starter set)
| Q | A |
|---|---|
| What is a foundation model? | A large pre-trained model adaptable to many tasks |
| Bedrock vs SageMaker? | Bedrock = managed FMs via API; SageMaker = build/train/deploy your own |
| What is RAG? | Retrieval-Augmented Generation: ground an LLM with your data |
| Service for image labels? | Rekognition |
| Service for sentiment/entities in text? | Comprehend |
| What do Bedrock Guardrails do? | Filter/limit unsafe content & topics |
| What is fine-tuning? | Further training an FM on your data |

→ More in `05-flashcards/aws-flashcards.md`.

## 17. Official docs / resources
- [ ] AIF-C01 exam guide: _add link_
- [ ] Amazon Bedrock docs: _add link_
- [ ] AWS Responsible AI resources: _add link_
- [ ] AWS Skill Builder AI Practitioner course: _add link_
