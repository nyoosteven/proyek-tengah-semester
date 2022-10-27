from authentication.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'date_birth', 'email', 'phone_number', 'username']