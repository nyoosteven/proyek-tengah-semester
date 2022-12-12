from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from timeline.models import Cards
from .forms import CreateCardForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def show_timeline(request):
    form = CreateCardForm()    
    if request.method == "GET":
        context = {'form': form}
        return render(request, 'timeline.html', context)
     
def show_json(request):
    data = Cards.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt   
def add_card(request):
    form = CreateCardForm(data=request.POST or None)    
    if request.method == "POST" and form.is_valid():
        data = form.save(request)
        return JsonResponse(
            data
        )

@csrf_exempt   
def add_card_flutter(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        desc = request.POST.get('desc')
        user = request.user
        card = Cards.objects.create(
            user=user,
            username=request.user.username,
            text=text,
            desc=desc,
        )
        return JsonResponse({"Message": "Task Success"},status=200)

@login_required(login_url="/authentication/login")       
def view_card(request, id, str):
    data = Cards.objects.filter(id=id)
    context = {'data': data, 'color': str}
    return render(request, 'viewcard.html', context)