from django.conf.urls import url
from .views import cart_views, cart_additions, cart_adjustments 
from accounts.views import user_profile
"""I learned how to write the code bellow through Code Institute and it is the only way I know how to do it. 
Source: https://codeinstitute.net/"""


urlpatterns = [
    url(r'^$', cart_views, name="cart_views"),
    url(r'^add/(?P<id>\d+)', cart_additions, name="cart_additions"),
    url(r'^adjustment/(?P<id>\d+)', cart_adjustments, name="cart_adjustments")
]