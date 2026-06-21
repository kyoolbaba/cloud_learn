# outputs.tf — values printed after `apply` (and queryable with `terraform output`).
# Wire these into config.sh so the boto3 scripts use the Terraform-created resources.

output "bucket_name" {
  value = aws_s3_bucket.forecast.bucket
}

output "ecr_repository_url" {
  value = aws_ecr_repository.engine.repository_url
}

output "task_role_arn" {
  value = aws_iam_role.task_role.arn
}
