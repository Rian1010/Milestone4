from django.shortcuts import render
from phoneShop.models import Product
from django.db.models import Q

# Create your views here.
def search_function(request):
    products = Product.objects.filter(Q(name__icontains=request.GET['search']))
    return render(request, "products.html", {"products": products})