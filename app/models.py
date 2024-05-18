from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)
    def __str__(self):
        return (self.name)


class Course(models.Model):
    course_name = models.CharField(max_length=150)
    fees = models.IntegerField()
    duration = models.CharField(max_length=100)

    def __str__(self):
        return (self.course_name)


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    mobile_no = models.IntegerField()
    college = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.FileField(upload_to='profile', max_length=100)

    def __str__(self):
        return (self.name)
