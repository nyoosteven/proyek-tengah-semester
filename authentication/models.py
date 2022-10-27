
from asyncio.windows_events import NULL
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField()
    date_birth = models.CharField(max_length=21)
    phone_number = models.CharField(max_length=12)