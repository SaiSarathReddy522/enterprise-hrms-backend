def create_employee(name, email, department):
    employee = {
        "name": name,
        "email": email,
        "department": department
    }
    return employee


def get_employee(employee):
    return employee


def update_employee(employee, name=None, email=None, department=None):
    if name:
        employee["name"] = name

    if email:
        employee["email"] = email

    if department:
        employee["department"] = department

    return employee


def delete_employee(employee):
    employee.clear()
    return employee