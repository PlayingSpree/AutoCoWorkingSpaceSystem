from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from feedback.models import Feedback, ProblemType, Problem
from feedback.serializers import FeedbackSerializer, ProblemTypeSerializer, ProblemSerializer
from meetingroom.permissions import get_permissions_multi


class ProblemTypeViewSet(viewsets.ModelViewSet):
    queryset = ProblemType.objects.all()
    serializer_class = ProblemTypeSerializer
    permission_classes = [IsAdminUser]


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permissions = [
        (['create'], [IsAuthenticated]),
        (['list', 'retrieve', 'update', 'partial_update', 'destroy'], [IsAdminUser])
    ]

    def get_permissions(self):
        return get_permissions_multi(self)
