from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderForm, MakePayment
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from phoneShop.models import Product
import stripe
"""I learned how to write the code bellow through Code Institute and it is the only way I know how to do it. 
Source: https://codeinstitute.net/"""

stripe.api_key=settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            order_form=OrderForm(request.POST)
            payment_form=MakePayment(request.POST)

            if order_form.is_valid() and payment_form.is_valid():
                order = order_form.save(commit=False)
                order.date = timezone.now()
                
                if request.user.is_authenticated:
                    order.user_account = request.user
                    cart = request.session.get('shopping_cart', {})    
                    total=0
                    order.save()
                    for id, quantity in cart.items():
                        product=get_object_or_404(Product, pk=id)
                        total += quantity * product.price
                        order_line_item=OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            total=total,
                            price=product.price,
                        )
                        order_line_item.save()
                    try:
                        # Stripe takes everything in cents, therefore total * 100
                        customer = stripe.Charge.create(
                            amount=int(total * 100),
                            currency="EUR",
                            description=request.user.email,
                            card=payment_form.cleaned_data['stripe_id'],
                        )
                    except stripe.error.CardError:
                        messages.error(request, "Your card was declined")
                    if customer.paid:
                        messages.error(request, "You have successfully paid")
                        request.session['shopping_cart']={}
                        return redirect(reverse('index'))
                    else:
                        messages.error(request, "Unable to take payment")
                
            else:
                messages.error(request, "We were unable to take a payment with that card")

        else:
            payment_form=MakePayment()
            order_form=OrderForm()

        return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
    else:
        return redirect(reverse('index'))