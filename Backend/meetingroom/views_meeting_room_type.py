from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from meetingroom.models import MeetingRoomType
from meetingroom.permissions import get_permissions_multi
from meetingroom.serializers import MeetingRoomTypeSerializer


class MeetingRoomTypeViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoomType.objects.all()
    serializer_class = MeetingRoomTypeSerializer
    permissions = [
        (['list', 'retrieve'], [AllowAny]),
        (['create', 'update', 'partial_update', 'destroy'], [IsAdminUser])
    ]

    def get_permissions(self):
        return get_permissions_multi(self)
