import pandas as pd
import sqlite3

conn = sqlite3.connect('hr_data.db')

query = "SELECT * FROM employees"
df = pd.read_sql_query(query, conn)

# RISK SCORE — combining 3 factors
def risk_score(row):
    score = 0
    
    # low salary = high risk
    if row['MonthlyIncome'] < 3000:
        score += 4
    elif row['MonthlyIncome'] < 5000:
        score += 2
        
    # overtime = high risk
    if row['OverTime'] == 'Yes':
        score += 3
        
    # young age = high risk
    if row['Age'] < 30:
        score += 2
    elif row['Age'] < 35:
        score += 1
        
    return score

df['RiskScore'] = df.apply(risk_score, axis=1)

# show top 10 employees most likely to quit
print("===== TOP 10 HIGH RISK EMPLOYEES =====")
top10 = df[['Age','Department','MonthlyIncome','OverTime','Attrition','RiskScore']]\
        .sort_values('RiskScore', ascending=False).head(10)
print(top10)

# save final data for Power BI
df.to_csv('hr_final.csv', index=False)
print("\nFinal data saved as hr_final.csv!")

conn.close()
print("Day 6 Done!")