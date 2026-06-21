# 🧪 Azure Labs — Reusable Guides & Cleanup

Hands-on labs live inside each certification file (section 8). This folder holds **reusable lab guidance** and the **golden cleanup rules**.

## 🔑 Golden lab rules
1. **Put every lab's resources in a dedicated Resource Group** named like `rg-certstudy-<topic>`.
2. **Delete the resource group when done** — this removes everything inside in one action. This is the #1 Azure cost-safety habit.
3. **Use free/low-cost SKUs** (B-series VMs, free/basic tiers, serverless where possible).
4. **Set a budget** in Cost Management + spending alert.
5. **Log each lab + cleanup** in `04-trackers/lab-completion-tracker.md`.

## 💸 "These cost money even when idle" — delete first
| Resource | Why it bills | Cleanup |
|---|---|---|
| Virtual Machines | Compute hourly (stopped ≠ deallocated) | **Deallocate or delete** (stop from portal to deallocate) |
| Public IPs (static) | Hourly | Delete |
| App Gateway / Load Balancer | Hourly | Delete |
| Azure SQL / Cosmos DB | Provisioned throughput / DTUs | Delete or scale to serverless/free |
| AKS clusters | Node VMs | Delete cluster |
| Azure Firewall | Hourly (expensive) | Delete |
| Search / OpenAI / Synapse | Provisioned capacity | Delete service/deployment |
| Recovery Services vault | Backups stored | Delete recovery points + vault |

## 🧹 End-of-session cleanup checklist
- [ ] Deleted the lab's **resource group(s)**
- [ ] Confirmed VMs are deleted/deallocated (not just "stopped")
- [ ] Released unused static public IPs
- [ ] Deleted Azure Firewall / App Gateway / Load Balancers
- [ ] Deleted Recovery Services vaults + backup items
- [ ] Checked **Cost Management → Cost analysis** for surprises
- [ ] Logged the lab + cleanup in the lab tracker

## 🛠️ Lab environment tips
- Prefer the **Azure Portal** for learning; CLI/Bicep later.
- Keep everything in **one region** to avoid orphaned resources.
- Screenshot as evidence; note it in the lab tracker.
- Remember: **stopping** a VM in the OS still bills — use **Deallocate** (portal "Stop") or delete.
