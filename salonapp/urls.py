from django.urls import path
from . import views
#from django.urls import path, include <- add this to line 17
# #if local host isnt open and is stuck on the django template and isn't showing hey welcome 

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('clients', views.clients, name='clients'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('form', views.form, name='form'), 
    path('profile', views.profile, name='profile'),
    path('calendar', views.calendar, name='calendar'),
    path('users/', views.get, name='get_user'),
    path('userupdated/', views.update_user, name='update_user'),
    path('useradded/', views.post_user, name='post_user'),
    path('userremoved/', views.delete_user, name='delete_user'),
] 
