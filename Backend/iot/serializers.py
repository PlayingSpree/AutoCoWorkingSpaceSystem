import ipaddress

from rest_framework import serializers

from iot.models import MeetingRoomIoT, CoworkingAccess, MeetingRoomAccess


class MeetingRoomIoTSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoomIoT
        fields = ['room', 'iot_ip', 'door_ip']
        extra_kwargs = {'room': {'required': False}}

    def validate_ip(self, value):
        try:
            [ip, port] = value.split(':', 1)
            ip = ipaddress.ip_address(ip)
            port = int(port)
            if not 0 <= port <= 65536:
                raise ValueError
        except ValueError:
            raise serializers.ValidationError('Ip address is invalid: {}'.format(value))
        return '{}:{}'.format(ip, port)

    def validate_iot_ip(self, value):
        return self.validate_ip(value)

    def validate_door_ip(self, value):
        return self.validate_ip(value)


class MeetingRoomIoTUpdateSerializer(serializers.Serializer):
    iot_id = serializers.IntegerField(required=True)
    data = serializers.JSONField(required=True)

    class Meta:
        fields = ['iot_id', 'data']
        extra_kwargs = {'room': {'required': True}}


class DoorSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    type = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_type(self, value):
        if value == 'room' or value == 'space':
            return value
        raise serializers.ValidationError('type is invalid: {}'.format(value))


class CoworkingAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoworkingAccess
        fields = ['user', 'date_access']


class MeetingRoomAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoomAccess
        fields = ['user', 'room', 'date_access']
