from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from meetingroom.models import MeetingRoomBooking
from meetingroom.serializers import MeetingRoomBookingSerializer


class MeetingRoomBookingViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoomBooking.objects.all()
    serializer_class = MeetingRoomBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or self.request.method in SAFE_METHODS:
            return MeetingRoomBooking.objects.all()
        return MeetingRoomBooking.objects.filter(user=user)