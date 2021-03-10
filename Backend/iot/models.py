import os

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
