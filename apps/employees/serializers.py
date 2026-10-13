 
from rest_framework import serializers

from .models import Employee
from . import services
from apps.departments.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name", "status"]
        read_only_fields = ["id", "name", "status"]


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all()
    )

    department_details = DepartmentSerializer(
        source="department",
        read_only=True
    )

    class Meta:
        model = Employee
        fields = [
            "id",
            "employee_code",
            "first_name",
            "last_name",
            "email",
            "phone",
            "date_of_joining",
            "status",
            "department",
            "department_details",
        ]
        read_only_fields = ["id", "department_details"]

    def validate_employee_code(self, value):
        value = value.strip().upper()

        if not value:
            raise serializers.ValidationError(
                "Employee code cannot be empty."
            )

        existing = Employee.objects.filter(
            employee_code__iexact=value
        )

        if self.instance:
            existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
            raise serializers.ValidationError(
                "An employee with this employee code already exists."
            )

        return value

    def validate_first_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "First name cannot be empty."
            )

        return value

    def validate_last_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Last name cannot be empty."
            )

        return value

    def validate_email(self, value):
        value = value.strip().lower()

        if not value:
            raise serializers.ValidationError(
                "Email cannot be empty."
            )

        existing = Employee.objects.filter(email__iexact=value)

        if self.instance:
            existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
            raise serializers.ValidationError(
                "An employee with this email already exists."
            )

        return value

    def validate_phone(self, value):
        value = value.strip()

        if value and not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain digits only."
            )

        return value

    def validate_department(self, department):
        if department.status != "Active":
            raise serializers.ValidationError(
                "Employees can only be assigned to active departments."
            )

        return department

    def create(self, validated_data):
        return services.create_employee(validated_data)

    def update(self, instance, validated_data):
        return services.update_employee(instance, validated_data)
