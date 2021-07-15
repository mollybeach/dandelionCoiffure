from django.db import models
from django import forms
# Create your models here.


#create your models here 
class Feature(models.Model): 
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100)
'''
class Feature:
    id : int 
    name : str
    details : str
    is_true : bool
'''

# without migrations 
# 
