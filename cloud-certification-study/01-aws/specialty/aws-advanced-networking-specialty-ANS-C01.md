# AWS Certified Advanced Networking – Specialty

> 🍼 **Beginner explanation:** Deep cert on AWS networking — VPCs, routing, DNS, hybrid connections to on-prem, and network security. Niche; only do it if networking is your job.
>
> 🌍 **Real-world example:** Design a global network connecting 30 VPCs, an on-prem data center over Direct Connect, with private DNS and tight security.

| Field | Value |
|---|---|
| **1. Certification name** | AWS Certified Advanced Networking – Specialty |
| **2. Exam code** | ANS-C01 |
| **3. Level** | Specialty |
| **4. Best for role** | Network engineers, cloud architects |
| **5. Prerequisites** | Strong networking background + SAA recommended |

---

## 6. Core topics
- VPC design (subnets, route tables, NAT, IGW, endpoints)
- Hybrid connectivity (Direct Connect, VPN, Transit Gateway)
- Routing (BGP basics), DNS (Route 53, resolver)
- Network security (NACLs, SGs, Network Firewall, WAF, Shield)
- Load balancing + content delivery (ELB, Global Accelerator, CloudFront)
- Monitoring & troubleshooting (VPC Flow Logs, Reachability Analyzer)

## 7. AWS services to learn
| Category | Services |
|---|---|
| Core | VPC, subnets, route tables, NAT/IGW, VPC endpoints (Gateway/Interface), PrivateLink |
| Hybrid | Direct Connect, Site-to-Site VPN, Transit Gateway |
| DNS | Route 53 (public/private), Resolver endpoints |
| Security | Security Groups, NACLs, Network Firewall, WAF, Shield |
| Delivery | ELB (ALB/NLB/GWLB), Global Accelerator, CloudFront |
| Ops | VPC Flow Logs, Reachability Analyzer, CloudWatch |

## 8. Hands-on labs (build + diagram)
1. **VPC design** with public/private subnets + endpoints. *(Cleanup: delete NAT GW first, then VPC.)*
2. **Subnet routing + VPC peering** between 2 VPCs. *(Cleanup: delete peering + VPCs.)*
3. **Transit Gateway** connecting 3 VPCs (diagram + optional build). *(Cleanup: delete attachments + TGW — billed!)*
4. **Route 53 private hosted zone** + resolver concept. *(Cleanup: delete hosted zone.)*

## 9. Two-week plan (refresher)
| Day | Focus |
|---|---|
| 1–2 | VPC fundamentals + endpoints; Lab 1 |
| 3–4 | Routing + peering; Lab 2 |
| 5–6 | Transit Gateway + hybrid; Lab 3 |
| 7 | Direct Connect + VPN |
| 8 | DNS / Route 53; Lab 4 |
| 9 | Network security |
| 10 | Load balancing + delivery |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 75%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | VPC + routing + endpoints (Labs 1–2) |
| 2 | Hybrid + Transit Gateway + DX/VPN (Lab 3) |
| 3 | DNS + security + delivery (Lab 4) |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | VPC deeply + endpoints (Lab 1) |
| 3 | Routing + peering (Lab 2) |
| 4 | Transit Gateway (Lab 3) |
| 5 | Direct Connect + VPN + BGP |
| 6 | DNS / Route 53 (Lab 4) |
| 7 | Security + delivery + troubleshooting |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **75%+**. Deep, detailed networking scenarios + troubleshooting.
- Practice routing-table reasoning and hybrid connectivity choices.
- 3+ timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] Gateway vs Interface endpoints (PrivateLink)
- [ ] Transit Gateway vs peering vs VPN
- [ ] Direct Connect types + resiliency + DX+VPN
- [ ] Route 53 routing policies + resolver endpoints
- [ ] SG (stateful) vs NACL (stateless)
- [ ] VPC Flow Logs + Reachability Analyzer for troubleshooting
- [ ] Flashcards reviewed twice

## 14. Notes template
```
### Topic: <name>
- Concept:
- Real-world use:
- AWS service(s):
- Azure equivalent:
- Common exam trap:
- Trade-off notes:
```

## 15. Mistake log template
| Date | Topic | What I got wrong | Correct concept | Revisit date |
|---|---|---|---|---|

## 16. Flashcards (starter set)
| Q | A |
|---|---|
| Private access to S3 without internet? | Gateway VPC endpoint |
| Private access to a partner service? | Interface endpoint / PrivateLink |
| Connect many VPCs + on-prem centrally? | Transit Gateway |
| Stateful firewall at instance level? | Security Group |
| Stateless filtering at subnet level? | NACL |
| Diagnose if traffic can reach a resource? | Reachability Analyzer |

→ More in `05-flashcards/aws-flashcards.md`.

## 17. Official docs / resources
- [ ] ANS-C01 exam guide: _add link_
- [ ] VPC + Transit Gateway docs: _add link_
- [ ] Direct Connect docs: _add link_
- [ ] Official practice exam: _add link_
