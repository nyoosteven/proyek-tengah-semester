from django.forms import ModelForm
from django import forms
from .models import Notes

class CreateNote(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}))
    description= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'description'}))
    
    class Meta:
        model = Notes
        fields = ('title', 'description')

    def save(self, request):
        user = request.user
        title = self.cleaned_data.get("title")
        description = self.cleaned_data.get("description")
        note = Notes.objects.create(
            user=request.user,
            username=request.user.username,
            title=title,
            description=description,
        )

        user.save()
        data =  {
            "pk": note.id,
            "fields": {
                "title": note.title,
                "description": note.description,
                "username": note.user.username,
                "date": note.date,
            },
        }
        return data