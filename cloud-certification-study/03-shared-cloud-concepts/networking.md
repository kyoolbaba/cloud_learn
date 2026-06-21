# 🌐 Networking (Concept + AWS↔Azure)

> **Concept note:** Networking = your private space in the cloud + the roads and locked doors controlling traffic.

## Core ideas
| Idea | Plain meaning |
|---|---|
| Virtual network | Your isolated network in the cloud |
| Subnet | A slice of that network (public or private) |
| Route table | Rules for where traffic goes |
| Internet/NAT gateway | Door to the internet (in / out) |
| Firewall rules | Who can talk to what (stateful/stateless) |
| Load balancer | Spreads traffic across servers |
| DNS | Turns names into addresses |
| Private connectivity | Reach services without the public internet |

## AWS ↔ Azure service mapping
| Capability | AWS | Azure |
|---|---|---|
| Virtual network | VPC | Virtual Network (VNet) |
| Subnet firewall (stateful) | Security Group | Network Security Group (NSG) |
| Subnet ACL (stateless) | Network ACL | NSG (combined) |
| L7 load balancer | ALB | Application Gateway |
| L4 load balancer | NLB | Azure Load Balancer |
| Global delivery | CloudFront + Global Accelerator | Front Door |
| DNS | Route 53 | Azure DNS / Traffic Manager |
| Private link to PaaS | VPC Endpoint / PrivateLink | Private Endpoint |
| Hybrid private link | Direct Connect | ExpressRoute |
| Connect many networks | Transit Gateway | Virtual WAN |
| Managed firewall | Network Firewall | Azure Firewall |

## Hands-on lab
- Build a VPC/VNet with a public + private subnet, attach a firewall rule, deploy a VM in private subnet.
- **Cleanup:** delete NAT gateway first (AWS), then delete VPC / resource group.

## ⚠️ Common exam traps
- Security Group = **stateful** (return traffic auto-allowed); NACL = **stateless**.
- NAT Gateway bills hourly — a classic forgotten cost.
- Private Endpoint vs Service Endpoint (Azure) differ; Endpoint = private IP into your VNet.

## 🃏 Flashcards
| Q | A |
|---|---|
| AWS private network? | VPC |
| Azure equivalent? | VNet |
| Stateful instance firewall (AWS)? | Security Group |
| Dedicated private link to on-prem (Azure)? | ExpressRoute |
| Global HTTP delivery + WAF (Azure)? | Front Door |

🔗 Related: [[iam-security]] · [[architecture-patterns]]
