import pandas as pd

# Load the dataset
file_path = "India_Job_Market_Salary_Trends_2026_CLEAN.xlsx"
df = pd.read_excel(file_path)

# 1. Dataset dimensions
print("1. DATASET DIMENSIONS")
print("Rows and Columns:", df.shape)

# 2. Column data types
print("\n2. DATA TYPES")
print(df.dtypes)

# 3. Missing values
print("\n3. MISSING VALUES")
print(df.isnull().sum())

# 4. Duplicate records
print("\n4. DUPLICATE RECORDS")
print("Total Duplicates:", df.duplicated().sum())
print("Duplicate Job IDs:", df["job_id"].duplicated().sum())

# 5. Statistical summary
print("\n5. STATISTICAL SUMMARY")
print(df.describe())

# 6. Unique values in important columns
print("\n6. UNIQUE JOB TITLES")
print(df["job_title"].value_counts())

print("\n7. EMPLOYMENT TYPE DISTRIBUTION")
print(df["employment_type"].value_counts())

print("\n8. REMOTE OPTION DISTRIBUTION")
print(df["remote_option"].value_counts())

# 9. Salary range
print("\n9. SALARY SUMMARY")
print(df[["salary_min_inr", "salary_max_inr"]].describe())

print("\nInspection completed successfully!")

