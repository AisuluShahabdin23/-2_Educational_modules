from rest_framework.permissions import BasePermission


class IsModeratorPermission(BasePermission):
    def has_permission(self, request, view):
        if 'moderator' in request.user.roles:
            return True
        return False


class IsTeacherPermission(BasePermission):
    def has_permission(self, request, view):
        if 'teacher' in request.user.roles:
            return True
        return False
