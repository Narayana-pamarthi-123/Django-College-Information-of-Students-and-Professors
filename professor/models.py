from django.db import models

# Create your models here.
class Professor(models.Model):
     Code= models.IntegerField(unique=True)
     Professor_name = models.CharField(max_length=100)
     Subject_name = models.CharField(max_length=10)
     Age = models.IntegerField(blank=True, null=True)
     Contact=models.CharField(max_length=10)
