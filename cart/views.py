from django.shortcuts import render, redirect, reverse

# Create your views here.
def cart_views(request):
    """Render the contents page for the cart"""
    return render(request, "cart.html")

def cart_additions(request, id):
    """Include the requested quantity of a product to the cart"""
    quantity = int(request.POST.get('quantity'))
    shopping_cart = request.session.get("shopping_cart", {})
    
    if id in shopping_cart:
        shopping_cart[id] = int(shopping_cart[id]) + quantity
    else:
        shopping_cart[id] = shopping_cart.get(id, quantity)

    request.session['shopping_cart'] = shopping_cart

    return redirect(reverse('cart_views'))

def cart_adjustments(request, id):
    """Adjustment of the quantity of a product to the given amount"""
    quantity = int(request.POST.get("quantity"))
    shopping_cart = request.session.get("shopping_cart", {})

    if quantity > 0:
        shopping_cart[id] = quantity
    else:
        shopping_cart.pop(id)
    
    request.session['shopping_cart'] = shopping_cart
    return redirect(reverse('cart_views'))