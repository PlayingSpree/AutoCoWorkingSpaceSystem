import requests
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from iot_room.models import MeetingRoomIoT
from iot_room.serializers import MeetingRoomIoTUpdateSerializer


class IoTRoomViewSet(viewsets.ViewSet):
    queryset = MeetingRoomIoT.objects.all()
    serializer_class = MeetingRoomIoTUpdateSerializer

    # permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        iot = get_object_or_404(MeetingRoomIoT.objects.filter(pk=pk))
        try:
            r = requests.get('http://{}/'.format(iot.ip))
            if r.status_code == 200:
                return Response(r.json())
            else:
                return Response(status=r.status_code)
        except:
            return Response(status=status.HTTP_502_BAD_GATEWAY)

    def update(self, request, pk=None):
        iot = get_object_or_404(MeetingRoomIoT.objects.filter(pk=pk))
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data['data'])
        try:
            r = requests.put('http://{}/{}/'.format(iot.ip,serializer.data['iot_id']), json=serializer.data['data'])
            if r.status_code == 200:
                return Response(r.json())
            else:
                return Response(r.text,status=r.status_code)
        except:
            return Response(status=status.HTTP_502_BAD_GATEWAY)
