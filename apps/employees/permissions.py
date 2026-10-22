
from rest_framework.permissions import BasePermission, SAFE_METHODS


class EmployeeRolePermission(BasePermission):
    """
    Employee API role permissions.

    Admin: full access.
    HR: create, read and update; no delete.
    Manager: read-only access.
    Employee: read own linked record only.
    """

    def get_roles(self, request):
        """
        Cache role names on the underlying Django request
        so permission checks and views can reuse them.
        """
        django_request = request._request

        roles = getattr(django_request, "_employee_role_names", None)

        if roles is None:
            roles = set(
                request.user.groups.values_list("name", flat=True)
            )
            django_request._employee_role_names = roles

        return roles

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        roles = self.get_roles(request)

        if "Admin" in roles:
            return True

        if "HR" in roles:
            return request.method != "DELETE"

        if "Manager" in roles:
            return request.method in SAFE_METHODS

        if "Employee" in roles:
            return request.method in SAFE_METHODS

        return False

    def has_object_permission(self, request, view, obj):
        roles = self.get_roles(request)

        if "Admin" in roles:
            return True

        if "HR" in roles:
            return request.method != "DELETE"

        if "Manager" in roles:
            return request.method in SAFE_METHODS

        if "Employee" in roles:
            return (
                request.method in SAFE_METHODS
                and obj.user_id == request.user.id
            )

        return False
