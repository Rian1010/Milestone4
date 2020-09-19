from django.db import models
from phoneShop.models import Product
from django.contrib.auth.models import User
from django import forms
"""
I learned how to write parts of the code below through Code Institute. 
Source: https://codeinstitute.net/
"""


class BuyProduct(models.Model):
    user_account = models.ForeignKey('auth.User', null=True, related_name='user_account')
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2=models.CharField(max_length=40, blank=True)
    county=models.CharField(max_length=40, blank=False)
    date=models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
    

class OrderLineItem(models.Model):
    order=models.ForeignKey(BuyProduct, null=False, related_name='lineitems')
    product=models.ForeignKey(Product, null=False, related_name='lineproduct')
    quantity=models.IntegerField(blank=False)
    total=models.DecimalField(blank=False, decimal_places=2, max_digits=6, default=0)
    price=models.IntegerField(blank=False, default=0)

    def __str__(self):
        return "{0} {1} @ {2} | {3}".format(self.quantity, self.product.name, self.price, self.product.image)
        