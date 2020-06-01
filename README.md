[![Build Status](https://travis-ci.org/Rian1010/Milestone4.svg?branch=master)](https://travis-ci.org/Rian1010/Milestone4)

# Phone-Shop
This is my fourth milestone project that I have done on the Full Stack Software Development course at Code Institute. In this project, the main focus was using Django and VSCode was used as code editor. The project is published [here](https://milestone4-django-phone-shop.herokuapp.com/).

## Purpose of This Project
This project is an e-commerce website to sell trending mobile phones from all over the world. Users can easily search for their desired brands that vary at different prices and can choose how many they want to put into a shopping-cart to purchase. 

These are the following sections of te website:
- Home page: As it is the first page that a user gets to see, it contains examples of product that are being sold, examples of smartphone photography and a section for the call to action of buying a product. 

- Login/Registration Page: Enables users to sign in or sign up to visit the rest of the web pages, besides the home page.

- Reset Password Page: Allows a user to reset one's own password.

- Shop Page: The page that contains all products that the website has to offer. A user can add a product from that page to the cart page.

- Cart Page: A logged in user can see the items that one has added into the cart, how much the total price is and each chosen product's details, before checking out. 

- Profile Page: Shows the user account's information and order history.

- Logout: Allows a user to sign out of the website

## UX
#### User Stories
- As a user, I would like to know what kind of phones this website sells
- As a user, I would like to see interesting things that I could do with a product from the website and quick examples of good phone
- As a user, I would like to be able to simply search for the keywords of or about a product that I am looking for. 
- As a user, I would like to add the items that I am interested in, to save them there and see what the total price is.
- As a user, I would like to enter the required information for me to purchase a product in a simple way and view the items that I bought with the order information, in an order history
- As a user, I would like see my account details again, before I forget them, and be able to reset the password, in case I do not remember it anymore
- As a user, I would like to be able to visit the website from multiple devices, if phone, tablet, laptop
#### Admin Stories
- As an admin, I would like to sign in to the administration panel
- As an admin, I would not like a user to have the ability to edit, add or remove product details from the shop page

## Front-End Design

The overall design was inspired from what I was taught about web designing at Code Institute and an internship that I did, before starting this project, at [The Ambitious](https://www.ambitious-consulting.de/) from Jan Ruthard. The colours that I used were white, orange and blue. I wanted to use bright colours that match well together, such as white, light blue and light orange, so that it would give off a positive look on first glance, but still a sense of importance by usind sharp edges on the pictures and boxes and not choosing too light colours.

The font that I used was the default sans-serif font-family, as I found it fitting to the website and theme already.

## Wireframes
- [Home Page](https://github.com/Rian1010/Milestone4/blob/master/wireframes/djang-homepage-wireframe.jpeg)
- [Shop Page](https://github.com/Rian1010/Milestone4/blob/master/wireframes/djang-shop-wireframe.jpeg)
- [Cart Page](https://github.com/Rian1010/Milestone4/blob/master/wireframes/django-cart-wireframe.jpeg)
- [Checkout Page](https://github.com/Rian1010/Milestone4/blob/master/wireframes/django-checkout-wireframe.jpeg)
- [Login Page](https://github.com/Rian1010/Milestone4/blob/master/wireframes/django-login-wireframe.jpeg)
- [Registration Page](https://github.com/Rian1010/Milestone4/blob/master/wireframes/django-registration-wireframe.jpeg)
- [Profile Page](https://github.com/Rian1010/Milestone4/blob/master/wireframes/django-profile-wireframe.jpeg)
- [Reset Password Page](https://github.com/Rian1010/Milestone4/blob/master/wireframes/django-reset-password-wireframe.jpeg)

Some of the ideas that are shown in the wireframes have been changed throughout the process of the website for better design and logic.

## Utilised Technologies
### Languages
- HTML5: As mark-up language
- CSS3: For styling
- JavaScript: To add functionalities and animations in the front end
- Python3: To add functionalities through the back-end

### Frameworks
- Django 1.11.24: Framework based on Python
- Bootstrap 4: For responsive web designing 

### Database
- PostgresSql: Database from Heroku
- SQLite3: Database from Django

### API
- Stripe: For payment functionalities

### Validators
- [PEP8 Validator](http://pep8online.com/)
- [JavaScript Validator](https://jshint.com/)
- [CSS Validator](http://csslint.net/)
- [HTML Validator](https://www.freeformatter.com/html-validator.html)

### Other Tools
- jQuery
- Github: hosts the website
- Git: version control
- Heroku: app Deployment
- Gunicorn: runs Python applications
- Travis CI: continiuous integration
- AWS S3 Bucket: cloud storage
- Boto3: ror the usage of Amazon S3
- VSCode: code editor
- Psycopg2-Binary: to connect Python to the database
- Pillow: stores images with the usage of django on the website
- [MiniWebtool](https://miniwebtool.com/django-secret-key-generator/): generates new SECRET_KEY

## Features
### Existing Features
- Users can login, registrate and reset their passwords
- Users can select how many products they want in a shopping-cart and buy them by checking out
- Users can view their own order histories on the profile page
- Stripe API was added for payment functionalities to work
- Users can search for items through keywords that are included in their titles or or descriptions

### Features Left to Implement and Unsolved Bugs
- I want to add pagination, so that the items are in different brand categories and can click on arrows to scroll through a list of phones by specific brands
- I made a page for password resets, on which a user is supposed to enter his or her email address to receive an email that links the person to a page for resetting the password however, I only managed to get the email through the terminal, but not in my email inbox. Since I do not have more time to work on it, it is left as a feature that I want to implement in the future. What I tried to do to solve it was to get a Google password for emails from my Google account on the [security page](https://myaccount.google.com/security?rapt=AEjHL4Mps0KBp02VHygwrbuviAPywFDORznFPftIXniGD1tb5dpI0u8nYM9JEKf6lT1RfHcwsLY6aLBlatEFwztsC0KZbf1DzA)

## Process 
### Django
Most of the Django code was heavily inspired from what's been taught at [Code Institute](https://codeinstitute.net/). I used the code that I learned from them for user authorisation and authentication in the accounts app, a lot in the search app, phoneShope app, checkout app and cart app. However, I did add my own edits and codes in there, through research, assistance of tutors and Slack members of the Code Institute course and through my own understanding. The things codes that I learned from the course are indicated with comments in their files.

I was able to use and understand a lot of what has been taught at Code Institute, but I spent loads of time trying to figure out how to make most things, which were not shown in the course, work. One of those challenges was to create an order history on the profile page. 

At first, I asked a tutor from Code Institute lots of questions to understand things to tackle this challenge better. So, I tried the following:

```python
test = get_object_or_404(OrderLineItem, pk=1)
print(test.quantity, test.product.name, test.product.price)
return render(request, "profile.html", {"test": test, "profile": user})
```

In the code above, I wanted to get each primary key of the OrderLineItem and print some of the required information. This then worked, but I could not grab everything that I needed from that model. 

So, after talking to tutors from Code Institute again, explaining more of what I was trying to do, my next try was the following:

```python
if request.user.is_authenticated:
    orders = BuyProduct.objects.filter(user_account=request.user)

    for order in orders:
        history = order.lineitems.all()
        print(history.quantity, history.total, history.product.price)

     return render(request, 'profile.html', {"profile": user,
                                            "history": history,
                                            "orders": orders,
                                            })
```

At that point, I thought I had it, because this print statement was printing out the querysets, and the orders were working fine in the templates, but the problem was that the history variable was only available inside of the for loop, so it did not show up in the templates. I tested it by printing the same print statement outside of the for loop and it was empty. 

Therefore, I needed to append `history = order.lineitems.all()` and I failed trying the following things:
```python
    history = []
    for order in orders:
        history.append(order.lineitems.all())
    for hist in history:
        print(hist)
```
This code returned querysets again.

```python

    with open('views.py','r') as f:
            for order in f.orders:
                history = order.lineitems.all()
                break
            
        print(history)
```
I learned this way, above from [StackOverflow](https://stackoverflow.com/questions/25406399/python-get-variable-outside-the-loop), [W3Schools](https://www.w3schools.com/python/python_file_handling.asp) and [Reading and Writing files in Pure Python Documentation](https://python4mpia.github.io/pure_python/files.html)

Someone from the course, on Slack, who seems to often help others told me to try the following for loop, so I googled it, trying to understand it and this is what I did:

```python
for i, c in enumerate(history):
        print(c.product.name)
        print(i, c, type(c))
    print(history.value_list())
```
This printed each queryset next to its index number. So I still could not get the information from the queryset correctly in the template. Then, I showed it to a tutor from Code Institute again, who told me that I have to loop through it twice to get the correct details. It worked and this is what the function looked like at that point.

```python
@login_required
def user_profile(request, pk=None):
    """The user's profile page"""
    user = User.objects.get(username=request.user.username, email=request.user.email, pk=pk)

    if request.user.is_authenticated:
        orders = BuyProduct.objects.filter(user_account=request.user)

        history = []
        for order in orders:
            for lineitem in order.lineitems.all():
                history.append(lineitem)
        print(history)
        
    else:
        user = request.user
    
    context = {"profile": user, "orders": orders, "history": history}

    return render(request, 'profile.html', context)

```
Although it printed out the correct things and I could show the right information on the profile page, I could not show orders and history within the same for loop. I tried using zip or nesting the two for loops and then using an if statement, like so:  
```html
{% for info in orders %}
    {% for purchase in history %}
        {% if forloop.counter == forloop.parentloop.counter&}
            <!-- Code goes here in profile.html -->
        {% endif %}
    {% endfor %}
{% endfor %}
```
However, this only increased the number of times a previously purchased item was bought by 1, after every other purchase was made. The idea for using zip came from a Stack Overflow page. Click [here](https://stackoverflow.com/questions/2415865/iterating-through-two-lists-in-django-templates) to visit that page. The Stack Overflow page that inspired me for the for loops and if statement in the template can be found by clicking [here](https://stackoverflow.com/questions/14841165/is-there-a-way-to-loop-over-two-lists-simultaneously-in-django/14841466). So, I looped through the queryset in the template, instead of views.py and it worked, as I wanted! Here is the final code: 
- views.py
```python
@login_required
def user_profile(request, pk=None):
    """The user's profile page"""
    user = User.objects.get(username=request.user.username, email=request.user.email, pk=pk)

    if request.user.is_authenticated:
        orders = BuyProduct.objects.filter(user_account=request.user)
        
    else:
        user = request.user
    
    context = {"profile": user, "orders": orders,}

    return render(request, 'profile.html', context)
```
- profile.html
```html
{% for order in orders %}
    {% for lineitem in order.lineitems.all %}
        <!-- Code goes here in profile.html -->
    {% endfor %}
{% endfor %}
```

In the search app, another challenge was to allow users to search for products with keywords that target both, the name and description of the product, instead of just its name. At first I tried using two variable to filter them separately, which did not work correctly. Later, I found out about Q objects and used the [django documentation](https://docs.djangoproject.com/en/3.0/ref/models/querysets/), as assistance to get it to work in the views.py file of the search app. Here is the code that I ended up writing, which works:

```python
def search_function(request):
    products = Product.objects.filter(Q(name__icontains=request.GET['search']) | Q(description__icontains=request.GET['search']))
    return render(request, "products.html", {"products": products})
```

### JavaScript
The JavaScript code was written by myself, except for the code that takes the value that is give by the user through input to display the username that one enters above the input fields. I learned how to write that code from the [jQuery API Documentation](https://api.jquery.com/val/). Here is the code that I am talking about:

```javascript
$("input[name = 'username']").keyup(function () {
    let nameVal = $(this).val();
    $('.username').text(` ${[nameVal]}`);
});
```

## Testing
### Manual Testing
- Tried to register with wrongly formatted passwords, and also unmatched passwords
    - Both tests resulted in the correct error messages
- Tried to register without filling in a required field
    - The registrations did not work 
- Registered and logged in
    - Both tests worked
- Tried to have access to another web page besides the home by clicking on the available buttons before being logged in
    - Each page lead me to the login page
- Logged in and scrolled through each page to make sure that the JavaScript on the navigation bars work correctly
    - It worked correctly on scroll and the item links work rightly on hover, both on ever page
- Tried typing something into the username input boxes of the login and registration forms to check if the JavaScript code correctly picked up the values to display the letters above the input fields
    - Test worked
- Went to the second section of the home page, where phone brand examples are shown, and hovered over the name of the brand to test if JavaScript would display the picture the of each phone's name rightly according to which name I hover on 
    - Tests worked
- Checked if the design on each page looks fine responsively and if it is easy to use
    - Everything is fine now
- Went to the shop page and tried adding items to the cart buy clicking on the arrows that appear in the input field and tried changing the number manually too
    - Tests worked
- Clicked on the add button without inserting a number into the field of an item in the shop page
    - Showed correctly that an input in required
- Clicked on the add button after inserting a number into the input field
    - Correctly lead me to the cart page with the right information of the added item 
- Added more items to the cart field
    - Each item was displayed correctly with the right total price at the bottom 
- Clicked on the checkout button to pay
    - It lead me to the right checkout page and displayed the correct items that were being bought
- After entering the testing information into the fields, (with 4242 4242 4242 4242 as test credit card number and 111 as security code), I clicked on the pay button
    - It correctly lead me to the home page, showing the correct message
- Checked if the user's profile information and order history would show up correctly on the profile page
    - Both were rightly displayed with the correct user information and details of each purchased product
- Tried adding an item to the cart page, inserted a number in the input field next to the amend button and then clicked on the button to change the product's quantity
    - Test worked
- Tried adding an item to the cart page, went to the checkout page, inserted a number in the input field next to the amend button and then clicked on the button to change the product's quantity
    - Test worked
- Tested if amending an item to 0 on the cart and checkout page would delete an item from both pages
    - Both tests worked
- Tested if the cart page would display the correct text and remove the checkout button, when there was no item inside
    - Tests worked
- Checked if the correct number showed up next to the 'Go to Cart' button in the navigation bar, if there were items in the cart
    - Test worked
- Clicked on the logout button in the navigation bar and checked if it would log out the account and display the correct message
    - Tests worked, the account was logged off and the correct message showed up
- Tested the responsiveness of the website through a phone and the Chrome DevTools on desktop 
### Automated Testing
- Did some automated testing in order to test if all the views in the accounts and checkout apps return the correct statuses to see if they link to the right templates correctly 
    - All tests worked fine
#### Tests for the accounts app
- Tested if the logout view and its success message work correctly through the test_logout function 
    - That test went rightly too
- Tested the forms of the accounts app to see, if the registration for took in the email, username, password1 and password2 correctly
    - Tests passed rightly
- Tested if empty the right error message would appear, if no value was given for email, username, password1 and password2
    - Tests Passed correctly, as well
#### Tests for the checkout app
- Tested if the BuyProduct model would work, if correct information was given from a logged in user in the test_buy_product function
    - Tests run correctly
- Tested if the string function of the BuyProduct model returned the right information, through the test_order_as_string
    - Tests worked rightly
- Tested in the test_order_line_item_as_string function, if the string function of the OrderLineItem model returned the correct information, through user login and having order information in the BuyProduct Model
    - Tests run fine
- Test in the test_order_history function if the orders would go to the order history on the profile page correctly
    - Tests run well

### Installing and Using Coverage
- sudo pip3 install coverage
- coverage run manage.py test
- coverage run --source=app_name manage.py test
- coverage report (Shows how much code has been tested)
- coverage html
- Display the HTML page to see the parts of an app that needs to be tested

## Deployment and Publishing 
### Deployment to Github
- git add .
- git status
- git commit -m "a short description of the update"
- git remote add origin 
- git push origin master

### Heroku Deployment
- In Resources, add Heroku Postgres in add-ons
- Get the DATABASE_URL in the conguration variables and copy it into the env.py file
- os.environ.setdefault("DATABASE_URL", "postgres://---")
- Do the same to SECRET_KEY and STRIPE_PUBLISHABLE
- sudo pip3 install dj-database-url
- sudo pip3 install psycopg2-binary
- pip3 freeze > requirements.txt
- import dj_database_url in settings.py
- Switch DATABASE to postgres in settings.py
- Migrate the existing migrations to the postgres database, although there are no changes detected through python3 manage.py makemigrations (use the following commands: `python3 manage.py makemigrations`, `python3 manage.py migrate`)

- For the website to work on Heroku, the statics must be disabled, through `DISABLE_COLLECTSTATIC=1`

### Amazon Web Services
- Once logged in, choose S3 
- Untick all checkboxes in 'Set Permissions'
- Open the bucket
- Go to Properties and then 'Static website hosting'
- Click on 'Use this bucket to host a website' and insert 'index.html' and 'error.html'
- Click on Permissions, then CORS configuration
- Write the following code in it:
```html
<CORSConfiguration>
<CORSRule>
<AllowedOrigin>*</AllowedOrigin>
<AllowedMethod>GET</AllowedMethod>
<AllowedMethod>HEAD</AllowedMethod>
<MaxAgeSeconds>3000</MaxAgeSeconds>
<AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
- Click on Bucket Policy
- Paste in the following:
```javascript
{
    "Version":"2012-10-17",
    "Statement":[{
      "Sid":"PublicReadGetObject",
        "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::example-bucket/*"]
      ]
    }
  ]
}
```
- Replace example-bucket, in the code, with what's given above the box (Name of the bucket)
- Go to dashboard through one of the things that can be pinned in the navigation bar, called IAM, then click on groups to create a group
- Click on Policy and Create a new policy
- Click on Import managed policy
- Search for s3 and choose AmazonS3FullAccess
- In JSON, change the string from 'Resource' to a list and add ["arn:aws:s3:::bucket-name"], ["arn:aws:s3:::bucket-name/*"]
- Click on the Review Policy button and give it a name, such as bucket-name-policy
- Go to the created group, go to permissions, search for the policy just created, check it and click on the 'Attach policy' button
- Click on Users in the side-navigation-bar, then click on Add User and name it with something that is associated with the bucket name and tick programmatic access
- Choose the created group, skip the keys, as they're not needed and create the user
- It is very important to make sure to download the .csv, this has the access keys needed in the software. It's important to keep them safe. One is never able to generate them again.
- Go back to S3, click on the bucket and test it by trying to upload a file
- The image should have a link that can be accessed from anywhere

## Change the code for S3
- sudo pip3 install django-storages
- sudo pip3 install boto3 
- Include 'storages' to INSTALLED-APPS in settings.py

- For AWS to save the static and media folders, the following content needs to be added to the custom_storages.py file:
```python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
And this code below must be added to the settings.py file for it to work:
```python
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
```

## Resources 
- [Code Institute](https://codeinstitute.net/)
- [StackOverflow](https://stackoverflow.com/questions/25406399/python-get-variable-outside-the-loop)
- [W3Schools](https://www.w3schools.com/python/python_file_handling.asp)
- [Reading and Writing files in Pure Python Documentation](https://python4mpia.github.io/pure_python/files.html)
- [StackOverflow](https://stackoverflow.com/questions/2415865/iterating-through-two-lists-in-django-templates)
- [StackOverflow](https://stackoverflow.com/questions/14841165/is-there-a-way-to-loop-over-two-lists-simultaneously-in-django/14841466)
- [Django documentation](https://docs.djangoproject.com/en/3.0/ref/models/querysets/)
- [jQuery API Documentation](https://api.jquery.com/val/)
- [PEP8 Validator](http://pep8online.com/)
- [JavaScript Validator](https://jshint.com/)
- [CSS Validator](http://csslint.net/)
- [HTML Validator](https://www.freeformatter.com/html-validator.html)

### Resources that helped me for testing 
- [StackOverflow](https://stackoverflow.com/questions/16143149/django-testing-check-messages-for-a-view-that-redirects/42252248)
- [StackOverflow](https://stackoverflow.com/questions/21215035/django-test-always-returning-301)
- [StackOverflow](https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages)

### Image
- Personal Smartphone Banner: https://www.pikrepo.com/fcncs/young-woman-holding-iphone-in-her-right-hand
- Smartphone Photography Banner: https://www.pikrepo.com/fvhil/man-capturing-a-stunning-sunset-with-his-mobile-iphone-smartphone-camera
- Smartphone Journey Banner: https://www.wallpaperflare.com/man-using-a-tablet-technology-work-hands-business-smartphone-wallpaper-wkkpa

- iPhone 11 Brand Examples: https://pixabay.com/de/illustrations/iphone-iphone-11pro-max-apple-4858453/
- Samsung S10E Brand Example: https://www.flickr.com/photos/nepaltibet2005/46208893305
- Huawei P30 Pro Bran Example: https://www.flickr.com/photos/janitors/33595154558
- LG V30 Example: https://commons.wikimedia.org/wiki/File:LG_V30_(cropped).jpg
- Xiaomi Redmi Note 9 Pro-Max Example: https://pixabay.com/de/illustrations/xiaomi-redmi-redmi-note-9-pro-max-4936657/

- Huawei Mate 20 Pro Photography: https://www.flickr.com/photos/janitors/31641238948
- iPhone Photography: https://www.wallpaperflare.com/iphone-photography-golden-gate-bridge-photo-backgrounds-earth-wallpaper-aazxq
- Samsung Galaxy S7 Photography: https://www.pexels.com/de-de/foto/samsung-galaxy-s7-rand-schone-blumen-verschwimmen-verwischen-706962/
- LG Photography: https://www.pxfuel.com/en/free-photo-qfbiw
- iPhone photography: https://www.pxfuel.com/en/free-photo-qwtlx

- Phone Shopping Link: https://www.flickr.com/photos/robbertjnoordzij/22257890101

- Phone Shop Banner: https://pixnio.com/media/hands-skin-telephone-mobile-phone 

## Acknowledgements 
I was inspired to do this project by [Code Institute](https://codeinstitute.net/). Thank you to my mentor, Brian Macharia to guide me throughout the process of the project! Thank you to the tutors, Michael, Tim, Xavier, Anna, Stephan, Kevin, Samantha, Haley, Luca and Niel for helping me with the problems that I encountered.




