---
tags: [cert/aif-c01, aws/ai-ml, responsible-ai]
cert: AIF-C01
domain: 4
aliases: [AIF-C01 Domain 4, Responsible AI]
---
> [[domain-3-applications-of-foundation-models|◀ Domain 3]] · [[AIF-C01|AIF-C01 Home]] · [[domain-5-security-compliance-governance|Domain 5 · Security ▶]]

# Domain 4 — Guidelines for Responsible AI (14%)

Building AI that's fair, safe, transparent, and accountable. Conceptual — learn the dimensions
and which AWS tool supports each.

## 4.1 The dimensions of responsible AI (recognize each)
- **Fairness** — no unjust bias against groups.
- **Bias** — systematic skew from unrepresentative data or labels.
- **Inclusivity / diversity** — works across users and is accessible.
- **Robustness** — holds up to noisy/adversarial/edge-case inputs.
- **Safety** — won't produce harmful/toxic/dangerous output.
- **Transparency** — people know they're dealing with AI and how it's used.
- **Explainability / interpretability** — you can explain *why* a model decided what it did.
- **Veracity** — truthfulness; managing **hallucination** and misinformation.
- **Accountability / governance** — clear ownership and oversight.
- **Privacy** — protect personal data used or produced.

## 4.2 Bias & fairness (commonly tested)
- Bias creeps in via **training data** (under-represented groups), labels, or features that proxy a protected attribute.
- Harm types: allocation harm (denied a loan), quality-of-service harm (works worse for some), stereotyping.
- **Fix:** representative/balanced data, bias metrics, human review, ongoing monitoring (bias can appear *after* deployment as data drifts).

## 4.3 AWS tools for responsible AI (match tool → job)
| Tool | What it does |
|---|---|
| **SageMaker Clarify** | detects **bias** (pre-training in data + post-training in predictions) and provides **explainability** (feature importance, SHAP). |
| **SageMaker Model Monitor** | watches a deployed model for **data/quality drift** over time. |
| **Amazon Bedrock Guardrails** | block harmful content, filter topics, redact **PII**, reduce hallucination via grounding checks. |
| **SageMaker Model Cards** | document a model's intended use, data, metrics, limitations (governance artifact). |
| **AI Service Cards** | AWS-published transparency docs on its AI services' intended use + limits. |
| **Augmented AI (A2I)** | route low-confidence predictions to **human review**. |

**Trap:** "detect bias / explain predictions" → **Clarify**. "monitor deployed model for drift" → **Model Monitor**. "block toxic/PII output from an FM" → **Guardrails**.

## 4.4 Transparency & explainability trade-offs
- **Interpretable models** (linear/trees) are easy to explain but may be less accurate; **deep/FM models** are powerful but **opaque** ("black box").
- Where decisions affect people (credit, hiring, health), favor **explainable** approaches or add explainability tooling — and keep a **human in the loop**.
- **Model Cards / datasheets** document intended use, training data, performance, and limitations.

## 4.5 Human-centered & governance practices
- **Human-in-the-loop** review for high-stakes or low-confidence outputs (A2I).
- Define **intended use** and out-of-scope use up front.
- Continuous **monitoring** post-deployment (fairness/quality can degrade).
- Clear **accountability** and escalation paths.

## How this is real for you
A forecast that's systematically wrong for a region/product line is a **fairness/quality** problem; being able to say *why* a number came out (feature importance) is **explainability** — exactly what **Clarify** gives a SageMaker model.

## Hands-on (`$env:AWS_PROFILE="learn"` — responsible AI you can run)
```powershell
$env:AWS_PROFILE = "learn"
# Find PII so you can redact it BEFORE sending data to a model (privacy + safety):
aws comprehend detect-pii-entities --language-code en `
  --text "Patient Milan, DOB 1990-05-01, card 4111-1111-1111-1111, Bengaluru."
# Returns the PII spans + types — the basis for masking/anonymization.
```
**Cleanup:** none (serverless). For toxicity/safety, create a **Bedrock Guardrail** in the console, attach it to a Playground chat, then delete the guardrail to keep things tidy.

## Flashcards
- Dimensions: fairness, bias, robustness, safety, transparency, explainability, veracity, privacy.
- Clarify = bias + explainability; Model Monitor = drift; Guardrails = safe FM output; A2I = human review.
- Model Cards = document a model; AI Service Cards = AWS service transparency docs.
- Bias source = unrepresentative data; fix = better data + monitoring + humans.

## Practice questions
**Q1.** Which detects bias in training data and explains model predictions?
- A) Model Monitor  B) **SageMaker Clarify** ✅  C) Guardrails  D) Macie

**Q2.** You must stop an FM from returning toxic content or leaking PII. Use:
- A) Clarify  B) **Bedrock Guardrails** ✅  C) Model Cards  D) Kendra

**Q3.** Routing low-confidence predictions to people for review uses:
- A) **Amazon Augmented AI (A2I)** ✅  B) CloudTrail  C) Personalize  D) Comprehend

**Q4.** A model works well overall but much worse for one demographic. This is a problem of:
- A) Latency  B) **Fairness/bias** ✅  C) Throughput  D) Cost

**Q5.** A document describing a model's intended use, data, and limitations is a:
- A) Guardrail  B) Knowledge Base  C) **Model Card** ✅  D) Vector store
