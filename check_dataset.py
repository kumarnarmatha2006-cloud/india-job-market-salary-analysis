import pandas as pd
import os

folder_path = os.path.dirname(os.path.abspath(__file__))

print("Project folder:", folder_path)
print("Files available in folder:")

for file in os.listdir(folder_path):
    print(repr(file))

file_path = os.path.join(
    folder_path,
    "India_Job_Market_Salary_Trends_2026_CLEAN.xlsx"
)

if os.path.exists(file_path):
    df = pd.read_excel(file_path)

    print("\nDataset loaded successfully!")
    print("Dataset Shape:", df.shape)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nColumn Names:")
    print(df.columns.tolist())

else:
    print("\nDataset file not found. Check the filename above.")
