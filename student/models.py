from datetime import datetime

from django.db import models

# Create your models here.





class Student(models.Model):
    Roll_number=models.IntegerField(unique=True)
    Student_name=models.CharField(max_length=100)
    Branch_name=models.CharField(max_length=4)
    Age=models.IntegerField(blank=True,null=True)
    Date_of_joining = models.DateField(default=datetime.now())


















