<<<<<<< Updated upstream
from datetime import datetime
from inspect import formatannotationrelativeto
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from timeline.models import Cards
=======
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from loveiscaring.models import Cards
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
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

def deleteNote(noteId):
    delete_note = Notes.objects.get(id=noteId)
    delete_note.delete()
    return redirect("user_profile:show_profile")
=======
def edit(request):
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
>>>>>>> Stashed changes
