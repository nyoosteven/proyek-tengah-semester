from django.contrib import admin
from .models import User
from timeline.models import Cards
# Register your models here.

admin.site.register(User)
admin.site.register(Cards)