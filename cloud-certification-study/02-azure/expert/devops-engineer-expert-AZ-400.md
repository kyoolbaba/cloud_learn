# Microsoft Certified: DevOps Engineer Expert

> 🍼 **Beginner explanation:** Advanced cert combining people + process + tools to deliver software continuously on Azure — source control, CI/CD, security/compliance, and monitoring.
>
> 🌍 **Real-world example:** Set up Git workflows, Azure Pipelines/GitHub Actions that build+test+deploy with approvals, infrastructure as code, and dashboards that track delivery health.

> 📌 **Prerequisite:** You must already hold **Azure Administrator Associate (AZ-104)** *or* **Azure Developer Associate (AZ-204)**.

| Field | Value |
|---|---|
| **1. Certification name** | Microsoft Certified: DevOps Engineer Expert |
| **2. Exam code** | AZ-400 |
| **3. Level** | Expert |
| **4. Best for role** | DevOps engineers |
| **5. Prerequisites** | **AZ-104 or AZ-204 required** |

---

## 6. Core topics
- Source control & branching strategies (Git)
- CI/CD (Azure Pipelines, GitHub Actions)
- Security & compliance in pipelines (secrets, scanning)
- Infrastructure as code (Bicep/ARM/Terraform)
- Instrumentation, monitoring & feedback
- Communication, processes, and collaboration

## 7. Azure services to learn
| Category | Services |
|---|---|
| Source/CI/CD | Azure Repos, Azure Pipelines, GitHub, GitHub Actions |
| IaC | Bicep, ARM, Terraform |
| Artifacts/Containers | Azure Artifacts, Azure Container Registry |
| Security | Key Vault, secret scanning, Defender for DevOps |
| Observability | Azure Monitor, Application Insights |

## 8. Hands-on labs
1. **Azure Pipelines** build + deploy. *(Cleanup: delete pipeline + RG.)*
2. **GitHub Actions** workflow deploying to Azure. *(Cleanup: delete RG + workflow.)*
3. **IaC with Bicep** (deploy + update). *(Cleanup: delete RG/stack.)*
4. **Release strategy** (approvals, environments, blue/green). *(Design + build.)*
5. **Monitoring dashboard** (App Insights + Azure Monitor). *(Cleanup: delete RG.)*

## 9. Two-week plan (refresher)
| Day | Focus |
|---|---|
| 1–2 | Source control + branching |
| 3–5 | CI/CD (Pipelines + Actions); Labs 1–2 |
| 6–7 | IaC (Bicep); Lab 3 |
| 8 | Release strategies; Lab 4 |
| 9 | Security/compliance in pipelines |
| 10 | Instrumentation + feedback; Lab 5 |
| 11–12 | Mock #1 + gaps |
| 13 | Revise |
| 14 | Mock #2 → book if 75%+ |

## 10. Four-week plan
| Week | Focus |
|---|---|
| 1 | Source control + CI/CD (Labs 1–2) |
| 2 | IaC + release strategies (Labs 3–4) |
| 3 | Security + monitoring (Lab 5) |
| 4 | 3 mocks + revision |

## 11. Eight-week plan
| Weeks | Focus |
|---|---|
| 1 | Git + branching |
| 2–3 | CI/CD (Labs 1–2) |
| 4 | IaC (Lab 3) |
| 5 | Release strategies (Lab 4) |
| 6 | Security/compliance |
| 7 | Instrumentation (Lab 5) |
| 8 | Mocks + revision |

## 12. Mock exam strategy
- Target **75%+**. Scenario-heavy: choose pipeline/branching/release/IaC approach.
- 3+ timed mocks; log misses.

## 13. Final revision checklist (last 3 days)
- [ ] Branching strategies (trunk, GitFlow, feature flags)
- [ ] Pipelines vs Actions; YAML stages/environments/approvals
- [ ] Deployment strategies (canary/blue-green/rolling)
- [ ] Secrets management + secure pipelines
- [ ] DORA metrics + monitoring
- [ ] Flashcards reviewed twice

## 14. Notes template
```
### Topic: <name>
- Concept:
- Real-world use:
- Azure service(s):
- AWS equivalent:
- Common exam trap:
- Trade-off notes:
```

## 15. Mistake log template
| Date | Topic | What I got wrong | Correct concept | Revisit date |
|---|---|---|---|---|

## 16. Flashcards (starter set)
| Q | A |
|---|---|
| Azure-native CI/CD? | Azure Pipelines |
| Azure IaC language? | Bicep |
| AWS equivalent of Azure Pipelines? | CodePipeline |
| Store build artifacts? | Azure Artifacts |
| Gate a deployment for sign-off? | Environment approvals |
| Measure delivery performance? | DORA metrics |

→ More in `05-flashcards/azure-flashcards.md`.

## 17. Official docs / resources
- [ ] AZ-400 exam page: _add link_
- [ ] Azure DevOps + GitHub Actions docs: _add link_
- [ ] Bicep docs: _add link_
- [ ] Practice assessment: _add link_
