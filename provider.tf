terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }

  backend "s3" {
    bucket         = "bruno-terraform-state-bucket"
    key            = "global/aws-memorydb-cf-template.tfstate"
    region         = "eu-central-1"
    dynamodb_table = "bruno-terraform-state-table"
  }
}

provider "aws" {
  region = "eu-central-1"
}
