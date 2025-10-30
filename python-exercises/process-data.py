import sys
import pandas as pd
import os

# Receive arguments
input_folder = sys.argv[1]
output_file = sys.argv[2]

print(f"Reading files from {input_folder}...")
print(f"Saving cleaned data to {output_file}...")