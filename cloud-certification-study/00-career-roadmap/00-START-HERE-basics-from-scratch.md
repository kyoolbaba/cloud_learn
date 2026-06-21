# 🍼 Cloud From Scratch — Explained Like You're New

You asked to be taught "like a baby, basics from scratch." Here it is. No assumed knowledge. Read top to bottom once.

---

## 1. What is "the cloud," really?

Imagine you want to run a website or train a machine-learning model. You need **computers** (to do the work), **storage** (to keep your files), and **networking** (to connect it all).

You have two choices:
- **Buy your own servers** → expensive, you maintain them, they sit idle at night.
- **Rent computers from a giant company** → pay only for what you use, turn them on/off anytime, someone else fixes the hardware.

**The cloud = renting computers, storage, and software over the internet, on demand.**

The two biggest landlords are:
- **AWS** (Amazon Web Services)
- **Azure** (Microsoft)

(Google Cloud is third. We focus on AWS + Azure.)

---

## 2. The 4 building blocks (these never change)

Everything in any cloud is one of these four:

| Block | What it does | Real-world analogy | AWS example | Azure example |
|---|---|---|---|---|
| **Compute** | Runs your code / does the thinking | The kitchen that cooks | EC2, Lambda | Virtual Machines, Functions |
| **Storage** | Keeps your files & data | The pantry/fridge | S3 | Blob Storage |
| **Networking** | Connects things, controls who can reach what | Roads + locked doors | VPC | Virtual Network (VNet) |
| **Database** | Organized, queryable data | A labeled filing cabinet | RDS, DynamoDB | Azure SQL, Cosmos DB |

If you ever feel lost, ask: *"Is this thing compute, storage, networking, or a database?"* That usually unlocks it.

---

## 3. Words you'll see everywhere (plain English)

| Term | Plain meaning |
|---|---|
| **Region** | A physical part of the world where the cloud has data centers (e.g., "US East", "India West"). You pick one close to your users. |
| **Availability Zone (AZ)** | A separate building inside a region. Using 2+ AZs means if one building loses power, your app survives. |
| **Service** | A specific rentable product (e.g., S3 is a storage service). |
| **Resource** | One thing you actually created (e.g., *your* specific S3 bucket). |
| **Console / Portal** | The website where you click buttons to create things (AWS Console / Azure Portal). |
| **IAM** | "Identity and Access Management" = who is allowed to do what. The security guard. |
| **Scalability** | The ability to handle more work by adding more resources automatically. |
| **High Availability (HA)** | Designed so it keeps working even if a part breaks. |
| **Serverless** | You run code without managing the server. You don't see the computer; you just upload the function. |
| **Pay-as-you-go** | You're billed by usage (per hour, per GB, per request). |

---

## 4. The single most important safety rule 💸

**The cloud charges you for resources that are RUNNING, even if you forget about them.**

A virtual machine left on for a month, or a big database you spun up "just to try," can cost real money.

**Three habits that protect you:**
1. **Set a billing alert** the day you make your account (e.g., "email me if I spend > $5").
2. **Use the free tier** — both clouds give generous free amounts for learning.
3. **Delete everything after each lab.** Every lab in this workspace ends with a *Cleanup* step. Do it.

---

## 5. How a Data Scientist actually uses the cloud

You won't just click buttons randomly. As a DS/analytics person, your typical cloud workflow:

```
Raw data lands in storage   →   You clean/transform it   →   Store the clean version
   (S3 / Blob)                   (Glue / Databricks /          (data lake / warehouse)
                                  Synapse / notebooks)
        ↓
You query it (Athena / Synapse SQL)  →  Train a model (SageMaker / Azure ML)
        ↓
Deploy the model as an API  →  Monitor it  →  (Modern) wrap it with GenAI (Bedrock / Azure OpenAI)
```

The certifications in this workspace teach exactly these pieces. That's why your recommended path covers: **cloud basics → data → AI/ML → architecture → GenAI → security**.

---

## 6. AWS vs Azure — do I learn both?

Short answer for you: **learn the concepts once, then map them to both.**

- The *ideas* (compute, storage, IAM, networking, data pipelines) are ~90% the same.
- Only the *names and buttons* differ.
- Knowing both makes your resume stand out and protects you against "this company uses Azure" surprises.

The file `03-shared-cloud-concepts/` exists for exactly this — learn a concept once, see both clouds side by side.

---

## 7. How certifications work (the exam itself)

- They're **multiple-choice** (single answer + "choose 2/3" questions).
- Taken **online (proctored from home)** or at a test center.
- **Foundational** exams (CLF-C02, AZ-900) are beginner-friendly, mostly conceptual.
- **Associate** exams expect you to have built things (hence the labs).
- **Professional / Expert / Specialty** are advanced; do them later.
- You **don't** memorize commands. You learn *what each service is for* and *when to choose it*.

**Passing strategy that works:**
1. Learn concepts (these notes).
2. Do hands-on labs (so it sticks).
3. Drill flashcards (recall).
4. Take mock exams until you consistently score **80%+**.
5. Do the last-3-days revision checklist.
6. Book and take it.

---

## 8. Your very first 3 actions (do today)

1. ☐ Read `recommended-path-for-data-scientist.md` and pick **Path C**.
2. ☐ Create an AWS free account **and** set a billing alarm (this is Lab 1 of Cloud Practitioner).
3. ☐ Open `01-aws/foundational/aws-cloud-practitioner-CLF-C02.md` and start Week 1.

That's it. You now know enough vocabulary to begin. Everything else is explained inside each cert file as you reach it.

> 🔗 Related: [[recommended-path-for-data-scientist]] · [[aws-vs-azure-decision-guide]] · shared concepts in `03-shared-cloud-concepts/`
