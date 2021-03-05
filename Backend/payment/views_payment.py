from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdminUser]
