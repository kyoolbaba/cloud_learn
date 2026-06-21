# 🗄️ Databases (Concept + AWS↔Azure)

> **Concept note:** Pick a database by data shape + access pattern. Relational for structured + transactions; NoSQL for scale + flexible schema; specialized stores for caching/search/graph.

## Database families
| Family | Use when | Example data |
|---|---|---|
| Relational (SQL) | Structured, transactions, joins | Orders, customers |
| Key-value / document (NoSQL) | Huge scale, flexible schema, low latency | Sessions, events, profiles |
| In-memory cache | Ultra-fast reads | Leaderboards, sessions |
| Data warehouse | Analytics over big history | Reporting/BI |
| Search | Full-text / vector search | Logs, documents, RAG |

## AWS ↔ Azure service mapping
| Capability | AWS | Azure |
|---|---|---|
| Managed relational | RDS / Aurora | Azure SQL Database / DB for PostgreSQL/MySQL |
| NoSQL | DynamoDB | Cosmos DB |
| In-memory cache | ElastiCache | Azure Cache for Redis |
| Data warehouse | Redshift | Synapse / Microsoft Fabric |
| Search | OpenSearch | Azure AI Search |
| Graph | Neptune | Cosmos DB (Gremlin) |
| Ledger/Time series | QLDB / Timestream | (various) |

## Relational HA/scaling
- **AWS RDS:** Multi-AZ = HA (standby); Read Replicas = scale reads.
- **Azure SQL:** zone-redundant / geo-replication; read scale-out.

## Hands-on lab
- Stand up a small managed SQL DB; connect; insert rows.
- Stand up a NoSQL table/container; add an item; note throughput units.
- **Cleanup:** delete DB instance / resource group (these bill hourly!).

## ⚠️ Common exam traps
- Multi-AZ (HA) ≠ Read Replica (scale) in RDS.
- Cosmos DB throughput is **RU/s**; pick partition key carefully to avoid hot partitions.
- Warehouse (Redshift/Synapse) is for analytics, not high-frequency transactions.

## 🃏 Flashcards
| Q | A |
|---|---|
| AWS NoSQL? | DynamoDB |
| Azure NoSQL? | Cosmos DB |
| HA for RDS? | Multi-AZ |
| Scale reads (RDS)? | Read replicas |
| AWS warehouse? | Redshift |
| Azure warehouse? | Synapse / Fabric |
| Cache service (Azure)? | Azure Cache for Redis |

🔗 Related: [[data-engineering]] · [[storage]]
