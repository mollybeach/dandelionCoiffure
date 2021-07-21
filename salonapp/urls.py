from django.urls import path
from . import views
#from django.urls import path, include <- add this to line 17
# #if local host isnt open and is stuck on the django template and isn't showing hey welcome 

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter') ,
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post') ,
    path('form', views.form, name='form'), 
    path('profile', views.profile, name='profile'),
    path('clients', views.clients, name='clients'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('calendar', views.calendar, name='calendar'),
] 