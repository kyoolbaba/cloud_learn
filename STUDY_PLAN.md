---
tags: [moc, study-plan, hands-on]
aliases: [Study Plan, Cloud Study Plan]
---
> [[HOME|🏠 Home]] · [[START-HERE|Start here]] · [[PROGRESS|Tracker]] · [[CERT_ROADMAP|Certs]] · foundations: [[04-git-cicd-basics|Git/CI-CD]] · [[05-lakehouse-basics|Lakehouse]] · [[06-mlops-basics|MLOps]] · [[07-finops-basics|FinOps]] · [[08-kubernetes-basics|K8s]]

# Cloud & Infrastructure Study Plan — From Laptop to Cloud Forecasting

**Owner:** Milan
**Created:** 2026-06-17
**Companion to:** `FORECAST_PLAN.md` (§8 Compute & Cloud Offload). The capstone here builds the actual "Run in cloud" toggle for `db_polars_app.py`.
**Style:** every module = **Learn → Tools → Hands-on Labs → Checkpoint**. Do the labs; reading alone won't stick. "Max practice" is the point.

> You're on Windows 11. The single best setup move: install **WSL2 (Ubuntu)** so you get a real Linux box on your laptop for free. Everything in Module 0–2 runs there.

---

## ⚠️ Golden safety rules (read before touching a cloud account)

1. **Set a budget alarm on day one** — AWS Budgets / Azure Cost Management, e.g. alert at $5 and $20. Do this *before* launching anything.
2. **Stay in the Free Tier.** AWS: `t2.micro`/`t3.micro` EC2, 5 GB S3, 1M Lambda calls/mo. Azure: B1s VM, free Blob tier.
3. **Tear down after every lab.** Stop/terminate EC2, delete Fargate tasks, empty S3 buckets. The #1 cause of surprise bills is *forgotten running resources*.
4. **Never use the root account** for daily work. Enable MFA on root, create an admin IAM user, then an even tighter user for the app. **Never commit access keys to a file or git.**
5. **Tag everything** `project=forecast` so you can find and delete it.
6. **One cloud first.** Learn AWS *or* Azure end-to-end before touching the other; concepts transfer 1:1.

---

## Suggested pace (part-time, ~9–11 weeks @ 6–8 h/week)

| Week | Module |
|---|---|
| 1 | M0 Linux + M1 Networking |
| 2 | M2 Docker + **M2.5 Git + GitHub + CI/CD** |
| 3 | M3 Cloud 101 + AWS core (IAM, S3, EC2, CloudWatch, CLI, boto3) |
| 4 | M4 Serverless & containers (ECR, Fargate, Lambda) |
| 5 | M5 Orchestration & scale (SQS, Step Functions, Batch, SageMaker) |
| 6 | **M5.5 Lakehouse architecture** + **M5.6 MLOps lifecycle** |
| 7 | M6 Production hardening (Terraform, secrets, VPC, monitoring) |
| 8 | **M6.5 Cost Engineering / FinOps** + **M6.6 Kubernetes basics** |
| 9–11 | Capstone — the cloud forecast toggle |

> New `.5`/`.6` modules added 2026-06-21 to round the plan into a full Data/ML/MLOps/DE learning system. Each has a beginner note in `foundations/`.

---

## Module 0 — Linux fundamentals

**Learn:** shell navigation, filesystem layout (`/etc`, `/var`, `/home`), file permissions (`chmod`/`chown`, the `rwx`/octal model), processes & signals, `systemd` services, package managers (`apt`), environment variables & `PATH`, `ssh`/`scp`, `tmux`, `cron`, redirection & pipes (`>`, `>>`, `|`), `grep`/`find`/`sed`/`awk` basics.

**Tools/commands:** `ls cd pwd cat less` · `chmod chown` · `ps top htop kill` · `systemctl journalctl` · `apt` · `ssh scp` · `tmux` · `crontab -e` · `df du free`

**Hands-on labs:**
1. Install **WSL2 Ubuntu** (`wsl --install -d Ubuntu` in PowerShell). Open the Ubuntu shell.
2. Filesystem tour: navigate `/etc /var/log /home`. `cat /etc/os-release`. Read a log with `less /var/log/dpkg.log`.
3. Permissions: create `secret.txt`, `chmod 600` it, create another user, prove they can't read it. Practice octal (`chmod 754`) until you can read `rwxr-xr--` instantly.
4. Processes: run `python3 -m http.server 8000 &` in the background; find it with `ps aux | grep http.server`; kill it; rerun under `nohup` and confirm it survives logout; then do the same inside a `tmux` session and detach/reattach (`Ctrl-b d`, `tmux attach`).
5. Write a bash script `backup.sh` that tars a folder with a timestamped name; make it executable (`chmod +x`); run it.
6. **systemd service:** turn that `http.server` into a service — write `/etc/systemd/system/hello.service`, `systemctl enable --now hello`, check `systemctl status hello` and `journalctl -u hello`.
7. **cron:** schedule a job that appends `$(date)` to `~/heartbeat.log` every minute; watch it tick; remove it.
8. **OverTheWire "Bandit"** (free online game) — play levels 0→15. It teaches shell + ssh + permissions by doing. *This is the best single Linux practice resource.*

