from django.shortcuts import render
from phoneShop.models import Product

# Create your views here.
def search_function(request):
    products = Product.objects.filter(name__icontains=request.GET['search'])
    return render(request, "products.html", {"products": products})