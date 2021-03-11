from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView


class PingAPI(APIView):

    def get(self, request):
        return Response({'time': timezone.now(),
                         'localtime': timezone.localtime(),
                         'localdate': timezone.localdate(),
                         'Timezone': timezone.get_default_timezone_name()})
