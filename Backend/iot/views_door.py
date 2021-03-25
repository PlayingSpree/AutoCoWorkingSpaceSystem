import requests
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from iot.models import MeetingRoomIoT
from iot.serializers import MeetingRoomIoTUpdateSerializer


class IoTDoorViewSet(viewsets.ViewSet):
    queryset = MeetingRoomIoT.objects.all()
    serializer_class = MeetingRoomIoTUpdateSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        iot = get_object_or_404(MeetingRoomIoT.objects.filter(pk=pk))
