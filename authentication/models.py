from email.policy import default
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField(null=TRUE)
    date_birth = models.CharField(max_length=21)
    phone_number = models.CharField(max_length=12)