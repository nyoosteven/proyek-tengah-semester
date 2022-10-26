from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from loveiscaring.models import Cards

# Create your views here.

def show_timeline(request):
    return render(request, 'timeline.html')

def show_json(request):
    data = Cards.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add(request):
    if request.method == "POST":
        text = request.POST.get("text")
        desc = request.POST.get("desc")
        card = Cards.objects.create(
            user=request.user,
            username=request.user.username,
            text=text,
            desc=desc,
        )
    return JsonResponse(
        {
            "pk": card.id,
            "fields": {
                "text": card.text,
                "desc": card.desc,
                "username": card.user.username,
                },
        }
    )