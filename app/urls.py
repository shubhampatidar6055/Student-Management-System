from django.urls import path
from .views import *

urlpatterns = [
    path("",index),
    path("sign_in/",sign_in),
    path("sign_up/",sign_up),
    path("sign_up_data/",sign_up_data),
    path("viewstudents/",viewstudents),
    path("profile/",profile),
    path("dashboard/",dashboard),
    path("courses/",courses),
]
