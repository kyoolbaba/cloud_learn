# variables.tf — inputs to the stack. Override at apply time:
#   terraform apply -var bucket_name=milan-forecast-lab -var region=ap-south-1
# or create a terraform.tfvars file (gitignored) with the values.

variable "region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-1"
}

variable "bucket_name" {
  description = "Globally-unique S3 bucket name for jobs/results"
  type        = string
}
