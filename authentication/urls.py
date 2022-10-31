from django.urls import path
from authentication.views import register_profile
from authentication.views import login_user
from authentication.views import is_logged_in
from loveiscaring.views import index

app_name = 'authentication'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register_profile, name='register'),
    path('login/', login_user, name='login'),
]