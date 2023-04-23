from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Department, Course, Student, Faculty


class StudentForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all())

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'courses']


def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            form.save_m2m()
            return redirect('student_list')
    else:
        form = StudentForm()
        departments = Department.objects.all()
        courses = Course.objects.all()
        students = Student.objects.all()
        faculties = Faculty.objects.all()

        return render(request, 'index.html',
                      {
                          'departments': departments,
                          'courses': courses,
                          'students': students,
                          'faculties': faculties,
                          'form': form

                      })


def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculty_list.html', {'faculties': faculties})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            form.save_m2m()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})