from django.shortcuts import render
from django.shortcuts import redirect
from authentication.models import RegisterProfile

@login_required(login_url='/authentication/login/')

def show_profile(request):
    profile_items = RegisterProfile.objects.filter(user=request.user)
    user = request.user

    data = {
        'profile_items': profile_items,
        'nama': user
    }
    return render(request, "profile.html", data)

def edit_profile(request):
    return render