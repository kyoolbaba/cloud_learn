---
tags: [project, 01-s3-file-vault]
aliases: [01-s3-file-vault]
---
> [[projects/README|⬅ Projects]] | [[HOME|Home]] | [[PROGRESS|Tracker]]

# Project 01 — S3 file vault  🗄️

**Service:** Amazon S3 · **Time:** 1–2h · **Cost:** free (5GB free tier)

## Goal
Build `s3vault.py` — a personal backup tool that:
- tars a folder and uploads it to S3 with a timestamped key (`backups/2026-06-20T.../`),
- lists your backups with sizes,
- restores a chosen backup back to disk,
- prints a **24-hour shareable link** (presigned URL) for any backup.

## Why (ties to capstone)
S3 is where `job.json`, `progress.json`, and `forecast.parquet` live — the app and
the cloud worker hand data back and forth through it. Presigned URLs are exactly how
the finished forecast gets downloaded to the browser.

## Learn from
`../../labs/m3-aws/s3_lab.py` — has every S3 call you need (upload/list/download/presign).

## Build it
1. First, set up config once:
   ```powershell
   cd ..\..\labs\m3-aws
   copy config.example.sh config.sh    # edit: FORECAST_BUCKET = milan-forecast-lab-<something-unique>
   ```
   (On Windows just set the env var: `$env:FORECAST_BUCKET="milan-forecast-lab-857"`, `$env:AWS_REGION="ap-south-1"`.)
2. Create the bucket: `python s3_lab.py create-bucket`.
3. In a new `projects/01-s3-file-vault/s3vault.py`, write functions using boto3:
   - `backup(folder)` → make a `.tar.gz`, `upload_file` to `backups/<timestamp>.tar.gz`
   - `list_backups()` → `list_objects_v2(Prefix="backups/")`, print key + size + date
   - `restore(key, dest)` → `download_file` then extract
   - `share(key)` → `generate_presigned_url("get_object", ..., ExpiresIn=86400)`
4. Test the full cycle on a throwaway folder.

## ✅ Done when
- [ ] `python s3vault.py backup ./somefolder` uploads a timestamped archive
- [ ] `python s3vault.py list` shows it with size + date
- [ ] `python s3vault.py share <key>` prints a URL that downloads in your browser
- [ ] `python s3vault.py restore <key> ./restored` recreates the folder
- [ ] You can explain bucket vs key vs object, and what a presigned URL is

## 🧹 Teardown
```powershell
aws s3 rm s3://$env:FORECAST_BUCKET/backups/ --recursive   # keep the bucket for later projects
```

## 🚀 Stretch
- Add `--keep N` that deletes all but the newest N backups (lifecycle by hand).
- Then do it the real way: set an S3 **lifecycle rule** to auto-expire `backups/` after 30 days.
