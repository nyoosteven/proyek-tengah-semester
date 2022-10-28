from django.urls import path
from timeline.views import show_timeline
from timeline.views import show_json
from timeline.views import add_card
from timeline.views import view_card

app_name = 'timeline'

urlpatterns = [
    path('', show_timeline, name='show_timeline'),
    path('json/', show_json, name='show_json'),
    path('add-card/', add_card, name='add_card'),
    path("view_card/<int:id>/<str:str>", view_card, name="view_card"),
]