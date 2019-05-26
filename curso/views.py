from django.shortcuts import render
from .models import Course
# Create your views here.


def home(request):
    college = Course.objects.all()
    context = {'allCourses': college}
    return render(request, 'curso.html', context)
