from email.policy import default
from django.db import models
from authentication.models import User
import datetime

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.TextField(default="USER")
    title = models.TextField()
    description = models.TextField()
    date = models.DateField(default=datetime.datetime.now())

