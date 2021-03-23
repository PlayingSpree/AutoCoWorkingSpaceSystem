from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from meetingroom.models import MeetingRoomBooking, MeetingRoom
from meetingroom.permissions import get_permissions_multi
from meetingroom.serializers import MeetingRoomBookingReadSerializer, MeetingRoomBookingCreateSerializer
from payment.models import Payment


class MeetingRoomBookingViewSet(viewsets.ModelViewSet):
    """ Query Param: future(bool) Only future booking, now(bool) Only now booking"""
    queryset = MeetingRoomBooking.objects.all().order_by('-date_start')
    serializer_class = MeetingRoomBookingCreateSerializer
    permissions = [
        (['create', 'list', 'retrieve'], [IsAuthenticated]),
        (['update', 'partial_update', 'destroy'], [IsAdminUser])
    ]

    def get_permissions(self):
        return get_permissions_multi(self)

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return
        if user.is_staff:
            return self.queryset
        if 'future' in self.request.query_params:
            return self.queryset.filter(user=user, date_end__gte=timezone.now())
        if 'now' in self.request.query_params:
            return self.queryset.filter(user=user, date_start__gte=timezone.now(), date_end__lte=timezone.now())
        return self.queryset.filter(user=user)

    def get_serializer_class(self):
        if self.action == 'create':
            return self.serializer_class
        return MeetingRoomBookingReadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Date
        room_type = serializer.validated_data['room_type']
        date_start = serializer.validated_data['date_start']
        date_end = serializer.validated_data['date_end']
        room = MeetingRoom.objects.filter(type=room_type,
                                          is_active=True).exclude(meetingroombooking__date_end__gt=date_start,
                                                                  meetingroombooking__date_start__lt=date_end,
                                                                  meetingroombooking__is_canceled=False).first()
        if room is None:
            return Response({"room_type": "Not available."}, status=status.HTTP_400_BAD_REQUEST)
        # Payment
        room_type = serializer.validated_data['room_type']
        payment = Payment.pay(serializer.validated_data['card_token'],
                              room_type.price * round((date_end - date_start).seconds / 3600))
        if payment is None:
            return Response({"error": "Cannot make payment."}, status=status.HTTP_402_PAYMENT_REQUIRED)
        # Save
        serializer.save(room=room, payment=payment, user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
