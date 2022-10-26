from django.urls import path
from loveiscaring.views import index
from loveiscaring.views import register
from loveiscaring.views import login_user 
from loveiscaring.views import logout_user

app_name = 'loveiscaring'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]