from django.test import TestCase
from .models import BuyProduct, OrderLineItem
from phoneShop.models import Product
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
"""
A tutor from Code Institute (https://codeinstitute.net/), called Michael has helped me to understand the logic of my mistakes of trying to 
get the functions in the class below to run correctly.
"""


class TestCheckoutModels(TestCase):
    def test_buy_product(self):
        """Tests if the BuyProduct model really takes in the correct user information for an order"""
        date = timezone.now() 
        order = BuyProduct(full_name="Full Name Test", phone_number="123", country="TheCountry", postcode="902180", 
                            town_or_city="TheCity", street_address1="TheStreet", street_address2="TheStreetPart2", 
                            county="TheCounty", date=date)
        self.assertEqual(order.full_name, "Full Name Test")
        self.assertEqual(order.phone_number, "123")
        self.assertEqual(order.country, "TheCountry")
        self.assertEqual(order.postcode, "902180")
        self.assertEqual(order.town_or_city, "TheCity")
        self.assertEqual(order.street_address1, "TheStreet")
        self.assertEqual(order.street_address2, "TheStreetPart2")
        self.assertEqual(order.county, "TheCounty")
        self.assertEqual(order.date, date)
    
    def test_order_as_string(self):
        """Tests if the string function of the BuyProduct model returns the right output"""
        date = timezone.now()

        order = BuyProduct.objects.create(full_name="Full Name", id=1, date=date)
        self.assertEqual("1-{}-Full Name".format(date), str(order))
    
    def test_order_line_item_as_string(self):
        """Tests if the the sting function of the orderLineItem model returns the correct output"""
        test_user = User.objects.create_user(username="test", email="test@example.com", password="SecretPassword")      
        self.client.login(username='test', password='SecretPassword') 
        date = timezone.now()
        order = BuyProduct.objects.create(user_account=test_user, full_name="The Username", phone_number="123", 
                    country="TheCountry", postcode="902180", town_or_city="TheCity", street_address1="TheStreet",
                    street_address2="TheStreetPart2", county="TheCounty", date=date)
        

        product = Product.objects.create(name="Product Name", description="Description of the Product",price=400.00)
        order_line = OrderLineItem.objects.create(order=order, quantity=1, product=product, price=400.00)
        self.assertEqual("1 Product Name @ 400.0 | ", str(order_line))

    def test_order_history(self):
        """Tests if the correct order history has been taken in for the right user that the order 
        history is supposed to relate to"""
        test_user = User.objects.create_user(username="test", email="test@example.com", password="SecretPassword")      
        self.client.login(username='test', password='SecretPassword') 
        orders = BuyProduct.objects.create(user_account=test_user, full_name="The Username", phone_number="123", 
                country="TheCountry", postcode="902180", town_or_city="TheCity", street_address1="TheStreet",
                street_address2="TheStreetPart2", county="TheCounty", date=timezone.now())
        page = self.client.get("accounts/profile/")
        page.orders = orders    
        self.assertEqual(orders.user_account, test_user)