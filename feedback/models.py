from django.db import models
from authentication.models import User

# Create your models here.
class CardsFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.TextField(default="USER")
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField()