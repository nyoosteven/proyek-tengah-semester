import imp
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cards(models.Model):
    desc = models.TextField()