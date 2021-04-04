import requests
from django.db import models

from authapp.models import User
from meetingroom.models import MeetingRoom


class MeetingRoomIoT(models.Model):
    room = models.OneToOneField(
        MeetingRoom,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    iot_ip = models.CharField(max_length=21)
    door_ip = models.CharField(max_length=21)


class MeetingRoomAccess(models.Model):
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_access = models.DateTimeField(auto_now=True)


class CoworkingAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_access = models.DateTimeField(auto_now=True)
