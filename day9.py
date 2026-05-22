import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# load data
df = pd.read_csv('hr_final.csv')

# create PDF report
with PdfPages('HR_Attrition_Report.pdf') as pdf:

    # PAGE 1 — Title Page
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.axis('off')
    ax.text(0.5, 0.7, 'HR Attrition Analysis Report',
            fontsize=28, fontweight='bold',
            ha='center', va='center')
    ax.text(0.5, 0.55, 'IBM HR Dataset — 1,470 Employees',
            fontsize=16, ha='center', color='grey')
    ax.text(0.5, 0.45, 'Tools: Python | SQL | pandas | matplotlib',
            fontsize=14, ha='center', color='grey')
    ax.text(0.5, 0.30, 'Key Finding: 16.12% Attrition Rate',
            fontsize=18, ha='center', color='red',
            fontweight='bold')
    pdf.savefig(fig)
    plt.close()
    print("Page 1 done — Title!")

    # PAGE 2 — Attrition by Department
    fig, ax = plt.subplots(figsize=(10, 6))
    dept = df.groupby('Department')['Attrition'].apply(
        lambda x: round((x=='Yes').sum()/len(x)*100, 2))
    dept.plot(kind='bar', ax=ax, color=['blue','orange','red'])
    ax.set_title('Attrition Rate by Department', fontsize=18)
    ax.set_ylabel('Attrition Rate %')
    ax.set_xlabel('Department')
    for i, v in enumerate(dept):
        ax.text(i, v + 0.3, f'{v}%', ha='center', fontweight='bold')
    pdf.savefig(fig)
    plt.close()
    print("Page 2 done — Department chart!")

    # PAGE 3 — Salary Comparison
    fig, ax = plt.subplots(figsize=(10, 6))
    salary = df.groupby('Attrition')['MonthlyIncome'].mean().round(2)
    salary.plot(kind='bar', ax=ax, color=['green','red'])
    ax.set_title('Average Salary — Left vs Stayed', fontsize=18)
    ax.set_ylabel('Monthly Income')
    ax.set_xlabel('Attrition')
    for i, v in enumerate(salary):
        ax.text(i, v + 50, f'₹{v}', ha='center', fontweight='bold')
    pdf.savefig(fig)
    plt.close()
    print("Page 3 done — Salary chart!")

    # PAGE 4 — Overtime Impact
    fig, ax = plt.subplots(figsize=(10, 6))
    ot = df.groupby('OverTime')['Attrition'].apply(
        lambda x: round((x=='Yes').sum()/len(x)*100, 2))
    ot.plot(kind='bar', ax=ax, color=['blue','red'])
    ax.set_title('Overtime vs Attrition Rate', fontsize=18)
    ax.set_ylabel('Attrition Rate %')
    ax.set_xlabel('Overtime')
    for i, v in enumerate(ot):
        ax.text(i, v + 0.3, f'{v}%', ha='center', fontweight='bold')
    pdf.savefig(fig)
    plt.close()
    print("Page 4 done — Overtime chart!")

    # PAGE 5 — Risk Score
    fig, ax = plt.subplots(figsize=(10, 6))
    df['RiskScore'].value_counts().sort_index().plot(
        kind='bar', ax=ax, color='purple')
    ax.set_title('Employee Risk Score Distribution', fontsize=18)
    ax.set_ylabel('Number of Employees')
    ax.set_xlabel('Risk Score')
    pdf.savefig(fig)
    plt.close()
    print("Page 5 done — Risk score chart!")

    # PAGE 6 — Recommendations
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.axis('off')
    ax.text(0.5, 0.95, 'Business Recommendations',
            fontsize=22, fontweight='bold', ha='center')
    recommendations = [
        "1. Sales dept has 20.6% attrition — conduct stay interviews immediately",
        "2. Salary gap of 30% — review and correct low salary bands",
        "3. Overtime workers 3x more likely to quit — cap overtime hours",
        "4. Employees under 30 leaving fast — create career growth paths",
    ]
    for i, rec in enumerate(recommendations):
        ax.text(0.1, 0.75 - i*0.15, rec,
                fontsize=13, va='center', color='darkblue')
    pdf.savefig(fig)
    plt.close()
    print("Page 6 done — Recommendations!")

print("\nHR_Attrition_Report.pdf saved in your HR-Project folder!")
print("\nDay 9 Done!")