from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
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
        ]
        read_only_fields = ["id"]

    def validate_email(self, value):
        return value.lower()