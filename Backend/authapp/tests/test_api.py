from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from rest_framework.test import APITestCase

from authapp.models import User


class TestAuth(APITestCase):

    def setUp(self):
        self.register_url = reverse('rest_register')
        self.login_url = reverse('rest_login')
        self.logout_url = reverse('rest_logout')

        self.user_data = {
            'email': 'user@user.com',
            'password': 'user1234',
            'password1': 'user1234',
            'password2': 'user1234',
        }
        return super().setUp()

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_cannot_register_with_invalid_email(self):
        res = self.client.post(self.register_url, {
            'email': 'user',
            'password1': 'user1234',
            'password2': 'user1234',
        })
        self.assertEqual(res.status_code, 400)

    def test_user_cannot_register_with_mismatch_password(self):
        res = self.client.post(self.register_url, {
            'email': 'user',
            'password1': 'user1234',
            'password2': 'user5678',
        })
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        res = self.client.post(
            self.register_url, self.user_data)
        self.assertIsNotNone(res.data['key'])
        self.assertEqual(res.status_code, 201)

    def test_user_cannot_login_with_invalid_password(self):
        self.client.post(
            self.register_url, self.user_data)
        res = self.client.post(self.login_url, {
            'email': self.user_data['email'],
            'password': 'invalidpass',
        })
        self.assertEqual(res.status_code, 400)

    def test_user_can_login(self):
        self.client.post(self.register_url, self.user_data)
        res = self.client.post(self.login_url, self.user_data)
        self.assertEqual(res.status_code, 200)

        user = User.objects.get(email=self.user_data['email'])
        self.assertIsNotNone(user.auth_token)

    def test_user_can_logout(self):
        self.test_user_can_login()

        res = self.client.post(self.logout_url)
        self.assertEqual(res.status_code, 200)

        user = User.objects.get(email=self.user_data['email'])
        with self.assertRaises((AttributeError, ObjectDoesNotExist)):
            user.auth_token


class TestDetail(APITestCase):

    def setUp(self):
        self.detail_url = reverse('rest_user_details')

        self.user_data = {
            'email': 'user@user.com',
            'password': 'user1234',
            'password1': 'user1234',
            'password2': 'user1234',
        }

        self.client.post(reverse('rest_register'), self.user_data)
        return super().setUp()

    def test_user_can_get_data(self):
        res = self.client.get(self.detail_url)
        self.assertEqual(res.status_code, 200)

        user = User.objects.get(email=self.user_data['email'])
        self.assertEqual(user.id,res.data['id'])

    def test_user_can_update_data(self):
        res = self.client.patch(self.detail_url,{
            'phone': '0123456789'
        })
        self.assertEqual(res.status_code, 200)

        user = User.objects.get(email=self.user_data['email'])
        self.assertEqual(user.phone,'0123456789')
