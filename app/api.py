from .models import *
from rest_framework import generics
from .serializer import Userserializer,Courseserializer,Studentserializer

class Userapi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

class updateuserapi(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

class deleteuserapi(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

class Courserapi(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = Courseserializer

class updatecourseapi(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = Courseserializer


class deletecourseapi(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = Courseserializer

class Studentapi(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

class updatestudentseapi(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

class deletestudentapi(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer