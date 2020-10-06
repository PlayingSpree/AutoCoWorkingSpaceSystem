from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, SAFE_METHODS


def get_permissions_multi(self):
    permission_classes = [IsAdminUser]
    for p in self.permissions:
        if self.action in p[0]:
            permission_classes = p[1]
            break
    return [permission() for permission in permission_classes]


class AdminAndSelfOrReadOnlyPermission(permissions.BasePermission):
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return bool(
                request.method in SAFE_METHODS or
                request.user and
                request.user.is_authenticated
            )
        else:
            return False
