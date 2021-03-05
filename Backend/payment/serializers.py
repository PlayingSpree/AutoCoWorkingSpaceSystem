from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['charge_token', 'status', 'amount', 'date_created', 'date_modified']
        read_only_fields = ['id', 'date_created', 'date_modified']
