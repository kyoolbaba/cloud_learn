---
tags: [cert/aif-c01, aws/ai-ml, genai]
cert: AIF-C01
domain: 3
aliases: [AIF-C01 Domain 3, Applications of Foundation Models]
---
> [[domain-2-generative-ai-fundamentals|◀ Domain 2]] · [[AIF-C01|AIF-C01 Home]] · [[domain-4-responsible-ai|Domain 4 · Responsible AI ▶]]

# Domain 3 — Applications of Foundation Models (28%)

The biggest domain. *Using* FMs well: choosing one, prompting it, grounding it with RAG,
adapting it, and evaluating it. Lots of "which technique fits this scenario."

## 3.1 Choosing a foundation model (selection criteria)
Weigh: **cost** (per-token price), **latency/speed**, **modality** (text vs image vs multimodal),
**context window** size, **performance/quality** on your task, **customizability** (can you fine-tune it?),
**language support**, and **licensing**. No single "best" — match model to the job (small/cheap for
classification; large for hard reasoning).

## 3.2 Prompt engineering (high-yield — know the techniques by name)
- **Zero-shot** — just ask, no examples.
- **Few-shot** — include a few input→output **examples** in the prompt to show the pattern.
- **Chain-of-thought (CoT)** — ask it to "think step by step"; improves reasoning/math.
- **Prompt template** — reusable structure with slots you fill at runtime.
- **Good prompt parts:** clear **instruction**, **context**, **input data**, **output format**, optional examples + role ("You are a…").
- **Negative prompting** — tell it what *not* to do / exclude.

**Risks:** **prompt injection** (malicious input hijacks instructions) and **jailbreaking** (bypassing safety). Mitigate with **Guardrails**, input validation, and least-privilege.

## 3.3 RAG in depth (the exam's favorite pattern)
**Problem:** FMs hallucinate and don't know your private/recent data.
**RAG fix:** at query time → **embed** the question → **search a vector store** for the most relevant chunks of *your* documents → stuff them into the prompt as context → the FM answers grounded in those chunks.

**On AWS:** **Bedrock Knowledge Bases** wires this up for you — point it at S3 docs, it chunks + embeds (via an embeddings model like Titan Embeddings) + stores vectors (OpenSearch Serverless, Aurora pgvector, etc.) + retrieves at query time.

- **Use RAG when:** answers must reflect private, large, or frequently-changing knowledge; you want **citations**; you want to **cut hallucination** without retraining.
- **RAG vs fine-tuning:** RAG adds **knowledge/facts** (and is easy to update); fine-tuning changes **behavior/style/format**. They're complementary.

## 3.4 Adapting an FM (when prompting isn't enough)
- **Fine-tuning** — train on your **labeled** examples to specialize behavior/tone/format.
- **Domain adaptation / continued pre-training** — feed lots of unlabeled domain text so it "speaks your domain."
- **Instruction tuning** — teach it to follow a task format.
- Cost/effort: prompt < RAG < fine-tune < pre-train. **Escalate only when the cheaper rung fails.**

## 3.5 Agents (orchestration)
**Bedrock Agents** let an FM **call tools/APIs and take multi-step actions** (e.g. look up an order, then issue a refund). The FM plans; the agent executes steps against your APIs/Lambda + Knowledge Bases.

## 3.6 Evaluating FM outputs (know the metric names)
| Metric | For | Idea |
|---|---|---|
| **ROUGE** | summarization | overlap of generated vs reference summary |
| **BLEU** | translation | n-gram overlap with reference |
| **BERTScore** | semantic similarity | meaning match, not exact words |
| **Perplexity** | language modeling | how "surprised" the model is (lower better) |
| **Human evaluation** | quality/helpfulness/safety | people rate outputs — often the gold standard |

**Bedrock Model Evaluation** offers automatic + human-in-the-loop evaluation jobs. Define success criteria up front (accuracy, relevance, toxicity, latency, cost).

## 3.7 Bedrock features to recognize
- **Knowledge Bases** → RAG. **Agents** → tool use/actions. **Guardrails** → block harmful/PII content + topic filters. **Model Evaluation** → compare models. **Provisioned Throughput** → reserved capacity for steady high volume (vs on-demand per-token).

## Hands-on (free / near-free, cement it)
- Build a tiny app in **PartyRock** (free): give it a system prompt, try zero-shot vs few-shot, watch temperature change outputs.
- In your `learn` account, open **Bedrock → Playground**, request model access, paste a few-shot prompt. **Cleanup:** nothing persistent is created in the playground; just don't buy **Provisioned Throughput** (that's a standing commitment).

Or drive a **few-shot** prompt from the CLI and watch the pattern hold:
```powershell
$env:AWS_PROFILE = "learn"
'{"anthropic_version":"bedrock-2023-05-31","max_tokens":10,"temperature":0,"messages":[{"role":"user","content":"Classify sentiment as POS or NEG. Examples: great=POS; awful=NEG. Now: the wait was long but worth it ="}]}' | Out-File -Encoding ascii fs.json
aws bedrock-runtime invoke-model --model-id anthropic.claude-3-haiku-20240307-v1:0 --body file://fs.json --cli-binary-format raw-in-base64-out fsout.json
Get-Content fsout.json
```
**Cleanup:** `Remove-Item fs.json, fsout.json` (per-token billing only).

## Flashcards
- Zero-shot / few-shot / chain-of-thought — name them on sight.
- RAG = embed → retrieve from vector store → ground the prompt (Bedrock Knowledge Bases).
- RAG adds knowledge; fine-tuning changes behavior.
- ROUGE=summary, BLEU=translation, BERTScore=semantic, human eval=quality.
- Guardrails = safety filter; Agents = tool use; Knowledge Bases = RAG.

## Practice questions
**Q1.** Giving the model 3 example input→output pairs in the prompt is:
- A) Zero-shot  B) **Few-shot** ✅  C) Fine-tuning  D) RAG

**Q2.** A support bot must answer from your latest internal docs and cite them, updated daily, no retraining. Best?
- A) Fine-tune nightly  B) **RAG via Bedrock Knowledge Bases** ✅  C) Raise temperature  D) Bigger context window only

**Q3.** Which metric best evaluates a **summarization** model?
- A) BLEU  B) **ROUGE** ✅  C) RMSE  D) Accuracy

**Q4.** You need the FM to look up an order via your API and then act on it. Use:
- A) Knowledge Bases  B) **Bedrock Agents** ✅  C) Guardrails  D) Embeddings

**Q5.** Malicious user input that overrides your system instructions is:
- A) Hallucination  B) Data drift  C) **Prompt injection** ✅  D) Overfitting
