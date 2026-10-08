from django.urls import path

from .views import (
    EmployeeListCreateAPIView,
    EmployeeDetailAPIView,
)


urlpatterns = [
    path(
        "",
        EmployeeListCreateAPIView.as_view(),
        name="employee-api-list-create",
    ),
    path(
        "<int:pk>/",
        EmployeeDetailAPIView.as_view(),
        name="employee-api-detail",
    ),
]