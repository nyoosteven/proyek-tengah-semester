from django.shortcuts import render

# Create your views here.

def show_timeline(request):
    return render(request, 'timeline.html')