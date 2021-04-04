from django.db.models import Count, DateField
from django.db.models.functions import TruncDay
from django.utils.dateparse import parse_date
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from iot.models import MeetingRoomAccess, CoworkingAccess


class AccessStat(APIView):
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
        query_coworking = CoworkingAccess.objects.filter(date_access__date__gte=start, date_access__date__lte=end)
        group_coworking = query_coworking.annotate(
            date=TruncDay('date_access', output_field=DateField())) \
            .values('date').annotate(count=Count('id'))
        stat_coworking = []
        coworkingspace_access = 0
        for result in group_coworking:
            stat_coworking.append(result)
            coworkingspace_access += result['count']

        # Meeting Room
        query_meetingroom = MeetingRoomAccess.objects.filter(date_access__date__gte=start, date_access__date__lte=end)
        group_meetingroom = query_meetingroom.annotate(
            date=TruncDay('date_access', output_field=DateField())) \
            .values('date').annotate(count=Count('id'))
        stat_meetingroom = []
        meetingroom_access = 0
        for result in group_meetingroom:
            stat_meetingroom.append(result)
            meetingroom_access += result['count']

        return Response({
            'total_access': coworkingspace_access + meetingroom_access,
            'coworkingspace_access': coworkingspace_access,
            'meetingroom_access': meetingroom_access,
            'coworkingspace_access_by_date': stat_coworking,
            'meetingroom_access_by_date': stat_meetingroom,
        })
