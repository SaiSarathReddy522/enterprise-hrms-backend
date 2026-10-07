from django.db import models

# Create your models here.
from django.db import models


class Employee(models.Model):
    employee_code = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_joining = models.DateField()
    status = models.CharField(max_length=20, default="Active")

    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.PROTECT,
        related_name="employees",
    )

    def __str__(self):
        return f"{self.employee_code} - {self.first_name} {self.last_name}"