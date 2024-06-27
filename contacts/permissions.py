from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
    """
    To only allow superusers to access the view.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser