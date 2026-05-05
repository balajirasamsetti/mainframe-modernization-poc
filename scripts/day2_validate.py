import pandas as pd
import os

def validate():
    file_path = os.path.join('scripts', 'modernized_customers.parquet')
    
    if not os.path.exists(file_path):
        print(f"ERROR: {file_path} not found. Run Day 2 script first.")
        return

    df = pd.read_parquet(file_path)
    print("--- Data Integrity Check ---")
    print(f"Total Records: {len(df)}")
    print(f"Column Types:\n{df.dtypes}")
    
    # Verify a specific value (John Smith's balance from Day 1)
    target = df[df['CUSTOMER_ID'] == '00000001']['ACCOUNT_BALANCE'].values[0]
    
    if target == 1250.50:
        print("Integrity Check Passed: Balance values match legacy source.")
    else:
        print(f"Integrity Check Failed: Expected 1250.50, got {target}")

if __name__ == "__main__":
    validate()