import pandas as pd
df = pd.read_csv("/home/sergio_guirado/Basic-scripting/backup/sales.csv")

# Preview data
print(df.head())

# Clean and transform
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Product"] = df["Product"].str.strip().str.lower()

# Filter rows
df = df[df["Price"] > 0]

# Add new column
df["Total"] = df["Price"] * df["Quantity"]
print(df.head())