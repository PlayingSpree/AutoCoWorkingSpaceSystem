from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class PaymentForm(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'payment/payment.html'

    def get(self, request):
        if request.query_params.get('amount', None) is None:
            return Response({'amount': 0})
        return Response({'amount': request.query_params.get('amount', None)})
