from django.db import models
from authentication.models import User

# Create your models here.
class Cards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.TextField(default="USER")
    text = models.TextField()
    desc = models.TextField()

    def __str__(self):
        return self.text[0:29] + "... by " + self.username if len(self.text) >= 30 else self.text + " by " + self.username