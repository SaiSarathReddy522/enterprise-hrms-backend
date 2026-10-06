from django.shortcuts import render


departments = [
    {
        "id": 1,
        "name": "IT",
        "manager": "Rahul",
    },
    {
        "id": 2,
        "name": "HR",
        "manager": "Priya",
    },
    {
        "id": 3,
        "name": "Finance",
        "manager": "Anusha",
    },
]


def department_list(request):
    return render(
        request,
        "departments/list.html",
        {
            "departments": departments,
        },
    )