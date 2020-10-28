import os
from datetime import timedelta

from django.db import models
from django.utils import timezone

from authapp.models import User


def meetingroom_file_name(instance, filename):
    return '/'.join(['uploads/meetingroom/', str(instance.id), 'picture{0}'.format(os.path.splitext(filename)[1])])


class MeetingRoom(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to=meetingroom_file_name)
    active = models.BooleanField(default=False)
    price = models.FloatField()

    def __str__(self):
        return '[MeetingRoom id:{}] {}'.format(self.id, self.name)

    # Model Save override to set id as filename
    def save(self, *args, **kwargs):
        if self.id is None:
            picture = self.picture
            self.picture = None
            super(MeetingRoom, self).save(*args, **kwargs)
            self.picture = picture
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(MeetingRoom, self).save(*args, **kwargs)


class MeetingRoomBooking(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(MeetingRoom, on_delete=models.SET_NULL, null=True)
    is_canceled = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[MeetingRoomBooking id:{}{}] {} to {} by {} at {}'.format(self.id,
                                                                          ' CANCELED' if self.is_canceled else '',
                                                                          self.date_start, self.date_end, self.user,
                                                                          self.room)

    @staticmethod
    def is_available(date_start, date_end, room):
        return not MeetingRoomBooking.objects.filter(date_end__gt=date_start, date_start__lt=date_end,
                                                     room=room, is_canceled=False).exists()

    @staticmethod
    def is_user_in_reserved_time(user, room, date=timezone.now(), min_early=0):
        return MeetingRoomBooking.objects.filter(date_start__lte=date + timedelta(minutes=min_early),
                                                 date_end__gte=date, room=room, is_canceled=False, user=user).exists()
