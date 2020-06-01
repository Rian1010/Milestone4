from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile
from accounts import urls_reset
"""I learned how to write this code bellow through Code Institute and it is the only way I know doing it ´. Source: https://codeinstitute.net/"""


urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/(?P<pk>\d+)/', user_profile, name="profile"), 
    url(r'^password-reset/', include(urls_reset))
]
