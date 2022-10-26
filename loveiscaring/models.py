from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.TextField(default="USER")
    text = models.TextField()
    desc = models.TextField()