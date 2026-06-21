# 🤖 AI / ML (Concept + AWS↔Azure)

> **Concept note:** Two layers. **Classic ML** = train your own model on your data. **Generative AI** = use large foundation models (often via API) and ground them with your data (RAG) or adapt them (fine-tune).

## ML lifecycle
```
Data prep → Feature engineering → Train → Tune → Evaluate → Deploy → Monitor → (retrain)
```

## GenAI building blocks
| Term | Meaning |
|---|---|
| Foundation model (FM) | Big pre-trained model (text/image) |
| Embedding | Numeric vector representing meaning |
| Vector DB | Stores embeddings for similarity search |
| RAG | Retrieve your data + feed it to the FM (reduces hallucination) |
| Fine-tuning | Further train an FM on your data |
| Prompt engineering | Crafting inputs to steer outputs |
| Guardrails | Block unsafe/unwanted content |

## AWS ↔ Azure service mapping
| Capability | AWS | Azure |
|---|---|---|
| ML platform | SageMaker | Azure Machine Learning |
| AutoML | SageMaker Autopilot | Automated ML |
| Foundation models / GenAI | Bedrock | Azure OpenAI Service |
| Model hub | SageMaker JumpStart | Azure AI Foundry (model catalog) |
| Vector / RAG search | OpenSearch / Kendra | Azure AI Search |
| Vision | Rekognition | Azure AI Vision |
| Language/NLP | Comprehend | Azure AI Language |
| Speech | Transcribe / Polly | Azure AI Speech |
| Doc extraction | Textract | Document Intelligence |
| Content safety | Bedrock Guardrails | Azure AI Content Safety |

## Deployment patterns
| Need | Pattern |
|---|---|
| Low-latency single predictions | Real-time endpoint |
| Large offline scoring | Batch transform |
| Spiky/cheap | Serverless inference |

## Hands-on lab
- Classic: train a small model + deploy an endpoint (SageMaker / Azure ML), invoke, then **delete the endpoint**.
- GenAI: build a tiny RAG flow (embeddings → vector store → FM).
- **Cleanup:** delete endpoints, vector indexes, resource groups (these bill hourly!).

## ⚠️ Common exam traps
- For imbalanced data, **accuracy misleads** — use precision/recall/F1/AUC.
- Try **RAG + better prompts before fine-tuning** (cheaper, faster).
- Endpoints bill per hour even when idle — delete after labs.
- Detecting **drift** requires monitoring (Model Monitor / Azure ML monitoring).

## 🃏 Flashcards
| Q | A |
|---|---|
| AWS managed FMs? | Bedrock |
| Azure managed FMs? | Azure OpenAI |
| Reduce hallucination cheaply? | RAG |
| Metric for imbalanced classes? | Precision/Recall/F1 |
| AWS ML platform? | SageMaker |
| Azure ML platform? | Azure Machine Learning |
| Store/search embeddings (Azure)? | Azure AI Search |

🔗 Related: [[data-engineering]] · [[architecture-patterns]]
