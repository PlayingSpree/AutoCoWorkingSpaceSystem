from django.db import models

from meetingroom.models import MeetingRoom


class MeetingRoomIoT(models.Model):
    room = models.OneToOneField(
        MeetingRoom,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    ip = models.CharField(max_length=21)