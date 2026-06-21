---
tags: [cert/aif-c01, aws/ai-ml, moc]
cert: AIF-C01
level: foundational
aliases: [AIF-C01, AWS AI Practitioner]
---
> **Track notes:** [[domain-1-ai-ml-fundamentals|1 · AI/ML Basics]] · [[domain-2-generative-ai-fundamentals|2 · GenAI]] · [[domain-3-applications-of-foundation-models|3 · FM Apps]] · [[domain-4-responsible-ai|4 · Responsible AI]] · [[domain-5-security-compliance-governance|5 · Security & Governance]] · [[AIF-C01-practice|🧪 Practice]] · [[AIF-C01-readiness|✅ Readiness]]
> **Up:** [[CERTS-MOC|All certs]] · [[CERT_ROADMAP|Roadmap]]

# AWS Certified AI Practitioner (AIF-C01) — study track

Your **AI/GenAI foundation** cert — the on-ramp to the Data Scientist / ML lane. It's
*knowledge-based* (recognize concepts + which AWS service fits), no coding required to pass.
Pairs naturally with CLF-C02; many people sit them close together. Directly relevant to your
forecasting work and to anything GenAI you build on top of it.

> ✅ **Verified 2026-06-21** against [aws.amazon.com](https://aws.amazon.com/certification/certified-ai-practitioner/) + the official **AIF-C01 Exam Guide** (docs.aws.amazon.com): 65 Q · 90 min · pass **700/1000** · **$100** · domains **20/24/28/14/14**. Still re-skim the current Exam Guide PDF before booking in case AWS revises it.

## Exam facts (verified 2026-06-21)
| | |
|---|---|
| Code | **AIF-C01** |
| Level | Foundational |
| Questions | **65** (multiple-choice + multiple-response; ~15 unscored) |
| Time | **90 minutes** |
| Pass | **700 / 1000** (scaled) |
| Cost | **$100 USD** |
| Prereqs | none (AWS suggests up to ~6 months of AI/ML exposure) |
| Validity | 3 years |
| Delivery | Pearson VUE — test center **or** online proctored |

## The 5 domains (memorize these weightings)
| # | Domain | Weight | File |
|---|---|---|---|
| 1 | Fundamentals of AI and ML | **20%** | `domain-1-ai-ml-fundamentals.md` |
| 2 | Fundamentals of Generative AI | **24%** | `domain-2-generative-ai-fundamentals.md` |
| 3 | Applications of Foundation Models | **28%** | `domain-3-applications-of-foundation-models.md` |
| 4 | Guidelines for Responsible AI | **14%** | `domain-4-responsible-ai.md` |
| 5 | Security, Compliance & Governance for AI | **14%** | `domain-5-security-compliance-governance.md` |

Domains 2 + 3 are **52%** — generative AI and foundation models are the heart of this exam.

## 2-week study plan (~1 hr/day)
| Days | Do |
|---|---|
| 1–2 | Domain 1 (AI/ML basics) + its practice Qs |
| 3–5 | Domain 2 (GenAI: FMs, tokens, embeddings, prompts) |
| 6–8 | Domain 3 (Bedrock, RAG, prompt engineering, evaluation) — the big one |
| 9–10 | Domain 4 (responsible AI: bias, fairness, transparency) |
| 11 | Domain 5 (security/governance of AI) |
| 12–13 | `practice-questions.md` full mock — review every miss |
| 14 | `exam-readiness-checklist.md` → if all ticked, **book it** |

## How this maps to YOUR work
- Your `db_polars_app.py` forecasting = **supervised ML / time-series regression** (Domain 1 vocabulary).
- A "explain this forecast in plain English" or "chat with your data" feature = **GenAI on Bedrock** (Domains 2–3).
- "Don't leak Healthium data into a public model" = **Domain 5** (security/governance) — very real for you.

## Hands-on you *can* do free (optional, cements it)
- **PartyRock** (partyrock.aws) — build a tiny GenAI app in the browser, no account/cost. Best 20-min intro to FMs + prompts.
- **Amazon Bedrock** in your `learn` account — open the console, request access to a model (e.g. Claude/Titan), try the text playground. Tiny per-token cost; **delete nothing to clean up (no standing resource), but don't leave a provisioned-throughput commitment running.**

## Exam-day wrong-answer tells
- "Use a pre-trained model via an API, no training" → **Bedrock** (or an AI service like Comprehend), *not* SageMaker.
- "Build/train/tune your own model" → **SageMaker**.
- "Reduce hallucination / ground answers in my documents" → **RAG** (Knowledge Bases + embeddings + vector store).
- "Adapt an FM to my domain with examples" → **fine-tuning**; "just better instructions/context" → **prompt engineering / RAG** (cheaper, try first).
- "Detect bias / explain a model" → **SageMaker Clarify**; "monitor a deployed model" → **Model Monitor**.
