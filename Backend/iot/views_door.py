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
        try:
            r = requests.get('http://{}/'.format(iot.iot_ip))
            if r.status_code == 200:
                return Response(r.json())
            else:
                return Response(status=r.status_code)
        except:
            return Response(status=status.HTTP_502_BAD_GATEWAY)
