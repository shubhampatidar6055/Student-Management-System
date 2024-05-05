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
    course_obj = Course.objects.all()
    return render(request, "viewstudents.html", {"course_obj":course_obj})

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        college = request.POST.get('college')
        degree = request.POST.get('degree')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        course_id = request.POST.get('courses')
        new_course = Course.objects.get(id=course_id)
        if Student.objects.filter(email=email).exists():
            return HttpResponse("Email Already Exists")
        elif Student.objects.filter(mobile_no=mobile_no).exists():
            return HttpResponse("Mobile Number Already Registered")
        else:
            Student.objects.create(name=name, email=email,mobile_no=mobile_no, college=college, degree=degree,
                                   address=address, image=image, courses=new_course)
            return redirect("/viewstudents/")

def profile(request):
    return render(request,"profile.html")

def dashboard(request):
    return render(request,"dashboard.html")

def courses(request):
    course_obj = Course.objects.all()
    return render(request, "courses.html", {"course_obj":course_obj})

def course_registration(request):
    if request.method == "POST":
        course_name = request.POST['course_name']
        fees = request.POST['fees']
        duration = request.POST['duration']
        if Course.objects.filter(course_name=course_name).exists():
            return HttpResponse("Course Already Exists")
        else:
            Course.objects.create(course_name=course_name, fees=fees, duration=duration)
            return redirect("/courses/")
