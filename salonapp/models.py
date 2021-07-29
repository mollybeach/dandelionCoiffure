from django.db import models
from django import forms
from datetime import datetime
# Create your models here.
class Users(models.Model):
    firstname = models.CharField(max_length=2000, null=True, blank=True, default=None)
    lastname = models.TextField(max_length=20000, null=True, blank=True, default=None)
    email = models.TextField(max_length=20000, null=True, blank=True, default=None)
    service = models.TextField(max_length=20000, null=True, blank=True, default=None)
    telephone = models.TextField(max_length=20000, null=True, blank=True, default=None)
    appointmentdate= models.TextField(max_length=20000, null=True, blank=True, default=None)
    def _str_(self):
        return self.firstname +" " + self.lastname + " " +self.email+" "+self.service+" "+self.telephone+" "+self.appointmentdate







