
from django.urls import path

from . import views
from .views import (CourseCreateView, CourseDetailView, CourseListView,
                    CourseUpdateView,
                    MatterCreateView, MatterDetailView, MatterListView,
                    MatterUpdateView,
                    StudentDetailView, StudentCreateView)

app_name = 'curso'


urlpatterns = [
    path('', CourseListView.as_view(), name='home'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='description'),
    path('course/edit/<int:pk>/', CourseUpdateView.as_view(), name='course_edit'),
    path('matter/<int:pk>/', MatterDetailView.as_view(), name='matterDesc'),
    path('matter/edit/<int:pk>/', MatterUpdateView.as_view(), name='matter_edit'),
    path('novocurso/', CourseCreateView.as_view(), name='newCourse'),
    path('novamateria/', MatterCreateView.as_view(), name='nova_materia'),
    path('novoestudante/', StudentCreateView.as_view(), name='novo_estudante'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_desc'),
]

# como colocar uma url atrás da outra?
