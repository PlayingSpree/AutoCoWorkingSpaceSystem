from datetime import datetime

from rest_framework import serializers

from meetingroom.models import MeetingRoom, MeetingRoomBooking


class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = ['id', 'name', 'description', 'picture', 'active', 'price']
        read_only_fields = ['id']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("price ({}) is less than or equal to 0".format(value))
        return value


class MeetingRoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoomBooking
        fields = ['id', 'date_start', 'date_end', 'user', 'room', 'is_canceled', 'date_created', 'date_modified']
        read_only_fields = ['id', 'date_created', 'date_modified']

    def validate_date_start(self, value):
        if value <= datetime.now():
            raise serializers.ValidationError("date_start ({}) is in the past".format(value))
        return value

    def validate_date_end(self, value):
        if value <= datetime.now():
            raise serializers.ValidationError("date_end ({}) is in the past".format(value))
        return value

    def validate(self, data):
        if data['date_start'] >= data['date_end']:
            raise serializers.ValidationError(
                "date_end ({}) must occur after date_start ({})".format(data['date_end'], data['date_start']))
        return data
