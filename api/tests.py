import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .serializers import UserSerializer


# Create your tests here.


class UserTests(TestCase):
    def setUp(self) -> None:
        self.test_user_1 = User.objects.create(username='Test user 1', email='testemail@gmail.com')
        self.test_user_2 = User.objects.create(username='Test user 2', email='testemail2@gmail.com')

        self.valid_payload = {
            'username': 'Testuser3',
            'email': 'testemail3@gmail.com'
        }

        self.invalid_payload = {
            'username': '',
            'email': 'testemail3@gmail.com'
        }

        self.put_valid_payload = {
            'username': 'test_user_1_updated',
            'email': 'updatedemail@gmail.com'
        }

        self.put_invalid_payload = {
            'username': '',
            'email': 'updatedemail@gmail.com'
        }

    def test_get_all_users(self):
        response = self.client.get(reverse('users-list'))
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_user(self):
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.test_user_1.pk}))
        test_user_1 = User.objects.get(pk=self.test_user_1.pk)

        serializer = UserSerializer(test_user_1, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_user(self):
        response = self.client.post(
            reverse('user-create'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = self.client.post(
            reverse('user-create'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_user(self):
        response = self.client.delete(
            reverse('user-delete', kwargs={'pk': self.test_user_1.pk}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_user(self):
        response = self.client.delete(
            reverse('user-delete', kwargs={'pk': 10}),
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_user(self):
        response = self.client.put(
            reverse('user-update', kwargs={'pk': self.test_user_1.pk}),
            data=json.dumps(self.put_valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_user(self):
        response = self.client.put(
            reverse('user-update', kwargs={'pk': self.test_user_1.pk}),
            data=json.dumps(self.put_invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
