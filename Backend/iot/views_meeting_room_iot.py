from rest_framework import viewsets
from rest_framework.generics import RetrieveDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from iot.models import MeetingRoomIoT
from iot.serializers import MeetingRoomIoTSerializer


class MeetingRoomIoTViewSet(viewsets.GenericViewSet, RetrieveDestroyAPIView):
    queryset = MeetingRoomIoT.objects.all()
    serializer_class = MeetingRoomIoTSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
            request.data['room'] = self.kwargs[lookup_url_kwarg]
            serializer = self.get_serializer(data=request.data)
        else:
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        if self.request.method == 'PUT':
            try:
                obj = queryset.get(**filter_kwargs)
            except queryset.model.DoesNotExist:
                return None
        else:
            obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj