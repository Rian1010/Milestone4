from django.contrib import admin
from .models import BuyProduct, OrderLineItem
"""
I learned how to write the code below through Code Institute. 
Source: https://codeinstitute.net/
"""


# Register your models here.
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

admin.site.register(BuyProduct, OrderAdmin)
