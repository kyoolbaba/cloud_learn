# 💰 Cost Optimization (Concept + AWS↔Azure)

> **Concept note:** Cloud is pay-as-you-go. Costs come from compute hours, storage GB, data transfer, and requests. Optimize by right-sizing, choosing the right pricing model, and turning off what you don't use.

## The big levers
| Lever | What to do |
|---|---|
| Right-size | Match instance/SKU to actual need |
| Pricing model | Commit (Reserved/Savings) for steady; Spot for interruptible; On-demand for spiky |
| Storage tiering | Move cold data to cheaper tiers/archive |
| Turn it off | Stop/delete dev resources nights/weekends |
| Reduce data transfer | Keep traffic in-region; use CDN |
| Serverless | Pay per use for spiky workloads |

## Pricing models
| Model | AWS | Azure |
|---|---|---|
| Commit for discount | Savings Plans / Reserved Instances | Reservations / Savings Plans |
| Cheap interruptible | Spot Instances | Spot VMs |
| On-demand | On-Demand | Pay-as-you-go |

## Cost tools
| Capability | AWS | Azure |
|---|---|---|
| Analyze spend | Cost Explorer | Cost Management (Cost analysis) |
| Set spend alerts | Budgets | Budgets |
| Recommendations | Trusted Advisor / Compute Optimizer | Azure Advisor |
| Estimate before building | Pricing Calculator | Pricing / TCO Calculator |

## Hands-on lab (do this DAY ONE)
- Set a **budget + spending alert** in both clouds.
- Tag resources with `project=cert-study`.
- Review Cost Explorer / Cost analysis weekly.

## ⚠️ Common exam traps
- "Most cost-effective" + "interruptible OK" → **Spot**.
- Steady 24/7 workload → **Reserved / Savings Plan**.
- Forgotten **NAT gateways, idle endpoints, unattached IPs, running DBs/endpoints** = silent bills.
- Cross-region/cross-AZ data transfer can be a hidden cost.

## 🃏 Flashcards
| Q | A |
|---|---|
| Steady workload discount (AWS)? | Savings Plan / Reserved |
| Interruptible cheap compute? | Spot |
| Set a spend alert (Azure)? | Budgets (Cost Management) |
| Right-sizing recommendations (Azure)? | Azure Advisor |
| Estimate cost before building? | Pricing/TCO Calculator |

🔗 Related: [[compute]] · [[storage]] · [[architecture-patterns]]
