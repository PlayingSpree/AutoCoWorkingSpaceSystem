from django.db.models import Count
from django.utils.dateparse import parse_date
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from feedback.models import Problem, ProblemType


class FeedbackStat(APIView):
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

        # Problem
        query = Problem.objects.filter(date_created__date__gte=start, date_created__date__lte=end)
        group = query.values('type__name').annotate(count=Count('id'))
        problem = []
        for result in group:
            problem.append(result)

        return Response({
            'total_problem': query.count(),
            'problem_count': problem,
        })
