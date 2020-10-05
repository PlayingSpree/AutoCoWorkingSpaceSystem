from datetime import datetime

from django.test import TestCase
from django.utils.timezone import make_aware

from meetingroom.models import MeetingRoomBooking


class TestModel(TestCase):

    def setUp(self):
        booking_date = [[datetime(2030, 6, 15, 10, 0), datetime(2030, 6, 15, 10, 30)],
                        [datetime(2030, 6, 15, 10, 30), datetime(2030, 6, 15, 11, 0)],
                        [datetime(2030, 6, 15, 12, 0), datetime(2030, 6, 15, 13, 0)]]
        for l in booking_date:
            l[0] = make_aware(l[0])
            l[1] = make_aware(l[1])
            MeetingRoomBooking.objects.create(date_start=l[0], date_end=l[1])
        return super().setUp()

    def test_is_available_method(self):
        testing_date_false = [[datetime(2030, 6, 15, 10, 0), datetime(2030, 6, 15, 10, 30)],
                              [datetime(2030, 6, 15, 11, 0), datetime(2030, 6, 15, 12, 30)],
                              [datetime(2030, 6, 15, 12, 30), datetime(2030, 6, 15, 13, 30)],
                              [datetime(2030, 6, 15, 9, 0), datetime(2030, 6, 15, 18, 0)]]
        for l in testing_date_false:
            l[0] = make_aware(l[0])
            l[1] = make_aware(l[1])
            self.assertTrue(not MeetingRoomBooking.is_available(l[0], l[1]), "{} / {}".format(l[0], l[1]))

        testing_date_true = [[datetime(2030, 6, 15, 9, 0), datetime(2030, 6, 15, 10, 0)],
                             [datetime(2030, 6, 15, 11, 0), datetime(2030, 6, 15, 12, 0)],
                             [datetime(2030, 6, 15, 13, 0), datetime(2030, 6, 15, 16, 0)],
                             [datetime(2030, 6, 15, 17, 0), datetime(2030, 6, 15, 19, 0)],
                             [datetime(2030, 6, 16, 9, 0), datetime(2030, 6, 16, 18, 0)]]
        for l in testing_date_true:
            l[0] = make_aware(l[0])
            l[1] = make_aware(l[1])
            self.assertTrue(MeetingRoomBooking.is_available(l[0], l[1]), "{} / {}".format(l[0], l[1]))

# class TestAuth(APITestCase):
#
#     def setUp(self):
#         self.register_url = reverse('rest_register')
#         self.login_url = reverse('rest_login')
#         self.logout_url = reverse('rest_logout')
#
#         self.user_data = {
#             'email': 'user@user.com',
#             'password': 'user1234',
#             'password1': 'user1234',
#             'password2': 'user1234',
#         }
#         return super().setUp()
#
#     def test_user_cannot_register_with_no_data(self):
#         res = self.client.post(self.register_url)
#         self.assertEqual(res.status_code, 400)
#
#     def test_user_cannot_register_with_invalid_email(self):
#         res = self.client.post(self.register_url, {
#             'email': 'user',
#             'password1': 'user1234',
#             'password2': 'user1234',
#         })
#         self.assertEqual(res.status_code, 400)
#
#     def test_user_cannot_register_with_mismatch_password(self):
#         res = self.client.post(self.register_url, {
#             'email': 'user',
#             'password1': 'user1234',
#             'password2': 'user5678',
#         })
#         self.assertEqual(res.status_code, 400)
#
#     def test_user_can_register_correctly(self):
#         res = self.client.post(
#             self.register_url, self.user_data)
#         self.assertIsNotNone(res.data['key'])
#         self.assertEqual(res.status_code, 201)
#
#     def test_user_cannot_login_with_invalid_password(self):
#         self.client.post(
#             self.register_url, self.user_data)
#         res = self.client.post(self.login_url, {
#             'email': self.user_data['email'],
#             'password': 'invalidpass',
#         })
#         self.assertEqual(res.status_code, 400)
#
#     def test_user_can_login(self):
#         self.client.post(self.register_url, self.user_data)
#         res = self.client.post(self.login_url, self.user_data)
#         self.assertEqual(res.status_code, 200)
#
#         user = User.objects.get(email=self.user_data['email'])
#         self.assertIsNotNone(user.auth_token)
#
#     def test_user_can_logout(self):
#         self.test_user_can_login()
#
#         res = self.client.post(self.logout_url)
#         self.assertEqual(res.status_code, 200)
#
#         user = User.objects.get(email=self.user_data['email'])
#         with self.assertRaises((AttributeError, ObjectDoesNotExist)):
#             user.auth_token
