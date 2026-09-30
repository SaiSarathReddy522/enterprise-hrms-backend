employees = {
    101: {
        "name": "Rahul",
        "department": "IT",
        "salary": 50000
    },
    102: {
        "name": "Priya",
        "department": "HR",
        "salary": 45000
    }
}


def create_employee(employee_id, name, department, salary=30000):
    employees[employee_id] = {
        "name": name,
        "department": department,
        "salary": salary
    }

    return f"Employee {name} created successfully."


def get_employee(employee_id):
    return employees.get(employee_id, "Employee not found.")


def update_employee(employee_id, name=None, department=None, salary=None):
    if employee_id not in employees:
        return "Employee not found."

    if name is not None:
        employees[employee_id]["name"] = name

    if department is not None:
        employees[employee_id]["department"] = department

    if salary is not None:
        employees[employee_id]["salary"] = salary

    return "Employee updated successfully."


def delete_employee(employee_id):
    if employee_id not in employees:
        return "Employee not found."

    del employees[employee_id]

    return "Employee deleted successfully."


def calculate_salary(basic_salary, hra=0, allowance=0):
    total_salary = basic_salary + hra + allowance
    return total_salary


def employee_details(*args):
    print("Employee Details:")
    for value in args:
        print(value)


def employee_information(**kwargs):
    print("Employee Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


if __name__ == "__main__":

    print(create_employee(
        103,
        "Anusha",
        "Finance",
        40000
    ))

    print(get_employee(103))

    print(update_employee(
        103,
        salary=45000
    ))

    print(get_employee(103))

    print(calculate_salary(
        basic_salary=40000,
        hra=5000,
        allowance=3000
    ))

    employee_details(
        103,
        "Anusha",
        "Finance",
        45000
    )

    employee_information(
        employee_id=103,
        name="Anusha",
        department="Finance",
        salary=45000
    )

    print(delete_employee(103))

    print(get_employee(103))