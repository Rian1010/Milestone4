from django.test import TestCase
from .forms import UserRegistrationForm, UserLoginForm

# Create your tests here.
class TestForms(TestCase):
    def test_register_information(self):
        form = UserRegistrationForm({'email': 'testing@gmail.com', 'username': 'Name', 'password1': 'SuperSecretPassword', 'password2': 'SuperSecretPassword'})
        self.assertTrue(form.is_valid())

    def test_correct_result_for_no_value(self):
        form = UserRegistrationForm({'email': '', 'username': '', 'password1': '', 'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u'This field is required.'])
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        self.assertEqual(form.errors['password1'], [u'This field is required.'])
        self.assertEqual(form.errors['password2'], [u'This field is required.'])