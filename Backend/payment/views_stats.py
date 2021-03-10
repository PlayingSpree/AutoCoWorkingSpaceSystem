from django.utils.dateparse import parse_datetime
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.models import Payment
from payment.serializers import PaymentSerializer


class ListUsers(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        start = self.request.query_params.get('start', None)
        end = self.request.query_params.get('end', None)
        if start is not None and end is not None:
            start = parse_datetime(start)
            end = parse_datetime(end)
            if start is not None and end is not None:
                query = Payment.objects.filter(date_created__gte=start, date_created__lte=end)
                response = {}
                response
                return Response(response)
        return Response({'error': 'date incorrect'}, status=status.HTTP_400_BAD_REQUEST)
