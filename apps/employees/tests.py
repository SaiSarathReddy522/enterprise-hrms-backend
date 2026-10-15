from datetime import date

from django.contrib.auth import get_user_model
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

        User = get_user_model()
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPass123!",
        )
        self.client.force_authenticate(user=self.user)

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
        response = self.client.get(
            f"{self.list_url}999999/"
        )

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

    def test_duplicate_employee_email_returns_400(self):
        payload = {
            "employee_code": "TEST004",
            "first_name": "Duplicate",
            "last_name": "Email",
            "email": "test.employee@example.com",
            "phone": "9876543213",
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

    def test_create_employee_without_first_name_returns_400(self):
        payload = {
            "employee_code": "TEST005",
            "last_name": "MissingFirstName",
            "email": "missing.firstname@example.com",
            "phone": "9876543214",
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
        self.assertIn("first_name", response.data)

    def test_patch_employee_last_name_returns_200(self):
        url = f"{self.list_url}{self.employee.pk}/"

        payload = {
            "last_name": "Updated",
        }

        response = self.client.patch(
            url, payload, format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.employee.refresh_from_db()
        self.assertEqual(self.employee.last_name, "Updated")
        self.assertEqual(self.employee.first_name, "Test")

    def test_unauthenticated_user_cannot_list_employees(self):
        self.client.force_authenticate(user=None)

        response = self.client.get(self.list_url)

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ],
        )

    def test_unauthenticated_user_cannot_create_employee(self):
        self.client.force_authenticate(user=None)

        payload = {
            "employee_code": "TEST006",
            "first_name": "Unauthorized",
            "last_name": "User",
            "email": "unauthorized@example.com",
            "phone": "9876543215",
            "date_of_joining": "2026-03-01",
            "department": self.department.pk,
        }

        response = self.client.post(
            self.list_url, payload, format="json"
        )

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ],
        )
        self.assertFalse(
            Employee.objects.filter(
                employee_code="TEST006"
            ).exists()
        )

    def test_unauthenticated_user_cannot_retrieve_employee(self):
        self.client.force_authenticate(user=None)

        response = self.client.get(
            f"{self.list_url}{self.employee.pk}/"
        )

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ],
        )
    
    def test_search_employees_by_name(self):
        response = self.client.get(
            self.list_url,
            {"search": "Test"},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            [item["employee_code"] for item in response.data["results"]],
            ["TEST001"],
        )

    def test_active_only_filter(self):
        self.employee.status = "Inactive"
        self.employee.save(update_fields=["status"])

        response = self.client.get(
            self.list_url,
            {"active_only": "true"},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])

    def test_put_employee_returns_200(self):
        payload = {
            "employee_code": "TEST001",
            "first_name": "Updated",
            "last_name": "Employee",
            "email": "test.employee@example.com",
            "phone": "9876543210",
            "date_of_joining": "2026-01-01",
            "status": "Active",
            "department": self.department.pk,
        }

        response = self.client.put(
            f"{self.list_url}{self.employee.pk}/",
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.first_name, "Updated")

    def test_deactivated_employee_can_be_deleted(self):
        self.client.post(
            f"{self.list_url}{self.employee.pk}/deactivate/"
        )

        response = self.client.delete(
            f"{self.list_url}{self.employee.pk}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Employee.objects.filter(pk=self.employee.pk).exists()
        )
    def test_unauthenticated_user_cannot_update_employee(self):
        self.client.force_authenticate(user=None)
        response = self.client.patch(
            f"{self.list_url}{self.employee.pk}/",
            {"last_name": "Unauthorized"},
            format="json",
        )
        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN],
        )
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.last_name, "Employee")

    def test_unauthenticated_user_cannot_delete_employee(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(
            f"{self.list_url}{self.employee.pk}/"
        )
        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN],
        )
        self.assertTrue(
            Employee.objects.filter(pk=self.employee.pk).exists()
        )

    def test_unauthenticated_user_cannot_deactivate_employee(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(
            f"{self.list_url}{self.employee.pk}/deactivate/"
        )
        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN],
        )
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.status, "Active")
