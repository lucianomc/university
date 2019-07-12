from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import CourseForm
from .models import Course, Matter, Student

# Create your views here.


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('curso:home')
    form_class = CourseForm


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course


class MatterCreateView(CreateView):
    model = Matter
    success_url = reverse_lazy('curso:home')
    fields = '__all__'


class MatterListView(ListView):
    model = Matter


class MatterDetailView(DetailView):
    model = Matter


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('curso:home')
    fields = '__all__'


class StudentDetailView(DetailView):
    model = Student


# def home(request):
#     college = Course.objects.all().order_by('nameCourse')
#     context = {'allCourses': college}
#     return render(request, 'curso/course.html', context)


def description(request, courseId):
    try:
        detailCourse = Course.objects.get(idCourse=courseId)
        mattersCourse = detailCourse.matter_set.all().order_by('nameMatter')
    except Course.DoesNotExist:
        raise Http404("Nenhum curso foi encontrado com esse Id")

    context = {'details': detailCourse, 'matters': mattersCourse}
    return render(request, 'curso/detailsCourse.html', context)


def matterDesc(request, matterId):
    matter = Matter.objects.get(idMatter=matterId)
    studentMatter = matter.studenthasmatter_set.all()

    context = {'students': studentMatter, 'matter': matter}
    return render(request, 'curso/detailsMatter.html', context)


# def StudentDesc(request, studentId):
#    pass


# def new_course(request):
#     data = {}
#     form = CourseForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('curso:home')

#     data['form'] = form
#     return render(request, 'curso/newcourse.html', data)
