from django.db import models
from django import forms
from datetime import datetime
# Create your models here.
class Feature(models.Model): 
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)


class schedule(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    service=models.CharField(max_length=150)
    telephone=models.CharField(max_length=150)
    appointment_date=models.DateTimeField() 









