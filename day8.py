import pandas as pd

# load final data
df = pd.read_csv('hr_final.csv')

# ================================================
# BUSINESS RECOMMENDATIONS — based on findings
# ================================================

print("=" * 60)
print("HR ATTRITION PROJECT — BUSINESS RECOMMENDATIONS")
print("=" * 60)

# RECOMMENDATION 1 — Department
dept = df.groupby('Department')['RiskScore'].mean().round(2)
worst_dept = dept.idxmax()
print(f"""
RECOMMENDATION 1 — DEPARTMENT FOCUS
Highest risk department: {worst_dept}
Average risk score: {dept[worst_dept]}

Action: HR should immediately conduct stay interviews
in {worst_dept} department. Find out what is causing
dissatisfaction before more people resign.
""")

# RECOMMENDATION 2 — Salary
left_salary = df[df['Attrition']=='Yes']['MonthlyIncome'].mean().round(2)
stay_salary = df[df['Attrition']=='No']['MonthlyIncome'].mean().round(2)
gap = round(((stay_salary - left_salary) / stay_salary) * 100, 2)
print(f"""
RECOMMENDATION 2 — SALARY CORRECTION
Average salary of employees who LEFT: {left_salary}
Average salary of employees who STAYED: {stay_salary}
Gap: {gap}%

Action: Review salary bands for employees earning below
{left_salary}. A 15-20% salary correction could
significantly reduce attrition risk.
""")

# RECOMMENDATION 3 — Overtime
ot = df.groupby('OverTime')['Attrition'].apply(
    lambda x: round((x=='Yes').sum()/len(x)*100, 2))
print(f"""
RECOMMENDATION 3 — OVERTIME MANAGEMENT
Attrition rate with overtime: {ot['Yes']}%
Attrition rate without overtime: {ot['No']}%

Action: Cap overtime hours. Hire additional resources
in high overtime departments. Introduce comp-off policy
for overtime workers.
""")

# RECOMMENDATION 4 — Young Employees
young = df[df['Age'] < 30]
young_attrition = round((young['Attrition']=='Yes').sum()/len(young)*100, 2)
print(f"""
RECOMMENDATION 4 — RETAIN YOUNG TALENT
Attrition rate for employees under 30: {young_attrition}%

Action: Create clear career growth paths for young
employees. Mentorship programs. Learning budgets.
Young employees leave when they see no future growth.
""")

print("=" * 60)
print("END OF RECOMMENDATIONS")
print("=" * 60)

# save recommendations to text file
with open('recommendations.txt', 'w') as f:
    f.write("HR ATTRITION — BUSINESS RECOMMENDATIONS\n\n")
    f.write(f"1. Focus on {worst_dept} department — highest risk\n")
    f.write(f"2. Salary gap of {gap}% — review low salary bands\n")
    f.write(f"3. Overtime attrition {ot['Yes']}% vs {ot['No']}% — cap overtime\n")
    f.write(f"4. Under 30 attrition {young_attrition}% — create growth paths\n")

print("\nRecommendations saved as recommendations.txt!")
print("\nDay 8 Done!")