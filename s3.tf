resource "aws_s3_bucket" "bucket" {
  bucket = "aws-memorydb-cf-template"
  acl    = "public-read"

  versioning {
    enabled = true
  }

  tags = {
    Name = "bschaatsbergen/aws-memorydb-cf-template"
  }
}
