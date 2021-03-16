from django.urls import path, include
from rest_framework import routers

from iot.views_room import IoTRoomViewSet
from iot.views_meeting_room_iot import MeetingRoomIoTViewSet

router = routers.DefaultRouter()
router.register('room/setup', MeetingRoomIoTViewSet)
router.register('room', IoTRoomViewSet, basename='iotroom')

urlpatterns = [
    path('', include(router.urls)),
]
