from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    """user tests, get user, create user, show email"""
    def setUp(self):
        """create test users"""
        self.u = User.objects.create(username="john", email="john@gmail.com", password="1234")
        
    def test_user_create(self):
        """show the created model"""
        u = User.objects.get(username="john")
        print(self.assertEqual(u.email, "john@gmail.com"))