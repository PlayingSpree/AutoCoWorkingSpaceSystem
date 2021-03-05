from django.utils import timezone
from rest_framework import serializers
from django.utils.dateparse import parse_datetime

from meetingroom.models import MeetingRoom, MeetingRoomBooking, MeetingRoomType


class MeetingRoomSerializer(serializers.ModelSerializer):
    available = serializers.SerializerMethodField(read_only=True)

    def get_available(self, obj):
        start = self.context['request'].query_params.get('start', None)
        end = self.context['request'].query_params.get('end', None)
        return MeetingRoomBooking.is_available(start, end, obj)

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("price ({}) is less than or equal to 0".format(value))
        return value

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        start = self.context['request'].query_params.get('start', None)
        end = self.context['request'].query_params.get('end', None)
        if start is not None and end is not None:
            start = parse_datetime(start)
            end = parse_datetime(end)
            if start is not None and end is not None:
                return
        self.fields.pop('available')

    class Meta:
        model = MeetingRoom
        fields = ['id', 'name', 'detail', 'is_active', 'available']
        read_only_fields = ['id']


class MeetingRoomTypeSerializer(serializers.ModelSerializer):
    available = serializers.SerializerMethodField(read_only=True)

    def get_available(self, obj):
        start = self.context['request'].query_params.get('start', None)
        end = self.context['request'].query_params.get('end', None)
        return MeetingRoomBooking.objects.filter(date_end__gt=start, date_start__lt=end, room__type=obj,
                                                 is_canceled=False).count()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        start = self.context['request'].query_params.get('start', None)
        end = self.context['request'].query_params.get('end', None)
        if start is not None and end is not None:
            start = parse_datetime(start)
            end = parse_datetime(end)
            if start is not None and end is not None:
                return
        self.fields.pop('available')

    class Meta:
        model = MeetingRoomType
        fields = ['id', 'name', 'detail', 'price', 'available']
        read_only_fields = ['id']


class MeetingRoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoomBooking
        fields = ['id', 'date_start', 'date_end', 'user', 'room', 'is_canceled', 'date_created', 'date_modified']
        read_only_fields = ['id', 'date_created', 'date_modified']
        extra_kwargs = {'user': {'required': True},
                        'room': {'required': True}}

    def validate_date_start(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("date_start ({}) is in the past".format(value))
        return value

    def validate_date_end(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("date_end ({}) is in the past".format(value))
        return value

    def validate_room(self, value):
        if not value.is_active:
            raise serializers.ValidationError("room ({}) is not active".format(value))
        return value

    def validate(self, data):
        if data['date_start'] >= data['date_end']:
            raise serializers.ValidationError(
                "date_end ({}) must occur after date_start ({})".format(data['date_end'], data['date_start']))
        return data
