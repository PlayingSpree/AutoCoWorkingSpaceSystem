from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from iot.models import UserImage
from iot.serializers import UserImageSerializer
from meetingroom.permissions import get_permissions_multi


class UserImageViewSet(viewsets.ModelViewSet):
    queryset = UserImage.objects.all()
    serializer_class = UserImageSerializer
    permissions = [
        (['me', 'me_put'], [IsAuthenticated]),
        (['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy'], [IsAdminUser])
    ]

    def get_permissions(self):
        return get_permissions_multi(self)

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        instance = self.me_get_object(request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @me.mapping.put
    def me_put(self, request):
        instance = self.me_get_object(request.user)
        if instance is None:
            serializer = self.get_serializer(data=request.data)
        else:
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def me_get_object(self, pk):
        queryset = self.filter_queryset(self.get_queryset())

        if self.request.method == 'PUT':
            try:
                obj = queryset.get(pk=pk)
            except queryset.model.DoesNotExist:
                return None
        else:
            obj = get_object_or_404(queryset, pk=pk)

        self.check_object_permissions(self.request, obj)

        return obj
