from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from meetingroom.models import MeetingRoom
from meetingroom.permissions import get_permissions_multi
from meetingroom.serializers import MeetingRoomSerializer


class MeetingRoomViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    permissions = [
        (['list', 'retrieve'], [IsAuthenticated]),
        (['create', 'update', 'partial_update', 'destroy'], [IsAdminUser])
    ]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return MeetingRoom.objects.all()
        else:
            return MeetingRoom.objects.filter(active=True)

    def get_permissions(self):
        return get_permissions_multi(self)
