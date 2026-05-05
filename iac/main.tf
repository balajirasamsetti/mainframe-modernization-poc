# 1. Provider Configuration
provider "aws" {
  region = "us-east-1" # Change to your preferred region
}

# 2. S3 Bucket for Modernized Data
resource "aws_s3_bucket" "modernized_storage" {
  bucket = "mainframe-migration-poc-data-${random_id.suffix.hex}"
  force_destroy = true 
}

# Generate a unique ID for the bucket name to avoid collisions
resource "random_id" "suffix" {
  byte_length = 4
}

# 3. Enable Versioning (Mainframe mindset: Data Recovery)
resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.modernized_storage.id
  versioning_configuration {
    status = "Enabled"
  }
}

# 4. IAM Policy for Migration (Least Privilege)
resource "aws_iam_policy" "migration_policy" {
  name        = "MainframeToS3UploadPolicy"
  description = "Policy for migrating mainframe extracts to S3"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = ["s3:PutObject", "s3:ListBucket"]
        Effect   = "Allow"
        Resource = [
          "${aws_s3_bucket.modernized_storage.arn}",
          "${aws_s3_bucket.modernized_storage.arn}/*"
        ]
      }
    ]
  })
}

# 5. Output the Bucket Name
output "s3_bucket_name" {
  value = aws_s3_bucket.modernized_storage.id
}