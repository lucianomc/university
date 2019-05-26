from django.shortcuts import render
from .models import Course
# Create your views here.


def home(request):
    college = Course.objects.all()
    context = {'allCourses': college}
    return render(request, 'course.html', context)


def description(request, courseId):
    detailCourse = Course.objects.get(idCourse=courseId)
    context = {'details': detailCourse}
    return render(request, 'detailsCourse.html', context)
