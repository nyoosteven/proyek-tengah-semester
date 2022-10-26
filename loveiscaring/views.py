from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from loveiscaring.models import Cards

def index(request):
    return render(request, 'index.html')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('loveiscaring:index')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('loveiscaring:index')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('loveiscaring:index')

def show_json(request):
    data = Cards.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add(request):
    if request.method == "POST":
        text = request.POST.get("text")
        desc = request.POST.get("desc")
        task = Cards.objects.create(
            user=request.user,
            username=request.user.username,
            text=text,
            desc=desc,
        )
    return JsonResponse(
        {
            "pk": task.id,
            "fields": {
                "text": task.text,
                "desc": task.desc,
                "username": task.user.username,
                },
        }
    )