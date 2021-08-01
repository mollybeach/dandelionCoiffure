from django.shortcuts import redirect, render
from django.http.response import HttpResponse, BadHeaderError, JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.db import connection
from django.contrib import messages
from salonapp.models import Users, Payment
import calendar
from  calendar import HTMLCalendar
from django.core.mail import send_mail
from django.conf import settings
from django.template import RequestContext, loader
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
#import models 
from salonapp import models
from json import dumps
import json
from django.core import serializers

def index(request):
    return render(request, 'users/index.html')
appname = 'Users'

@csrf_exempt
def calendar(request):
    eventdata = serializers.serialize('json', Users.objects.all())
    result = dumps(eventdata)
    return render(request, 'calendar.html', {'result': result})

@csrf_exempt
def get(request):
    context= serializers.serialize('json', Users.objects.all())
    return JsonResponse(context, safe=False)

            
@csrf_exempt
def post_user(request):
    if request.method == 'POST':
        rp = json.loads(request.body.decode('utf-8'))
        user = Users(firstname=rp['firstname'],lastname=rp['lastname'],email=rp['email'],service=rp['service'],telephone=rp['telephone'],appointmentdate=rp['appointmentdate'],time=rp['time'])
        user.save()
        context = serializers.serialize('json', Users.objects.all())
        subjectforclient="Appointment with MadeleineSalonDeCoiffure on  '" + user.appointmentdate+ "'  for  '" + user.service+ "'"
        subjectforhairdresser="Client Appointment with ' "+user.firstname+ "' ' "+user.lastname+ "' on  '" + user.appointmentdate+ "'  for  '" + user.service+ "'"
        messageforclient="Thank you for scheduling an appointment with Madeleine for this date  '" + user.appointmentdate+ "' "
        messageforhairdresser="You are scheduled with' "+user.firstname+ "' ' "+user.lastname+ "'  for  '" + user.appointmentdate+ "' please make sure to follow up with your client at either' "+user.email+ "' or  ' "+user.telephone+ "' "
        try:
                send_mail(subjectforclient, messageforclient, user.email, [user.email])
                send_mail(subjectforhairdresser, messageforhairdresser, user.email, ['madeleinesalondecoiffure@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return JsonResponse(context, safe=False)
    else:
        return render(request, 'calendar.html')

@csrf_exempt
def delete_user(request):
    rp=json.loads(request.body.decode('utf-8'))
    Users.objects.get(pk=rp['pk']).delete()
    return get(request)

@csrf_exempt
def update_user(request):
    rp=json.loads(request.body.decode('utf-8'))
    field = Users.objects.get(pk=rp['pk'])
    field.firstname=rp['firstname']
    field.lastname=rp['lastname']
    field.email=rp['email']
    field.service=rp['service']
    field.telephone=rp['telephone']
    field.appointmentdate=rp['appointmentdate']
    field.time=rp['time']
    field.save()
    return get(request)
@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else: 
               # user = User.objects.request.POST(username = request.POST['username'],email=request.POST['email'])
                info = User.objects.create_user(username=username, email=email, password=password)
                info.save();
                subjectfornewuser="Thank you for creating an account with MadeleineSalonDeCoiffure  '" + info.username+ "'  for  '" + info.email+ "'"
                subjectforhairdressernewuser="A new client has created an account with MadeleineSalonDeCoiffure: '" + info.username+ "'  for  '" + info.email+ "'"
                messagefornewuser="Thank you for creating an account with MadeleineSalonDeCoiffure  '" + info.username+ "'  for  '" + info.email+ "'"
                messageforhairdressernewuser="A new client has created an account with MadeleineSalonDeCoiffure: '" + info.username+ "'  for  '" + info.email+ "'"
                try:
                        send_mail(subjectfornewuser, messagefornewuser, info.email, [info.email])
                        send_mail(subjectforhairdressernewuser, messageforhairdressernewuser, info.email, ['madeleinesalondecoiffure@gmail.com'])
                        messages.success(request, 'Account successfully created check your email for conformation')
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else: 
        return render(request, 'register.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None: #check if user None that means is not register
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'User does not exist please create an account')
            return redirect('register')
    else:
        messages.success(request, 'Logging in!')
        return render(request, 'login.html', )

@csrf_exempt
def logout(request):
    messages.success(request, 'Logging out')
    auth.logout(request)
    return redirect('/')

@csrf_exempt
def profile(request):
    messages.success(request, 'Signed in!')
    userprofile = {'user': request.user}
    return render(request, 'profile.html', userprofile)

@csrf_exempt
def clients(request):
    return render(request, 'clients.html')

@csrf_exempt
def contact(request):
    return render(request, 'contact.html')

@csrf_exempt
def about(request):
    return render(request, 'about.html')

@csrf_exempt
def payment(request):
    billingdata = serializers.serialize('json', Payment.objects.all())
    result = dumps(billingdata)
    return render(request, 'payment.html', {'result': result})








        


