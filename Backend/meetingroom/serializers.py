from rest_framework import serializers

from meetingroom.models import MeetingRoom, MeetingRoomBooking


class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = ['id', 'name', 'description', 'cover', 'active', 'price']
        read_only_fields = ['id']


class MeetingRoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoomBooking
        fields = ['id', 'date_start', 'date_end', 'user', 'room', 'is_canceled', 'date_created', 'date_modified']
        read_only_fields = ['id', 'date_created', 'date_modified']

