from django.urls import path
from artikel.views import anxiety

app_name = 'artikel'

urlpatterns = [
    path('anxiety/', anxiety, name='anxiety'),
]