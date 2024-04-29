from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
def index(request):
    return render(request, "index.html")

def sign_in(request):
    if request.method == "POST":
        user = User.objects.get(email = request.POST['email'])
        if check_password(request.POST['password'],user.password):
            request.session['login'] = True
            request.session['email'] = User.email
            return redirect('/dashboard/')
        else:
            return HttpResponse("Invalid Id Password")
        
def sign_up(request):
    return render(request,"sign-up.html")

def sign_up_data(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if User.objects.filter(email = email).exists():
            return("Email Already Exists")
        else:
            User.objects.create(name=name, email=email, password=password)
            return redirect('/dashboard/')
        
def viewstudents(request):
    return render(request,"viewstudents.html")

def profile(request):
    return render(request,"profile.html")

def dashboard(request):
    return render(request,"dashboard.html")

def courses(request):
    return render(request,"courses.html")