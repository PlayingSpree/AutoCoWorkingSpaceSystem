from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from coworkingspace.models import CoworkingSpaceSubscription
from iot.models import MeetingRoomAccess, CoworkingAccess
from iot.serializers import DoorSerializer
from meetingroom.models import MeetingRoomBooking


class IoTDoorViewSet(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = DoorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        queryset = CoworkingSpaceSubscription.objects.all()
        if serializer.validated_data['type'] == 'room':
            queryset = MeetingRoomBooking.objects.all()
        obj = get_object_or_404(queryset.filter(id=serializer.validated_data['id']))
        if obj.get_qr_key() != serializer.validated_data['password']:
            return Response('{"error":"Invalid input"}', status=status.HTTP_400_BAD_REQUEST)
        if serializer.validated_data['type'] == 'room':
            MeetingRoomAccess.objects.create(room=obj.room, user=obj.user)
        elif serializer.validated_data['type'] == 'space':
            CoworkingAccess.objects.create(user=obj.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
