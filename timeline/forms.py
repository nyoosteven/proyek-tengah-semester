from django.forms import ModelForm
from django import forms
from .models import Cards
from django.http import JsonResponse

class CreateCardForm(ModelForm):
    text= forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'id': 'text'}))
    desc= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'desc'}))
    class Meta:
        model = Cards
        fields = ('text', 'desc')

    def save(self, request):
        user = request.user
        text = self.cleaned_data.get("text")
        desc = self.cleaned_data.get("desc")
        card = Cards.objects.create(
            user=request.user,
            username=request.user.username,
            text=text,
            desc=desc,
        )

        user.save()
        data =  {
            "pk": card.id,
            "fields": {
                "text": card.text,
                "desc": card.desc,
                "username": card.user.username,
                },
        }
        return data