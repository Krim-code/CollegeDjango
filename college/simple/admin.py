from django.contrib import admin

from .models import Department, Student, Faculty, Course

# Register your models here.
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Course)
