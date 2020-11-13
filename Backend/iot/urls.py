from django.urls import path, include
from rest_framework import routers

from iot.views_room import IoTRoomViewSet
from iot.views_meeting_room_iot import MeetingRoomIoTViewSet
from iot.views_user_image import UserImageViewSet

router = routers.DefaultRouter()
router.register('room/setup', MeetingRoomIoTViewSet)
router.register('room', IoTRoomViewSet, basename='iotroom')
router.register('face', UserImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
