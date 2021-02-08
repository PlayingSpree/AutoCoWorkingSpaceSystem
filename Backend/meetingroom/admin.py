from django.contrib import admin

# Register your models here.
from meetingroom.models import MeetingRoom, MeetingRoomBooking

admin.site.register(MeetingRoom)
admin.site.register(MeetingRoomBooking)
