
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from timeline.models import Cards
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from user_profile.form import CreateNote
from user_profile.models import Notes


@login_required(login_url='/authentication/login/')

def show_profile(request):
    form = CreateNote(data=request.POST or None)    

    if request.method == "GET":
        context = { 'form': form }
        return render(request, 'profile.html', context)

def show_json(request):
    data = Cards.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_profile_detail(request):
    return JsonResponse({
    "fields": {
        "fn": request.user.first_name,
        "ln": request.user.last_name,
        "age": request.user.age,
        "bd": request.user.date_birth,
        "em": request.user.email,
        "pn": request.user.phone_number,
        },
    })

def show_note_json(request):
    dataNote = Notes.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", dataNote), content_type="application/json")

@login_required(login_url='/authentication/login/')
def create_card_note(request):
    formNote = CreateNote(data=request.POST or None)    
    if request.method == "POST" and formNote.is_valid():
        data = formNote.save(request)
        return JsonResponse(
            data
        )

