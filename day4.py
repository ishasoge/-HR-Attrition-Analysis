import pandas as pd
import sqlite3

# connect to the database we created on day 3
conn = sqlite3.connect('hr_data.db')

# SQL QUERY 1 — attrition rate per department
print("===== Q1: Attrition by Department =====")
q1 = """
SELECT Department,
       COUNT(*) as Total,
       SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Left_Company,
       ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as Attrition_Rate
FROM employees
GROUP BY Department
ORDER BY Attrition_Rate DESC
"""
print(pd.read_sql_query(q1, conn))

# SQL QUERY 2 — average salary who left vs stayed
print("\n===== Q2: Avg Salary — Left vs Stayed =====")
q2 = """
SELECT Attrition,
       ROUND(AVG(MonthlyIncome), 2) as Avg_Salary
FROM employees
GROUP BY Attrition
"""
print(pd.read_sql_query(q2, conn))

# SQL QUERY 3 — overtime vs attrition
print("\n===== Q3: Overtime vs Attrition =====")
q3 = """
SELECT OverTime,
       COUNT(*) as Total,
       SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Left_Company
FROM employees
GROUP BY OverTime
"""
print(pd.read_sql_query(q3, conn))

conn.close()
print("\nDay 4 Done!")