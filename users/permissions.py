from rest_framework import permissions

class IsModer(permissions.BasePermission):
    """Проверка пользователя на модератора"""
    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsNotModer(permissions.BasePermission):
    """Проверка, что пользователь не модератор"""
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return not request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):
    """Проверка пользователя на автора"""
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False

