---
tags: [mlops, hands-on, cloud-only, setup, sagemaker]
aliases: [Cloud Workspace, SageMaker Studio Setup, MLOps Setup]
---
> [[mlops/README|◀ MLOps track]] · [[HOME|🏠 Home]] · [[projects/SETUP-personal-aws|Personal AWS setup]] · [[mlops/labs/L1-experiment-tracking/README|L1 ▶]]

# 00 · Cloud workspace setup (your laptop installs nothing)

This is the **only setup** for the whole MLOps track. Once done, every lab opens in a
browser tab and runs on AWS hardware. Your laptop is just a screen.

## What you're setting up — and what each thing is
| Thing | Plain English | Why |
|---|---|---|
| **SageMaker Studio** | A full ML IDE (JupyterLab) that runs **in AWS**, in your browser | Where you write + run all lab notebooks. Code & data live in the cloud, not on disk. |
| **Studio domain** | The "account" that owns your Studio (user profiles, storage, permissions) | One-time creation; everything attaches to it. |
| **Execution role** | An IAM role Studio *uses on your behalf* to call S3, training, endpoints | So your notebooks can create cloud resources without pasting keys. |
| **AWS CloudShell** | A Linux terminal **in the browser**, pre-loaded with AWS CLI | For quick `aws ...` commands without PowerShell. |
| **An S3 bucket** | Cloud disk for datasets + model artifacts | Every lab reads/writes here. |

## ⚠️ Before you start — personal account only
Do this on your **personal `learn` account**, never the company one. Confirm in CloudShell:
```bash
aws sts get-caller-identity --query Account --output text   # must be YOUR personal account id
```
(See [[projects/SETUP-personal-aws]] if you haven't created it yet.)

## ☁️ Steps (all in the AWS Console — nothing local)

### 1 — Open SageMaker Studio (the cloud IDE)
1. AWS Console → search **SageMaker** → **Studio** (left nav).
2. First time: **Set up for single user (Quick setup)**. AWS creates a **domain** + an
   **execution role** automatically (~5 min). Region: **`ap-south-1`** (match your other labs).
3. When status = *Ready*, click **Open Studio**. You're now in JupyterLab — **running on a
   cloud instance**, not your machine.

### 2 — Create your MLOps bucket (in CloudShell)
Open **CloudShell** (terminal icon, top bar of the Console) and run:
```bash
# Unique bucket name; S3 names are global
ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
export MLOPS_BUCKET="mlops-learn-${ACCOUNT}-ap-south-1"
aws s3 mb "s3://${MLOPS_BUCKET}" --region ap-south-1
echo "Your MLOps bucket: ${MLOPS_BUCKET}"
```
Write that bucket name down — every lab uses it.

### 3 — Sanity-check from inside Studio (your first cloud notebook)
In Studio: **File → New → Notebook** → kernel **Python 3 (ipykernel)**. Run:
```python
import sagemaker, boto3
sess = sagemaker.Session()
print("Region :", sess.boto_region_name)
print("Role   :", sagemaker.get_execution_role())   # the execution role Studio uses
print("Default bucket:", sess.default_bucket())      # SageMaker's auto bucket (also fine to use)
```
If this prints a role ARN and a region, **your cloud workbench is live.** No keys, no installs.

> 💡 `sagemaker.get_execution_role()` only works *inside* Studio — it reads the role Studio
> is running as. That's the cloud-only magic: identity comes from the environment, not a file.

## 💸 Shut it down when you stop (do this every day)
Studio keeps a **kernel instance running** (and billing) until you stop it:
- Left sidebar → **Running Terminals and Kernels** (the ⏻ icon) → **Shut Down** all apps.
- This does **not** delete your work — notebooks persist in the domain's cloud storage.
- You are **not** billed for a stopped Studio; you *are* billed for running kernels + any live endpoints.

## ✅ Done when
- [ ] SageMaker Studio opens and shows JupyterLab.
- [ ] CloudShell confirms you're on the **personal** account.
- [ ] Your `mlops-learn-...` S3 bucket exists.
- [ ] The sanity-check notebook printed a role ARN + region.
- [ ] You know where the **Shut Down** button is.

## 🔁 Azure ML equivalent (for later, when you do Azure certs)
Studio ≈ **Azure ML Studio** + a **compute instance**; execution role ≈ a **managed identity**;
S3 ≈ **Blob Storage**; CloudShell ≈ **Azure Cloud Shell**. Same shape, different names.

---
Next: [[mlops/labs/L1-experiment-tracking/README|L1 · Experiment tracking ▶]] · Back: [[mlops/README]]
