"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls
"""

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),

    # Existing HTML pages
    path("employees/", include("apps.employees.urls")),
    path("departments/", include("apps.departments.urls")),

    # Day 4 - REST API
    path("api/employees/", include("apps.employees.api_urls")),
]