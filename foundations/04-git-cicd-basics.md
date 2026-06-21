---
tags: [foundations, beginner, git, cicd, devops]
aliases: [Git CICD Basics, Git and GitHub, CI/CD Basics]
---
> [[03-glossary|◀ Glossary]] · [[HOME|🏠 Home]] · [[START-HERE|Start here]] · [[STUDY_PLAN|Plan (M2.5)]] · [[PROGRESS|Tracker]] · [[05-lakehouse-basics|Lakehouse ▶]]

# 04 · Git + GitHub + CI/CD (ship code like a pro)

## In plain English
- **Git** = *save-points + undo history* for your code. Every change is a snapshot you can return to.
- **GitHub** = the cloud home for your Git projects — backup, sharing, and teamwork in one place.
- **CI/CD** = a robot that, every time you save code, **automatically tests it and ships it**.
  - **CI** (Continuous Integration) = "did my change break anything?" → run the tests.
  - **CD** (Continuous Delivery/Deployment) = "package it and put it where it runs" → build a container, deploy it.

> Analogy: Git is the *track-changes + version history* in a Google Doc; CI/CD is a *robot reviewer* that checks every edit and publishes the doc the moment it passes.

## Why it matters for your career
Every Data Analyst / Data Scientist / ML / MLOps / Data Engineer role assumes you can use Git — it's table stakes. **CI/CD is the literal backbone of MLOps**: retraining, testing, and deploying models all run through pipelines. Knowing this lifts you from "writes notebooks" to "ships reliable systems."

## Key concepts
- **repo** (repository) — one project's folder, tracked by Git.
- **commit** — one saved snapshot, with a message.
- **branch** — a parallel line of work (e.g. `feature/add-forecast`) so you don't break `main`.
- **merge** / **merge conflict** — combining branches; a *conflict* is when two edits touch the same line and you must choose.
- **pull request (PR)** — "please review + merge my branch." Where teams discuss code.
- **remote / origin** — the GitHub copy; `push` (send up), `pull` (get down), `clone` (copy down).
- **.gitignore** — files Git should ignore (secrets, `.venv`, big data). **Never commit credentials.**
- **GitHub Actions** — GitHub's CI/CD: a **workflow** (YAML) runs **jobs** of **steps** on a **runner** when you push.
- **Pipeline stages** — typically **build → test → package (Docker) → deploy**.
- **unit test (pytest)** — a tiny automated check that a function returns what it should.
- **ECR / ECS-Fargate** — where the container image is stored / run (see [[STUDY_PLAN|Module 4]]).

## Tools
`git` · GitHub · GitHub Actions · `pytest` · Docker · AWS CLI · ECR · ECS/Fargate

## Mini lab (full version = [[STUDY_PLAN|STUDY_PLAN Module 2.5]])
1. `git init` a repo; make 2–3 commits with clear messages.
2. Create a `feature` branch, change a file, open a **pull request** on GitHub.
3. Force a **merge conflict** (edit the same line on two branches) and resolve it.
4. Add a `test_*.py` with one `pytest` assertion; run `pytest` locally.
5. Add `.github/workflows/ci.yml` that runs `pytest` on every push — watch it go green.
6. Extend the workflow to **build a Docker image**.
7. Push the image to **ECR** (your personal `learn` account only).
8. Trigger an **ECS/Fargate** deploy from the workflow.

> 💸 Cost/safety: steps 1–6 are free (local + GitHub). Steps 7–8 touch AWS — use your **personal `learn` account**, never the company account, and tear resources down after.

## ✅ Checkpoint
I can explain and build a basic **CI/CD pipeline from a code commit to a container deployment**, and I understand branches, PRs, merge conflicts, and unit tests.

---
Back to: [[HOME]] · [[START-HERE]] · [[STUDY_PLAN]] · [[PROGRESS]]
