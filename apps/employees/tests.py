from datetime import date

from rest_framework import status
from rest_framework.test import APITestCase

from apps.departments.models import Department
from apps.employees.models import Employee


class EmployeeAPITests(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(
            name="Testing Department",
            description="Department created for API tests",
        )

        self.employee = Employee.objects.create(
            employee_code="TEST001",
            first_name="Test",
            last_name="Employee",
            email="test.employee@example.com",
            phone="9876543210",
            date_of_joining=date(2026, 1, 1),
            department=self.department,
        )

        self.list_url = "/api/employees/"

    def test_list_employees_returns_200(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_existing_employee_returns_200(self):
        response = self.client.get(
            f"{self.list_url}{self.employee.pk}/"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["employee_code"], "TEST001")

    def test_unknown_employee_returns_404(self):
        response = self.client.get(f"{self.list_url}999999/")

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_create_employee_with_invalid_email_returns_400(self):
        payload = {
            "employee_code": "TEST002",
            "first_name": "Invalid",
            "last_name": "Email",
            "email": "not-an-email",
            "phone": "9876543211",
            "date_of_joining": "2026-02-01",
            "department": self.department.pk,
        }

        response = self.client.post(
            self.list_url, payload, format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_create_employee_with_valid_data_returns_201(self):
        payload = {
            "employee_code": "TEST003",
            "first_name": "Valid",
            "last_name": "Employee",
            "email": "valid.employee@example.com",
            "phone": "9876543212",
            "date_of_joining": "2026-02-01",
            "department": self.department.pk,
        }

        response = self.client.post(
            self.list_url, payload, format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertTrue(
            Employee.objects.filter(employee_code="TEST003").exists()
        )

    def test_deactivate_employee_returns_inactive_status(self):
        response = self.client.post(
            f"{self.list_url}{self.employee.pk}/deactivate/"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.employee.refresh_from_db()
        self.assertEqual(self.employee.status, "Inactive")

    def test_duplicate_employee_code_returns_400(self):
        payload = {
            "employee_code": "TEST001",
            "first_name": "Duplicate",
            "last_name": "Employee",
            "email": "duplicate@example.com",
            "phone": "9876543211",
            "date_of_joining": "2026-02-01",
            "department": self.department.pk,
        }

        response = self.client.post(
            self.list_url, payload, format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_active_employee_cannot_be_deleted(self):
        response = self.client.delete(
            f"{self.list_url}{self.employee.pk}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertTrue(
            Employee.objects.filter(pk=self.employee.pk).exists()
        )
