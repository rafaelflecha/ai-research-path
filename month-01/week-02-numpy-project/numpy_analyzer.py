import numpy as np

employees_data = np.genfromtxt('employees.csv', delimiter=',', dtype=str, encoding='utf-8')

salaries  = employees_data[1:, 3].astype(float)
departments = employees_data[1:, 2]

is_engineering_mask = (departments == 'Engineering')
engineering_salaries = salaries[is_engineering_mask]

print(f"""
--- NumPy Employee Data Analysis ---

Overall Average Salary: ${salaries.mean():.2f}
Maximum Salary: ${salaries.max():.2f}
Minimum Salary: ${salaries.min():.2f}

Average Engineering Salary: ${engineering_salaries.mean():.2f})
""")