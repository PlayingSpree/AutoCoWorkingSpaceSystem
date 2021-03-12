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
        }
        self.required = ['name']
        self.non_valid = []

        MeetingRoom.objects.create(name="Active", is_active=True)
        MeetingRoom.objects.create(name="Inactive")

        self.user = User.objects.create_user(email='user@user.com', password='user1234')
        self.admin = User.objects.create_superuser(email='admin@admin.com', password='admin1234')
        return super().setUp()

    def test_auth_anon(self):
        self.auth_test(self.url, 403, 403, 403, 403, 403)

    def test_auth_user(self):
        self.client.force_authenticate(user=self.user)
        self.auth_test(self.url, 200, 200, 403, 403, 403)

    def test_auth_admin(self):
        self.client.force_authenticate(user=self.admin)
        self.auth_test(self.url, 200, 200, 400, 400, 204)

    def test_list_anon(self):
        res = self.client.get(self.url)
        self.assertEqual(len(res.data), 1)

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)

        res = self.client.get(self.url)
        self.assertEqual(len(res.data), 2)
