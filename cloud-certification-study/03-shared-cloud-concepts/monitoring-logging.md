# 📈 Monitoring & Logging (Concept + AWS↔Azure)

> **Concept note:** Three pillars of observability: **metrics** (numbers over time), **logs** (event records), **traces** (a request's journey). Plus **audit logs** (who did what) and **alerts** (tell me when something's wrong).

## What each answers
| Question | Tool type |
|---|---|
| Is it healthy / how busy? | Metrics + dashboards |
| What happened / why did it fail? | Logs |
| Where is the slowdown across services? | Tracing |
| Who changed/called this? | Audit log |
| Notify me when X breaks | Alerts |

## AWS ↔ Azure service mapping
| Capability | AWS | Azure |
|---|---|---|
| Metrics + alarms + dashboards | CloudWatch | Azure Monitor |
| Logs | CloudWatch Logs | Log Analytics (Azure Monitor Logs) |
| Tracing | X-Ray | Application Insights |
| Audit (API activity) | CloudTrail | Activity Log |
| Compliance/config state | AWS Config | Azure Policy + Resource Graph |
| App performance monitoring | CloudWatch + X-Ray | Application Insights |

## Hands-on lab
- Create a metric alarm (CPU) → notification (SNS / Action Group).
- View a service's logs; find a specific event in the audit log.
- **Cleanup:** delete alarms, topics/action groups, log groups/workspaces.

## ⚠️ Common exam traps
- **CloudWatch** = performance/logs/alarms; **CloudTrail** = API audit; **Config** = compliance. Don't mix them up.
- Azure: **Azure Monitor** is the umbrella; **Log Analytics** stores logs; **Activity Log** = audit.
- Log retention costs money — set retention policies.

## 🃏 Flashcards
| Q | A |
|---|---|
| Who called this API? (AWS) | CloudTrail |
| Performance metrics + alarms (AWS) | CloudWatch |
| Azure umbrella for monitoring | Azure Monitor |
| App tracing in Azure | Application Insights |
| Is a resource compliant? (AWS) | AWS Config |
| Audit activity in Azure | Activity Log |

🔗 Related: [[iam-security]] · [[cost-optimization]]
