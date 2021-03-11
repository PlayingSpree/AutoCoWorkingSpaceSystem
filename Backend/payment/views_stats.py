from django.db.models import Count, DateField, Sum
from django.db.models.functions import ExtractMonth, ExtractDay, TruncDay
from django.utils.dateparse import parse_datetime, parse_date
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from authapp.models import User
from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentStat(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        start = self.request.query_params.get('start', None)
        end = self.request.query_params.get('end', None)

        # Validation
        if start is None and end is None:
            return Response({'error': 'date not provide'}, status=status.HTTP_400_BAD_REQUEST)
        start = parse_date(start)
        end = parse_date(end)
        if start is None and end is None:
            return Response({'error': 'date incorrect'}, status=status.HTTP_400_BAD_REQUEST)

        # Coworking Space
        query_coworking = Payment.objects.filter(date_created__date__gte=start, date_created__date__lte=end,
                                                 coworkingspacesubscription__isnull=False)
        group_coworking = query_coworking.annotate(
            date=TruncDay('date_created', output_field=DateField())) \
            .values('date').annotate(count=Count('id'), amount=Sum('amount'))
        stat_coworking = []
        coworkingspace_sale = 0
        for result in group_coworking:
            stat_coworking.append(result)
            coworkingspace_sale += result['amount']

        # Meeting Room
        query_meetingroom = Payment.objects.filter(date_created__date__gte=start, date_created__date__lte=end,
                                                   meetingroombooking__isnull=False)
        group_meetingroom = query_meetingroom.annotate(
            date=TruncDay('date_created', output_field=DateField())) \
            .values('date').annotate(count=Count('id'), amount=Sum('amount'))
        stat_meetingroom = []
        meetingroom_sale = 0
        for result in group_meetingroom:
            stat_meetingroom.append(result)
            meetingroom_sale += result['amount']

        # Payment Method
        query_method = Payment.objects.filter(date_created__date__gte=start, date_created__date__lte=end)
        group_method = query_method.values('method').annotate(count=Count('id'), amount=Sum('amount'))
        payment_method = []
        for result in group_method:
            payment_method.append(result)

        # Customer
        query_customer = User.objects.filter(date_joined__date__lte=end)
        customer_all = query_customer.count()
        customer_new = query_customer.filter(date_joined__date__gte=start).count()
        customer_old = customer_all - customer_new

        return Response({
            'total_sale': coworkingspace_sale + meetingroom_sale,
            'coworkingspace_sale': coworkingspace_sale,
            'meetingroom_sale': meetingroom_sale,
            'coworkingspace_sale_by_date': stat_coworking,
            'meetingroom_sale_by_date': stat_meetingroom,
            'payment_method': payment_method,
            'customer_all': customer_all,
            'customer_new': customer_new,
            'customer_old': customer_old
        })
