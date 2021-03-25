from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from iot.models import MeetingRoomAccess, CoworkingAccess
from iot.serializers import MeetingRoomAccessSerializer, CoworkingAccessSerializer


class MeetingRoomAccessViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoomAccess.objects.all()
    serializer_class = MeetingRoomAccessSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user is not None:
            return self.queryset.filter(user_id=user)
        return self.queryset


class CoworkingAccessViewSet(viewsets.ModelViewSet):
    queryset = CoworkingAccess.objects.all()
    serializer_class = CoworkingAccessSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user is not None:
            return self.queryset.filter(user_id=user)
        return self.queryset
