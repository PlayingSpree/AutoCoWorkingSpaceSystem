from django.contrib import admin

# Register your models here.
from meetingroom.models import MeetingRoom, MeetingRoomBooking, MeetingRoomType

admin.site.register(MeetingRoom)
admin.site.register(MeetingRoomType)
admin.site.register(MeetingRoomBooking)
