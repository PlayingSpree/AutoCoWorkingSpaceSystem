from django.utils import timezone
from rest_framework import serializers

from coworkingspace.models import CoworkingSpacePackage, CoworkingSpaceSubscription


class CoworkingSpacePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoworkingSpacePackage
        fields = ['id', 'name', 'detail', 'is_active', 'price', 'duration']
        read_only_fields = ['id']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("price ({}) is less than or equal to 0".format(value))
        return value


class CoworkingSpaceSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoworkingSpaceSubscription
        fields = ['id', 'date_start', 'date_end', 'user', 'package', 'is_canceled', 'date_created', 'date_modified']
        read_only_fields = ['id', 'date_created', 'date_modified']
        extra_kwargs = {'user': {'required': True},
                        'package': {'required': True}}

    def validate_package(self, value):
        if not value.is_active:
            raise serializers.ValidationError("package ({}) is not active".format(value))
        return value

    def validate(self, data):
        if data['date_start'] >= data['date_end']:
            raise serializers.ValidationError(
                "date_end ({}) must occur after date_start ({})".format(data['date_end'], data['date_start']))
        # if data['date_end'] - data['date_start'] > timezone.timedelta(days=data['package'].duration):
        #     raise serializers.ValidationError("duration are longer than package")
        return data
