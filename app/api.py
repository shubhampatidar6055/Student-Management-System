from .models import *
from rest_framework import generics
from .serializer import Userserializer

class Userapi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

class updateuserapi(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

class deleteuserapi(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer