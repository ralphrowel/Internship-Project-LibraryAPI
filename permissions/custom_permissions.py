from rest_framework.permissions import BasePermission
from .roles import LIBRARIAN, ADMIN

class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == LIBRARIAN

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == ADMIN
