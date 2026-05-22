# Step 1: import pandas — this is the tool that reads data
import pandas as pd                                

# Step 2: load the CSV file into Python
# df means dataframe — think of it as your Excel sheet in Python
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Step 3: how many rows and columns does the data have?
print("Rows and columns:", df.shape)

# Step 4: show the first 5 rows of data
print("\nFirst 5 rows:")
print(df.head())

# Step 5: show all column names
print("\nAll columns:")
print(df.columns.tolist())
# Step 6: how many people LEFT the company vs STAYED?
print("\nAttrition count (Yes = left, No = stayed):")
print(df['Attrition'].value_counts())