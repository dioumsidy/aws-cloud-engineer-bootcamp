terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "terraform_lab" {
  bucket = var.bucket_name

  tags = {
    Name        = "Terraform Lab"
    Environment = "Learning"
    Team        = "Cloud Engineering"
  }
}