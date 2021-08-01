from django.contrib import admin
from .models import Payment, Users


# Register your models here 

admin.site.register(Users) #add new data base table in my app in admin
admin.site.register(Payment)
