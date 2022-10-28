from django.urls import path
from artikel.views import anxiety,depression,schizophrenia,eating,mood,ptsd,addcard
from artikel.views import *
app_name = 'artikel'

urlpatterns = [
    path('anxiety/', anxiety, name='anxiety'),
    path('depression/',depression,name='depression'),
    path('schizophrenia/',schizophrenia,name='schizophrenia'),
    path('eating/',eating,name='eating'),
    path('mood/',mood,name='mood'),
    path('ptsd/',ptsd,name='ptsd'),
    path('addcard/<int:tipe>',addcard,name='addcard'),
    path('json/<int:tipe>', show_json, name='show_json'),
]