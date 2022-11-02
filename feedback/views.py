from datetime import date
from multiprocessing import context
from django.shortcuts import render
from feedback.models import CardsFeedback
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def show_feedback(request):
    context = {
       "list": CardsFeedback.objects.all() 
    }
    return render(request, "feedback.html", context=context)

def show_json(request):
    data = CardsFeedback.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add(request):
    if request.method == "POST":
        rating = request.POST.get("rating")
        desc = request.POST.get("desc")
        card = CardsFeedback.objects.create(
            user=request.user,
            username=request.user.username,
            desc=desc,
            date=date,
            rating=rating,

        )
    return JsonResponse(
        {
            "pk": card.id,
            "fields": {
                "rating": card.rating,
                "desc": card.desc,
                "username": card.user.username,
                "date" : card.date,
                },
        }
    )