---
tags: [cert/aif-c01, aws/ai-ml, practice-exam]
cert: AIF-C01
aliases: [AIF-C01 Practice Exam, AIF-C01 Mock]
---
> [[AIF-C01|⬅ AIF-C01 Home]] · [[AIF-C01-readiness|Readiness Checklist ➡]]

# AIF-C01 — mixed mock exam (25 Q)

Roughly domain-weighted (AI/ML 20% · GenAI 24% · FM Apps 28% · Responsible AI 14% · Security 14%).
Cover the key, do all 25 in one ~30-min sitting, then review **every** miss. Target ≥ 70% (18/25).

1. Which term contains all the others: AI, ML, deep learning, generative AI?
   A) ML  B) Deep learning  C) **AI**  D) Generative AI

2. Predicting next month's sales (a continuous number) is:
   A) Classification  B) **Supervised regression**  C) Clustering  D) Reinforcement learning

3. Add sentiment analysis to reviews with no model training and no ML staff:
   A) SageMaker  B) **Amazon Comprehend**  C) EC2 + PyTorch  D) Forecast

4. Grouping customers into segments with no labels:
   A) Regression  B) Classification  C) **Clustering (unsupervised)**  D) RL

5. Using a trained model to make a prediction in production is:
   A) Training  B) **Inference**  C) Labeling  D) Feature engineering

6. Serverless access to many foundation models through one API:
   A) SageMaker  B) **Amazon Bedrock**  C) Comprehend  D) EC2

7. You're billed per ___ for foundation-model usage:
   A) request only  B) **token (input + output)**  C) GB stored  D) vCPU-hour

8. An embedding is:
   A) a GPU type  B) **a numeric vector capturing meaning**  C) a prompt template  D) a billing unit

9. Output must be consistent and factual every run. Set:
   A) high temperature  B) **low temperature**  C) higher top-k  D) bigger max tokens

10. Cheapest first step to improve FM answers, before any retraining:
    A) Fine-tuning  B) Continued pre-training  C) **Prompt engineering**  D) Train from scratch

11. Answer from private PDFs, kept current, no retraining:
    A) Fine-tune nightly  B) **RAG**  C) Raise temperature  D) Bigger model

12. Putting 3 example input→output pairs in the prompt is:
    A) Zero-shot  B) **Few-shot**  C) Fine-tuning  D) RAG

13. AWS feature that wires up RAG over your S3 docs:
    A) Bedrock Agents  B) **Bedrock Knowledge Bases**  C) Guardrails  D) Macie

14. Best metric to evaluate a summarization model:
    A) BLEU  B) **ROUGE**  C) RMSE  D) Accuracy

15. You need the FM to call your API and take multi-step actions:
    A) Knowledge Bases  B) **Bedrock Agents**  C) Guardrails  D) Embeddings

16. "Think step by step" to improve reasoning is:
    A) Few-shot  B) **Chain-of-thought**  C) RAG  D) Zero-shot

17. RAG vs fine-tuning — fine-tuning primarily changes:
    A) the facts it knows  B) **its behavior/style/format**  C) the Region  D) the token price

18. Block toxic output and redact PII from an FM app:
    A) Clarify  B) **Bedrock Guardrails**  C) Model Cards  D) Kendra

19. Detect bias in training data and explain predictions:
    A) Model Monitor  B) **SageMaker Clarify**  C) Guardrails  D) GuardDuty

20. Watch a deployed model for data/quality drift over time:
    A) Clarify  B) **SageMaker Model Monitor**  C) Artifact  D) Lex

21. Route low-confidence predictions to humans for review:
    A) **Amazon Augmented AI (A2I)**  B) CloudTrail  C) Personalize  D) Polly

22. A model performs much worse for one demographic group. This is a problem of:
    A) Latency  B) **Fairness/bias**  C) Throughput  D) Cost

23. Which service logs **who invoked which model** (audit trail)?
    A) CloudWatch  B) **CloudTrail**  C) Macie  D) Config

24. Keep traffic to Bedrock off the public internet:
    A) Public IP + SG  B) **VPC endpoints / PrivateLink**  C) CloudFront  D) IGW

25. On Amazon Bedrock, your prompts/data are:
    A) used to train the base models  B) **not used to train base FMs; your fine-tune stays private**  C) public  D) deleted after 1 day

---

## Answer key
1-C, 2-B, 3-B, 4-C, 5-B, 6-B, 7-B, 8-B, 9-B, 10-C, 11-B, 12-B, 13-B, 14-B, 15-B,
16-B, 17-B, 18-B, 19-B, 20-B, 21-A, 22-B, 23-B, 24-B, 25-B

### Why (the ones people miss)
- **3:** "no training / no ML staff" → an **AI service** (Comprehend), never SageMaker.
- **6 vs 19/20:** Bedrock = *use* FMs serverlessly; SageMaker (Clarify/Model Monitor) = *build/govern* your own model.
- **11 vs 17:** **RAG adds knowledge** (and is easy to refresh); **fine-tuning changes behavior**. Different jobs.
- **13/15/18:** Knowledge Bases = RAG, Agents = tool use/actions, Guardrails = safety. Don't swap them.
- **14:** ROUGE = summarization, BLEU = translation, BERTScore = semantic similarity.
- **19 vs 20:** Clarify = bias + explainability (at build); Model Monitor = drift (after deploy).
- **25:** key Bedrock privacy fact — your data isn't used to train the base model; your fine-tuned copy is private to your account.

**Scoring:** 18+/25 → ready, do the readiness checklist. <18 → re-read the weak domain and retake.
