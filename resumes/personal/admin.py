from django.contrib import admin

from .models import User, ProfessionChoices
# Register your models here.

admin.site.register(User)
admin.site.register(ProfessionChoices)
