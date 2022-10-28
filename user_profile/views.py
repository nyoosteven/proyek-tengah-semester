from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from loveiscaring.models import Cards
from django.http import HttpResponse
from django.core import serializers

@login_required(login_url='/authentication/login/')

def show_profile(request):
    return render(request, "profile.html")

def show_json(request):
    data = Cards.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def delete_quote(request):
    return render