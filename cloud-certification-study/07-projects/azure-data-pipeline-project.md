# 🛠️ Project: Azure Data Pipeline (Blob → Data Factory → Synapse/Fabric)

> **Goal:** Build an end-to-end batch pipeline on Azure. Reinforces DP-900 + AZ-104 basics. Mirror of the AWS pipeline so you learn the mapping.
>
> 🌍 **Real-world story:** Raw files land in a data lake; Data Factory transforms them; Synapse/Fabric serves analytics to Power BI.

## What you'll build
```
Sample CSV → Data Lake (Blob, raw) → Data Factory pipeline (clean → Parquet) → Data Lake (curated)
                                                          ↓
                                  Synapse Serverless SQL / Microsoft Fabric  →  Power BI
```

## Skills practiced
- Data Lake Storage zoning + Parquet
- Azure Data Factory copy + mapping data flows
- Synapse serverless SQL queries (query-in-place)
- Power BI visualization basics
- RBAC + managed identity, Cost Management

## Steps
1. Create a Storage Account with **hierarchical namespace** (Data Lake); add `raw/` + `curated/` containers.
2. Upload a sample dataset.
3. Build a **Data Factory** pipeline: copy → transform to **Parquet** into `curated/`.
4. Query curated data with **Synapse Serverless SQL** (external table).
5. (Bonus) Build a simple **Power BI** report on the result.
6. Secure access with **managed identity** + RBAC.

## ✅ Success criteria
- [ ] Pipeline runs and writes curated Parquet
- [ ] Synapse query returns correct aggregates
- [ ] Access uses managed identity (no keys in plain text)

## 💸 Cleanup (do it!)
- [ ] **Delete the resource group** (removes Data Factory, Synapse, storage in one go)
- [ ] Confirm no Synapse pools left running
- [ ] Check **Cost Management → Cost analysis**

## 📝 Reflection / write-up
- Map each Azure service to its AWS equivalent (see [[aws-data-pipeline-project]])
- Which was easier/harder than AWS, and why?

🔗 Related: [[../03-shared-cloud-concepts/data-engineering]] · [[../02-azure/fundamentals/azure-data-fundamentals-DP-900]] · [[multi-cloud-comparison-project]]
