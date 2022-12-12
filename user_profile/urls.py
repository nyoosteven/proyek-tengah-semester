from django.urls import path
from user_profile.views import create_card_note, show_json, show_note_json, show_profile, show_profile_detail

app_name = 'user_profile'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('json/', show_json, name='show_json'),
    path('profile/', show_profile_detail, name='show_profile_detail'),
    path('jsonNote/', show_note_json, name='show_note_json'),
    path('create_card_note/', create_card_note, name='create_card_note'),

]