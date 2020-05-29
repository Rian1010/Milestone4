from django.test import TestCase
from .models import BuyProduct, OrderLineItem
from phoneShop.models import Product
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

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

        order = BuyProduct.objects.create(full_name="Full Name", id=1, date=date)
        self.assertEqual("1-{}-Full Name".format(date), str(order))
    
    def test_order_line_item_as_string(self):
        # theImage = SimpleUploadedFile(name='test_image.jpg', content=open('{{MEDIA_URL}}/media/images/', 'rb').read(), 
        #                                 content_type='image/jpeg')
        test_user = User.objects.create_user(username="test", email="test@example.com", password="SecretPassword")      
        self.client.login(username='test', password='SecretPassword') 
        date = timezone.now()
        order = BuyProduct.objects.create(user_account=test_user, full_name="The Username", phone_number="123", 
                    country="TheCountry", postcode="902180", town_or_city="TheCity", street_address1="TheStreet",
                    street_address2="TheStreetPart2", county="TheCounty", date=date)
        

        product = Product.objects.create(name="Product Name", description="Description of the Product",price=400.00)
        # image=theImage
        order_line = OrderLineItem.objects.create(order=order, quantity=1, product=product, price=400.00)
        self.assertEqual("1 Product Name @ 400.0 | ", str(order_line))

    def test_order_history(self):
        test_user = User.objects.create_user(username="test", email="test@example.com", password="SecretPassword")      
        self.client.login(username='test', password='SecretPassword') 
        orders = BuyProduct.objects.create(user_account=test_user, full_name="The Username", phone_number="123", 
                country="TheCountry", postcode="902180", town_or_city="TheCity", street_address1="TheStreet",
                street_address2="TheStreetPart2", county="TheCounty", date=timezone.now())
        page = self.client.get("accounts/profile/")
        page.orders = orders    
        self.assertEqual(orders.user_account, test_user)
            


            # self.assertEqual(test_user.errors['password'], ['This field is required.'])
            # self.assertTrue(test_user.is_valid())