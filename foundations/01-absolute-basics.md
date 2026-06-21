---
tags: [foundations, beginner]
aliases: [Absolute Basics, Basics From Zero]
---
> [[START-HERE|Start here]] · [[02-terminal-survival|Terminal survival ▶]] · [[03-glossary|Glossary]] · [[HOME|🏠 Home]]

# Absolute basics — from zero

Meet the words. Read once, slowly. Each idea has a **plain meaning**, an **analogy**, and
**why it matters**. You'll see all of these again and again; they'll feel obvious soon.

---

### 1. Code / program
**Plain:** instructions you write for a computer to follow.
**Analogy:** a recipe — steps the computer carries out exactly.
**Why:** everything you'll run (apps, scripts) is code.

### 2. Operating System (OS) — Windows, Linux, macOS
**Plain:** the master software that runs your computer and everything on it.
**Analogy:** the manager of a building — handles power, rooms, who gets in.
**Why:** your laptop is **Windows**. Cloud servers almost always run **Linux**. Same ideas, different commands.

### 3. Server (and client)
**Plain:** a **server** is a computer that stays on and answers requests. A **client** is
whoever asks (your browser, your phone).
**Analogy:** a waiter (server) takes orders from customers (clients) and brings food back.
**Why:** the cloud is full of servers. Your forecasting app *is* a server.

### 4. The cloud
**Plain:** renting computers that live in someone else's data center, over the internet.
**Analogy:** instead of **buying** a car (owning servers), you **rent** one by the hour (cloud).
Done with it? Hand it back, stop paying.
**Why:** this whole journey is learning to rent and drive those computers. AWS = Amazon's rental company.

### 5. Terminal / command line / shell
**Plain:** a text window where you **type commands** to tell the computer what to do.
**Analogy:** texting your computer instead of clicking buttons. More powerful, more precise.
**Why:** cloud work is mostly typed commands. (Full guide: `02-terminal-survival.md`.)

### 6. File, folder (directory), and path
**Plain:** a **file** holds data; a **folder/directory** holds files; a **path** is the address
that says exactly where something is.
**Analogy:** a path like `C:\Users\Milan\report.txt` is a postal address: country → city → street → house.
**Why:** commands need to know *where* things are; you'll give paths constantly.

### 7. Command (its anatomy)
**Plain:** one instruction typed in the terminal, often with extras.
**Example:** `aws s3 ls --region ap-south-1`
- `aws` = the **program** · `s3 ls` = **what to do** (list S3) · `--region ap-south-1` = an
**option/flag** (extra setting).
**Why:** once you can read this pattern (program → action → options), every command makes sense.

### 8. Programming language / Python
**Plain:** a language for writing code. **Python** is a popular, readable one (you already have it).
**Analogy:** human languages express ideas; programming languages express instructions.
**Why:** your forecasting code and the AWS scripts are Python.

### 9. Package / library / `pip` / dependency
**Plain:** a **package** (or library) is pre-written code someone else made that you reuse. **`pip`**
installs Python packages. A **dependency** is a package your code needs.
**Analogy:** LEGO kits — you don't mould plastic, you snap in a ready-made kit. `pip` is the LEGO store.
**Why:** `boto3` (talk to AWS), `fastapi` (web apps) are packages you `pip install`.

### 10. Environment variable
**Plain:** a named setting that lives *outside* your code, which programs read at run time.
**Analogy:** a sticky note on the fridge the program checks ("the bucket name is X").
**Why:** we use `AWS_PROFILE=learn` so tools know which account to use — without editing code.

### 11. API
**Plain:** a defined set of requests one program offers to others. "Ask me these things this way."
**Analogy:** a restaurant **menu** — you order from listed options; the kitchen does the work; you don't go cook.
**Why:** you control AWS through its API; apps talk to each other through APIs.

### 12. JSON
**Plain:** a simple text format for structured data, using `{ }` and `key: value`.
**Analogy:** a labeled form / nested bullet list. `{"name": "milan", "region": "ap-south-1"}`.
**Why:** AWS speaks JSON everywhere — policies, configs, responses.

### 13. HTTP — request & response
**Plain:** the language browsers and servers use. You send a **request**; you get a **response**
(with a status like `200 OK` or `404 Not Found`).
**Analogy:** ordering at a counter — you ask (request), they hand you food or "sold out" (response).
**Why:** web apps, APIs, and your forecasting UI all run on HTTP.

### 14. IP address & port
**Plain:** an **IP** is a computer's address on a network. A **port** is a numbered door on it.
**Analogy:** IP = the building's street address; port = the apartment number inside.
**Why:** `localhost:8011` means "this computer, door 8011." Servers listen on ports.

### 15. Virtual Machine (VM) vs Container
**Plain:** both let you run a computer-inside-a-computer. A **VM** is a whole simulated computer.
A **container** is a lightweight box holding just your app + what it needs.
**Analogy:** VM = renting a whole **house**; container = a **packed lunchbox** that tastes the same
wherever you open it. Containers are smaller and start in seconds.
**Why:** **Docker** makes containers. You'll package your app as a container so it runs identically
on your laptop and in the cloud.

### 16. Deploy
**Plain:** moving your app from "running on my laptop" to "running for real where others can reach it."
**Analogy:** going from cooking at home to opening the dish at a restaurant.
**Why:** the goal is deploying your forecasting work to the cloud.

### 17. CLI & SDK (how you control AWS)
**Plain:** **CLI** = type commands to AWS (`aws ...`). **SDK** = control AWS from inside code
(Python's `boto3`).
**Analogy:** CLI = a TV remote you press by hand; SDK = your code pressing the buttons automatically.
**Why:** you'll use both — CLI for quick actions, boto3 for scripts.

### 18. Version control / Git
**Plain:** a system that saves snapshots of your files so you can track changes and go back.
**Analogy:** **save points** in a video game — mess up, reload the last good save.
**Why:** standard for all code. Not required yet, but you'll meet it.

### 19. Infrastructure as Code (IaC) / Terraform
**Plain:** describing your cloud setup in text files so you can build or destroy it with one command.
**Analogy:** a **blueprint** — rebuild the exact house anytime, or tear it down, instantly.
**Why:** later you'll `terraform apply` to create your whole backend and `destroy` to remove it.

---

**That's the whole vocabulary** the rest of the materials assume. You don't need to memorize it —
just recognize the words. Keep `03-glossary.md` open and look things up whenever. Next:
`02-terminal-survival.md` to actually start typing.
