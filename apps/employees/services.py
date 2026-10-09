from django.db import IntegrityError, transaction
from django.db.models import Q
from django.db.models.deletion import ProtectedError
from rest_framework.exceptions import ValidationError

from .models import Employee

ACTIVE = "Active"
INACTIVE = "Inactive"

def create_employee(validated_data):
    validated_data["email"] = validated_data["email"].strip().lower()
    try:
        with transaction.atomic():
            return Employee.objects.create(**validated_data)
    except IntegrityError:
        raise ValidationError(
            "Employee code or email already exists. Please check and retry."
        )

def update_employee(employee, validated_data):
    if (
        employee.status.lower() == INACTIVE.lower()
        and validated_data.get("status", INACTIVE).lower() == ACTIVE.lower()
    ):
        raise ValidationError({
            "status": "An inactive employee cannot be reactivated through the normal update API."
        })

    if "email" in validated_data:
        validated_data["email"] = validated_data["email"].strip().lower()

    if "employee_code" in validated_data:
        duplicate = Employee.objects.filter(
            employee_code=validated_data["employee_code"]
        ).exclude(pk=employee.pk)
        if duplicate.exists():
            raise ValidationError({
                "employee_code": "This employee code already exists."
            })

    if "email" in validated_data:
        duplicate = Employee.objects.filter(
            email__iexact=validated_data["email"]
        ).exclude(pk=employee.pk)
        if duplicate.exists():
            raise ValidationError({
                "email": "This email address already exists."
            })

    try:
        with transaction.atomic():
            for field, value in validated_data.items():
                setattr(employee, field, value)
            employee.save()
            return employee
    except IntegrityError:
        raise ValidationError(
            "Employee code or email already exists. Please check and retry."
        )

def deactivate_employee(employee):
    if employee.status.lower() != INACTIVE.lower():
        employee.status = INACTIVE
        employee.save(update_fields=["status"])
    return employee

def delete_employee(employee):
    if employee.status.lower() == ACTIVE.lower():
        raise ValidationError({
            "detail": "Active employees cannot be deleted. Deactivate the employee first."
        })

    try:
        employee.delete()
    except ProtectedError:
        raise ValidationError({
            "detail": "This employee cannot be deleted because other records depend on it."
        })

def search_employees(query="", active_only=False):
    employees = Employee.objects.select_related("department").all()

    if active_only:
        employees = employees.filter(status__iexact=ACTIVE)

    query = query.strip()
    if query:
        employees = employees.filter(
            Q(employee_code__icontains=query)
            | Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(email__icontains=query)
        )

    return employees.order_by("employee_code")