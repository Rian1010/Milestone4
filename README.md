# Phone-Shop
This is my fourth Milestone Project that I have done on the Full Stack Software Development course at Code Institute. In this project, the main focus was using Django. 

## Purpose of This Project
This project is an e-commerce website to sell trending mobile phones from all over the world. Users can easily search for their desired brands that vary at different prices and can choose how many they want to put into a shopping-cart to purchase. 

These are the following sections of the website:
- Home page: As it is the first page that a user gets to see, it contains examples of product that are being sold, examples of smartphone photography and a section for the call to action of buying a product. 

- Login/Registration Page: Enables users to sign in or sign up to visit the rest of the web pages, besides the home page.

- Reset Password Page: Allows a user to reset one's own password.

- Shop Page: The page that contains all products that the website has to offer. A user can add a product from that page to the cart page.

- Cart Page: A logged in user can see the items that one has added into the cart, how much the total price is and each chosen product's details, before checking out. 

- Profile Page: Shows the user account's information and order history.

- Logout: Allows a user to sign out of the website

-Notes: Reset Password, second home page section

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

The overall design was inspired from what I was taught about web designing at Code Institute and an internship that I did, before starting this project, at [The Ambitious](www.theambitious.de) from Jan Ruthard. The colours that I used were white, orange and blue. I wanted to use bright colours that match well together, such as white, light blue and light orange, so that it would give off a positive look on first glance, but still a sense of importance by usind sharp edges on the pictures and boxes and not choosing too light colours.

The font that I used was the default sans-serif font-family, as I found it fitting to the website and theme already.

## Wireframes

## Features

## Utilised Technologies
### Languages
- HTML5
- CSS3
- JavaScript
- Python3

### Frameworks
- Django 1.11.24
- Bootstrap 4

### Database
- PostgresSql: from Heroku
- SQLite3: from Django

### API
- Stripe

### Validators

### Other Tools
- Github: hosts the website
- Git: version control
- Heroku: app Deployment
- Gunicorn: runs Python applications
- Travis CI: continiuous integration
- AWS S3 Bucket: cloud storage
- VSCode: code editor
- Psycopg2-Binary: to connect Python to the database
- Pillow: stores images with the usage of django on the website
- (MiniWebtool)[https://miniwebtool.com/django-secret-key-generator/]: generates new SECRET_KEY

## Process 
### Django
Most of the Django code was heavily inspired from what's been taught at (Code Institute)[https://courses.codeinstitute.net/program/FullstackWebDeveloper]

## Testing
### Manual Testing

### Automated Testing

- Messages and warnings

## Deployment 
### Deployment to Github

### Deployment to Heroku

### Amazon Web Services

## Resources 
### Image
- Personal Smartphone Banner: https://www.pikrepo.com/fcncs/young-woman-holding-iphone-in-her-right-hand
- Smartphone Photography Banner: https://www.pikrepo.com/fvhil/man-capturing-a-stunning-sunset-with-his-mobile-iphone-smartphone-camera
or 
https://www.pikist.com/free-photo-xzmyu
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

## Coverage
- sudo pip3 install coverage
- coverage run manage.py test
- coverage report 
- coverage run --source=accounts manage.py test
- coverage report (Shows how much code has been tested)
- coverage html

## Heroku Deployment
- In Resources, add Heroku Postgres in add-ons
- Get the DATABASE_URL in the conguration variables and copy it into the env.py file
- os.environ.setdefault("DATABASE_URL", "postgres://---")
- Do the same to SECRET_KEY and STRIPE_PUBLISHABLE
- sudo pip3 install dj-database-url
- sudo pip3 install psycopg2-binary
- pip3 freeze > requirements.txt
- import dj_database_url in settings.py
- Switch DATABASE to postgres in settings.py
- Migrate the existing migrations to the postgres database, although there are no changes detected through python3 manage.py makemigrations

## Amazon Web Services
- Once logged in, choose S3 
- Untick all checkboxes in 'Set Permissions'
- Open the bucket
- Go to Properties and then 'Static website hosting'
- Click on 'Use this bucket to host a website' and input 'index.html' and 'error.html'
- Click on Permissions, then CORS configuration
- Paste in the following LMS:
```html
<CORSConfiguration>
<CORSRule>
<AllowedOrigin>*</AllowedOrigin>
<AllowedMethod>GET</AllowedMethod>
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
- Go to dashboard, then groups with a click or the link extension of /iam/home?eu-region-west-1%2A%2Fpolicies=#/groups or /iam/home?eu-region-west-1*/groups
- Click on Policy and Create a new policy
- Click on Import managed policy
- Search for s3 and choose AmazonS3FullAccess
- In JSON, change the string from 'Resource' to a list and add ["arn:aws:s3:::bucket-name"], ["arn:aws:s3:::bucket-name/*"]
- Click on the Review Policy button and give it a name, such as bucket-name-policy
- Go to the created group, go to permissions, search for the policy just created, check it and click on the 'Attach policy' button
- Click on Users in the side-navigation-bar, then click on Add User and name it with something that is associated with the bucket name and tick programmatic access
- Choose the created group, skip the keys, as they're not needed and create the user
- IMPORTANT!!! Make sure to download the .csv, This is the access keys that you will need in your software, It's important to keep them safe. You'll never be able to generate them again. So if you lose them you would have to delete the user and create a new user with new access keys
- Go back to S3, click on the bucket and test it by trying to upload a file (Eg. an image)
- The image should have a link that can be accessed from anywhere

## Change the code for S3
- sudo pip3 install django-storages
- sudo pip3 install boto3 
- Include 'storages' to INSTALLED-APPS in settings.py