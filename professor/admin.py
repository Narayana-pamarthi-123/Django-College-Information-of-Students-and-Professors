from django.contrib import admin
from .models import Professor

class Professoradmin(admin.ModelAdmin):

     list_display = ['id','Code','Professor_name','Subject_name','Age','Contact']

admin.site.register(Professor,Professoradmin)