from django.shortcuts import redirect, render
from django.http.response import HttpResponse, BadHeaderError, JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.db import connection
from django.contrib import messages
from salonapp.models import Users, Payment
import calendar
from calendar import HTMLCalendar
from django.core.mail import send_mail
from django.conf import settings
from django.template import RequestContext, loader
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from salonapp import models
from json import dumps
import json
from django.core import serializers

# Static views suitable for `django-distill` rendering
def index(request):
    return render(request, 'index.html')
@csrf_exempt
def about(request):
    return render(request, 'about.html')

@csrf_exempt
def contact(request):
    return render(request, 'contact.html')

@csrf_exempt
def clients(request):
    return render(request, 'clients.html')

@csrf_exempt
def register(request):
    return render(request, 'register.html')

@csrf_exempt
def login(request):
    return render(request, 'login.html')

@csrf_exempt
def profile(request):
    userprofile = {'user': request.user}
    return render(request, 'profile.html', userprofile)

@csrf_exempt
def calendar(request):
    if settings.ENVIRONMENT == 'github-pages':
        # Static sample data for GitHub Pages
        sample_data = [
            {
                "model": "salonapp.users",
                "pk": 1,
                "fields": {
                    "firstname": "Sample",
                    "lastname": "Client",
                    "email": "sample@email.com",
                    "service": "Haircut",
                    "telephone": "123-456-7890",
                    "appointmentdate": "2024-03-20",
                    "time": "10:00"
                }
            }
        ]
        result = dumps(sample_data)
    else:
        # Normal database query for local/Heroku
        eventdata = serializers.serialize('json', Users.objects.all())
        result = dumps(eventdata)
    
    return render(request, 'calendar.html', {'result': result})

@csrf_exempt
def payment(request):
    billingdata = serializers.serialize('json', Payment.objects.all())
    result = dumps(billingdata)
    return render(request, 'payment.html', {'result': result})

# Dynamic views not suitable for static rendering
@csrf_exempt
def get(request):
    context = serializers.serialize('json', Users.objects.all())
    return JsonResponse(context, safe=False)

@csrf_exempt
def post_user(request):
    if request.method == 'POST':
        rp = json.loads(request.body.decode('utf-8'))
        user = Users(
            firstname=rp['firstname'],
            lastname=rp['lastname'],
            email=rp['email'],
            service=rp['service'],
            telephone=rp['telephone'],
            appointmentdate=rp['appointmentdate'],
            time=rp['time']
        )
        user.save()
        context = serializers.serialize('json', Users.objects.all())

        # Email notifications
        subject_for_client = f"Appointment with MadeleineSalonDeCoiffure on {user.appointmentdate} for {user.service} has been scheduled successfully!"
        subject_for_hairdresser = f"Client Appointment with {user.firstname} {user.lastname} on {user.appointmentdate} for {user.service}"
        message_for_client = f"Thank you for scheduling an appointment with Madeleine for this date {user.appointmentdate}."
        message_for_hairdresser = f"You are scheduled with {user.firstname} {user.lastname} for {user.appointmentdate}. Please follow up with the client at {user.email} or {user.telephone}."

        try:
            messages.success(request, f"{subject_for_client}. Please check your email for confirmation.")
            send_mail(subject_for_client, message_for_client, user.email, [user.email])
            send_mail(subject_for_hairdresser, message_for_hairdresser, user.email, ['madeleinesalondecoiffure@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        return JsonResponse(context, safe=False)
    else:
        return render(request, 'calendar.html')

@csrf_exempt
def delete_user(request):
    rp = json.loads(request.body.decode('utf-8'))
    Users.objects.get(pk=rp['pk']).delete()
    return get(request)

@csrf_exempt
def update_user(request):
    rp = json.loads(request.body.decode('utf-8'))
    user = Users.objects.get(pk=rp['pk'])
    user.firstname = rp['firstname']
    user.lastname = rp['lastname']
    user.email = rp['email']
    user.service = rp['service']
    user.telephone = rp['telephone']
    user.appointmentdate = rp['appointmentdate']
    user.time = rp['time']
    user.save()
    return get(request)

@csrf_exempt
def logout(request):
    messages.success(request, 'Logging out')
    auth.logout(request)
    return redirect('/')

