from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class PaymentForm(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'payment/payment.html'

    def get(self, request):
        return Response({'amount': 12345})
