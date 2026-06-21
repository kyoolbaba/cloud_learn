---
tags: [foundations, beginner, glossary, reference]
aliases: [Glossary, Cloud Glossary, Jargon Buster]
---
> [[02-terminal-survival|◀ Terminal survival]] · [[START-HERE|Start here]] · [[HOME|🏠 Home]]

# 03 · Glossary (plain-English jargon buster)

Keep this open in a tab. Every term gets a **one-line meaning + an everyday analogy**, and the
**AWS / Azure** name where it's a cloud service. Skim now; return whenever a word stumps you.

> ⭐ The one idea under everything: **the cloud is just other people's computers you rent by the minute.**

## The absolute basics
- **Server** — a computer that runs all the time to *serve* things to other computers. *Analogy:* a restaurant kitchen taking orders. (AWS **EC2** / Azure **VM** rent you one.)
- **Client** — the computer asking for something (your laptop, a browser). *Kitchen's customer.*
- **OS (Operating System)** — the software that runs a computer (Windows, macOS, **Linux**). *The building the kitchen lives in.*
- **Linux** — the free OS that runs almost all servers/cloud. Worth learning because the cloud *is* Linux. (See [[01-absolute-basics]].)
- **Terminal / Shell / CLI** — typing commands instead of clicking. *Texting your computer.* (See [[02-terminal-survival]].)
- **GUI** — the click-and-point interface (windows, buttons). Opposite of CLI.

## Talking over the network
- **Network** — computers connected so they can talk. *Roads between buildings.*
- **IP address** — a computer's address on the network, e.g. `10.0.0.5`. *A street address.*
- **Port** — a numbered "door" on a computer for a specific service: `22` SSH, `80` HTTP, `443` HTTPS, `8011` your app. *Apartment numbers at one address.*
- **DNS** — turns a name (`google.com`) into an IP. *The phone book / contacts app.* (AWS **Route 53**.)
- **HTTP / HTTPS** — the language browsers and APIs speak. **HTTPS** is the encrypted (padlock) version. *Sending a postcard (HTTP) vs a sealed letter (HTTPS).*
- **TLS / SSL** — the encryption that makes HTTPS sealed. *The envelope + tamper seal.*
- **API** — a defined way for programs to ask each other for things. *A restaurant menu: you order from set options, you don't go into the kitchen.*
- **SSH** — secure way to log into a remote computer's terminal. *A locked remote-control door to a server.*
- **Firewall / Security Group** — rules for which ports/traffic are allowed. *A bouncer checking who gets in.* (AWS **Security Group**.)
- **Public vs private IP** — public = reachable from the internet; private = only inside your network.

## Packaging & running software
- **Process** — a running program. *A chef currently cooking one dish.*
- **Environment variable** — a setting passed to programs, e.g. `AWS_PROFILE`. *A sticky note the program reads.* <a id="PATH"></a>
- **PATH** — the list of folders the shell searches for commands. If a tool "isn't recognized," it's not on the PATH. *The kitchen's list of where to find ingredients.*
- **Package manager** — installs software for you: `apt` (Ubuntu), `pip` (Python), `npm` (Node). *An app store for code.*
- **Container** — a program packed with everything it needs to run, identically anywhere. *A shipping container: same box works on any ship/truck.* (AWS **ECS/Fargate**.)
- **Image** — the frozen blueprint a container starts from. *A cookie cutter; the container is the cookie.*
- **Docker** — the tool that builds and runs containers. (Module 2.)
- **VM (Virtual Machine)** — a whole simulated computer running on a bigger one. *A guest apartment inside a building.* (AWS **EC2** / Azure **VM**.)
- **Serverless** — you run code without managing any server; the cloud handles it. *Vending machine vs hiring a chef.* (AWS **Lambda** / Azure **Functions**.)

## Cloud core (AWS terms you'll meet first)
- **Region** — a geographic cluster of AWS data centers (e.g. `ap-south-1` Mumbai). *A city where the cloud has warehouses.*
- **Availability Zone (AZ)** — an isolated data center within a Region. *Separate warehouses in that city, so one fire doesn't take all.*
- **IAM** — who can do what in your account (users, roles, permissions). *Office keycards.* (Azure: **Entra ID + RBAC**.)
- **S3** — cloud file storage (infinite hard drive); files = "objects" in "buckets." (Azure **Blob Storage**.)
- **Bucket** — a top-level S3 container for files.
- **EC2** — a rented virtual computer (server) in the cloud. (Azure **Virtual Machines**.)
- **VPC** — your own private network inside AWS. *Your fenced-off plot of land.* (Azure **VNet**.)
- **Lambda** — run a small function on demand, no server to manage. (Azure **Functions**.)
- **CloudWatch** — metrics, logs, and alarms (is it healthy? alert me). (Azure **Monitor**.)
- **Budget / Billing alarm** — emails you when spend crosses a limit. **Set this on day one.** (Azure **Cost Management**.)
- **CLI / SDK** — `aws` command-line tool / **boto3** (the Python library) to drive AWS from code.

## Building & versioning
- **IaC (Infrastructure as Code)** — define your cloud setup in files you can re-run. *A recipe instead of cooking from memory.* (**Terraform**, CloudFormation.)
- **Terraform** — popular IaC tool that works across clouds.
- **Git** — tracks versions of your files; **repository (repo)** = a tracked project. *Save-points + undo history for code.*
- **JSON / YAML** — text formats for config/data that humans and programs both read. *Fill-in-the-blanks forms.*
- **Environment (dev/test/prod)** — separate copies of a system: **prod** = the real one customers use (don't experiment there — this is why your `learn` AWS profile exists, see [[projects/SETUP-personal-aws]]).

## Machine-learning words (for your cert lane)
- **Model** — a program that *learned* patterns from data instead of being hand-coded.
- **Training vs Inference** — training = the model learns from data (slow, once); inference = using it to predict (fast, in production). (See [[domain-1-data-preparation|MLA-C01 D1]].)
- **Feature** — an input column the model learns from (e.g. last month's sales, day-of-week).
- **Supervised / Unsupervised** — learning from labeled answers vs finding structure in unlabeled data.
- **Foundation Model / LLM** — a huge pre-trained model you reuse (e.g. Claude); LLM = the text kind. (AWS **Bedrock**; see [[domain-2-generative-ai-fundamentals|AIF-C01 D2]].)
- **RAG** — feed a model your documents so it answers from *your* data, not just its training.
- **SageMaker** — AWS's build-train-deploy ML platform (your bullseye, [[MLA-C01]]).

## Where to go next
Confused by a word *not* here? Ask me — then I'll add it. Otherwise back to [[START-HERE]] or
jump into a cert at [[CERTS-MOC]].
