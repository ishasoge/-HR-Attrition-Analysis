import pandas as pd
import sqlite3

# load your data
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')

# create a SQL database file
conn = sqlite3.connect('hr_data.db')

# load dataframe into SQL table
df.to_sql('employees', conn, if_exists='replace', index=False)

print("Data loaded into SQL successfully!")

# now run your first SQL query
query = "SELECT Department, COUNT(*) as Total_Employees FROM employees GROUP BY Department"
result = pd.read_sql_query(query, conn)
print(result)

conn.close()
print("Done!")