from django.urls import path
from artikel.views import anxiety,depression,schizophrenia,eating,mood,ptsd

app_name = 'artikel'

urlpatterns = [
    path('anxiety/', anxiety, name='anxiety'),
    path('depression/',depression,name='depression'),
    path('schizophrenia/',schizophrenia,name='schizophrenia'),
    path('eating/',eating,name='eating'),
    path('mood/',mood,name='mood'),
    path('ptsd/',ptsd,name='ptsd')
]