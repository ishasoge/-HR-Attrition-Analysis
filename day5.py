import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# connect to database
conn = sqlite3.connect('hr_data.db')

# CHART 1 — Attrition by Department
q1 = """
SELECT Department,
ROUND(SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2) 
as Attrition_Rate
FROM employees
GROUP BY Department
"""
df1 = pd.read_sql_query(q1, conn)
plt.figure(figsize=(8,5))
plt.bar(df1['Department'], df1['Attrition_Rate'], color=['red','blue','orange'])
plt.title('Attrition Rate by Department')
plt.ylabel('Attrition Rate %')
plt.savefig('chart1_department.png')
plt.show()
print("Chart 1 saved!")

# CHART 2 — Salary: Left vs Stayed
q2 = "SELECT Attrition, ROUND(AVG(MonthlyIncome),2) as Avg_Salary FROM employees GROUP BY Attrition"
df2 = pd.read_sql_query(q2, conn)
plt.figure(figsize=(6,5))
plt.bar(df2['Attrition'], df2['Avg_Salary'], color=['green','red'])
plt.title('Average Salary — Left vs Stayed')
plt.ylabel('Monthly Income')
plt.savefig('chart2_salary.png')
plt.show()
print("Chart 2 saved!")

# CHART 3 — Overtime vs Attrition
q3 = "SELECT OverTime, SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) as Left_Company FROM employees GROUP BY OverTime"
df3 = pd.read_sql_query(q3, conn)
plt.figure(figsize=(6,5))
plt.bar(df3['OverTime'], df3['Left_Company'], color=['blue','red'])
plt.title('Overtime vs People Who Left')
plt.ylabel('Number of Employees')
plt.savefig('chart3_overtime.png')
plt.show()
print("Chart 3 saved!")

conn.close()
print("\nDay 5 Done! 3 charts saved in your HR-Project folder!")