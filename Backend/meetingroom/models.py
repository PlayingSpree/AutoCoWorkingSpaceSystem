import hashlib
import os
from datetime import timedelta

from django.db import models
from django.utils import timezone

from authapp.models import User
from meetingroom.appconfig import MEETING_ROOM_MIN_EARLY
from payment.models import Payment


class MeetingRoomType(models.Model):
    name = models.CharField(max_length=64)
    detail = models.TextField(blank=True)
    price = models.IntegerField()

    def __str__(self):
        return '[MeetingRoomType id:{}] {}'.format(self.id, self.name)


class MeetingRoom(models.Model):
    name = models.CharField(max_length=64)
    detail = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    type = models.ForeignKey(MeetingRoomType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '[MeetingRoom id:{}] {} Type: {}'.format(self.id, self.name, self.type)


class MeetingRoomBooking(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(MeetingRoom, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    is_canceled = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[MeetingRoomBooking id:{}{}] {} to {} by {} at {}'.format(self.id,
                                                                          ' CANCELED' if self.is_canceled else '',
                                                                          self.date_start, self.date_end, self.user,
                                                                          self.room)

    def get_qr_hash(self):
        data = self.date_start.__str__() + self.date_end.__str__() + self.id.__str__()
        return hashlib.md5(data.encode()).hexdigest()

    def is_in_reserved_time(self, date=timezone.now()):
        return not self.is_canceled and self.date_start <= date + timedelta(
            minutes=MEETING_ROOM_MIN_EARLY) and self.date_end >= date

    @staticmethod
    def is_available(date_start, date_end, room):
        return not MeetingRoomBooking.objects.filter(date_end__gt=date_start, date_start__lt=date_end,
                                                     room=room, is_canceled=False).exists()

    @staticmethod
    def is_user_in_reserved_time(user, room, date=timezone.now(), min_early=MEETING_ROOM_MIN_EARLY):
        return MeetingRoomBooking.objects.filter(date_start__lte=date + timedelta(minutes=min_early),
                                                 date_end__gte=date, room=room, is_canceled=False, user=user).exists()
