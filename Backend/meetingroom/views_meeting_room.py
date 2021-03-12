from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from meetingroom.models import MeetingRoom
from meetingroom.permissions import get_permissions_multi
from meetingroom.serializers import MeetingRoomSerializer


class MeetingRoomViewSet(viewsets.ModelViewSet):
    """
    query_params: start, end = Start/End DateTime
    """
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    permissions = [
        (['list', 'retrieve'], [IsAuthenticated]),
        (['create', 'update', 'partial_update', 'destroy'], [IsAdminUser])
    ]

    def get_queryset(self):
        queryset = self.queryset.all()
        # Check User
        user = self.request.user
        if not user.is_staff:
            queryset = queryset.filter(is_active=True)
        return queryset

    def get_permissions(self):
        return get_permissions_multi(self)
