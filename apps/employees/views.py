from django.shortcuts import render


employees = [
    {
        "id": 1,
        "name": "Rahul",
        "department": "IT",
        "salary": 30000,
    },
    {
        "id": 2,
        "name": "Priya",
        "department": "HR",
        "salary": 35000,
    },
    {
        "id": 3,
        "name": "Anusha",
        "department": "Finance",
        "salary": 40000,
    },
]


def employee_home(request):
    return render(
        request,
        "employees/list.html",
        {
            "employees": employees,
            "title": "Employee Home",
        },
    )


def employee_list(request):
    return render(
        request,
        "employees/list.html",
        {
            "employees": employees,
            "title": "Employee List",
        },
    )


def employee_detail(request, employee_id):
    employee = next(
        (
            employee
            for employee in employees
            if employee["id"] == employee_id
        ),
        None,
    )

    return render(
        request,
        "employees/detail.html",
        {
            "employee": employee,
        },
    )