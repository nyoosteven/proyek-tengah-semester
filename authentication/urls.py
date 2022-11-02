from django.urls import path
from authentication.views import register_profile
from authentication.views import show_login
from authentication.views import is_logged_in
from loveiscaring.views import index
from authentication.views import validate_login
from authentication.views import validate_username

app_name = 'authentication'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register_profile, name='register'),
    path('login/', show_login, name='login'),
    path('login/validate/', validate_login, name = 'validate_login'),
    path('register/validate/', validate_username, name = 'validate_username'),
]