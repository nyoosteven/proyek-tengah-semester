from django.urls import path
from feedback.views import show_feedback
from feedback.views import add
from feedback.views import show_json
# from feedback.views import add_feedback

app_name = 'feedback'

urlpatterns = [
    path('', show_feedback, name='show_feedback'),
    path('add', add, name='add'),
    path('json', show_json, name='show_json'),
]

