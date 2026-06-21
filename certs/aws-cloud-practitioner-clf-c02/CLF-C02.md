---
tags: [cert/clf-c02, aws/foundational, moc]
cert: CLF-C02
level: foundational
aliases: [CLF-C02, AWS Cloud Practitioner]
---
> **Track notes:** [[domain-1-cloud-concepts|1 · Cloud Concepts]] · [[domain-2-security-compliance|2 · Security]] · [[domain-3-technology-services|3 · Tech & Services]] · [[domain-4-billing-pricing-support|4 · Billing]] · [[CLF-C02-practice|🧪 Practice]] · [[CLF-C02-readiness|✅ Readiness]]
> **Up:** [[CERTS-MOC|All certs]] · [[CERT_ROADMAP|Roadmap]]

# AWS Certified Cloud Practitioner (CLF-C02) — study track

Your **foundation** cert. Knowledge-based (you mostly recognize services + concepts);
hands-on isn't required to pass but it makes everything stick — and you've already done
a lot of it in `../../labs/` and `../../projects/`.

## Exam facts
| | |
|---|---|
| Code | **CLF-C02** (current version) |
| Questions | **65** (multiple-choice + multiple-response); ~15 are unscored |
| Time | **90 minutes** |
| Pass | **700 / 1000** (scaled) |
| Cost | **$100 USD** (often a 50% retake/discount voucher floats around) |
| Prereqs | none |
| Validity | 3 years |
| Delivery | Pearson VUE — test center **or** online proctored from home |

## The 4 domains (memorize these weightings)
| # | Domain | Weight | File |
|---|---|---|---|
| 1 | Cloud Concepts | **24%** | `domain-1-cloud-concepts.md` |
| 2 | Security & Compliance | **30%** | `domain-2-security-compliance.md` |
| 3 | Cloud Technology & Services | **34%** | `domain-3-technology-services.md` |
| 4 | Billing, Pricing & Support | **12%** | `domain-4-billing-pricing-support.md` |

Domains 2 + 3 are **64%** of the exam — spend your time there.

## 2–3 week study plan (~1 hr/day)
| Days | Do |
|---|---|
| 1–2 | Domain 1 notes + hands-on; its practice Qs |
| 3–5 | Domain 2 (security/IAM) — biggest leverage from your IAM project |
| 6–9 | Domain 3 (services) — the long one; flashcard the service names |
| 10–11 | Domain 4 (billing/support) |
| 12–13 | `practice-questions.md` (full mock) — review every wrong answer |
| 14 | `exam-readiness-checklist.md` — if all ticked, **book it** |

## How to use this track
1. Read the domain notes (theory is trimmed to *only what the exam tests*).
2. Do the **Hands-on** in your `learn` AWS account (set `$env:AWS_PROFILE="learn"` first).
3. Answer the domain's practice questions; re-read anything you miss.
4. Take the full mock in `practice-questions.md`.
5. Clear the readiness checklist → register at **aws.amazon.com/certification**.

## What you've already built that maps here
| Already done | Covers (CLF-C02) |
|---|---|
| `projects/00-safety-budget`, `04-iam-least-privilege` | Domain 2 (IAM, MFA, least privilege), Domain 4 (Budgets) |
| `projects/01-s3-file-vault` | Domain 3 (S3, storage) |
| `projects/02/03-ec2*` | Domain 3 (EC2, security groups), Domain 1 (regions/AZs) |
| `projects/05-lambda-api`, `07-ecr-fargate` | Domain 3 (Lambda, containers, serverless) |
| `projects/11-terraform-backend` | Domain 3 (IaC concept; exam tests CloudFormation) |
| `labs/m1-networking` | Domain 3 (VPC, DNS, ports) |

## Exam-day tips
- Flag-and-return: answer easy ones first, revisit the rest.
- Wrong-answer tells: "manage the OS/patching for you" → managed/serverless; "cheapest for
  fault-tolerant batch" → Spot; "no servers to manage" → Lambda/Fargate/S3.
- When two answers look right, pick the **most managed / most AWS-native** option.
