from django.test import TestCase
from .models import Product
"""I learned how to write the code bellow through Code Institute and it is the only way I know how to do it. 
Source: https://codeinstitute.net/"""


# Create your tests here.
class ProductTests(TestCase):
    """
    Define the tests that will be run against the Post models
    """
    def test_str(self):
        test_name = Product(name="A product")
        self.assertEqual(str(test_name), 'A product')
