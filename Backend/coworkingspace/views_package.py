from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from coworkingspace.models import CoworkingSpacePackage
from coworkingspace.serializers import CoworkingSpacePackageSerializer
from meetingroom.permissions import get_permissions_multi


class PackageViewSet(viewsets.ModelViewSet):
    queryset = CoworkingSpacePackage.objects.all()
    serializer_class = CoworkingSpacePackageSerializer
    permissions = [
        (['list', 'retrieve'], [AllowAny]),
        (['create', 'update', 'partial_update', 'destroy'], [IsAdminUser])
    ]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return CoworkingSpacePackage.objects.all()
        else:
            return CoworkingSpacePackage.objects.filter(is_active=True)

    def get_permissions(self):
        return get_permissions_multi(self)
