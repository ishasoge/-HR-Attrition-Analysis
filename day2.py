# DAY 2 — Exploring the HR Attrition Dataset
# ============================================

# import pandas — same as day 1
import pandas as pd

# load the dataset
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')

# -----------------------------------------------
# SECTION 1: Understand the data shape and columns
# -----------------------------------------------

print("===== SECTION 1: BASIC INFO =====")
print("Total employees in dataset:", len(df))
print("Total columns:", len(df.columns))
print()

# show all column names
print("All column names:")
for col in df.columns:
    print(" -", col)
# SECTION 2: Check for missing values
# -----------------------------------------------

print()
print("===== SECTION 2: MISSING VALUES =====")
missing = df.isnull().sum()
print("Columns with missing values:")
print(missing[missing > 0])
print("Total missing values in entire dataset:", df.isnull().sum().sum())

# -----------------------------------------------
# SECTION 3: Overall attrition count and percentage
# -----------------------------------------------

print()
print("===== SECTION 3: ATTRITION OVERVIEW =====")
attrition_count = df['Attrition'].value_counts()
print("Attrition count:")
print(attrition_count)
print()

total = len(df)
left = df[df['Attrition'] == 'Yes'].shape[0]
stayed = df[df['Attrition'] == 'No'].shape[0]
attrition_pct = round((left / total) * 100, 2)

print(f"Employees who LEFT: {left}")
print(f"Employees who STAYED: {stayed}")
print(f"Attrition Rate: {attrition_pct}%")

# -----------------------------------------------
# SECTION 4: Attrition by Department
# -----------------------------------------------

print()
print("===== SECTION 4: ATTRITION BY DEPARTMENT =====")
dept_attrition = df.groupby('Department')['Attrition'].value_counts().unstack()
dept_attrition['Attrition_Rate_%'] = round(
    dept_attrition['Yes'] / (dept_attrition['Yes'] + dept_attrition['No']) * 100, 2
)
print(dept_attrition)

# -----------------------------------------------
# SECTION 5: Attrition by Job Role
# -----------------------------------------------

print()
print("===== SECTION 5: ATTRITION BY JOB ROLE =====")
role_attrition = df[df['Attrition'] == 'Yes'].groupby('JobRole')['Attrition'].count().sort_values(ascending=False)
print(role_attrition)

# -----------------------------------------------
# SECTION 6: Average salary — people who left vs stayed
# -----------------------------------------------

print()
print("===== SECTION 6: SALARY COMPARISON =====")
salary_compare = df.groupby('Attrition')['MonthlyIncome'].mean().round(2)
print("Average Monthly Income:")
print(salary_compare)

# -----------------------------------------------
# SECTION 7: Does overtime cause attrition?
# -----------------------------------------------

print()
print("===== SECTION 7: OVERTIME vs ATTRITION =====")
overtime = df.groupby(['OverTime', 'Attrition'])['Attrition'].count().unstack()
print(overtime)

# -----------------------------------------------
# SECTION 8: Age analysis
# -----------------------------------------------

print()
print("===== SECTION 8: AGE ANALYSIS =====")
print("Average age of people who LEFT:", df[df['Attrition']=='Yes']['Age'].mean().round(1))
print("Average age of people who STAYED:", df[df['Attrition']=='No']['Age'].mean().round(1))

print()
print("===== DAY 2 COMPLETE =====")