import csv

def load_employees(file_path):
    data_list = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_list.append(row)
    return data_list

def calculate_average_salary(employees):
    salary_total = 0
    for employee in employees:
        salary_total += int(employee['salary'])
    average_salary = salary_total / len(employees)
    return average_salary

def find_employees_in_department(employees, department):
    employees_in_department = []
    for employee in employees:
        if employee['department'] == department:
            employees_in_department.append(employee['name'])
    return employees_in_department

def find_highest_paid_employee(employees):
    highest_salary_employee = max(employees, key=lambda x: int(x['salary']))
    return highest_salary_employee

if __name__ == "__main__":
    file_path = 'employees.csv'
    employees = load_employees(file_path)
    highest_salary_employee = find_highest_paid_employee(employees)

    print(f"""
--- Employee Data Analysis Report ---
      
Average Salary: ${calculate_average_salary(employees):.2f}

Employees in Marketing: \n-{'\n-'.join(find_employees_in_department(employees, 'Marketing'))}

Highest Paid Employee:
Name: {highest_salary_employee['name']}, Department: {highest_salary_employee['department']}, Salary: ${highest_salary_employee['salary']}

------------------------------------
    """)