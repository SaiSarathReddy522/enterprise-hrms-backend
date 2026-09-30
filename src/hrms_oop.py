class Employee:

    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)


class Department:

    def __init__(self, department_id, name):
        self.department_id = department_id
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_department(self):
        print("Department ID:", self.department_id)
        print("Department:", self.name)

        print("Employees:")

        for employee in self.employees:
            print(
                employee.employee_id,
                employee.name
            )


class Payroll:

    def __init__(self, employee):
        self.employee = employee

    def calculate_salary(self):
        return self.employee.salary

    def generate_payslip(self):
        print("Employee:", self.employee.name)
        print("Salary:", self.calculate_salary())


if __name__ == "__main__":

    employee1 = Employee(
        101,
        "Rahul",
        "IT",
        50000
    )

    employee2 = Employee(
        102,
        "Priya",
        "HR",
        45000
    )

    employee1.display_employee()

    print()

    it_department = Department(
        1,
        "IT"
    )

    it_department.add_employee(employee1)

    it_department.display_department()

    print()

    payroll = Payroll(employee1)

    payroll.generate_payslip()