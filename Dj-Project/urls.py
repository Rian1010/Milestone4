"""memorisation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index
from accounts import urls as accounts_urls
from phoneShop import urls as url_products
from checkout import urls as url_checkout
from search import urls as search_url
from cart import urls as url_cart
from django.views import static
from .settings import MEDIA_ROOT
"""I learned how to write the code bellow through Code Institute and it is the only way I know how to do it. 
Source: https://codeinstitute.net/"""


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^shop/', include(url_products)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^cart/', include(url_cart)),
    url(r'^checkout', include(url_checkout)),
    url(r'^search/', include(search_url)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
