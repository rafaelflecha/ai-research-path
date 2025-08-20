import numpy as np
import matplotlib.pyplot as plt

employees_data = np.genfromtxt('employees.csv', delimiter=',', dtype=str, encoding='utf-8')

salaries  = employees_data[1:, 3].astype(float)
departments = employees_data[1:, 2]

department_names = np.unique(departments)
avg_salaries = []

for department in department_names:
    mask = (departments == department)
    avg_salaries.append(salaries[mask].mean())

plt.bar(department_names, avg_salaries)
plt.xlabel("Departments")
plt.ylabel("Average Salary")
plt.title("Average Salary by Department")
plt.show()