from django.forms import ModelForm
from django import forms
from .models import Notes

class CreateNote(ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}))
    description= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'description'}))
    
    class Meta:
        model = Notes
        fields = ('title', 'description')