from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Course
from django.http import HttpResponse, Http404
# Create your views here.


def home(request):
    college = Course.objects.all().order_by('nameCourse')
    context = {'allCourses': college}
    return render(request, 'course.html', context)


def description(request, courseId):
    try:
        detailCourse = Course.objects.get(idCourse=courseId)
    except Course.DoesNotExist:
        raise Http404("Nenhum curso foi encontrado com esse Id")

    context = {'details': detailCourse}
    return render(request, 'detailsCourse.html', context)


class CourseDetailView(DetailView):
    model = Course
