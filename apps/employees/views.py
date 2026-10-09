
from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer
from . import services


# HTML Views

def employee_home(request):
    return render(request, "employees/home.html")


def employee_list(request):
    employees = Employee.objects.all()
    return render(
        request,
        "employees/list.html",
        {"employees": employees},
    )


def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(
        request,
        "employees/detail.html",
        {"employee": employee},
    )


# Employee API: list, search, create

class EmployeeListCreateAPIView(APIView):

    def get(self, request):
        query = request.query_params.get("search", "")
        active_only = (
            request.query_params.get("active_only", "").lower() == "true"
        )

        employees = services.search_employees(
            query=query,
            active_only=active_only,
        )
        serializer = EmployeeSerializer(employees, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

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


# Employee API: retrieve, update, delete

class EmployeeDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Employee, pk=pk)

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)

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
        services.delete_employee(employee)
        return Response(status=status.HTTP_204_NO_CONTENT)


# Employee API: deactivate

class EmployeeDeactivateAPIView(APIView):

    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee = services.deactivate_employee(employee)
        return Response(
            EmployeeSerializer(employee).data,
            status=status.HTTP_200_OK,
        )