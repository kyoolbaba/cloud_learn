# Microsoft Certified: Azure Developer Associate

> 🍼 **Beginner explanation:** Teaches building apps on Azure — App Service, Functions, containers, storage, Cosmos DB, authentication, and monitoring.
>
> 🌍 **Real-world example:** Build a serverless API with Azure Functions that stores data in Cosmos DB, authenticates users with Entra ID, and is monitored by Application Insights.

| Field | Value |
|---|---|
| **1. Certification name** | Microsoft Certified: Azure Developer Associate |
| **2. Exam code** | AZ-204 |
| **3. Level** | Associate |
| **4. Best for role** | Developers building Azure apps |
| **5. Prerequisites** | 1–2 years dev + Azure basics; AZ-900 helpful |

---

## 6. Core topics
- Compute (App Service, Functions, Container Apps/ACI)
- Storage (Blob) + Cosmos DB development
- Authentication/authorization (Entra ID, MSAL, managed identities)
- Secure solutions (Key Vault, App Configuration)
- Integration (Service Bus, Event Grid, Event Hubs)
- Monitoring & troubleshooting (Application Insights), API Management

## 7. Azure services to learn
| Category | Services |
|---|---|
| Compute | App Service, Azure Functions, Container Apps, ACI |
| Data | Blob Storage, Cosmos DB |
| Security | Microsoft Entra ID, Managed Identity, Key Vault, App Configuration |
| Integration | Service Bus, Event Grid, Event Hubs, API Management |
| Observability | Application Insights, Azure Monitor |

## 8. Hands-on labs
1. **Azure Function** (HTTP trigger). *(Cleanup: delete RG.)*
2. **App Service** web app deploy. *(Cleanup: delete RG.)*
3. **Storage queue** producer/consumer. *(Cleanup: delete RG.)*
4. **Cosmos DB app** (CRUD). *(Cleanup: delete RG.)*
5. **Application Insights** on the function. *(Cleanup: delete RG.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–2 | App Service; Lab 2 |
| 3–4 | Functions; Lab 1 |
| 5 | Containers (Container Apps/ACI) |
| 6–7 | Cosmos DB; Lab 4 |
| 8 | Blob + queues; Lab 3 |
| 9 | Auth + Key Vault + managed identity |
| 10 | Integration (Service Bus/Event Grid) |
| 11 | App Insights + APIM; Lab 5 |
| 12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 80%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | App Service + Functions (Labs 1–2) |
| 2 | Storage + Cosmos DB (Labs 3–4) |
| 3 | Auth + integration + monitoring (Lab 5) |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1 | App Service (Lab 2) |
| 2 | Functions (Lab 1) |
| 3 | Containers |
| 4 | Cosmos DB (Lab 4) |
| 5 | Blob + queues (Lab 3) |
| 6 | Auth + Key Vault + managed identity |
| 7 | Integration + monitoring (Lab 5) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **80%+**. Code/SDK-aware questions + service selection.
- Know managed identity vs service principal, Cosmos consistency levels.
- 4 timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] Functions triggers/bindings + hosting plans
- [ ] Cosmos DB consistency levels + partition keys
- [ ] Managed identity vs app registration
- [ ] Key Vault vs App Configuration
- [ ] Service Bus vs Event Grid vs Event Hubs
- [ ] Flashcards reviewed twice

## 14. Notes template
```
### Topic: <name>
- Concept:
- Real-world use:
- Azure service(s):
- AWS equivalent:
- Common exam trap:
- My example:
```

## 15. Mistake log template
| Date | Topic | What I got wrong | Correct concept | Revisit date |
|---|---|---|---|---|

## 16. Flashcards (starter set)
| Q | A |
|---|---|
| Serverless functions in Azure? | Azure Functions |
| AWS equivalent of Functions? | Lambda |
| Event streaming (big scale)? | Event Hubs |
| Reactive event routing? | Event Grid |
| Reliable message queue? | Service Bus |
| App secrets/keys store? | Key Vault |
| Identity for code without secrets? | Managed Identity |

→ More in `05-flashcards/azure-flashcards.md`.

## 17. Official docs / resources
- [ ] AZ-204 exam page: _add link_
- [ ] Microsoft Learn AZ-204 path: _add link_
- [ ] Functions + Cosmos DB docs: _add link_
- [ ] Practice assessment: _add link_
