from django.contrib import admin
from .models import Student

class Studentadmin(admin.ModelAdmin):

     list_display = ['id','Roll_number','Student_name','Branch_name','Age','Date_of_joining']

admin.site.register(Student,Studentadmin)


