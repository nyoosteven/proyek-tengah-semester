from django.forms import ModelForm
from django import forms
from .models import Cards

class CreateCardForm(ModelForm):
    text= forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'id': 'text'}))
    desc= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'desc'}))
    class Meta:
        model = Cards
        fields = ('text', 'desc')