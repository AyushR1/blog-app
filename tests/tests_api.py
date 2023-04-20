from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Blog
from django.core.files.uploadedfile import SimpleUploadedFile
import io
from PIL import Image


class UserRegistrationTestCase(APITestCase):
    def test_RegisterView(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')


class UserLoginTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
    
    def test_login(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post('/api/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)


class PostBlogTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
    
    def test_post_list(self):
        image_io = io.BytesIO()
        image = Image.new('RGB', (100, 100), color='red')
        image.save(image_io, 'JPEG')
        image_io.seek(0)

        # create a SimpleUploadedFile object from the new image file
        image_file = SimpleUploadedFile("test_image.jpg", image_io.read(), content_type="image/jpeg")

        login_data = {'username': 'testuser', 'password': 'testpassword'}
        login_response = self.client.post('/api/login/', login_data)
        access_token = login_response.data['access']
        auth_head = {'Authorization': f'Bearer {access_token}'}

        
        # create the data dictionary with image and other fields
        data = {'title':'Test Post', 'description':'This is a test post', 'image': image_file}
        
        response = self.client.post('/api/posts/', data, headers=auth_head, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data['title'], 'Test Post')


