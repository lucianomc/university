from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, Http404

from .models import Course
from .models import Matter

from .form import CourseForm

# Create your views here.


def home(request):
    college = Course.objects.all().order_by('nameCourse')
    context = {'allCourses': college}
    return render(request, 'curso/course.html', context)


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


def new_course(request):
    data = {}
    form = CourseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('curso:home')

    data['form'] = form
    return render(request, 'curso/newcourse.html', data)
