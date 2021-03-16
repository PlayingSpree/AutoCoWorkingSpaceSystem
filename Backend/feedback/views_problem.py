from django.utils.dateparse import parse_date
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from feedback.models import ProblemType, Problem
from feedback.serializers import ProblemTypeSerializer, ProblemSerializer
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

    def get_queryset(self):
        start = self.request.query_params.get('start', None)
        end = self.request.query_params.get('end', None)

        if start is None and end is None:
            return self.queryset
        start = parse_date(start)
        end = parse_date(end)
        if start is None and end is None:
            return self.queryset
        return self.queryset.filter(date_created__date__gte=start, date_created__date__lte=end)

    def get_permissions(self):
        return get_permissions_multi(self)
