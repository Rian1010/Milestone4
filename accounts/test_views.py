from django.test import TestCase
from django.urls import reverse
from .forms import UserLoginForm
from django.contrib.auth.models import User
from checkout.models import BuyProduct, OrderLineItem
from django.utils import timezone
"""
A tutor called Michael has assisted me with some mistakes that I made, when trying to 
get the functions in the class below to run rightly. Source: https://codeinstitute.net/
"""


class TestAccountViews(TestCase):
    def test_home_page(self):
        """Tests if index.html is rendered correctly"""
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    def test_login_page(self):
        """Tests if login.html renders correctly and if index.html gets reversed to correctly"""
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        reverse_page = self.client.post(reverse('index'))
        self.assertEqual(reverse_page.status_code, 200)

    def test_registration_page(self):
        """Tests if registration.html is rendered correctly"""
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
    
    """
    Source that was used for assistance with the function bellow: 
    https://stackoverflow.com/questions/16143149/django-testing-check-messages-for-a-view-that-redirects/42252248
    """
    def test_logout(self):
        """Tests if a logged in user can logout correctly and if the right 
        success message for the logout is returned"""
        test_user = User.objects.create_user(username="test", email="test@example.com", password="SecretPassword")      
        self.client.login(username='test', password='SecretPassword') 
        page = self.client.get("/accounts/logout/", follow=True)
        self.assertEqual(page.status_code, 200)
        message = list(page.context.get('messages'))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("You have been successfully logged out." in message.message)

    def test_profile_page(self):
        """Test logs in a user to check if the profile page gets rendered collectly"""
        test_user = User.objects.create_user(username="test", email="test@example.com", password="SecretPassword")      
        self.client.login(username='test', password='SecretPassword') 
        page = self.client.get("/accounts/profile/{}".format(test_user.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")