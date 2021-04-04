from django.urls import path, include
from rest_framework import routers

from iot.views_access import MeetingRoomAccessViewSet, CoworkingAccessViewSet
from iot.views_door import IoTDoorViewSet
from iot.views_room import IoTRoomViewSet
from iot.views_meeting_room_iot import MeetingRoomIoTViewSet
from iot.views_stats import AccessStat

router = routers.DefaultRouter()
router.register('access/room', MeetingRoomAccessViewSet)
router.register('access/space', CoworkingAccessViewSet)
router.register('room/setup', MeetingRoomIoTViewSet)
router.register('room', IoTRoomViewSet, basename='iotroom')

urlpatterns = [
    path('key/', IoTDoorViewSet.as_view()),
    path('access/stat/', AccessStat.as_view()),
    path('', include(router.urls)),
]
