from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from coworkingspace.models import CoworkingSpaceSubscription
from coworkingspace.serializers import CoworkingSpaceSubscriptionSerializer


class CoworkingSpaceSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = CoworkingSpaceSubscription.objects.all()
    serializer_class = CoworkingSpaceSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return CoworkingSpaceSubscription.objects.all()
        if user.is_anonymous:
            return
        return CoworkingSpaceSubscription.objects.filter(user=user)
