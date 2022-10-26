from django.urls import path
from loveiscaring.views import index
from loveiscaring.views import register
from loveiscaring.views import login_user 
from loveiscaring.views import logout_user
from loveiscaring.views import show_json
from loveiscaring.views import add
from loveiscaring.views import is_logged_in

app_name = 'loveiscaring'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'),
    path('add/', add, name='add'),
    path('is-logged-in/', is_logged_in, name='is_logged_in'),
]