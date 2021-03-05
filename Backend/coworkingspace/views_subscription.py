from datetime import timedelta

from rest_framework import viewsets, status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone

from coworkingspace.models import CoworkingSpaceSubscription
from coworkingspace.serializers import CoworkingSpaceSubscriptionCreateSerializer, \
    CoworkingSpaceSubscriptionReadSerializer
from payment.models import Payment


class CoworkingSpaceSubscriptionViewSet(viewsets.GenericViewSet,
                                        mixins.CreateModelMixin,
                                        mixins.ListModelMixin,
                                        mixins.RetrieveModelMixin):
    queryset = CoworkingSpaceSubscription.objects.all()
    serializer_class = CoworkingSpaceSubscriptionCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return
        if user.is_staff:
            return self.queryset
        return self.queryset.filter(user=user)

    def get_serializer_class(self):
        if self.action == 'create':
            return self.serializer_class
        return CoworkingSpaceSubscriptionReadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Payment
        package = serializer.validated_data['package']
        payment = Payment.pay(serializer.validated_data['card_token'], package.price)
        if payment is None:
            return Response({"error": "Cannot make payment."}, status=status.HTTP_402_PAYMENT_REQUIRED)
        # Date
        date_start = timezone.localdate()
        query = CoworkingSpaceSubscription.objects.filter(user=request.user, date_end__gte=date_start)
        if query.exists():
            date_start = query.latest('date_end').date_end + timedelta(days=1)
        serializer.save(date_start=date_start, date_end=date_start + timedelta(days=package.duration - 1),
                        payment=payment, user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
