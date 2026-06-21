# Microsoft Certified: Azure Network Engineer Associate

> 🍼 **Beginner explanation:** Teaches designing and operating Azure networks — VNets, hybrid connectivity, load balancing, private access, and network security. Niche unless networking is your focus.
>
> 🌍 **Real-world example:** Connect on-prem to Azure over VPN/ExpressRoute, segment VNets, expose apps via private endpoints, and secure traffic with NSGs + firewall.

| Field | Value |
|---|---|
| **1. Certification name** | Microsoft Certified: Azure Network Engineer Associate |
| **2. Exam code** | AZ-700 |
| **3. Level** | Associate |
| **4. Best for role** | Network engineers |
| **5. Prerequisites** | AZ-104 / networking background recommended |

---

## 6. Core topics
- Core networking (VNets, subnets, routing, IP)
- Hybrid connectivity (VPN Gateway, ExpressRoute, Virtual WAN)
- Application delivery (Load Balancer, App Gateway, Front Door, Traffic Manager)
- Private access (Private Link, Private Endpoint, Service Endpoints)
- Network security (NSG, Azure Firewall, DDoS)

## 7. Azure services to learn
| Category | Services |
|---|---|
| Core | Virtual Network, subnets, UDR, DNS |
| Hybrid | VPN Gateway, ExpressRoute, Virtual WAN |
| Delivery | Load Balancer, Application Gateway, Front Door, Traffic Manager |
| Private | Private Link, Private Endpoint, Service Endpoints |
| Security | NSG, Azure Firewall, DDoS Protection |

## 8. Hands-on labs
1. **VNet + subnets + UDR**. *(Cleanup: delete RG.)*
2. **NSG** rules + effective security rules. *(Cleanup: delete RG.)*
3. **Load Balancer** across 2 VMs. *(Cleanup: delete RG.)*
4. **Private Endpoint** to a storage account. *(Cleanup: delete RG.)*
5. **Azure DNS / Private DNS** zone. *(Cleanup: delete RG.)*

## 9. Two-week plan
| Day | Focus |
|---|---|
| 1–3 | Core networking + routing; Lab 1 |
| 4–5 | Hybrid (VPN/ExpressRoute/vWAN) |
| 6–7 | Application delivery; Lab 3 |
| 8–9 | Private access; Lab 4 |
| 10 | Security + DNS; Labs 2, 5 |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 80%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Core networking (Labs 1–2) |
| 2 | Hybrid + delivery (Lab 3) |
| 3 | Private access + security + DNS (Labs 4–5) |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1–2 | Core networking + routing (Lab 1) |
| 3 | Hybrid connectivity |
| 4 | Application delivery (Lab 3) |
| 5 | Private access (Lab 4) |
| 6 | Network security (Lab 2) |
| 7 | DNS (Lab 5) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **80%+**. Detail-heavy: routing, gateway SKUs, delivery service choice.
- 4 timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] VPN vs ExpressRoute vs Virtual WAN
- [ ] Load Balancer vs App Gateway vs Front Door vs Traffic Manager
- [ ] Private Endpoint vs Service Endpoint
- [ ] UDR + system routes
- [ ] NSG vs Azure Firewall
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
| Global HTTP(S) delivery + WAF? | Azure Front Door |
| DNS-based global routing? | Traffic Manager |
| Private dedicated link to Azure? | ExpressRoute |
| Private IP access to PaaS? | Private Endpoint |
| AWS equivalent of ExpressRoute? | Direct Connect |
| Layer-4 load balancing? | Azure Load Balancer |

→ More in `05-flashcards/azure-flashcards.md`.

## 17. Official docs / resources
- [ ] AZ-700 exam page: _add link_
- [ ] Microsoft Learn AZ-700 path: _add link_
- [ ] Azure networking docs: _add link_
- [ ] Practice assessment: _add link_
