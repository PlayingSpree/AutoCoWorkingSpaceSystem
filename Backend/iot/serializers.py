import ipaddress

from rest_framework import serializers

from iot.models import MeetingRoomIoT


class MeetingRoomIoTSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoomIoT
        fields = ['room', 'iot_ip', 'door_ip']
        read_only_fields = ['room']
        extra_kwargs = {'room': {'required': True}}

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
