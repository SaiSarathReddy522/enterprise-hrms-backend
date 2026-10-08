from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer


# Day 2 - HTML Views

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


# Day 4 - DRF Employee API

class EmployeeListCreateAPIView(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            employee = serializer.save()

            return Response(
                EmployeeSerializer(employee).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class EmployeeDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Employee, pk=pk)

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk):
        employee = self.get_object(pk)

        serializer = EmployeeSerializer(
            employee,
            data=request.data,
        )

        if serializer.is_valid():
            employee = serializer.save()

            return Response(
                EmployeeSerializer(employee).data,
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request, pk):
        employee = self.get_object(pk)

        serializer = EmployeeSerializer(
            employee,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            employee = serializer.save()

            return Response(
                EmployeeSerializer(employee).data,
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )