# 🛠️ Project: Azure AI Project (RAG with Azure OpenAI + AI Search)

> **Goal:** Build a document Q&A assistant (RAG) on Azure. Reinforces AI-900 + (optionally) AI-102. Mirrors the AWS GenAI/Bedrock idea.
>
> 🌍 **Real-world story:** Employees ask questions; the assistant answers from your company PDFs, grounded and safe.

## What you'll build
```
Documents → chunk + embed (Azure OpenAI embeddings) → Azure AI Search (vector index)
                                                              ↓
        User question → retrieve top chunks → Azure OpenAI (chat) → grounded answer
                                                              ↓
                                          Content Safety (guardrails)
```

## Skills practiced
- Embeddings + vector search (RAG)
- Azure OpenAI deployments + prompts
- Azure AI Search index design (vector + semantic)
- Responsible AI / Content Safety
- Managed identity + Key Vault for secrets

## Steps
1. Create **Azure OpenAI** resource; deploy a chat model + an embedding model.
2. Create an **Azure AI Search** service; build a vector index.
3. Ingest sample docs: chunk → embed → upload to the index.
4. Query: retrieve top-k chunks → pass to the chat model with a grounding prompt.
5. Add **Content Safety** filtering.
6. Store keys in **Key Vault**; use **managed identity**.

## ✅ Success criteria
- [ ] Assistant answers from your docs (not made up)
- [ ] Citations/grounding visible
- [ ] Unsafe prompt is blocked
- [ ] No secrets hardcoded

## 💸 Cleanup (do it!)
- [ ] **Delete the resource group** (OpenAI deployment, AI Search, Key Vault)
- [ ] Confirm AI Search service deleted (provisioned capacity bills)
- [ ] Check **Cost Management**

## 📝 Reflection / write-up
- AWS↔Azure: Azure OpenAI ≈ Bedrock; AI Search ≈ Kendra/OpenSearch → see [[aws-ml-deployment-project]]
- When would you fine-tune instead of RAG?

🔗 Related: [[../03-shared-cloud-concepts/ai-ml]] · [[../02-azure/fundamentals/azure-ai-fundamentals-AI-900]] · [[../01-aws/professional/aws-generative-ai-developer-professional-AIP-C01]]
