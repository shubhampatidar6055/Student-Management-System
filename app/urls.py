from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",index),
    path("sign_in/",sign_in),
    path("sign_up/",sign_up),
    path("sign_up_data/",sign_up_data),
    path("viewstudents/",viewstudents),
    path("add_students/",add_student),
    path("profile/",profile),
    path("dashboard/",dashboard),
    path("courses/",courses),
    path("course_registration/",course_registration),
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
