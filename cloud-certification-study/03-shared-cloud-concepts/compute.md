# 🖥️ Compute (Concept + AWS↔Azure)

> **Concept note:** Compute = where your code/applications actually run. Choose based on how much control vs convenience you want, and how "bursty" the workload is.

## The spectrum (more control → less management)
| Model | What it is | Use when |
|---|---|---|
| Virtual machines | Full OS you manage | Lift-and-shift, full control |
| Containers | Packaged app + deps | Microservices, portability |
| Serverless functions | Just your code, event-driven | Spiky/irregular workloads, glue logic |
| PaaS app hosting | Deploy code, platform manages servers | Web apps/APIs fast |

## AWS ↔ Azure service mapping
| Capability | AWS | Azure |
|---|---|---|
| Virtual machines | EC2 | Virtual Machines |
| Auto scaling | Auto Scaling Groups | VM Scale Sets |
| Serverless functions | Lambda | Azure Functions |
| PaaS web hosting | Elastic Beanstalk | App Service |
| Containers (managed) | ECS / Fargate | Container Apps / ACI |
| Kubernetes | EKS | AKS |
| Batch | AWS Batch | Azure Batch |

## Hands-on lab (do once, both clouds)
- Launch a tiny VM (EC2 t3.micro / Azure B-series), connect, then **delete it**.
- Deploy a serverless "hello world" (Lambda / Azure Function).
- **Cleanup:** terminate VM / delete resource group.

## ⚠️ Common exam traps
- **Stopping** a VM may still cost (Azure: "stopped" ≠ "deallocated"; storage still bills).
- Serverless has limits (Lambda 15-min timeout; cold starts).
- Spot/low-priority VMs are cheap but can be reclaimed — not for stateful critical work.

## 🃏 Flashcards
| Q | A |
|---|---|
| Cheapest interruptible compute (AWS)? | Spot Instances |
| Kubernetes service in Azure? | AKS |
| Event-driven code, no servers? | Lambda / Azure Functions |
| Scale VMs automatically (Azure)? | VM Scale Sets |

🔗 Related: [[networking]] · [[cost-optimization]]
