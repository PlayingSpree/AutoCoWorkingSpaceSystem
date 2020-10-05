from django.urls import path, include
from rest_framework import routers

from meetingroom.views_meeting_room import MeetingRoomViewSet
from meetingroom.views_meeting_room_booking import MeetingRoomBookingViewSet

router = routers.DefaultRouter()
router.register('booking', MeetingRoomBookingViewSet)
router.register('', MeetingRoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
