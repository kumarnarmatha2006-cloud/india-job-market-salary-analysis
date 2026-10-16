import pandas as pd
import os

# Load dataset
folder_path = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(
    folder_path,
    "India_Job_Market_Salary_Trends_2026_CLEAN.xlsx"
)

df = pd.read_excel(file_path)

# Create average salary column
df["average_salary_inr"] = (
    df["salary_min_inr"] + df["salary_max_inr"]
) / 2

# 1. Average salary by job title
print("\n1. AVERAGE SALARY BY JOB TITLE")

salary_by_job = (
    df.groupby("job_title")["average_salary_inr"]
    .mean()
    .sort_values(ascending=False)
)

print(salary_by_job.round(2))

# 2. Average salary by location
print("\n2. AVERAGE SALARY BY LOCATION")

salary_by_location = (
    df.groupby("location")["average_salary_inr"]
    .mean()
    .sort_values(ascending=False)
)

print(salary_by_location.round(2))

# 3. Average salary by experience
print("\n3. AVERAGE SALARY BY EXPERIENCE")

salary_by_experience = (
    df.groupby("experience_required_years")["average_salary_inr"]
    .mean()
    .sort_index()
)

print(salary_by_experience.round(2))

# 4. Average salary by remote option
print("\n4. AVERAGE SALARY BY REMOTE OPTION")

salary_by_remote = (
    df.groupby("remote_option")["average_salary_inr"]
    .mean()
    .sort_values(ascending=False)
)

print(salary_by_remote.round(2))

# 5. Average salary by employment type
print("\n5. AVERAGE SALARY BY EMPLOYMENT TYPE")

salary_by_employment = (
    df.groupby("employment_type")["average_salary_inr"]
    .mean()
    .sort_values(ascending=False)
)

print(salary_by_employment.round(2))

# 6. Number of jobs by job title
print("\n6. JOB COUNT BY JOB TITLE")

print(df["job_title"].value_counts())

print("\nEDA COMPLETED SUCCESSFULLY!")

# Save EDA results for Power BI

output_folder = os.path.dirname(os.path.abspath(__file__))

# 1. Average salary by job title
salary_by_job.to_csv(
    os.path.join(output_folder, "salary_by_job_title.csv")
)

# 2. Average salary by location
salary_by_location.to_csv(
    os.path.join(output_folder, "salary_by_location.csv")
)

# 3. Average salary by experience
salary_by_experience.to_csv(
    os.path.join(output_folder, "salary_by_experience.csv")
)

# 4. Average salary by remote option
salary_by_remote.to_csv(
    os.path.join(output_folder, "salary_by_remote_option.csv")
)

# 5. Average salary by employment type
salary_by_employment.to_csv(
    os.path.join(output_folder, "salary_by_employment_type.csv")
)

# 6. Job count by job title
df["job_title"].value_counts().to_csv(
    os.path.join(output_folder, "job_count_by_title.csv")
)

print("\nEDA result files saved successfully!")

