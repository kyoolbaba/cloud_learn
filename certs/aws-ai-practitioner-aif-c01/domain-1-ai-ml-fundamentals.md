---
tags: [cert/aif-c01, aws/ai-ml]
cert: AIF-C01
domain: 1
aliases: [AIF-C01 Domain 1, AI and ML Fundamentals]
---
> [[AIF-C01|⬅ AIF-C01 Home]] · Next: [[domain-2-generative-ai-fundamentals|Domain 2 · Generative AI ▶]]

# Domain 1 — Fundamentals of AI and ML (20%)

The vocabulary layer. Mostly "which term/technique fits this scenario" and "which AWS service."

## 1.1 The nested terms (draw this — it's tested directly)
**AI ⊃ ML ⊃ Deep Learning ⊃ Generative AI**
- **AI** — broad: machines doing tasks that seem to need human intelligence.
- **ML** — a subset of AI: systems that **learn patterns from data** instead of being hand-coded.
- **Deep Learning (DL)** — ML using **neural networks** with many layers (great for images, audio, language).
- **Generative AI** — DL models that **create new content** (text, images, code) — covered in Domain 2.

> Real-world: your forecasting isn't hand-coded rules ("if December, add 10%"). It **learns** seasonality from history → that's **ML**.

## 1.2 The three learning types (high-yield)
| Type | Data | It learns to… | Examples |
|---|---|---|---|
| **Supervised** | **labeled** (input → known answer) | predict a label/number | **Classification** (spam/not), **Regression** (a number — *your forecasting*) |
| **Unsupervised** | **unlabeled** | find structure | **Clustering** (customer segments), anomaly detection, dimensionality reduction |
| **Reinforcement (RL)** | reward signal | act to maximize reward | game-playing, robotics, RLHF for LLMs |

**Trap:** Classification = predict a **category**; Regression = predict a **continuous number**. Forecasting demand = regression.

## 1.3 ML problem → technique cheat sheet
- Predict a number → **regression**. Predict a category → **classification**.
- Group similar items, no labels → **clustering** (unsupervised).
- Recommend items → **recommendation** (Amazon **Personalize**).
- Predict future values over time → **time-series forecasting** (Amazon **Forecast**; or your own).

## 1.4 The ML lifecycle (order matters on the exam)
1. **Frame the problem** (is ML even the right tool?) →
2. **Collect & prepare data** (the longest part — cleaning, labeling, feature engineering) →
3. **Train** a model →
4. **Evaluate** (metrics) →
5. **Deploy** (inference) →
6. **Monitor** & retrain (data drifts over time).

- **Training** = learning from data (expensive, batch). **Inference** = using the trained model to predict (what runs in production).
- **Features** = the input columns the model learns from. **Feature engineering** = crafting good inputs (lags, rolling means in your case).

## 1.5 The AWS AI/ML stack (3 layers — know which layer a service is on)
| Layer | What it is | Services |
|---|---|---|
| **AI services** (top) | pre-trained, call via API, no ML skill | **Rekognition** (vision), **Comprehend** (NLP/sentiment), **Transcribe** (speech→text), **Polly** (text→speech), **Translate**, **Textract** (docs→data), **Lex** (chatbots), **Personalize** (recommendations), **Forecast** (time-series), **Fraud Detector**, **Kendra** (search) |
| **ML platform** (middle) | build/train/deploy your own | **Amazon SageMaker** (+ Studio, JumpStart, Autopilot) |
| **Infrastructure** (bottom) | chips & frameworks | EC2 GPU/**Trainium**/**Inferentia**, Deep Learning AMIs |

**Trap:** "Add sentiment analysis without building a model" → **Comprehend** (AI service), not SageMaker. "Need full control / custom algorithm" → **SageMaker**.

## 1.6 Data basics the exam expects
- **Structured** (tables/SQL) vs **semi-structured** (JSON) vs **unstructured** (text, images, audio).
- **Labeled** vs **unlabeled** data → decides supervised vs unsupervised.
- More good, representative data usually beats a fancier model. **Garbage in → garbage out.**

## 1.7 When NOT to use ML (they ask this)
If a simple rule or deterministic logic solves it, or you have no data / can't tolerate any error / need full explainability by law — **ML may be the wrong tool**. ML fits when patterns are complex and you have representative historical data.

## AWS ↔ Azure quick map
| AWS | Azure |
|---|---|
| SageMaker | Azure Machine Learning |
| Comprehend / Rekognition / Transcribe | Azure AI Language / Vision / Speech |
| Forecast | (no direct; AzureML / SynapseML) |
| Bedrock | Azure OpenAI / Azure AI Foundry |

## Hands-on (`$env:AWS_PROFILE="learn"` — use ML with zero training)
Amazon Comprehend is a pre-trained **AI service** — one CLI call does NLP, no model to build (this *is* §1.5):
```powershell
$env:AWS_PROFILE = "learn"
# Sentiment = classification from a pre-trained model (no training step):
aws comprehend detect-sentiment --language-code en `
  --text "The delivery was late but the support team was fantastic."
# Entities + key phrases (what powers search and redaction):
aws comprehend detect-entities --language-code en --text "Milan shipped 200 units to Bengaluru on Monday."
```
**Cleanup:** none — Comprehend is serverless/per-request; nothing stays running.

## Flashcards
- Supervised = labeled; Unsupervised = unlabeled; RL = rewards.
- Classification = category; Regression = number; Clustering = groups.
- Training = learn; Inference = predict in prod.
- AI service = pre-trained API (Comprehend/Rekognition…); SageMaker = build your own.

## Practice questions
**Q1.** Predicting next month's demand (a continuous number) is which ML type/task?
- A) Unsupervised clustering  B) **Supervised regression** ✅  C) Reinforcement learning  D) Classification

**Q2.** A team wants sentiment from customer reviews with no ML expertise and no model training. Best choice?
- A) SageMaker training job  B) **Amazon Comprehend** ✅  C) EC2 + PyTorch  D) Amazon Forecast

**Q3.** Grouping customers into segments without any labels is:
- A) Classification  B) Regression  C) **Clustering (unsupervised)** ✅  D) RL

**Q4.** In the ML lifecycle, which phase typically takes the most effort?
- A) Model training  B) **Data collection & preparation** ✅  C) Deployment  D) Framing the problem

**Q5.** "AI, ML, deep learning, generative AI" — which contains all the others?
- A) ML  B) Deep learning  C) **AI** ✅  D) Generative AI
