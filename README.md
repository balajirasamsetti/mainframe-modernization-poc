# Mainframe-to-AWS Data Modernization PoC

## Overview
This Proof-of-Concept (PoC) demonstrates a secure, automated pipeline for migrating legacy Mainframe storage data (VSAM/Fixed-Width) to a modern AWS Data Lake architecture. The project bridges the gap between traditional DFSMS-managed storage and cloud-native analytics.

## Architecture
1.  **Source (Legacy):** Simulated VSAM KSDS 80-byte fixed-width records.
2.  **Transformation (Middleware):** Python ETL engine converting EBCDIC-style flat files to Snappy-compressed Parquet.
3.  **Storage (Cloud):** AWS S3 with versioning and AES-256 encryption.
4.  **Analytics (Modern):** AWS Athena for serverless SQL queries on modernized data.
5.  **IaC:** Terraform for reproducible infrastructure and IAM least-privilege security.

## Repository Structure
- **/mainframe**: Contains legacy artifacts including JCL (`DEFINE_KSDS.jcl`) and simulated raw extracts.
- **/scripts**: Core Python logic for data transformation (`day2_modernize_etl.py`) and AWS integration (`day4_upload_to_s3.py`).
- **/iac**: Infrastructure as Code (Terraform) and Athena DDL setup.
- **README.md**: Architectural overview and execution guide.

## Technical Highlights
- **Storage Optimization:** Leveraged Parquet format to enable predicate pushdown, reducing Athena query costs by ~90% compared to CSV.
- **Data Integrity:** Implemented custom Python logic to handle "Mainframe Implied Decimals" (e.g., converting `0000125050` to `1250.50`).
- **Security:** Infrastructure provisioned with private S3 access and IAM policies restricted to specific bucket ARNs.

## How to Run
1.  **Generate Data:** `python scripts/day1_generate_data.py`
2.  **Transform:** `python scripts/day2_modernize_etl.py`
3.  **Provision Cloud:** `cd iac && terraform apply`
4.  **Migrate:** `python scripts/day4_upload_to_s3.py`
5.  **Query:** Use `iac/athena_setup.sql` in the AWS Athena Console.
