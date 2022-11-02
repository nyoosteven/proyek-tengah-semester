from artikel.models import *
from django.forms import ModelForm, Textarea

class MessageForm(ModelForm):
    class Meta(ModelForm):
        model = Cards
        fields = ['desc']
        widgets = {
            'desc': Textarea(attrs={'rows': 2, 'class': 'form-control', 'placeholder': 'desc'}),
        }
        labels = {
           'message' : '',
        }