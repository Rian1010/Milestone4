from django.conf.urls import url
from .views import search_function

urlpatterns = [
    url(r'^$', search_function, name="search")
]