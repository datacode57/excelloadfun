import pandas as pd
import sys
import os

def load_excel_raw_all_tabs(file_path):
    """
    Reads all tabs from an Excel file into a dictionary of pandas DataFrames 
    exactly as they are, without assuming any structure (no headers).
    """
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return None
        
    try:
        # sheet_name=None loads all sheets into a dictionary.
        # header=None ensures the first row is treated as data, not column names.
        # This keeps the unstructured tables exactly as is.
        dfs = pd.read_excel(file_path, sheet_name=None, header=None)
        return dfs
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def main():
    # Put the full path to your Excel file here. 
    # Example for Mac: "/Users/sandeep/Downloads/my_data.xlsx"
    file_path = "/path/to/your/excel_file.xlsx"
    dfs = load_excel_raw_all_tabs(file_path)
    
    if dfs is not None:
        print(f"Successfully loaded '{file_path}'")
        print(f"Found {len(dfs)} tabs: {list(dfs.keys())}\n")
        
        # Iterate over each tab and print its shape and first few rows
        for sheet_name, df in dfs.items():
            print(f"--- Tab: '{sheet_name}' ---")
            print(f"DataFrame shape: {df.shape}")
            print("First 5 rows:")
            print(df.head())
            print("\n")

if __name__ == "__main__":
    main()
