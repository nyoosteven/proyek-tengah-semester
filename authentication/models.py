
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class RegisterProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    birth_date = models.CharField(max_length=17)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)