import pandas as pd
import os

folder_path = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(
    folder_path,
    "India_Job_Market_Salary_Trends_2026_CLEAN.xlsx"
)

df = pd.read_excel(file_path)

print("1. INVALID SALARY RECORDS")
invalid_salary = df[
    (df["salary_min_inr"] <= 0) |
    (df["salary_max_inr"] <= 0) |
    (df["salary_min_inr"] > df["salary_max_inr"])
]
print("Invalid salary records:", len(invalid_salary))
print(invalid_salary.head())

print("\n2. EXPERIENCE VALIDATION")
invalid_exp = df[
    (df["experience_required_years"] < 0) |
    (df["experience_required_years"] > 50)
]
print("Invalid experience records:", len(invalid_exp))

print("\n3. JOB TITLE CHECK")
print("Unique job titles:", df["job_title"].nunique())
print(sorted(df["job_title"].unique()))

print("\n4. COMPANY CHECK")
print("Unique companies:", df["company_name"].nunique())
print("Blank company names:", (df["company_name"].str.strip() == "").sum())

print("\n5. SKILLS CHECK")
print("Blank skills:", (df["skills"].str.strip() == "").sum())
print("Unique skills entries:", df["skills"].nunique())

print("\n6. LOCATION CHECK")
print("Unique locations:", df["location"].nunique())
print("Blank locations:", (df["location"].str.strip() == "").sum())

print("\n7. SALARY VALIDATION COMPLETED")