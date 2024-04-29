from django.contrib.auth.models import User
from account.serializers import UserCreationSerializer
from rest_framework.test import APITestCase

class UserSerializerTestCase(APITestCase):

    def setUp(self):
        # Define the data dictionary in the setUp method
        self.data = {
            'email': 'test@example.com',
            'username': 'test_user',
            'password': 'testpwd'
        }

        self.wrong_data = {
            'email': 'test@example.com',
            'username': 'test_user',
            'password': 'testpwd',
        }

    def test_user_serializer_validate_data(self):

        serializer = UserCreationSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})

