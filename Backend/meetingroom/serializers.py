from django.utils import timezone
from rest_framework import serializers
from django.utils.dateparse import parse_datetime
from rest_framework.fields import CharField, IntegerField

from meetingroom.models import MeetingRoom, MeetingRoomBooking, MeetingRoomType
from payment.serializers import PaymentSerializer


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

        try:
            start = self.context['request'].query_params.get('start', None)
            end = self.context['request'].query_params.get('end', None)
            if start is not None and end is not None:
                start = parse_datetime(start)
                end = parse_datetime(end)
                if start is not None and end is not None:
                    return
            self.fields.pop('available')
        except KeyError:
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
        return MeetingRoom.objects.filter(type=obj,
                                          is_active=True).exclude(meetingroombooking__date_end__gt=start,
                                                                  meetingroombooking__date_start__lt=end,
                                                                  meetingroombooking__is_canceled=False).count()

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


class MeetingRoomBookingReadSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField(read_only=True)
    room = MeetingRoomSerializer(read_only=True)

    def get_amount(self, obj):
        if obj.payment is None:
            return 0
        return obj.payment.amount

    class Meta:
        model = MeetingRoomBooking
        fields = ['id', 'date_start', 'date_end', 'user', 'room', 'payment', 'amount', 'is_canceled', 'date_created',
                  'date_modified']


class MeetingRoomBookingCreateSerializer(serializers.ModelSerializer):
    card_token = CharField(allow_blank=False, write_only=True)
    room_type = IntegerField(write_only=True)

    class Meta:
        model = MeetingRoomBooking
        fields = ['room_type', 'date_start', 'date_end', 'card_token']
        extra_kwargs = {'room_type': {'required': True},
                        'date_start': {'required': True},
                        'date_end': {'required': True},
                        'card_token': {'required': True}}

    def create(self, validated_data):
        validated_data.pop('card_token', None)
        validated_data.pop('room_type', None)
        return super().create(validated_data)

    def validate_date_start(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("date_start ({}) is in the past".format(value))
        return value

    def validate_date_end(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("date_end ({}) is in the past".format(value))
        return value

    def validate_room_type(self, value):
        query = MeetingRoomType.objects.filter(id=value)
        if query.exists():
            return query.get()
        else:
            raise serializers.ValidationError("room_type ({}) is invalid".format(value))

    def validate(self, data):
        if data['date_start'] >= data['date_end']:
            raise serializers.ValidationError(
                "date_end ({}) must occur after date_start ({})".format(data['date_end'], data['date_start']))
        return data
