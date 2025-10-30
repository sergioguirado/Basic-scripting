# clean_merge_csvs.py
import pandas as pd
import os
from glob import glob

# Step 1: Define the input folder
input_folder = "data"
output_file = "output/merged_cleaned.csv"

# Step 2: Create output folder if it doesn’t exist
os.makedirs("output", exist_ok=True)

# Step 3: Find all CSV files in the folder
csv_files = glob(os.path.join(input_folder, "*.csv"))

# Step 4: Read and clean each file
cleaned_dfs = []

for file in csv_files:
    print(f"Processing {file}")
    df = pd.read_csv(file)
    # Clean data: remove nulls
    df = df.dropna()
    # Normalize column values
    df["product"] = df["product"].str.strip().str.lower()
    # Convert price to float
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    # Re-clean in case price conversion created new nulls
    df = df.dropna()
    cleaned_dfs.append(df)

# Step 5: Merge all cleaned data
merged_df = pd.concat(cleaned_dfs, ignore_index=True)

# Step 6: Save final output
merged_df.to_csv(output_file, index=False)

print(f"Merged file saved as: {output_file}")