**Checkpoint:** From a fresh shell you can SSH to a host, find what's listening, edit a file with `nano`/`vim`, run a script as a background service, and explain `rwxr-x---`.

---

## Module 1 — Networking, ports & protocols

**Learn:** IP addresses (IPv4, CIDR like `10.0.0.0/16`), **ports** (what they are; 22 SSH, 80 HTTP, 443 HTTPS, 8011 your app), **TCP vs UDP**, the client→server request lifecycle, DNS (name → IP), **HTTP/HTTPS** (methods, status codes, headers), **TLS/certificates** (high level), SSH (keys vs passwords), **firewalls / security groups**, public vs private IP, NAT, localhost/`127.0.0.1` vs `0.0.0.0`, reverse proxy, WebSocket/SSE (for live progress later).

**Tools/commands:** `ip addr` · `ss -tlnp` (what's listening) · `curl -v` · `dig`/`nslookup` · `ping` · `traceroute` · `nc` (netcat) · `nmap` · `openssl s_client` · `ssh -L` (tunnels)

**Hands-on labs:**
1. `ip addr` — find your machine's IP. `ss -tlnp` — list listening ports; identify which port `db_polars_app.py` uses (you've run it on 8011/8014/8015).
2. Start `python3 -m http.server 8000`. From another shell: `curl -v http://localhost:8000` — read the full request/response with headers and status line. Note `0.0.0.0` vs `127.0.0.1` binding (only `0.0.0.0` is reachable from other machines).
3. DNS: `dig example.com` and `nslookup example.com` — see name→IP. `dig +trace` to watch resolution hops.
4. `nc -l 9000` in one shell, `nc localhost 9000` in another — type and see raw TCP move bytes. Now `nc -u` for UDP and feel the difference (no connection).
5. `nmap localhost` — see open ports. Understand a firewall = which ports are allowed in/out.
6. **SSH tunnel:** `ssh -L 8080:localhost:8011 user@remote` — forward a remote port to your laptop. (You'll use this to reach a cloud worker's UI.)
7. TLS: `openssl s_client -connect example.com:443` — inspect the certificate chain; understand what HTTPS adds over HTTP.
8. **Reverse proxy:** install nginx in WSL, put it in front of your FastAPI app (proxy `:80` → `:8011`); learn why production never exposes the app port directly.

**Checkpoint:** You can explain, end to end, what happens when you type `https://myapp.com:443` in a browser (DNS → TCP handshake → TLS → HTTP request → response), name 5 common ports, and tell TCP from UDP and a public from a private IP.

---

## Module 2 — Docker (highest-leverage skill here)

**Learn:** images vs containers, layers & caching, `Dockerfile` instructions (`FROM RUN COPY CMD ENTRYPOINT EXPOSE`), tags, registries, volumes (persistent data), port mapping (`-p`), env vars (`-e`), `docker compose`, multi-stage builds, why containers kill "works on my laptop."

**Tools/commands:** `docker build -t name:tag .` · `docker run -p 8011:8011 name` · `docker ps` · `docker logs` · `docker exec -it <id> bash` · `docker images` · `docker compose up`

