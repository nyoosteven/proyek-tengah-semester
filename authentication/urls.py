from django.urls import path
from authentication.views import register_profile
from authentication.views import show_login
from authentication.views import is_logged_in
from loveiscaring.views import index
from authentication.views import validate_login

app_name = 'authentication'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register_profile, name='register'),
    path('login/', show_login, name='login'),
    path('login/validate/', validate_login, name = 'validate_login')
]