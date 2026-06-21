---
tags: [foundations, beginner, kubernetes, devops]
aliases: [Kubernetes Basics, K8s Basics, Kubernetes]
---
> [[07-finops-basics|◀ FinOps]] · [[HOME|🏠 Home]] · [[STUDY_PLAN|Plan (M6.6)]] · [[PROGRESS|Tracker]] · [[CERTS-MOC|Certs ▶]]

# 08 · Kubernetes basics (and when *not* to use it)

## In plain English
**Kubernetes (K8s)** is software that **runs and manages lots of containers across many machines**
for you — restarting crashed ones, scaling up under load, and rolling out new versions safely.
It's powerful and complex. For *most* data-science/forecasting work you should reach for the simpler
**ECS/Fargate** first (see [[STUDY_PLAN|Module 4]]) — and only learn K8s because **interviews and
big platforms expect the vocabulary.**

> Analogy: one container is a food truck. Kubernetes is the **operations company** running a fleet of
> trucks — dispatching, replacing broken ones, adding trucks at lunch rush. You don't need a fleet to sell tacos from one truck.

## Why it matters for your career
You probably **won't run K8s yourself** as a data scientist — but ML platforms (Kubeflow, many
company stacks) run on it, and interviewers ask. Goal here: **understand the words and know when it's overkill.**

## Key concepts
- **Why it exists** — to run/heal/scale many containers across many servers automatically.
- **Pod** — the smallest unit: one (or a few) containers that run together.
- **Deployment** — declares "keep N copies of this pod running"; handles rollouts + self-healing.
- **Service** — a stable network address for a set of pods (they come and go).
- **Ingress** — routes outside HTTP traffic to services (the front door).
- **ConfigMap / Secret** — inject config / sensitive values into pods (don't bake secrets into images).
- **Namespace** — a folder to isolate workloads (dev vs prod).
- **Persistent Volume** — storage that survives pod restarts.
- **Autoscaling** — add pods (or nodes) as load rises.
- **kubectl** — the CLI you drive it with; **YAML manifests** describe the desired state.
- **ECS/Fargate vs K8s** — Fargate = simpler, serverless containers, less to manage; **K8s** = max flexibility/portability, much more to operate. **Pick Fargate unless you truly need K8s.**

## Tools
Docker Desktop (built-in Kubernetes) **or** `kind` / `minikube` · `kubectl` · YAML manifests

## Mini lab (full version = [[STUDY_PLAN|STUDY_PLAN Module 6.6]])
1. Turn on a **local** cluster (Docker Desktop K8s, or `kind`/`minikube`) — **free, on your laptop**.
2. Deploy a simple container (e.g. `nginx`) with a **Deployment**.
3. Expose it with a **Service**; reach it locally.
4. **Scale** replicas from 1 → 3; watch pods appear.
5. Read **logs** with `kubectl logs`.
6. Inject a **ConfigMap** and a **Secret**.
7. Write a note: **when would I pick ECS/Fargate over K8s?** (almost always, for your work).

> 💸 Cost/safety: do this **entirely locally** — no cloud, no cost. (Managed K8s like **EKS** costs money and is out of scope for now.)

## ✅ Checkpoint
I can explain **Kubernetes basics** (pod/deployment/service/ingress/config) and clearly say
**when not to use it** (prefer ECS/Fargate for most data/ML workloads).

---
Back to: [[HOME]] · [[START-HERE]] · [[STUDY_PLAN]] · [[PROGRESS]]
