import pandas as pd
import os

def clean_data(file_path):
    # 1. Load the data based on file extension
    ext = os.path.splitext(file_path)[-1].lower()
    
    if ext == '.csv':
        df = pd.read_csv(file_path)
    elif ext in ['.xlsx', '.xls']:
        df = pd.read_excel(file_path)
    elif ext == '.json':
        df = pd.read_json(file_path)
    else:
        print("Unsupported file format.")
        return None

    print(f"Original Shape: {df.shape}")

    # 2. Remove Redundant (Duplicate) Rows
    df = df.drop_duplicates()
    
    # 3. Handle Missing Values
    # Option A: Drop any row with ANY missing value
    df = df.dropna()
    
    # 4. Clean String Data
    # Strip whitespace from column names and string columns
    df.columns = df.columns.str.strip()
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # 5. Reset Index
    df = df.reset_index(drop=True)

    print(f"Cleaned Shape: {df.shape}")
    return df