**Hands-on labs:**
1. Install **Docker Desktop** (WSL2 backend). `docker run hello-world`.
2. `docker run -d -p 8080:80 nginx` — hit `localhost:8080`; `docker logs`, `docker exec -it <id> bash` to poke inside; stop & remove.
3. **Containerize your app (directly useful):** write a `Dockerfile` for `db_polars_app.py` — `FROM python:3.12-slim`, install `fastapi uvicorn polars statsforecast mlforecast hierarchicalforecast utilsforecast lightgbm`, `COPY`, `EXPOSE 8011`, `CMD uvicorn db_polars_app:app --host 0.0.0.0 --port 8011`. Build it. Run it. Open the UI from your browser. **This is the env-parity win that makes cloud safe.**
4. Volumes: run the container mounting `pudbo_store` as a volume (`-v`) so projects persist across restarts.
5. `.dockerignore` — exclude `.venv`, `frozen/`, `*.json` caches; rebuild and watch the image shrink and build faster (layer caching).
6. **compose:** write `docker-compose.yml` for the app; `docker compose up`; learn how multi-container apps wire together.
7. Push the image to **Docker Hub** (free) — `docker tag`, `docker push`. (Later you'll push to AWS ECR instead.)

**Checkpoint:** You can write a Dockerfile from scratch, build & run your forecasting app in a container with the port mapped and data persisted, and explain the image-vs-container and layer-cache concepts.

---

## Module 2.5 — Git + GitHub + CI/CD
> Beginner note: [[04-git-cicd-basics]]

**Learn:** Git basics (repo, commit, history), branches, commits, merge conflicts, pull requests, **GitHub Actions**, CI/CD, unit tests (`pytest`), building a Docker image in a pipeline, pushing the image to **AWS ECR**, and deploying to **ECS/Fargate** from CI/CD.

**Tools:** `git` · GitHub · GitHub Actions · `pytest` · Docker · AWS CLI · ECR · ECS/Fargate

**Hands-on labs:**
1. Create a repo (`git init` + first commits).
2. Make branches and open a pull request.
3. Create and resolve a merge conflict.
4. Add a simple Python test using `pytest`.
5. Create a GitHub Actions workflow that runs the tests.
6. Add a Docker image build step.
7. Push the image to **ECR** (personal `learn` account only — never the company account).
8. Trigger an **ECS/Fargate** deployment from CI/CD.

**Checkpoint:** I can explain and build a basic CI/CD pipeline from a code commit to a container deployment.

---

## Module 3 — Cloud 101 + AWS core

**Learn:** regions & availability zones, the shared-responsibility model, **IAM** (users, groups, roles, policies, least privilege, MFA), **S3** (buckets, objects, keys, presigned URLs), **EC2** (instance types, AMIs, security groups, key pairs, user-data bootstrap, start/stop/terminate), **CloudWatch** (metrics, logs, alarms), **AWS CLI** + **boto3** (the Python SDK), **Budgets**.

**Tools:** AWS Console · `aws` CLI · `boto3`

**Hands-on labs:**
1. Create an AWS account. **Enable MFA on root.** Create an IAM admin user; log in as that user from now on. **Create a Budget with an alarm at $5/$20.**
2. Install AWS CLI; `aws configure` (access key, region e.g. `ap-south-1`); verify `aws sts get-caller-identity`.
3. **S3:** `aws s3 mb s3://yourname-forecast-lab`; `aws s3 cp file.parquet s3://.../`; `aws s3 ls`; generate a presigned URL. Then do the same in **boto3** (`boto3.client('s3').upload_file(...)`, `download_file(...)`).
4. **EC2:** launch a free-tier `t3.micro` (Ubuntu AMI), security group allowing SSH (22) from *your IP only*; SSH in with the key pair; install Python; run a script. **Then STOP it. Then TERMINATE it.** Watch the billing/free-tier usage.
5. **user-data:** relaunch an instance with a user-data bootstrap script that installs Python + your deps automatically on boot. (This is how the cloud worker self-configures.)
6. **IAM policy writing:** craft a least-privilege JSON policy granting only `s3:GetObject/PutObject` on your one bucket + `ec2:StartInstances/StopInstances/DescribeInstances`. Attach to a dedicated `forecast-worker` user. Test that it *can't* do anything else.
7. **CloudWatch:** view EC2 CPU metrics; create an alarm "CPU > 80% for 5 min → notify" (SNS email). Create a billing alarm too.
8. **boto3 orchestration script (mini-capstone):** from your laptop, a Python script that (a) uploads a `job.json` to S3, (b) starts an EC2 instance, (c) the instance (via user-data) downloads the job, runs a dummy "forecast", uploads `result.parquet` + `progress.json`, (d) your script polls `progress.json` until done, (e) downloads the result, (f) stops the instance.

**Checkpoint:** You can stand up and tear down an EC2 box, move data through S3 from both CLI and boto3, write a least-privilege IAM policy, set alarms, and drive a remote run end-to-end from a Python script. **This lab is 80% of the eventual toggle.**

---

## Module 4 — Serverless & containers in the cloud

**Learn:** **ECR** (private container registry), **ECS/Fargate** (run containers without managing servers; task definitions, clusters), **Lambda** (event-driven functions <15 min; for *glue/triggering*, not heavy compute), API Gateway (HTTP → Lambda), S3 event triggers.

**Hands-on labs:**
1. **ECR:** create a repo; authenticate Docker to ECR; `docker tag` + `docker push` your forecasting image (from M2) to ECR.
2. **Fargate:** create an ECS cluster; write a task definition pointing at the ECR image; run a one-off task; read its CloudWatch logs. Pass the `job_id`/bucket as env vars or command overrides.
3. **Lambda:** write a "hello" Lambda; then one (Python + boto3) that **starts your Fargate task** on demand. Give it an IAM execution role with just that permission.
4. **API Gateway → Lambda:** expose an HTTPS endpoint that triggers the Lambda (this is the cloud-side entry the app calls).
5. **S3 trigger:** configure "object created in `jobs/`" → Lambda → launch Fargate task. Now dropping a `job.json` auto-starts compute.

**Checkpoint:** You can package the app as a container in ECR, run it serverlessly on Fargate, and trigger that run from an API call or an S3 upload — no VM to babysit.

---

## Module 5 — Orchestration & scale

**Learn:** **SQS** (decoupled job queue), **Step Functions** (state machines; `Task`, `Wait`, `Choice`, and **`Map`** for parallel fan-out; retries/catch), **AWS Batch** (array jobs across many workers), **SageMaker Processing jobs** (managed run+track+autostop, spot pricing).

**Hands-on labs:**
1. **SQS:** create a queue; boto3 producer puts 100 "shard" messages; a consumer pulls and processes them; learn visibility timeout & dead-letter queues.
2. **Step Functions:** build a state machine — *start Fargate task → Wait 30s → check progress (Choice) → loop until done → aggregate*. Run it; watch the visual execution graph.
3. **Map fan-out:** split SKUs into N shards; Step Functions `Map` runs N Fargate tasks in parallel; a final task concatenates the per-shard parquet files in S3. **This is the "make a 2-hour job take 10 minutes" pattern.**
4. **AWS Batch:** define a job queue + compute environment; submit an array job of N shards; compare effort vs Step Functions+Fargate.
5. **SageMaker Processing:** run your forecast script as a Processing job (input from S3, output to S3); note the built-in logging, autoscaling, and **spot instances** (cheap, interruptible). Good "managed" option.

**Checkpoint:** You can fan a forecast out across many parallel workers and aggregate the results, and you can articulate when Step Functions vs Batch vs SageMaker is the right tool.

---

## Module 5.5 — Lakehouse architecture
> Beginner note: [[05-lakehouse-basics]] · cert: [[DEA-C01]]

**Learn:** data lake vs warehouse vs lakehouse; **S3** as lake storage; **Parquet**; partitioning; compaction; schema evolution; **Delta Lake / Apache Iceberg / Apache Hudi**; **Glue Data Catalog**; **Lake Formation**; **Athena** optimization; **Databricks Unity Catalog**; data lineage; data quality.

**Tools:** S3 · Glue · Athena · Lake Formation · Spark · Databricks · Parquet · Delta/Iceberg/Hudi

**Hands-on labs:**
1. Store the same data as CSV and Parquet in S3.
2. Compare file sizes and query speed.
3. Partition data by year/month.
4. Create a Glue table.
5. Query it using Athena.
6. Simulate schema evolution.
7. Add basic data-quality checks.
8. Write notes comparing Delta, Iceberg, and Hudi.

**Checkpoint:** I can explain lake vs warehouse vs lakehouse and design a basic S3 + Glue + Athena data lake.

---

## Module 5.6 — MLOps lifecycle
> Beginner note: [[06-mlops-basics]] · cert: [[MLA-C01]] 🎯

**Learn:** experiment tracking; feature store; model registry; batch inference; real-time endpoint; model deployment; model monitoring; data drift; model drift; retraining pipeline; approval gates; rollback; CI/CD for ML; **SageMaker Pipelines / Model Registry / Batch Transform / Endpoints / Model Monitor**.

**Tools:** SageMaker · MLflow · GitHub Actions · Docker · ECR · S3 · CloudWatch · Step Functions

**Hands-on labs:**
1. Train a small ML model locally.
2. Track experiment metadata.
3. Save the model artifact to S3.
4. Register a model version.
5. Run batch inference.
6. Deploy a simple endpoint.
7. Log predictions.
8. Create drift-monitoring notes.
9. Build a simple retraining pipeline.

**Checkpoint:** I can explain the full ML lifecycle from data → training → deployment → monitoring → retraining.

---

## Module 6 — Production hardening & Infrastructure as Code

**Learn:** **Terraform** (or AWS CDK) — declare infra as code, `plan`/`apply`/`destroy`; **Secrets Manager / SSM Parameter Store** (no hardcoded creds); **VPC** deeper (subnets, route tables, security groups, public vs private subnets, NAT gateway); structured **logging/monitoring**; cost tagging; auto-stop/TTL.

**Hands-on labs:**
1. **Terraform basics:** `terraform init/plan/apply` to create the S3 bucket + IAM role + ECR repo from code; `terraform destroy` to wipe it. Re-create it in one command — feel the reproducibility.
2. **Terraform the worker stack:** Fargate task definition + IAM + S3 + (optional) Step Functions, all as code. Now your whole compute backend is `apply`/`destroy`-able.
3. **Secrets:** store a dummy API key in SSM Parameter Store / Secrets Manager; read it from boto3 at runtime instead of a file. Remove every plaintext credential.
4. **VPC:** put the worker in a private subnet with a NAT gateway for outbound; security group lets *nothing* in except what's needed. Understand why.
5. **Auto-stop/TTL:** add a CloudWatch alarm or a Lambda on a schedule that kills any forecast instance running >2h (runaway-cost insurance).

**Checkpoint:** `terraform apply` stands up your entire cloud-forecast backend; `terraform destroy` removes it; no secret is ever hardcoded; a runaway job auto-dies.

---

## Module 6.5 — Cost Engineering / FinOps
> Beginner note: [[07-finops-basics]]

**Learn:** AWS Pricing Calculator; Cost Explorer; Budgets; billing alarms; Free Tier traps; **NAT Gateway** cost traps; **CloudWatch Logs** cost traps; **SageMaker endpoint** cost traps; EC2 **stop vs terminate**; unattached EBS volumes; S3 storage classes; Spot instances; Savings Plans basics; tagging strategy.

**Tools:** AWS Budgets · Cost Explorer · Pricing Calculator · CloudWatch · S3 lifecycle rules

**Hands-on labs:**
1. Estimate cost before each lab.
2. Create a budget alarm.
3. Use Cost Explorer.
4. Add tags to resources.
5. Create an S3 lifecycle rule.
6. Identify risky services that can create surprise bills.
7. Create a teardown checklist.

**Checkpoint:** I can estimate, monitor, and control cloud cost before running experiments.

---

## Module 6.6 — Kubernetes basics
> Beginner note: [[08-kubernetes-basics]] — *includes when NOT to use it*

**Learn:** why Kubernetes exists; pods; deployments; services; ingress; config maps; secrets; namespaces; persistent volumes; autoscaling; logs; `kubectl`; when to use **ECS/Fargate vs Kubernetes**.

**Tools:** Docker Desktop Kubernetes (or `kind` / `minikube`) · `kubectl` · YAML manifests

**Hands-on labs:**
1. Run a local Kubernetes cluster.
2. Deploy a simple container.
3. Expose it as a service.
4. Scale replicas.
5. Read logs.
6. Use config maps and secrets.
7. Compare this with ECS/Fargate.

**Checkpoint:** I can explain Kubernetes basics and know when *not* to use it (prefer ECS/Fargate for most data/ML work).

---

## 🏁 Capstone — Build the real "Run in cloud" toggle (ties to FORECAST_PLAN §8 / Phase 6)

Assemble everything into the actual feature:

1. **Container:** the `forecast_engine` image in ECR (M2 + M4).
2. **App side (`db_polars_app.py`):** a "Run in cloud" toggle → `POST /api/ts/run?target=cloud`:
   - upload `job.json` (mapping, models, horizon, CV settings) to S3,
   - trigger the cloud run (Lambda/API Gateway → Fargate, or Step Functions Map for big jobs),
   - return a `job_id`.
3. **Worker:** container runs `forecast_engine.py`, writing `progress.json {done,total,stage,eta}` to S3 every N series, then `forecast.parquet` + `metrics.parquet` on finish, then self-terminates.
4. **Progress UI:** app polls `GET /api/ts/status/{job_id}` (reads `progress.json`) → progress bar + ETA; on completion, download results and `_register()` them as tables (so they flow into charts/export/dashboard).
5. **Guardrails:** least-privilege IAM, budget alarm, hard max-runtime kill switch, "provisioning…" state for cold start.
6. **IaC:** the whole backend defined in Terraform; `destroy` when not in use.

**Done = ** you flip a toggle in the dashboard, watch a live progress bar while thousands of SKUs forecast on cloud hardware, and get the results back as tables — with a backend you can stand up and tear down in one command, and a bill you control.

---

## 🛠️ Mini-project portfolio (one shippable output per domain)

The fastest way to *prove* a skill — to yourself and to a recruiter — is a small thing that **works
and produces an output**. Here is **one mini-project per domain**, each leaving a concrete artifact
(a repo, a screenshot, a Parquet file, a green CI badge) and laddering toward the **capstone**.
Tick them off in [[PROGRESS]] → *Mini-project portfolio*.

> 💸 Everything below runs **locally or on your personal `learn` account** with teardown — **never the company account**. The "completion proof" *is* the deliverable; collect them in the [[portfolio/README|`portfolio/`]] folder (or a public GitHub repo) so you have a portfolio at the end.

### 1. Linux — 🛠️ Worker bootstrap kit
- **What I'll build:** `setup_worker.sh` that installs Python + deps, runs a dummy forecast as a **systemd service**, plus a **cron** heartbeat that appends a timestamp to a log.
- **Tools:** WSL2 Ubuntu · bash · `systemd` · `cron` · `chmod`/`tmux`
- **Skills learned:** shell scripting, file permissions, background services, scheduling
- **Completion proof:** the script committed + a screenshot of `systemctl status` (active) and a few `journalctl -u` log lines.

### 2. Networking — 🛠️ Reverse-proxied forecast API
- **What I'll build:** your FastAPI app behind **nginx** in WSL (proxy `:80 → :8011`), inspected end-to-end with `curl -v`, `ss`, `dig`, `openssl`.
- **Tools:** nginx · `curl` · `ss -tlnp` · `dig` · `openssl s_client` · `ssh -L`
- **Skills learned:** ports, HTTP lifecycle, TLS, reverse proxy, SSH tunnels
- **Completion proof:** saved `curl -v` output + your `nginx.conf` + a short note tracing DNS → TCP → TLS → HTTP.

### 3. Docker — 🛠️ Containerized forecasting app
- **What I'll build:** a `Dockerfile` for `db_polars_app.py`, built and run with port + volume + `.dockerignore`, then pushed to **Docker Hub**.
- **Tools:** Docker · Dockerfile · `docker compose` · Docker Hub
- **Skills learned:** images vs containers, layers/caching, volumes, registries
- **Completion proof:** a **public Docker Hub image URL** + a screenshot of the app UI running from the container.

### 4. Git + CI/CD — 🛠️ Auto-tested forecast repo
- **What I'll build:** a GitHub repo with a `pytest` test and a **GitHub Actions** workflow that runs tests + builds the Docker image on every push. (See [[04-git-cicd-basics]].)
- **Tools:** git · GitHub · GitHub Actions · `pytest` · Docker
- **Skills learned:** branching, pull requests, CI/CD, unit testing
- **Completion proof:** a **green Actions badge** in the repo README + a link to one merged PR.

### 5. AWS Core — 🛠️ Remote run driven from boto3
- **What I'll build:** a boto3 script that uploads `job.json` to S3, starts an **EC2** box (user-data runs a dummy forecast), polls `progress.json`, downloads the result, then stops the instance. (= [[#Module 3 — Cloud 101 + AWS core|M3 mini-capstone]].)
- **Tools:** AWS CLI · boto3 · IAM · S3 · EC2 · CloudWatch
- **Skills learned:** IAM least-privilege, S3 I/O, EC2 lifecycle, orchestration from Python
- **Completion proof:** a downloaded `result.parquet` + the boto3 script committed + the CloudWatch log line.

### 6. S3 Data Lake — 🛠️ Partitioned Parquet sales lake
- **What I'll build:** convert sales CSV → **partitioned Parquet** (`year=/month=/`) in S3, add a lifecycle rule, and measure the size + query-scan savings vs CSV.
- **Tools:** S3 · AWS CLI · polars/pandas · Parquet · S3 lifecycle
- **Skills learned:** object storage, partitioning, columnar formats, lifecycle policies
- **Completion proof:** an S3 listing screenshot + a one-page **CSV-vs-Parquet** size/scan comparison note.

### 7. EC2 Compute — 🛠️ Disposable benchmark box
- **What I'll build:** launch a free-tier `t3.micro`, SSH in, run a forecasting benchmark, record timings, then **stop → terminate**.
- **Tools:** EC2 · security groups · SSH · key pairs
- **Skills learned:** compute lifecycle, security groups (your-IP-only), cost discipline
- **Completion proof:** a `benchmark.md` with results + a console screenshot showing **no running instances** (terminated).

### 8. Lambda / API Gateway — 🛠️ Forecast trigger API
- **What I'll build:** a Python **Lambda** that kicks off a job, fronted by an **API Gateway** HTTPS endpoint that returns a `job_id`.
- **Tools:** Lambda · API Gateway · IAM execution role · boto3
- **Skills learned:** serverless functions, event-driven design, HTTP APIs, least-privilege roles
- **Completion proof:** a saved response from `curl https://<api>/run` returning a real `job_id`.

### 9. ECR / Fargate — 🛠️ Serverless container run
- **What I'll build:** push the Module-2 image to **ECR**, run it as a one-off **Fargate** task with `job_id`/bucket as env vars, and read its CloudWatch logs.
- **Tools:** ECR · ECS/Fargate · task definitions · CloudWatch
- **Skills learned:** container registry, serverless containers, log retrieval
- **Completion proof:** the Fargate task's **CloudWatch log** of a completed run + the output it wrote to S3.

### 10. SQS — 🛠️ Parallel shard queue
- **What I'll build:** a boto3 producer that enqueues N "shard" messages and a consumer that processes them, with a **dead-letter queue** for failures.
- **Tools:** SQS · boto3 · DLQ
- **Skills learned:** decoupling, queues, visibility timeout, dead-letter handling
- **Completion proof:** a run log showing N messages produced/consumed + one poison message landing in the **DLQ**.

### 11. Step Functions — 🛠️ Fan-out & aggregate forecast
- **What I'll build:** a **Step Functions `Map`** state running N Fargate tasks in parallel; a final task concatenates per-shard Parquet in S3 ("2-hour job → 10 minutes").
- **Tools:** Step Functions · Fargate · S3 · `Map` state
- **Skills learned:** orchestration, parallel fan-out, retries/catch, aggregation
- **Completion proof:** a screenshot of the **green execution graph** + the aggregated `forecast.parquet`.

### 12. SageMaker / MLOps — 🛠️ Train → register → batch-score
- **What I'll build:** train a small forecasting model (DeepAR or your own container), **register** it in the Model Registry, and run a **Batch Transform** to score, logging metrics. (See [[06-mlops-basics]], [[MLA-C01]].)
- **Tools:** SageMaker (Training · Model Registry · Batch Transform) · S3 · MLflow (optional)
- **Skills learned:** ML lifecycle, experiment tracking, registry/approval, batch inference
- **Completion proof:** a **registered model version** (screenshot) + `metrics.parquet` + the batch predictions output.

### 13. Lakehouse — 🛠️ Glue + Athena query layer
- **What I'll build:** crawl the S3 Parquet lake into the **Glue Data Catalog**, query it with **Athena**, simulate a schema change, and write a Delta/Iceberg/Hudi comparison. (See [[05-lakehouse-basics]], [[DEA-C01]].)
- **Tools:** Glue · Athena · Lake Formation · Parquet/Iceberg
- **Skills learned:** data catalog, serverless SQL, table formats, governance
- **Completion proof:** an **Athena query result** (CSV export) + your Delta/Iceberg/Hudi comparison note.

### 14. Terraform — 🛠️ One-command forecast backend
- **What I'll build:** Terraform that creates S3 + IAM role + ECR (+ optional Step Functions) and tears it all down — reproducible in one command.
- **Tools:** Terraform · AWS provider
- **Skills learned:** Infrastructure as Code, `plan`/`apply`/`destroy`, reproducibility
- **Completion proof:** `main.tf` committed + saved `terraform plan` output + proof of a clean `destroy` (empty state).

### 15. Security — 🛠️ Least-privilege + encrypted bucket
- **What I'll build:** a least-privilege IAM policy for the `forecast-worker`, an S3 bucket with **Block Public Access + SSE-KMS**, and CloudTrail auditing.
- **Tools:** IAM · KMS · S3 Block Public Access · CloudTrail
- **Skills learned:** least privilege, encryption at rest, audit trails
- **Completion proof:** the **policy JSON** committed + a screenshot proving the worker **can't** do a disallowed action + `get-bucket-encryption` output.

### 16. FinOps — 🛠️ Cost guardrails + teardown kit
- **What I'll build:** a **Budget alarm** ($5/$20), `project=learn` tags everywhere, an S3 lifecycle rule, and a reusable **teardown checklist**. (See [[07-finops-basics]].)
- **Tools:** AWS Budgets · Cost Explorer · Pricing Calculator · S3 lifecycle · tags
- **Skills learned:** cost estimation, monitoring, control, the surprise-bill traps
- **Completion proof:** a screenshot of the **active budget alarm** + a committed `TEARDOWN.md` checklist.

### 17. Kubernetes basics — 🛠️ Local K8s forecast deploy
- **What I'll build:** deploy the forecast container to a **local** cluster (Docker Desktop K8s / `kind` / `minikube`), expose it as a Service, scale to 3 replicas, read logs, use a ConfigMap + Secret. (See [[08-kubernetes-basics]].)
- **Tools:** `kubectl` · kind/minikube · YAML manifests
- **Skills learned:** pods/deployments/services, scaling, config/secrets, *when to prefer Fargate*
- **Completion proof:** `kubectl get pods` showing **3 replicas** + your manifests + an ECS-vs-K8s note. **(100% local — no cloud cost.)**

### 18. Capstone — 🛠️ "Run in cloud" forecast toggle
- **What I'll build:** the real feature — a toggle in `db_polars_app.py` → upload job to S3 → trigger Fargate/Step Functions → poll `progress.json` → register results as tables, all **Terraform-managed**.
- **Tools:** S3 · Fargate · Step Functions · Lambda · Terraform · CloudWatch
- **Skills learned:** end-to-end system integration, the whole stack working as one
- **Completion proof:** a **screen-recording** of flipping the toggle → live progress bar → results appear as tables; then `terraform destroy` cleans up.

---

## AWS ↔ Azure equivalents (so the knowledge transfers)

| Concept | AWS | Azure |
|---|---|---|
| Identity/permissions | IAM | Entra ID + RBAC |
| Object storage | S3 | Blob Storage |
| Virtual machine | EC2 | Virtual Machines |
| Container registry | ECR | ACR |
| Serverless containers | Fargate / ECS | Container Instances / Container Apps |
| Functions | Lambda | Functions |
| Orchestration | Step Functions | Durable Functions |
| Batch/parallel | AWS Batch | Azure Batch |
| Queue | SQS | Service Bus / Storage Queues |
| Managed ML jobs | SageMaker | Azure ML |
| Monitoring/logs | CloudWatch | Monitor |
| Budgets/cost | AWS Budgets | Cost Management |
| Secrets | Secrets Manager / SSM | Key Vault |
| IaC | Terraform / CloudFormation / CDK | Terraform / Bicep / ARM |
| CLI / SDK | `aws` / boto3 | `az` / azure-sdk-for-python |

---

## Resource pointers (search for current links — names are stable)

- **Linux (hands-on):** OverTheWire **Bandit** (game), Linux Journey, MIT "The Missing Semester of Your CS Education".
- **Networking:** Cloudflare Learning Center, Beej's Guide to Network Programming, Julia Evans' networking zines.
- **Docker:** official "Docker — Get Started", Play with Docker (browser sandbox).
- **AWS:** AWS Free Tier, **AWS Skill Builder** (free official courses), **AWS Workshops** (workshops.aws — guided hands-on), freeCodeCamp AWS courses (YouTube). Deeper/paid: Adrian Cantrill, A Cloud Guru.
- **Terraform:** HashiCorp "Terraform Tutorials" (official, free).
- **Time-series (for the forecasting side):** Nixtla docs for statsforecast / mlforecast / hierarchicalforecast / utilsforecast; "Forecasting: Principles and Practice" (Hyndman, free online) for the theory behind ARIMA/ETS/Theta/intermittent demand.
- **Security practice:** TryHackMe (intro networking/Linux rooms).

---

## Master checklist (tick as you go)

**Fundamentals**
- [ ] WSL2 Ubuntu installed; comfortable in bash
- [ ] Permissions (octal + rwx) instant-readable
- [ ] Background processes, nohup, tmux
- [ ] systemd service created; cron job scheduled
- [ ] OverTheWire Bandit 0→15
- [ ] Identify listening ports; explain TCP vs UDP, public vs private IP
- [ ] curl a service and read headers/status; SSH tunnel works
- [ ] TLS cert inspected; nginx reverse proxy in front of the app

**Docker**
- [ ] Containerized `db_polars_app.py` with deps; runs with port mapped + volume
- [ ] `.dockerignore` + layer caching understood
- [ ] Image pushed to a registry

**AWS core**
- [ ] Root MFA + IAM admin user + **budget alarm**
- [ ] S3 via CLI and boto3 (incl. presigned URL)
- [ ] EC2 launch → SSH → run → stop → terminate
- [ ] user-data bootstrap works
- [ ] Least-privilege IAM policy written & tested
- [ ] CloudWatch alarm created
- [ ] boto3 script drives a full remote run (job→start→poll→result→stop)

**Serverless & scale**
- [ ] Image in ECR; runs on Fargate
- [ ] Lambda starts a Fargate task; API Gateway / S3 trigger wired
- [ ] SQS producer/consumer
- [ ] Step Functions Map fan-out + aggregation
- [ ] (opt) AWS Batch array job; SageMaker Processing job

**Hardening**
- [ ] Terraform apply/destroy the backend
- [ ] Secrets in Secrets Manager/SSM (zero hardcoded creds)
- [ ] VPC private subnet + tight security groups
- [ ] Auto-stop / max-runtime kill switch

**Capstone**
- [ ] "Run in cloud" toggle → cloud forecast → live progress bar → results registered as tables
