from django.urls import path
from timeline.views import show_timeline
from timeline.views import show_json
from timeline.views import add

app_name = 'timeline'

urlpatterns = [
    path('', show_timeline, name='show_timeline'),
    path('json/', show_json, name='show_json'),
    path('add/', add, name='add'),
]