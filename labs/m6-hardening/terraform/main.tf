# main.tf — declare the forecast backend as code. `apply` builds it, `destroy` wipes it.
# This is the reproducibility win: your whole cloud backend in version-controllable files.
#
#   terraform init      # download the AWS provider
#   terraform plan      # preview what will change (read this every time!)
#   terraform apply      # create the resources
#   terraform destroy    # delete them all (do this when not in use)

terraform {
  required_version = ">= 1.5"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" {
  region = var.region
}

# --- S3 bucket for jobs/progress/results ---
resource "aws_s3_bucket" "forecast" {
  bucket = var.bucket_name
  tags   = { project = "forecast" }
}

# Block all public access (security baseline)
resource "aws_s3_bucket_public_access_block" "forecast" {
  bucket                  = aws_s3_bucket.forecast.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# --- ECR repo for the forecast-engine image ---
resource "aws_ecr_repository" "engine" {
  name         = "forecast-engine"
  force_delete = true # lets `destroy` remove it even if images remain (lab convenience)
  tags         = { project = "forecast" }
}

# --- IAM role the Fargate task assumes (task role: what the CONTAINER may do) ---
data "aws_iam_policy_document" "task_assume" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "task_role" {
  name               = "forecast-task-role"
  assume_role_policy = data.aws_iam_policy_document.task_assume.json
  tags               = { project = "forecast" }
}

# Least privilege: the task may read/write ONLY this bucket.
data "aws_iam_policy_document" "task_perms" {
  statement {
    actions   = ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"]
    resources = ["${aws_s3_bucket.forecast.arn}/*"]
  }
  statement {
    actions   = ["s3:ListBucket"]
    resources = [aws_s3_bucket.forecast.arn]
  }
}

resource "aws_iam_role_policy" "task_perms" {
  name   = "forecast-task-s3"
  role   = aws_iam_role.task_role.id
  policy = data.aws_iam_policy_document.task_perms.json
}
