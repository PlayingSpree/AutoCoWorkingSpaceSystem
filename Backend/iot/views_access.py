from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from iot.models import MeetingRoomAccess, CoworkingAccess
from iot.serializers import MeetingRoomAccessSerializer, CoworkingAccessSerializer


class MeetingRoomAccessViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoomAccess.objects.all()
    serializer_class = MeetingRoomAccessSerializer
    permission_classes = [IsAdminUser]


class CoworkingAccessViewSet(viewsets.ModelViewSet):
    queryset = CoworkingAccess.objects.all()
    serializer_class = CoworkingAccessSerializer
    permission_classes = [IsAdminUser]
