from django.urls import path, include
from rest_framework import routers

from coworkingspace.views_package import PackageViewSet
from coworkingspace.views_subscription import CoworkingSpaceSubscriptionViewSet

router = routers.DefaultRouter()
router.register('subscription', CoworkingSpaceSubscriptionViewSet)
router.register('package', PackageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
