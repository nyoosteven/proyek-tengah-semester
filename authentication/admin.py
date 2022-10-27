from django.contrib import admin
from .models import User
from loveiscaring.models import Cards
# Register your models here.

admin.site.register(User)
admin.site.register(Cards)