from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password,check_password 
from django.contrib import messages
from django.db.models import  Q
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
            messages.error(request, "Invalid Id Password")
            return redirect('/')
def sign_up(request):
    return render(request,"sign-up.html")

def sign_up_data(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if User.objects.filter(email = email).exists():
            messages.error(request, "Email Already Exists")
            return redirect('/sign_up')
        else:
            User.objects.create(name=name, email=email, password=password)
            return redirect('/dashboard/')
        
def viewstudents(request):
    course_obj = Course.objects.all()
    student_obj = Student.objects.all()
    return render(request, "viewstudents.html", {"course_obj":course_obj, "student_obj":student_obj})

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
            messages.error(request, "Email Already Exists")
            return redirect('/viewstudents/')
        elif Student.objects.filter(mobile_no=mobile_no).exists():
            messages.error(request, "Mobile Number Already Registered")
            return redirect('/viewstudents/')
        else:
            Student.objects.create(name=name, email=email,mobile_no=mobile_no, college=college, degree=degree,
                                   address=address, image=image, courses=new_course)
            return redirect("/viewstudents/")
def update_student(request,uid):
    course_obj = Course.objects.all()
    student_update = Student.objects.get(id=uid)
    return render(request, "update_students.html", {"course_obj":course_obj, "student_update":student_update})

def update_student_data(request):
    if request.method == "POST":
        uid = request.POST.get('uid')
        name = request.POST.get('name')
        mobile_no = request.POST.get('mobile_no')
        college = request.POST.get('college')
        degree = request.POST.get('degree')
        address = request.POST.get('address')
        image = request.POST.get('image')
        course_id = request.POST.get('courses')
        new_course = Course.objects.get(id=course_id)
        Student.objects.filter(id=uid).update(name=name, mobile_no=mobile_no, college=college, degree=degree,
                                              address=address, image=image, courses=new_course)
        messages.success(request, "Student Update Sucessfully")
        return redirect('/viewstudents/')

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(name__icontains = q) | Q(email__icontains = q)) | Q(mobile_no__icontains = q)
        student_obj =Student.objects.filter(multiple_q)
        print(multiple_q)
    else:
        student_obj = Student.objects.all()
    context = {'student_obj':student_obj}
    return render(request, "viewstudents.html", context)
    
# def student_profile(request,pk):
#     Student.objects.get(id=pk)
#     return redirect('/profile/')

def delete_student(request,pk):
    Student.objects.get(id=pk).delete()
    return redirect('/viewstudents/')

def profile(request,pk):
    student_obj = Student.objects.get(id=pk)
    return render(request, "profile.html", {"student_obj":student_obj})

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
            messages.error(request, "Course Already Exists")
            return redirect('/courses/')
        else:
            Course.objects.create(course_name=course_name, fees=fees, duration=duration)
            return redirect("/courses/")

def delete_course(request,pk):
    Course.objects.get(id=pk).delete()
    return redirect('/courses/')

def update_course(request,uid):
    course_update = Course.objects.get(id=uid)
    return render(request, "update_course.html", {"course_update":course_update})

def update_courses(request):
    if request.method == "POST":
        uid = request.POST['uid']
        course_name = request.POST['course_name']
        fees = request.POST['fees']
        duration = request.POST['duration']
        Course.objects.filter(id=uid).update(course_name=course_name, fees=fees, duration=duration)
        messages.success(request, "Course Update Sucessfully")
        return redirect('/courses/')
