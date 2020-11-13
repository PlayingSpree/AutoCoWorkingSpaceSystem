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


def user_image_upload(instance, filename):
    return '/'.join(['uploads/user', str(instance.user.id), 'face', 'face{0}'.format(os.path.splitext(filename)[1])])


class UserImage(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    image1 = models.ImageField(upload_to=user_image_upload)
    image2 = models.ImageField(upload_to=user_image_upload)
    image3 = models.ImageField(upload_to=user_image_upload)
    image4 = models.ImageField(upload_to=user_image_upload)
    image5 = models.ImageField(upload_to=user_image_upload)
