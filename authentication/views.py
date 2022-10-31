from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from authentication.forms import RegisterForm
# Create your views here.

def register_profile(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authentication:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def show_login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')


def is_logged_in(request):
    user = request.user
    if user.is_authenticated:
        return JsonResponse(user)

def validate_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Valid")
        else:
            return HttpResponse("not Valid")

    return HttpResponse("not Valid")
