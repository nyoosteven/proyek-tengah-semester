from django.urls import path
from timeline.views import show_timeline

app_name = 'timeline'

urlpatterns = [
    path('', show_timeline, name='show_timeline'),
]