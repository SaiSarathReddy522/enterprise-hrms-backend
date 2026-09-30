class InvalidEmployeeIDError(Exception):
    pass


class InvalidSalaryError(Exception):
    pass


class EmployeeNotFoundError(Exception):
    pass


def validate_employee_id(employee_id):
    if not isinstance(employee_id, int) or employee_id <= 0:
        raise InvalidEmployeeIDError(
            "Employee ID must be a positive integer."
        )

    return True


def validate_salary(salary):
    if not isinstance(salary, (int, float)) or salary < 0:
        raise InvalidSalaryError(
            "Salary must be a positive number."
        )

    return True


def find_employee(employee_id, employees):
    validate_employee_id(employee_id)

    if employee_id not in employees:
        raise EmployeeNotFoundError(
            f"Employee {employee_id} not found."
        )

    return employees[employee_id]


def divide_salary(salary, employees_count):
    try:
        result = salary / employees_count

    except ZeroDivisionError:
        raise ZeroDivisionError(
            "Employees count cannot be zero."
        )

    else:
        return result

    finally:
        print("Division operation completed.")


if __name__ == "__main__":

    employees = {
        101: "Rahul",
        102: "Priya"
    }

    # try / except
    try:
        validate_employee_id(-10)

    except InvalidEmployeeIDError as error:
        print("Error:", error)

    # Invalid salary
    try:
        validate_salary(-5000)

    except InvalidSalaryError as error:
        print("Error:", error)

    # Missing employee
    try:
        print(find_employee(999, employees))

    except EmployeeNotFoundError as error:
        print("Error:", error)

    # Invalid input
    try:
        employee_id = int("abc")

    except ValueError:
        print("Error: Employee ID must be a number.")

    # Division by zero
    try:
        print(divide_salary(50000, 0))

    except ZeroDivisionError as error:
        print("Error:", error)