---
tags: [mlops, reference, software-engineering, code-quality, cloud-only]
aliases: [Code Craft, Production-Ready Code, Notebook to Production]
---
> [[mlops/README|◀ MLOps track]] · [[HOME|🏠 Home]] · [[04-git-cicd-basics|Git + CI/CD]] · [[mlops/resources|Resources]]

# 🧰 Code craft — turning notebook code into production code

The [[mlops/labs/L1-experiment-tracking/README|labs]] teach the AWS *services*. This note
teaches the **code-quality layer underneath them** — how to write code that's testable,
reproducible, and safe to deploy. Distilled from **Khuyen Tran's *Production-Ready Data
Science*** ([repo](https://github.com/kyoolbaba/production-ready-data-science-code)) and
mapped to where it bites you in this track.

> The gap it fills: a model that scores 0.95 in a notebook but is one 400-line cell with
> hardcoded paths **cannot be deployed**. Production = the *same* logic as a tested, versioned,
> configurable module. That refactor is exactly what gets tested in [[MLA-C01]] Domain 2.

## The 14 ideas, grouped (and where each lands in your track)
| Theme | Practice | Where it matters here |
|---|---|---|
| **Foundation** | Git workflow, dependency mgmt (`uv` / `pyproject.toml`), modular layout | every lab — Studio notebooks → `src/` modules |
| **Code quality** | clear names, small functions, a little OOP | the `process()` / `train()` helpers you reuse across labs |
| **Testing** | unit tests catch regressions early (`pytest`) | before [[mlops/labs/L7-pipeline-cicd/README\|L7]] — a pipeline runs your code unattended |
| **Config** | externalize settings, no hardcoded values | bucket/region/hyperparams as config, not literals |
| **Logging** | structured logs, not `print()` | [[mlops/labs/L6-model-monitor/README\|L6]] + endpoints — you debug from logs, not a screen |
| **Data** | input **validation** + dataset **versioning** | [[mlops/labs/L2-feature-store/README\|L2]] features, [[mlops/labs/L4-batch-inference/README\|L4]] inputs |
| **Deployment** | CI/CD, packaging, notebooks→production | [[mlops/labs/L7-pipeline-cicd/README\|L7]] + capstone |

## The 6 highest-leverage habits (start with these)

### 1 — Move logic out of the notebook, into a module
The single biggest jump. A notebook is for *exploring*; a `.py` module is for *running*.
```python
# ❌ notebook cell: works once, can't be tested, can't be imported
df = pd.read_csv("s3://my-bucket/data.csv"); df = df.dropna(); model = RandomForest().fit(...)

# ✅ src/features.py: a pure, importable, testable function
def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Drop nulls and de-duplicate. No I/O, no globals — easy to test."""
    return df.dropna().drop_duplicates()
```
Then the notebook just does `from src.features import clean`. **In Studio:** keep a `src/`
folder next to your notebooks — same cloud filesystem, importable from any cell.

### 2 — Config, not hardcoded values
```python
# ✅ config.yaml (one place to change bucket/region/params per environment)
bucket: mlops-learn-123456789012-ap-south-1
region: ap-south-1
train: { num_round: 100, max_depth: 4 }
```
```python
import yaml; CFG = yaml.safe_load(open("config.yaml"))
xgb.set_hyperparameters(**CFG["train"])     # no magic numbers in code
```
This is *the* habit that lets the same code run in dev and prod unchanged.

### 3 — Validate data at the door (cheap insurance)
Bad input is the most common production failure. Catch it before it reaches the model.
```python
import pandera as pa
schema = pa.DataFrameSchema({
    "mean_radius": pa.Column(float, pa.Check.in_range(0, 50)),
    "target":      pa.Column(int,   pa.Check.isin([0, 1])),
})
df = schema.validate(df)   # raises loudly on drift/garbage instead of training on it
```
Pairs directly with [[mlops/labs/L6-model-monitor/README|L6]] — validation is drift detection's
fast-fail cousin.

### 4 — Log, don't print
```python
import logging
log = logging.getLogger(__name__)
log.info("trained model", extra={"accuracy": acc, "n_estimators": n})  # structured, searchable
```
`print()` vanishes; logs land in **CloudWatch** where you actually debug a deployed model.

### 5 — Write one test (then you'll write more)
```python
# tests/test_features.py — runs in CloudShell or Studio terminal: `pytest`
from src.features import clean
def test_clean_drops_nulls():
    import pandas as pd, numpy as np
    out = clean(pd.DataFrame({"a": [1, np.nan, 1]}))
    assert out["a"].isna().sum() == 0 and len(out) == 1   # nulls gone, dupes gone
```
A pipeline ([[mlops/labs/L7-pipeline-cicd/README|L7]]) runs your code with **no human watching** —
tests are what let you trust that.

### 6 — Pin dependencies for reproducibility
```toml
# pyproject.toml — the exact libs, so "works in Studio" == "works in the training job"
[project]
requires-python = ">=3.10"
dependencies = ["scikit-learn==1.5.1", "pandas==2.2.2", "sagemaker>=2.230"]
```
Run `uv pip install -r ...` **inside Studio's terminal** (cloud), never on your laptop. Train/serve
parity starts with identical dependencies.

## ✅ "Production-ready" self-check (run before the capstone)
- [ ] Core logic lives in `src/*.py` functions, not notebook cells.
- [ ] No hardcoded bucket/region/params — they're in `config.yaml`.
- [ ] Inputs are validated (schema check) before training/scoring.
- [ ] Code uses `logging`, not `print`.
- [ ] At least the data-cleaning function has a `pytest` test.
- [ ] Dependencies are pinned in `pyproject.toml`.
- [ ] A pre-commit hook (`ruff` + `black`) formats on commit → [[04-git-cicd-basics]].

## 📚 Links
- Source: https://github.com/kyoolbaba/production-ready-data-science-code (14 chapters, free code)
- awesome-mlops → *Software Engineering* + *MLOps Core* sections ([[mlops/resources]]).

---
Back to: [[mlops/README]] · related: [[04-git-cicd-basics]] · [[foundations/06-mlops-basics]]
