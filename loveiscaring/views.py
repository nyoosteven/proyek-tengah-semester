from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    return redirect('loveiscaring:index')

def about(request):
    return render(request, 'about.html')