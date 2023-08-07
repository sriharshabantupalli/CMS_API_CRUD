from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['update', 'destroy']:
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user