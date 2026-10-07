from django.db import models

# Create your models here.
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, default="Active")

    def __str__(self):
        return self.name
