from datetime import datetime

from django.test import TestCase
from django.utils.timezone import make_aware
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from authapp.models import User
from meetingroom.models import MeetingRoomBooking, MeetingRoom
from meetingroom.tests.base_api_test import BaseApiTest


class TestModel(TestCase):

    def setUp(self):
        self.room = [MeetingRoom.objects.create(name="Active", active=True, price=100.0),
                     MeetingRoom.objects.create(name="Active", active=True, price=100.0)]
        booking_date = [[datetime(2030, 6, 15, 10, 0), datetime(2030, 6, 15, 10, 30)],
                        [datetime(2030, 6, 15, 10, 30), datetime(2030, 6, 15, 11, 0)],
                        [datetime(2030, 6, 15, 12, 0), datetime(2030, 6, 15, 13, 0)]]
        for l in booking_date:
            l[0] = make_aware(l[0])
            l[1] = make_aware(l[1])
            MeetingRoomBooking.objects.create(date_start=l[0], date_end=l[1], room=self.room[0])
        return super().setUp()

    def test_is_available_method(self):
        testing_date_false = [[datetime(2030, 6, 15, 10, 0), datetime(2030, 6, 15, 10, 30)],
                              [datetime(2030, 6, 15, 11, 0), datetime(2030, 6, 15, 12, 30)],
                              [datetime(2030, 6, 15, 12, 30), datetime(2030, 6, 15, 13, 30)],
                              [datetime(2030, 6, 15, 9, 0), datetime(2030, 6, 15, 18, 0)]]
        for l in testing_date_false:
            l[0] = make_aware(l[0])
            l[1] = make_aware(l[1])
            self.assertTrue(not MeetingRoomBooking.is_available(l[0], l[1], self.room[0]),
                            "Should not work (Overlap time): {} / {} at {}".format(l[0], l[1], self.room[0]))
            self.assertTrue(MeetingRoomBooking.is_available(l[0], l[1], self.room[1]),
                            "Should work (Different room): {} / {} at {}".format(l[0], l[1], self.room[1]))

        testing_date_true = [[datetime(2030, 6, 15, 9, 0), datetime(2030, 6, 15, 10, 0)],
                             [datetime(2030, 6, 15, 11, 0), datetime(2030, 6, 15, 12, 0)],
                             [datetime(2030, 6, 15, 13, 0), datetime(2030, 6, 15, 16, 0)],
                             [datetime(2030, 6, 15, 17, 0), datetime(2030, 6, 15, 19, 0)],
                             [datetime(2030, 6, 16, 9, 0), datetime(2030, 6, 16, 18, 0)]]
        for l in testing_date_true:
            l[0] = make_aware(l[0])
            l[1] = make_aware(l[1])
            self.assertTrue(MeetingRoomBooking.is_available(l[0], l[1], self.room[0]),
                            "Should work (Non-overlap time): {} / {} at {}".format(l[0], l[1], self.room[0]))

        for b in MeetingRoomBooking.objects.all():
            b.is_canceled = True
            b.save()

        for l in testing_date_false:
            self.assertTrue(MeetingRoomBooking.is_available(l[0], l[1], self.room[0]),
                            "Should work (Canceled booking): {} / {} at {}".format(l[0], l[1], self.room[0]))


class TestApi(APITestCase, BaseApiTest):

    def setUp(self):
        self.url = reverse('meetingroombooking-list')

        self.request = {
            "date_start": make_aware(datetime(2030, 6, 15, 9, 0)),
            "date_end": make_aware(datetime(2030, 6, 15, 10, 0)),
            "user": 1,
            "room": 1,
            "is_canceled": False
        }
        self.required = ['date_start', 'date_end', 'user', 'room']
        self.non_valid = [['user', 3],
                          ['room', 2],
                          ['room', 3],
                          ['date_start', make_aware(datetime(2020, 6, 15, 9, 0))],
                          ['date_end', make_aware(datetime(2020, 6, 15, 10, 0))]]

        self.room = [MeetingRoom.objects.create(name="Active", active=True, price=100.0),
                     MeetingRoom.objects.create(name="Inactive", price=10.0)]

        self.user = User.objects.create_user(email='user@user.com', password='user1234')
        self.admin = User.objects.create_superuser(email='admin@admin.com', password='admin1234')

        MeetingRoomBooking.objects.create(date_start=make_aware(datetime(2030, 4, 15, 9, 0)),
                                          date_end=make_aware(datetime(2030, 4, 15, 10, 0)),
                                          user=self.user,
                                          room=self.room[0])
        MeetingRoomBooking.objects.create(date_start=make_aware(datetime(2030, 5, 15, 9, 0)),
                                          date_end=make_aware(datetime(2030, 5, 15, 10, 0)),
                                          user=self.admin,
                                          room=self.room[0])
        return super().setUp()

    def test_auth_anon(self):
        self.auth_test(self.url, 403, 403, 403, 403, 403)

    def test_auth_user(self):
        self.client.force_authenticate(user=self.user)
        self.auth_test(self.url, 200, 200, 400, 400, 204)

    def test_auth_admin(self):
        self.client.force_authenticate(user=self.admin)
        self.auth_test(self.url, 200, 200, 400, 400, 204)

    def test_list_anon(self):
        res = self.client.get(self.url)
        print(self.request)
        self.assertEqual(len(res.data), 1)

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)

        res = self.client.get(self.url)
        self.assertEqual(len(res.data), 2)
