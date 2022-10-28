from django.urls import path
from loveiscaring.views import index
from loveiscaring.views import logout_user

app_name = 'loveiscaring'

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout_user, name='logout'),
]