from django.urls import path, include
from rest_framework import routers

from iot_room.views import IoTRoomViewSet
from iot_room.views_meeting_room_iot import MeetingRoomIoTViewSet

router = routers.DefaultRouter()
router.register('setup', MeetingRoomIoTViewSet)
router.register('', IoTRoomViewSet, basename='iotroom')

urlpatterns = [
    path('', include(router.urls)),
]
