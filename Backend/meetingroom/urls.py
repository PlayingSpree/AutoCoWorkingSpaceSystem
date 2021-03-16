from django.urls import path, include
from rest_framework import routers

from meetingroom.views_key import MeetingRoomKey
from meetingroom.views_meeting_room import MeetingRoomViewSet
from meetingroom.views_meeting_room_booking import MeetingRoomBookingViewSet
from meetingroom.views_meeting_room_type import MeetingRoomTypeViewSet

router = routers.DefaultRouter()
router.register('booking', MeetingRoomBookingViewSet)
router.register('type', MeetingRoomTypeViewSet)
router.register('', MeetingRoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('key/<int:id>/', MeetingRoomKey.as_view())
]
