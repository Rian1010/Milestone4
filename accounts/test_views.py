from django.test import TestCase
from django.urls import reverse
from .forms import UserLoginForm
from django.contrib.auth.models import User
from checkout.models import BuyProduct, OrderLineItem
from django.utils import timezone


class TestAccountViews(TestCase):
    def test_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    def test_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        reverse_page = self.client.post(reverse('index'))
        self.assertEqual(reverse_page.status_code, 200)


    def test_registration_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
    
    def test_logout(self):
        test_user = User.objects.create_user(username="test", email="test@example.com", password="SecretPassword")      
        self.client.login(username='test', password='SecretPassword') 
        page = self.client.get("/accounts/logout/", follow=True)
        self.assertEqual(page.status_code, 200)
        message = list(page.context.get('messages'))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("You have been successfully logged out." in message.message)

    # def test_profile_page(self):
    #     test_user = User.objects.create_user(username="test", email="test@example.com", password="SecretPassword")      
    #     self.client.login(username='test', password='SecretPassword') 
    #     orders = BuyProduct.objects.create(user_account=test_user, full_name="The Username", phone_number="123", 
    #             country="TheCountry", postcode="902180", town_or_city="TheCity", street_address1="TheStreet",
    #             street_address2="TheStreetPart2", county="TheCounty", date=timezone.now())
    #     page = self.client.get("accounts/profile/")
    #     page.orders = orders    
    #     self.assertEqual(list(orders)[0].user_account, test_user)
    #     self.assertEqual(page.status_code, 200)


        # self.assertEqual(test_user.errors['password'], ['This field is required.'])
        # self.assertTrue(test_user.is_valid())