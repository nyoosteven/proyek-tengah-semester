from django.urls import path
from user_profile.views import show_profile
from user_profile.views import edit_profile

app_name = 'user_profile'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),

]