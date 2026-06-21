#!/usr/bin/env bash
# push_to_ecr.sh — push your Docker image (from Module 2) to AWS ECR (private registry).
# ECR is "Docker Hub, but private and inside AWS" — Fargate pulls the image from here.
#
# Prereqs: aws CLI configured, Docker running, image built (forecast-app:0.1).
# Usage:   source ../m3-aws/config.sh && ./push_to_ecr.sh
set -euo pipefail

REPO="forecast-engine"
TAG="0.1"
ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
REGISTRY="${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"

echo "1) Create the ECR repo (ok if it already exists)"
aws ecr create-repository --repository-name "$REPO" --region "$AWS_REGION" 2>/dev/null || true

echo "2) Log Docker into ECR (token is valid 12h)"
aws ecr get-login-password --region "$AWS_REGION" \
  | docker login --username AWS --password-stdin "$REGISTRY"

echo "3) Tag the local image with the ECR URI"
docker tag "forecast-app:${TAG}" "${REGISTRY}/${REPO}:${TAG}"

echo "4) Push"
docker push "${REGISTRY}/${REPO}:${TAG}"

echo
echo "Image URI (put this in ecs_taskdef.json):"
echo "   ${REGISTRY}/${REPO}:${TAG}"
