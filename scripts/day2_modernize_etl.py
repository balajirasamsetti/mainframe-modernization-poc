import pandas as pd
import os

# 1. Define the offsets based on our Day 1 Copybook
# ID: 8, LNAME: 15, FNAME: 15, BAL: 10
FIELD_WIDTHS = [8, 15, 15, 10]
COL_NAMES = ['CUSTOMER_ID', 'LAST_NAME', 'FIRST_NAME', 'ACCOUNT_BALANCE']

def run_modernization():
    # Use os.path.join for Windows compatibility
    input_path = os.path.join('mainframe', 'CUSTOMER_EXTRACT.txt')
    output_path = os.path.join('scripts', 'modernized_customers.parquet')

    print(f"Reading legacy file: {input_path}...")

    # 2. Read Fixed-Width File (FWF)
    df = pd.read_fwf(input_path, widths=FIELD_WIDTHS, names=COL_NAMES, dtype=str)

    # 3. Data Transformation
    df['LAST_NAME'] = df['LAST_NAME'].str.strip()
    df['FIRST_NAME'] = df['FIRST_NAME'].str.strip()

    # Convert Mainframe implied decimal (0000125050 -> 1250.50)
    df['ACCOUNT_BALANCE'] = df['ACCOUNT_BALANCE'].astype(float) / 100

    # 4. Convert to Parquet
    df.to_parquet(output_path, index=False, compression='snappy')
    
    print(f"SUCCESS: Modernized file created at {output_path}")
    print(df.head())

if __name__ == "__main__":
    # Check for file existence before running
    check_path = os.path.join('mainframe', 'CUSTOMER_EXTRACT.txt')
    if os.path.exists(check_path):
        run_modernization()
    else:
        print(f"ERROR: {check_path} not found. Run Day 1 script first.")