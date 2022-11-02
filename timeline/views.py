from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from timeline.models import Cards
from .forms import CreateCardForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def show_timeline(request):
    form = CreateCardForm()    
    if request.method == "GET":
        context = {'form': form}
        return render(request, 'timeline.html', context)
     
def show_json(request):
    data = Cards.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url="/authentication/login")       
def add_card(request):
    form = CreateCardForm(data=request.POST or None)    
    if request.method == "POST" and form.is_valid():
        data = form.save(request)
        return JsonResponse(
            data
        )
    else:
        return HttpResponse("gagal")

@login_required(login_url="/authentication/login")       
def view_card(request, id, str):
    data = Cards.objects.filter(id=id)
    context = {'data': data, 'color': str}
    return render(request, 'viewcard.html', context)