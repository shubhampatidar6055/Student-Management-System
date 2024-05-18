from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .api import*

urlpatterns = [
    path("",index),
    path("sign_in/",sign_in),
    path("sign_up/",sign_up),
    path("sign_up_data/",sign_up_data),
    path("viewstudents/",viewstudents),
    path("add_students/",add_student),
    path("delete_student/<int:pk>/", delete_student, name="delete_student"),
    path("update_student/<int:uid>/", update_student, name="update_student"),
    path("update_student_data/",update_student_data),
    path("search/", search , name="search"),
    # path("student_profile/<int:pk>/", student_profile, name="student_profile"),
    path("profile/<int:pk>/", profile, name="profile"),
    path("dashboard/",dashboard),
    path("courses/",courses),
    path("course_registration/",course_registration),
    path("delete_course/<int:pk>/", delete_course, name="delete"),
    path("update_course/<int:uid>/", update_course, name="update_course"),
    path("update_courses/", update_courses),
    
    # This is Api Url
    path("api/user/",Userapi.as_view()),
    path("api/updateuserapi/<int:pk>/",updateuserapi.as_view()),
    path("api/deleteuserapi/<int:pk>/",deleteuserapi.as_view()),
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
