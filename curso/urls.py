
from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.home, name='home'),
    path('course/<int:courseId>/', views.description, name='description'),
    path('matter/<int:matterId>/', views.matterDesc, name='matterDesc'),
    path('novo/', views.new_course, name='newCourse'),
    #path('student/<int:studentId>/', views.StudentDesc, name='StudentDesc'),
]

#como colocar uma url atrás da outra?