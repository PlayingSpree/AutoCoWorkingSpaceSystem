from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from authapp.models import User
from meetingroom.models import MeetingRoom
from meetingroom.tests.base_api_test import BaseApiTest


class TestApi(APITestCase, BaseApiTest):

    def setUp(self):
        self.url = reverse('meetingroom-list')

        self.request = {
            "name": "Meeting Room 1",
            "description": "Test",
            "active": True,
            "price": 99.99
        }
        self.required = ['name', 'price']
        self.non_valid = [['price', 0],
                          ['price', -19.99]]

        MeetingRoom.objects.create(name="Active", active=True, price=100.0)
        MeetingRoom.objects.create(name="Inactive", price=0.0)

        self.user = User.objects.create_user(email='user@user.com', password='user1234')
        self.admin = User.objects.create_superuser(email='admin@admin.com', password='admin1234')
        return super().setUp()

    def test_auth_anon(self):
        self.auth_test(self.url, 200, 200, 403, 403, 403)

    def test_auth_user(self):
        self.client.force_login(user=self.user)
        self.auth_test(self.url, 200, 200, 403, 403, 403)

    def test_auth_admin(self):
        self.client.force_login(user=self.admin)
        self.auth_test(self.url, 200, 200, 400, 400, 204)

    def test_list_anon(self):
        res = self.client.get(self.url)
        print(self.request)
        self.assertEqual(len(res.data), 1)

    def test_list_admin(self):
        self.client.force_login(user=self.admin)

        res = self.client.get(self.url)
        self.assertEqual(len(res.data), 2)
