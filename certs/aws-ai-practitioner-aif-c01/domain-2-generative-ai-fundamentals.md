---
tags: [cert/aif-c01, aws/ai-ml, genai]
cert: AIF-C01
domain: 2
aliases: [AIF-C01 Domain 2, Generative AI Fundamentals]
---
> [[domain-1-ai-ml-fundamentals|◀ Domain 1]] · [[AIF-C01|AIF-C01 Home]] · [[domain-3-applications-of-foundation-models|Domain 3 · FM Apps ▶]]

# Domain 2 — Fundamentals of Generative AI (24%)

What foundation models are and the core GenAI vocabulary. Heavily tested — learn the terms cold.

## 2.1 Foundation models (FMs) & LLMs
- **Foundation model (FM)** — a very large model **pre-trained on massive, broad data**, then reused for many tasks. You *adapt* it instead of training from scratch.
- **Large Language Model (LLM)** — an FM specialized for text/language (e.g. Claude, Titan, Llama).
- **Multimodal** — handles more than one type (text + images), e.g. image generation or image+text input.
- **Why it matters:** instead of collecting data + training a model per task, you take one FM and steer it with prompts/context. Huge time saver — that's the GenAI shift.

## 2.2 The core mechanics (these terms appear constantly)
- **Token** — a chunk of text (~¾ of a word). Models read/write in tokens; **you're billed per token** (input + output).
- **Embedding** — text turned into a **vector of numbers** that captures meaning. Similar meaning → vectors close together. Powers **semantic search** and **RAG**.
- **Vector / vector database** — stores embeddings so you can find "most similar" items fast (e.g. OpenSearch, Aurora pgvector, Pinecone).
- **Context window** — how many tokens the model can consider at once (prompt + history + retrieved docs). Bigger = more context but more cost/latency.
- **Prompt** — the input instruction. **Inference** — the model generating a response.

## 2.3 Inference settings (knobs you'll be asked about)
| Setting | Effect |
|---|---|
| **Temperature** | randomness/creativity. **Low (0–0.2)** = focused, deterministic; **high** = creative, varied. |
| **Top-p / Top-k** | limit the token choices sampled from (nucleus sampling). |
| **Max tokens** | cap on response length (cost control). |

**Trap:** Want **consistent, factual** output (e.g. extracting fields)? → **low temperature**. Want brainstorming/variety? → higher.

## 2.4 How you adapt an FM (cheapest → most expensive — exam loves this ladder)
1. **Prompt engineering** — write better instructions/examples. **Free, instant. Try first.**
2. **RAG (Retrieval-Augmented Generation)** — fetch relevant docs and put them in the prompt so the model answers from *your* data. **No retraining**; great for fresh/private knowledge; reduces hallucination.
3. **Fine-tuning** — further-train the FM on your labeled examples to change its behavior/style. Costs money + data + time.
4. **Continued pre-training / train from scratch** — rare, very expensive.

> Rule of thumb the exam rewards: **prompt → RAG → fine-tune → pre-train**, in that order of escalation.

## 2.5 The AWS GenAI stack (know what each is)
| Service | What it is | Use when |
|---|---|---|
| **Amazon Bedrock** | **serverless API to many FMs** (Anthropic Claude, Amazon **Titan/Nova**, Meta Llama, Cohere, AI21, Stability). Plus Knowledge Bases (RAG), Agents, Guardrails. | You want to *use/adapt* FMs without managing infrastructure. **The default GenAI answer.** |
| **Amazon Q** | AWS's GenAI **assistant** (Q Developer for code, Q Business for your company data). | Ready-made assistant, minimal build. |
| **SageMaker JumpStart** | hub to deploy/fine-tune open FMs on **your own** SageMaker infra. | You need full control/customization. |
| **PartyRock** | free no-code Bedrock playground. | Learning / quick demos. |

**Trap:** **Bedrock = managed, serverless, multiple providers via one API.** SageMaker = you manage the model/infra. If the scenario says "no infrastructure to manage, pick from several leading models" → **Bedrock**.

## 2.6 Strengths & limits (commonly tested)
- **Good at:** drafting/summarizing text, Q&A, code, translation, chatbots, image generation, brainstorming.
- **Limits:** **hallucination** (confident but wrong), **knowledge cutoff** (stale facts), **non-determinism**, **bias** from training data, **cost/latency** at scale, no true reasoning guarantees.
- **Mitigations:** RAG for freshness/grounding, **Guardrails** for safety, human review, low temperature for facts.

## 2.7 GenAI use cases to recognize
Text summarization · chatbots/virtual assistants · code generation · semantic search · content creation/marketing copy · document Q&A over private data (RAG) · image generation (Stability/Titan Image) · personalization.

## Hands-on (`$env:AWS_PROFILE="learn"` — meet real foundation models)
```powershell
$env:AWS_PROFILE = "learn"
# List the FMs available to you (Titan, Claude, Llama, ...):
aws bedrock list-foundation-models --query "modelSummaries[].modelId" --output table
# Invoke one (request model access once in the Bedrock console first).
# The body carries the prompt + inference knobs — note "temperature":
'{"anthropic_version":"bedrock-2023-05-31","max_tokens":120,"temperature":0.2,"messages":[{"role":"user","content":"Explain embeddings in one sentence."}]}' | Out-File -Encoding ascii body.json
aws bedrock-runtime invoke-model --model-id anthropic.claude-3-haiku-20240307-v1:0 `
  --body file://body.json --cli-binary-format raw-in-base64-out out.json
Get-Content out.json
```
Re-run with `"temperature":0.9` and watch the answer get more varied. **Cleanup:** `Remove-Item body.json, out.json` — per-token billing only, nothing stays running.

## Flashcards
- FM = big pre-trained, reusable model; LLM = FM for text.
- Token = billing unit; Embedding = meaning-as-vector; RAG = ground answers in your docs.
- Low temperature = factual/consistent; high = creative.
- Adapt ladder: **prompt → RAG → fine-tune → pre-train**.
- Bedrock = serverless multi-FM API (default GenAI answer); SageMaker = build your own.

## Practice questions
**Q1.** You want an FM to answer using your company's private PDFs, kept up to date, **without retraining**. Best approach?
- A) Fine-tuning  B) **RAG (Retrieval-Augmented Generation)** ✅  C) Train from scratch  D) Raise temperature

**Q2.** Which AWS service gives serverless access to multiple foundation models through one API?
- A) SageMaker  B) Comprehend  C) **Amazon Bedrock** ✅  D) EC2

**Q3.** Extraction must be consistent and factual every run. Which setting?
- A) High temperature  B) **Low temperature** ✅  C) More top-k  D) Larger max tokens

**Q4.** What is an embedding?
- A) A billing unit of text  B) **A numeric vector representing meaning** ✅  C) A type of GPU  D) A prompt template

**Q5.** Cheapest first step to improve an FM's answers before any retraining?
- A) Fine-tuning  B) Continued pre-training  C) **Prompt engineering** ✅  D) Buy a bigger model
