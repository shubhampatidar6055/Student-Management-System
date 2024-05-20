from rest_framework import serializers
from .models import *


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Courseserializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'