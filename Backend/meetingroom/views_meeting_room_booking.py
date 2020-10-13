from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from meetingroom.models import MeetingRoomBooking
from meetingroom.serializers import MeetingRoomBookingSerializer


class MeetingRoomBookingViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoomBooking.objects.all()
    serializer_class = MeetingRoomBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return MeetingRoomBooking.objects.all()
        return MeetingRoomBooking.objects.filter(user=user)
