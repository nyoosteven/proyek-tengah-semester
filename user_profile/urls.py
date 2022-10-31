from django.urls import path
from user_profile.views import create_card_note, deleteNote, show_json, show_note_json, show_profile

app_name = 'user_profile'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('json/', show_json, name='show_json'),
    path('deleteNote/<int:taskId>', deleteNote, name='deleteNote'),
    path('jsonNote/', show_note_json, name='show_note_json'),
    path('create_card_note/', create_card_note, name='create_card_note'),

]