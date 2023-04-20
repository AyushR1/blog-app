from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Blog


class UserRegistrationTestCase(APITestCase):
    def test_RegisterView(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')