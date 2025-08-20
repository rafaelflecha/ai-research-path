import pandas as pd

df = pd.read_csv('employees.csv')

avg_salary_by_dept = df.groupby('department')['salary'].mean()

print(f"""
--- NumPy Employee Data Analysis ---

Overall Average Salary: ${df['salary'].mean():.2f}
Maximum Salary: ${df['salary'].max():.2f}
Minimum Salary: ${df['salary'].min():.2f}

--- Average Salary by Department ---
{avg_salary_by_dept}
""")