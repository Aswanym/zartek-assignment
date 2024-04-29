from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

class RegisterViewTestCase(APITestCase):

    def setUp(self):
        # Define the data dictionary in the setUp method
        self.data = {
                    "username": "new_user",
                    "password": "1234",
                    "email": "example@gmail.com"
                }

        self.client = APIClient()

    def test_register_view_success(self):

        url = reverse('register')

        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access_token', response.data)

    def test_register_view_duplicate_username(self):

        """Registering a user with already existing username and expecting a 404 bad request."""
        User.objects.create_user(username=self.data['username'],
                                 password=self.data['password'])

        url = reverse('register')

        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginUserTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('login')

        # Create a test user
        self.data = {
            "username": "new_user",
            "password": "1234",
            "email": "example@gmail.com"
        }

    def test_login_user_success(self):

        # create a user first. so that we can log in using that credentials
        User.objects.create_user(**self.data)

        # Make a POST request to the login endpoint
        response = self.client.post(self.url, self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertIn('user_id', response.data)
        self.assertEqual(response.data['user_name'], self.data['username'])
        self.assertIn('access_token', response.data)

    def test_login_user_failure(self):

        # Make a POST request to the login endpoint without creating a user first and expecting a 400 error.
        response = self.client.post(self.url, self.data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], "User authentication failed")



