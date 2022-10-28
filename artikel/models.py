import imp
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cards(models.Model):
    desc = models.TextField()
    tipe = models.IntegerField(default=0)

class Cards_anxiety(models.Model):
    desc = models.TextField()

class Cards_depression(models.Model):
    desc = models.TextField()

class Cards_schizophrenia(models.Model):
    desc = models.TextField()

class Cards_eating(models.Model):
    desc = models.TextField()

class Cards_mood(models.Model):
    desc = models.TextField()

class Cards_ptsd(models.Model):
    desc = models.TextField()