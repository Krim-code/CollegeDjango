from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name='index'),
    path('', department_list, name='home'),
    path('department/', department_list, name='department_list'),
    path('course/', course_list, name='course_list'),
    path('faculty/', faculty_list, name='faculty_list'),
    path('student/', student_list, name='student_list'),
    path('student/add/', add_student, name='add_student'),

]