from django.shortcuts import render
from phoneShop.models import Product
from django.db.models import Q


""" This source was used to know how to work with the Q object https://docs.djangoproject.com/en/3.0/topics/db/queries/ """
def search_function(request):
    products = Product.objects.filter(Q(name__icontains=request.GET['search']) | Q(description__icontains=request.GET['search']))
    return render(request, "products.html", {"products": products})
