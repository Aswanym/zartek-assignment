from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTest(TestCase):
    def test_create_user(self):

        username = 'test user'
        password = 'testpwd'

        user = User.objects.create_user(username=username,
                                        password=password)

        # assertEqual(first, second, msg=None)
        # Test that first and second are equal. If the values do not compare equal, the test will fail.
        self.assertEqual(user.username, username)

        # assertTrue(expr, msg=None)
        # Test that expr is true.
        self.assertTrue(user.check_password(password))

        # assertFalse(expr, msg=None)
        # Test that expr is false.
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_super_user(self):

        username = 'test user'
        password = 'testpwd'

        user = User.objects.create_superuser(username=username, password=password)

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
