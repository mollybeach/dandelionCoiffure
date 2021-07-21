from django.http.response import BadHeaderError
from django.shortcuts import redirect, render
from django.http import HttpResponse, BadHeaderError
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db import connection
from salonapp.models import Feature, schedule
import calendar
from  calendar import HTMLCalendar
from django.core.mail import send_mail
from django.conf import settings
#from datatime import datetime


def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html',{'features': features})

# we have new variable that we get from feature.object.all() this variable is a list 
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
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else: 
        return render(request, 'register.html')
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
        return render(request, 'login.html', )

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    posts = [1,2,3,4,5, 'mary', 'jane', 'tom']
    return render(request, 'counter.html', {'posts' : posts})

def post(request, pk):
    return render(request, 'post.html', {'pk': pk}) #<--send that value in url to html ? 

def profile(request):
    userprofile = {'user': request.user}
    return render(request, 'profile.html', userprofile)

def clients(request):
    clients = {'user': request.user}
    return render(request, 'clients.html', clients)

def contact(request):
    contact = {'user': request.user}
    return render(request, 'contact.html', contact)
def about(request):
    about = {'user': request.user}
    return render(request, 'about.html', about)


def form(request):
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
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else: 
        return render(request, 'form.html')


def calendar(request):
    if request.method=="POST":
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email') and request.POST.get('telephone') and request.POST.get('appointment_date'):
            saveobj = schedule()
            saveobj.first_name=request.POST.get('first_name')
            saveobj.last_name=request.POST.get('last_name')
            saveobj.email=request.POST.get('email')
            saveobj.telephone=request.POST.get('telephone')
            saveobj.appointment_date=request.POST.get('appointment_date')
            subjectforclient='Appointment with MadeleineSalonDeCoiffure'
            subjectforhairdresser='Appointment with {saveobj.firstname} {saveobj.lastname} on {saveobj.appointmentdate} on  {saveobj.appointmentdate}'
            messageforclient='Thank you for scheduling an appointment with Madeleine for this date {saveobj.appointmentdate}'
            messageforhairdresser='You are scheduled to for an appointment with {saveobj.firstname} {saveobj.lastname} on {saveobj.appointmentdate} make sure to follow up with them at {saveobj.telephone}'
            cursor=connection.cursor()
            cursor.execute("INSERT INTO schedule(first_name, last_name, email, telephone, appointment_date) values(' "+saveobj.first_name+ "', ' "+saveobj.last_name+ "',  ' "+saveobj.email+ "',  ' "+saveobj.telephone+ "',  '" + saveobj.appointment_date+ "' )")
            messages.success(request, "Thank you! "+saveobj.first_name+ " "+saveobj.last_name+ "has successfully scheduled appointment on "+ saveobj.appointment_date)
            try:
                send_mail(subjectforclient, messageforclient, saveobj.email, saveobj.email)
                send_mail(subjectforhairdresser, messageforhairdresser, saveobj.email, ['madeleinesalondecoiffure@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'calendar.html')
    else:
        return render(request, 'calendar.html')



#['madeleinesalondecoiffure@gmail.com']




