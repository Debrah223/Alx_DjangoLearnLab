from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission: Only admin users can edit or delete, others can only read.
    """
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:  # Read-only methods
            return True
        return request.user.is_staff  # Only admin users can modify data
