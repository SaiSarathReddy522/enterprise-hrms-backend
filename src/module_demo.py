from employees.employee_service import create_employee
from payroll.payroll_service import calculate_salary
from departments.department_service import create_department
from utils.helpers import format_name, is_active


employee = create_employee(
    format_name("rahul"),
    "rahul@example.com",
    "IT"
)

department = create_department(
    "IT",
    "Information Technology Department"
)

salary = calculate_salary(
    30000,
    5000,
    3000,
    1000
)

print("Employee:")
print(employee)

print("\nDepartment:")
print(department)

print("\nSalary:")
print(salary)

print("\nEmployee Active:", is_active("Active"))