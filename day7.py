import pandas as pd
import matplotlib.pyplot as plt

# load final data
df = pd.read_csv('hr_final.csv')

# CHART 1 — Risk Score Distribution
plt.figure(figsize=(8,5))
df['RiskScore'].value_counts().sort_index().plot(kind='bar', color='red')
plt.title('How Many Employees at Each Risk Level')
plt.xlabel('Risk Score')
plt.ylabel('Number of Employees')
plt.savefig('chart_riskscore.png')
plt.show()
print("Chart 1 done!")

# CHART 2 — Risk Score by Department
plt.figure(figsize=(8,5))
dept_risk = df.groupby('Department')['RiskScore'].mean().round(2)
dept_risk.plot(kind='bar', color=['blue','orange','red'])
plt.title('Average Risk Score by Department')
plt.xlabel('Department')
plt.ylabel('Average Risk Score')
plt.savefig('chart_dept_risk.png')
plt.show()
print("Chart 2 done!")

# CHART 3 — Salary vs Risk Score
plt.figure(figsize=(8,5))
plt.scatter(df['MonthlyIncome'], df['RiskScore'], 
            alpha=0.5, color='purple')
plt.title('Salary vs Risk Score')
plt.xlabel('Monthly Income')
plt.ylabel('Risk Score')
plt.savefig('chart_salary_risk.png')
plt.show()
print("Chart 3 done!")

print("\nDay 7 Done! 3 charts saved!")