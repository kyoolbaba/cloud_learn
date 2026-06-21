# Dockerfile — the forecast_engine image that runs on Fargate/EC2/Batch.
# Build:  docker build -t forecast-engine:0.1 .
# Push:   ../m4-serverless/push_to_ecr.sh (retag for ECR)
#
# Swap requirements for your real deps (polars statsforecast mlforecast
# hierarchicalforecast utilsforecast lightgbm) when you drop in the real engine.

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

# deps first (layer caching)
RUN pip install --no-cache-dir boto3 pandas pyarrow

COPY forecast_engine.py .

# No EXPOSE/CMD server — this is a BATCH container: it runs once and exits.
# Fargate/Batch override the command/env at launch (JOB_ID, BUCKET, SHARD).
CMD ["python3", "forecast_engine.py"]
