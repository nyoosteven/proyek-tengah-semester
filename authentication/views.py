from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from django.core import serializers
from authentication.forms import RegisterForm
from authentication.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json, re
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

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)

# @login_required(login_url='/login/')
# def get_user_data(request, username):
#     user = request.user

#     if request.method == "GET" and user.username == username:

#         # Mendapatkan objek dari database
#         profile_data = User.objects.filter(user = user)
#         profile_data_json = serializers.serialize('json', profile_data)
#         profile_data_json = re.sub('"user": [0-9]*,', f'"user": {getJsonUser(user)},', profile_data_json)

#         return HttpResponse(profile_data_json, content_type="application/json")

#     return HttpResponseNotFound()

# def getJsonUser(user):
#     user_data = {}

#     user_data['id'] = user.pk
#     user_data['is_superuser'] = user.is_superuser
#     user_data['username'] = user.username
#     user_data['first_name'] = user.first_name
#     user_data['last_name'] = user.last_name
#     user_data['email'] = user.email

#     return json.dumps(user_data)

@csrf_exempt
def login_flutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return JsonResponse({
            "status": True,
            "username": request.user.username,
            "message": "Successfully Logged In!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def logout_flutter(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({
                "status": True,
                "message": "Successfully Logout !"
                }, status=200)

@csrf_exempt
def register_flutter(request):
    if request.method == "POST":
        print(request.POST)
        data =request.POST

        username = data["username"]
        email = data["email"]
        password = data["password"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        age = data["age"]
        date_birth = data["date_birth"]
        phone_number = data["phone_number"]

        newUser = User.objects.create_user(
            username = username,
            email = email, 
            password = password,
            first_name = first_name,
            last_name = last_name, 
            age = age,
            date_birth = date_birth,
            phone_number = phone_number,
        )

        newUser.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
        