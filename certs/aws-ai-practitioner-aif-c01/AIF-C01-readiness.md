---
tags: [cert/aif-c01, aws/ai-ml, readiness]
cert: AIF-C01
aliases: [AIF-C01 Readiness Checklist]
---
> [[AIF-C01|⬅ AIF-C01 Home]] · [[AIF-C01-practice|🧪 Practice Exam]]

# AIF-C01 — exam-readiness checklist

Book only when you can tick **every** box.

## Domain 1 — AI & ML fundamentals
- [ ] Draw AI ⊃ ML ⊃ Deep Learning ⊃ Generative AI
- [ ] Supervised vs unsupervised vs reinforcement (one example each)
- [ ] Classification vs regression vs clustering
- [ ] Training vs inference; what a feature is
- [ ] Name the 3 AWS AI/ML layers (AI services / SageMaker / infra) + 3 AI services

## Domain 2 — Generative AI fundamentals
- [ ] Define foundation model, LLM, token, embedding, vector store, context window
- [ ] Temperature/top-p effect; low = factual, high = creative
- [ ] The adapt ladder: **prompt → RAG → fine-tune → pre-train**
- [ ] Bedrock vs SageMaker (serverless multi-FM API vs build-your-own)

## Domain 3 — Applications of foundation models
- [ ] Zero-shot / few-shot / chain-of-thought on sight
- [ ] Explain RAG end-to-end + Bedrock Knowledge Bases
- [ ] RAG (knowledge) vs fine-tuning (behavior) — when each
- [ ] Bedrock Agents / Guardrails / Knowledge Bases — what each does
- [ ] Eval metrics: ROUGE / BLEU / BERTScore / human eval

## Domain 4 — Responsible AI
- [ ] List the dimensions (fairness, bias, robustness, safety, transparency, explainability, veracity, privacy)
- [ ] Clarify (bias + explainability) vs Model Monitor (drift) vs Guardrails (safe output) vs A2I (human review)
- [ ] What a Model Card / AI Service Card is

## Domain 5 — Security, compliance & governance
- [ ] Secure AI data: IAM least privilege, KMS encryption, VPC endpoints/PrivateLink
- [ ] Bedrock data privacy fact (not used to train base FMs; fine-tune private)
- [ ] CloudTrail (audit) vs CloudWatch (metrics/logs); AWS Artifact (compliance reports)
- [ ] Threats: prompt injection, data poisoning, data leakage + mitigations

## Practice gate
- [ ] Scored **≥ 18/25** on [[AIF-C01-practice|the mock]]
- [ ] Took the official AWS Skill Builder **AIF-C01 practice question set**

## Logistics
- [ ] Confirmed current exam format on the **official AIF-C01 Exam Guide PDF**
- [ ] Registered at aws.amazon.com/certification (Pearson VUE: test center or online-proctored)
- [ ] Know cost (~$100) + that it's foundational (no prereqs)

## Free official resources
- **AWS Skill Builder** — "AWS Certified AI Practitioner" learning plan + official practice questions
- **PartyRock** (partyrock.aws) — free hands-on with FMs/prompts
- **Amazon Bedrock User Guide** — read the intro + Knowledge Bases + Guardrails sections
- **AIF-C01 Exam Guide + sample questions** (PDF) — the source of truth

When every box is ticked → **book it**, then continue to [[MLA-C01|MLA-C01 (your bullseye)]] or [[DEA-C01|DEA-C01]]. See [[CERT_ROADMAP]].
