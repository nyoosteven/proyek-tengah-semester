from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from timeline.models import Cards
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from user_profile.form import CreateNote
from user_profile.models import Notes



@login_required(login_url='/authentication/login/')

def show_profile(request):
    form = CreateNote(data=request.POST or None)    
    new_note = None
    if request.method == "GET":
        context = {'form': form}
        return render(request, 'profile.html', context)

def show_json(request):
    data = Cards.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_note_json(request):
    dataNote = Notes.objects.all()
    return HttpResponse(serializers.serialize("json", dataNote), content_type="application/json")

def create_card_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_note = Notes.objects.create(
            user=request.user,
            username=request.user.username,
            title=title,
            description=description,
            date=datetime.now()
        )
        new_note.save()
        
        return redirect('user_profile:show_profile')
    return render(request, 'profile.html')

def deleteNote(request, noteId):
    deleted_task = Notes.objects.get(id=noteId)
    deleted_task.delete()
    return redirect("user_profile:show_profile")
