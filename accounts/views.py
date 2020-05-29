from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from phoneShop.models import Product
from django.utils import timezone
from checkout.forms import OrderForm, MakePayment
from checkout.models import OrderLineItem, BuyProduct

def index(request):
    """Return the index file"""
    return render(request, 'index.html')

@login_required
def logout(request):
    """Logs the user out"""
    auth.logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in.")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect.")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(
                    request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {"registration_form": registration_form})

@login_required
def user_profile(request, pk=None):
    """The user's profile page"""
    user = User.objects.get(username=request.user.username, email=request.user.email, pk=pk)

    if request.user.is_authenticated:
        orders = BuyProduct.objects.filter(user_account=request.user)
        # for info in orders:
        #     user_info = info
        #     print(user_info)

        # history = []
        # for order in orders:
        #     for lineitem in order.lineitems.all():
        #         history.append(lineitem)
        # print(history)
        
    else:
        user = request.user
    
    context = {"profile": user, "orders": orders,}

    return render(request, 'profile.html', context)


    
# def history(request):
#     """Show a user's history of purchased products"""
    
        # if order_form.is_valid() and payment_form.is_valid():
        #     order = order_form.save(commit=False)
        #     order.date = timezone.now()
        #     order.save()

