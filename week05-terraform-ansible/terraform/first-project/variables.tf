variable "aws_region" {
  description = "AWS region for the lab"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "Name of the Terraform lab S3 bucket"
  type        = string
  default     = "sidy-terraform-lab-2026"
}