from authentication.models import RegisterProfile
from django.forms import ModelForm

class registerForm(ModelForm):
    class Meta:
        model = RegisterProfile
        fields = ['username', 'firstname', 'lastname', 'age', 'birth_date', 'email', 'phone_number']