import boto3
import os

# REPLACE this with your actual bucket name from the Terraform output
BUCKET_NAME = "mainframe-migration-poc-data-aadd76b6"
FILE_TO_UPLOAD = "scripts/modernized_customers.parquet"
S3_KEY = "modernized-data/customers.parquet"

def upload_data():
    s3 = boto3.client('s3')

    if not os.path.exists(FILE_TO_UPLOAD):
        print(f"Error: {FILE_TO_UPLOAD} not found. Run Day 2 script first.")
        return

    print(f"Uploading {FILE_TO_UPLOAD} to s3://{BUCKET_NAME}/{S3_KEY}...")

    try:
        s3.upload_file(FILE_TO_UPLOAD, BUCKET_NAME, S3_KEY, 
                       ExtraArgs={'Metadata': {'source-system': 'mainframe', 'format': 'parquet'}})
        print("SUCCESS: Data is now in the AWS Data Lake.")
    except Exception as e:
        print(f"Upload failed: {e}")

if __name__ == "__main__":
    upload_data()