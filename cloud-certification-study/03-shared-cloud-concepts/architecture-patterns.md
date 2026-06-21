# 🏛️ Architecture Patterns (Concept + AWS↔Azure)

> **Concept note:** Reusable designs that make systems reliable, scalable, secure, and cost-effective. Both clouds have a "Well-Architected" framework built on the same ideas.

## Well-Architected pillars (same idea, both clouds)
| Pillar | Question it asks |
|---|---|
| Operational excellence | Can we run + improve it smoothly? |
| Security | Is data + access protected? |
| Reliability | Does it survive failures? |
| Performance efficiency | Are we using the right resources well? |
| Cost optimization | Are we avoiding waste? |
| Sustainability (AWS) | Are we minimizing environmental impact? |

> AWS = **AWS Well-Architected Framework**. Azure = **Azure Well-Architected Framework** (same pillars, minus separate sustainability).

## Common patterns
| Pattern | Use for | Building blocks |
|---|---|---|
| **N-tier web app** | Classic apps | LB + auto-scaling compute + managed DB |
| **Serverless API** | Spiky/event apps | API GW + Functions + NoSQL |
| **Event-driven** | Decoupling, async | Queue/topic + consumers |
| **Microservices** | Independent scaling | Containers (EKS/AKS) + service mesh |
| **Data lake + warehouse** | Analytics | Object storage + ETL + warehouse |
| **RAG / GenAI app** | AI over your data | Vector store + FM + guardrails |
| **HA / Multi-AZ** | Survive zone failure | Resources across AZs |
| **DR (multi-region)** | Survive region failure | Replication + failover |

## High availability vs disaster recovery
| | HA | DR |
|---|---|---|
| Goal | No downtime from small failures | Recover from big/region failures |
| Scope | Multi-AZ | Multi-region |
| Metric | Uptime | RTO (recover time) / RPO (data loss) |

## DR strategies (cheap → expensive)
Backup & restore → Pilot light → Warm standby → Active/active (multi-site).

## AWS ↔ Azure mapping (decoupling + delivery)
| Capability | AWS | Azure |
|---|---|---|
| Queue | SQS | Service Bus / Storage Queue |
| Pub/sub | SNS | Event Grid |
| Event streaming | Kinesis | Event Hubs |
| Workflow orchestration | Step Functions | Logic Apps / Durable Functions |
| Global delivery | CloudFront | Front Door |

## Hands-on lab
- Diagram a resilient web app (LB + auto-scaling + Multi-AZ DB + object storage + CDN) for **both** clouds.
- Then build a minimal version once and **clean up**.

## ⚠️ Common exam traps
- HA (Multi-AZ) ≠ DR (multi-region).
- Decouple with queues to absorb spikes + isolate failures.
- "Least operational overhead" usually → managed/serverless options.
- Match DR strategy to required **RTO/RPO + budget**.

## 🃏 Flashcards
| Q | A |
|---|---|
| Survive an AZ failure? | Multi-AZ (HA) |
| Survive a region failure? | Multi-region (DR) |
| Cheapest DR? | Backup & restore |
| Lowest RTO/RPO DR? | Active/active multi-site |
| Decouple components? | Queue (SQS / Service Bus) |
| Both clouds' design guide? | Well-Architected Framework |

🔗 Related: [[compute]] · [[networking]] · [[cost-optimization]] · [[ai-ml]]
