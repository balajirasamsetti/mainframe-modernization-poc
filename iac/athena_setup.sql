-- Run this in the AWS Athena Console on Day 4
    CREATE EXTERNAL TABLE IF NOT EXISTS customer_master (
      CUSTOMER_ID STRING,
      LAST_NAME STRING,
      FIRST_NAME STRING,
      ACCOUNT_BALANCE DOUBLE
    )
    STORED AS PARQUET
    LOCATION 's3://REPLACE_WITH_YOUR_BUCKET_NAME/';
    ```

---

### Day 3 Deliverables Check
*   [x] `main.tf` created with S3 and IAM logic.
*   [x] Infrastructure deployed via `terraform apply`.
*   [x] S3 bucket is active and versioning is enabled.
*   [x] SQL schema prepared for the "Modernized" data.
