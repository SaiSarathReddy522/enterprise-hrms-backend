
from django.urls import path

from .views import (
    EmployeeListCreateAPIView,
    EmployeeDetailAPIView,
    EmployeeDeactivateAPIView,
)

urlpatterns = [
    path(
        "",
        EmployeeListCreateAPIView.as_view(),
        name="employee-api-list-create",
    ),
    path(
        "<int:pk>/deactivate/",
        EmployeeDeactivateAPIView.as_view(),
        name="employee-api-deactivate",
    ),
    path(
        "<int:pk>/",
        EmployeeDetailAPIView.as_view(),
        name="employee-api-detail",
    ),
]