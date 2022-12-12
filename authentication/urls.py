from django.urls import path
from authentication.views import register_profile
from authentication.views import show_login
from authentication.views import is_logged_in
from loveiscaring.views import index
from authentication.views import validate_login
from authentication.views import *
#from authentication.views import get_user_data


app_name = 'authentication'

urlpatterns = [
    path('', index, name='index'),
    path('login-async/', login_flutter, name='login-async'),
    path('register-async/', register_flutter, name='register-async'),
    path('logout-async/', logout_flutter, name='logout-async'),
    path('register/', register_profile, name='register'),
    path('login/', show_login, name='login'),
    path('login/validate/', validate_login, name = 'validate_login'),
    path('register/validate/', validate_username, name = 'validate_username'),
    #path('register/json/', get_user_data, name = '')
]