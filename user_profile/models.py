from email.policy import default
from django.db import models
from authentication.models import User
<<<<<<< Updated upstream
import datetime

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.TextField(default="USER")
    title = models.TextField()
    description = models.TextField()
    date = models.DateField(default=datetime.datetime.now())
=======
# from loveiscaring.models import Cards

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # quote= models.ForeignKey(Cards, on_delete=models.CASCADE)
>>>>>>> Stashed changes
