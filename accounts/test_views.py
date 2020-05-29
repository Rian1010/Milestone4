from django.test import TestCase
from django.urls import reverse
from .forms import UserLoginForm

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
        page = self.client.get("/accounts/logout/", follow=True)
        self.assertEqual(page.status_code, 200)
        message = list(page.context.get('messages'))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("You have been successfully logged out." in message.message)

        # self.assertEqual(page.status_code, 200)

    # def test_profile_page(self):
    #     user = UserLoginForm({'username' : 'Name'})
    #     self.assertEqual(user.errors['password'], ['This field is required.'])
    #     self.assertTrue(user.is_valid())
    