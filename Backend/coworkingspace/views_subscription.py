from datetime import timedelta

from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from coworkingspace.models import CoworkingSpaceSubscription
from coworkingspace.serializers import CoworkingSpaceSubscriptionCreateSerializer, \
    CoworkingSpaceSubscriptionReadSerializer
from meetingroom.permissions import get_permissions_multi
from payment.models import Payment


class CoworkingSpaceSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = CoworkingSpaceSubscription.objects.all().order_by('-date_start')
    serializer_class = CoworkingSpaceSubscriptionCreateSerializer
    permissions = [
        (['create', 'list', 'retrieve', 'me'], [IsAuthenticated]),
        (['update', 'partial_update', 'destroy'], [IsAdminUser])
    ]

    def get_permissions(self):
        return get_permissions_multi(self)

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
        query = CoworkingSpaceSubscription.objects.filter(user=request.user, is_canceled=False,
                                                          date_end__gte=date_start)
        if query.exists():
            date_start = query.latest('date_end').date_end + timedelta(days=1)
        serializer.save(date_start=date_start, date_end=date_start + timedelta(days=package.duration - 1),
                        payment=payment, user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False)
    def me(self, request):
        query = CoworkingSpaceSubscription.objects.filter(user=request.user, is_canceled=False)
        if query.exists():
            obj = query.latest('date_end')
            member_date_end = obj.date_end
            member_duration = max(0, (obj.date_end - timezone.localdate()).days + 1)
            return Response({'member_date_end': member_date_end, 'member_duration': member_duration})
        else:
            return Response({'member_date_end': timezone.localdate(), 'member_duration': 0})
