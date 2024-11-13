from django.urls import path
from django_distill import distill_path
from . import views

def get_none():
    return None

urlpatterns = [
    distill_path('', views.index, name='index', distill_func=get_none),
    distill_path('about.html', views.about, name='about', distill_func=get_none),
    distill_path('contact.html', views.contact, name='contact', distill_func=get_none),
    distill_path('clients', views.clients, name='clients', distill_func=get_none),
    distill_path('register', views.register, name='register', distill_func=get_none),
    distill_path('login', views.login, name='login', distill_func=get_none),
    distill_path('profile', views.profile, name='profile', distill_func=get_none),
    distill_path('calendar', views.calendar, name='calendar', distill_func=get_none),
    
    # Dynamic views that are not suitable for static rendering
    path('logout', views.logout, name='logout'),
    path('users/', views.get, name='get_user'),
    path('userupdated/', views.update_user, name='update_user'),
    path('useradded/', views.post_user, name='post_user'),
    path('userremoved/', views.delete_user, name='delete_user'),
]
