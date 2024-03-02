from django.contrib import admin
from .models import User

class Useradmin(admin.ModelAdmin):
      pass


admin.site.register(User,Useradmin)