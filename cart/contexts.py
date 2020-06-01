from django.shortcuts import get_object_or_404
from phoneShop.models import Product
"""I learned how to write the code bellow through Code Institute and it is the only way I know how to do it. 
Source: https://codeinstitute.net/"""


def cart_contents(request):
    """
    Sets cart ready for the rendering of the page
    """
    cart = request.session.get('shopping_cart', {})

    cart_items = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}