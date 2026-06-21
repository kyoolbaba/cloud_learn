---
tags: [moc, home, beginner]
aliases: [Start Here, Beginner Path]
---
> [[HOME|🏠 Vault home]] · [[foundations/01-absolute-basics|Foundations ▶]] · [[CERTS-MOC|Certs]] · [[PROGRESS|Tracker]]

# 👋 Start here

This folder is your cloud-learning home. It looks like a lot — but you only ever do
**one small thing at a time**. This page tells you what's here and the order to use it.

## What you're ultimately building toward
The ability to use **the cloud** (rented computers on the internet) to run your
forecasting work — ending in a "Run in cloud" button. But that's the *destination*.
You start at the very bottom and climb. No step assumes you already know the next.

## What's in this folder (in plain terms)
| Folder / file | What it is | When to use it |
|---|---|---|
| **`foundations/`** | Absolute basics + career domains (Git/CI-CD, Lakehouse, MLOps, FinOps, K8s) | **Right now, if any word confuses you** |
| `STUDY_PLAN.md` | The big multi-week plan (Linux → networking → Docker → AWS) | Background reading |
| `labs/` | Guided walkthroughs + ready-made code for each topic | As you reach each module |
| `projects/` | Small "build one thing" projects, one per AWS service | Your hands-on practice |
| `certs/` | Study tracks: CLF-C02, AIF-C01, DEA-C01, MLA-C01 (+ optional) | Your certification goal |
| `CERT_ROADMAP.md` | Which certs to chase, in order, for data roles | To see the cert path |
| `PROGRESS.md` | Your checklist / tracker | Tick things as you finish |

## ⚠️ Safety first (read this once)
**Do NOT run labs in the company / shared AWS account. Use a personal learning account only.**
The shared `default` account holds Healthium **production** data — creating or deleting things there
is unsafe. Every lab uses the `learn` profile on **your own** account → [[projects/SETUP-personal-aws|set it up here]].

## The order to actually do things (beginner path)
1. **Read Absolute Basics** → [[foundations/01-absolute-basics|① Absolute basics]] — meet the words; don't memorize.
2. **Learn Terminal Survival** → [[02-terminal-survival|② Terminal survival]] — open and use the terminal (everything needs this).
3. **Use the Glossary** → keep [[03-glossary|③ Glossary]] open in a tab; look up anything that stumps you.
4. **Set up a personal AWS account safely** → [[projects/SETUP-personal-aws|SETUP-personal-aws]] (personal account, **never** the company one).
5. **Complete Project 00 — budget alarm** → [[projects/00-safety-budget/README|Project 00]] so a surprise bill can never happen.
6. **Start CLF-C02** → [[CLF-C02|AWS Cloud Practitioner]] — read one domain at a time.
7. **Learn Linux / networking / Docker** → [[STUDY_PLAN|Study Plan]] Modules 0–2 (what everything runs on).
8. **Add Git + CI/CD** → [[04-git-cicd-basics|Git + CI/CD]] (Module 2.5) — the skill every job expects.
9. **Continue the AWS projects** → [[projects/README|Projects]] 01–12, one per service.
10. **Move into Data Engineering, Lakehouse & MLOps** → [[05-lakehouse-basics|Lakehouse]] + [[06-mlops-basics|MLOps]] (Modules 5.5–5.6).
11. **Then prepare for the certs** → [[AIF-C01]] → [[DEA-C01]] → [[MLA-C01|MLA-C01 🎯]] (your bullseye).

## How to learn this without drowning (read this twice)
- **Go slow. One concept at a time.** Confusion is *normal* and temporary, not a sign you're bad at this.
- **Type commands yourself, don't just copy-paste.** Your hands remember what your eyes skip.
- **Errors are not failures** — they're the computer telling you what it needs. Read the last line.
- **You don't need to understand everything before moving on.** Understanding comes from repetition.
- **Ask me anything, at any level.** "What is a terminal?" is a perfect question. So is "explain
  this error." I can also run commands and debug *with* you. There are no dumb questions here.

> If you remember one thing: **the cloud is just other people's computers that you rent
> by the minute.** Everything else is details on top of that.
