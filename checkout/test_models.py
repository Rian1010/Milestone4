from django.test import TestCase
from .models import BuyProduct, OrderLineItem
from django.utils import timezone

class TestCheckoutModels(TestCase):
    def test_buy_product(self):
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
        date = timezone.now()
        order = BuyProduct(full_name="Full Name", id=1, date=date)
        self.assertEqual("1-{}-Full Name".format(date), str(order))
    
    def test_order_line_item_as_string(self):
        order = OrderLineItem(quantity=1, product.name="Name of Product",
                            price=400.00, product.image="/images/photo.jpg")
        self.assertEqual("1 Name of Product @ 400.00 | /images/photo.jpg", str(order))
