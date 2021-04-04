from django.utils import timezone
from rest_framework import serializers
from rest_framework.fields import CharField

from coworkingspace.models import CoworkingSpacePackage, CoworkingSpaceSubscription
from payment.serializers import PaymentSerializer


class CoworkingSpacePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoworkingSpacePackage
        fields = ['id', 'name', 'detail', 'is_active', 'price', 'duration']
        read_only_fields = ['id']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("price ({}) is less than or equal to 0".format(value))
        return value


class CoworkingSpaceSubscriptionReadSerializer(serializers.ModelSerializer):
    package = CoworkingSpacePackageSerializer(read_only=True)

    class Meta:
        model = CoworkingSpaceSubscription
        fields = ['id', 'user', 'package', 'payment', 'is_canceled', 'date_start', 'date_end', 'date_created',
                  'date_modified']


class CoworkingSpaceSubscriptionCreateSerializer(serializers.ModelSerializer):
    card_token = CharField(allow_blank=False, write_only=True)

    class Meta:
        model = CoworkingSpaceSubscription
        fields = ['package', 'card_token']
        extra_kwargs = {'package': {'required': True},
                        'card_token': {'required': True}}

    def validate_package(self, value):
        if not value.is_active:
            raise serializers.ValidationError("package ({}) is not active".format(value))
        return value

    def create(self, validated_data):
        validated_data.pop('card_token', None)
        return super().create(validated_data)


class CoworkingSpaceSubscriptionAdminCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoworkingSpaceSubscription
        fields = ['user', 'package', 'payment', 'is_canceled', 'date_start', 'date_end']
        extra_kwargs = {'user': {'required': True},
                        'package': {'required': True}}
