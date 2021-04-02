from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from coworkingspace.models import CoworkingSpaceSubscription
from iot.models import MeetingRoomIoT


class CoworkingSpaceKey(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        obj = get_object_or_404(CoworkingSpaceSubscription.objects.filter(id=id))

        if request.user is None:
            ip_addr = request.META['REMOTE_ADDR']
            if not MeetingRoomIoT.objects.filter(door_ip__istartswith=ip_addr).exists():
                return Response({"detail": "Invalid authentication detail."}, status=status.HTTP_403_FORBIDDEN)
        elif not request.user.is_staff:
            if request.user.id != obj.user.id:
                return Response({"detail": "Invalid user."}, status=status.HTTP_403_FORBIDDEN)
            elif not obj.is_in_subscription_date():
                return Response({"detail": "Not in subscription date."}, status=status.HTTP_403_FORBIDDEN)

        return Response({
            'id': id,
            'type': 'space',
            'pass': obj.get_qr_key()
        })
