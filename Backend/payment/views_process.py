from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from meetingroom.models import MeetingRoom
from meetingroom.permissions import get_permissions_multi
from meetingroom.serializers import MeetingRoomSerializer


class ProcessView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response(request.data)