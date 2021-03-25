from django.contrib import admin

# Register your models here.
from iot.models import MeetingRoomIoT, MeetingRoomAccess, CoworkingAccess

admin.site.register(MeetingRoomIoT)
admin.site.register(MeetingRoomAccess)
admin.site.register(CoworkingAccess)
