from django.urls import path
from user_profile.views import show_json, show_profile

app_name = 'user_profile'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('json/', show_json, name='show_json'),

]