
from django.urls import path

from . import views
from .views import (CourseCreateView, CourseDetailView, CourseListView,
                    MatterCreateView, MatterDetailView, MatterListView,
                    StudentDetailView, StudentCreateView)

app_name = 'curso'


urlpatterns = [
    # path('', views.home, name='home'),
    path('', CourseListView.as_view(), name='home'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='description'),
    path('matter/<int:pk>/', MatterDetailView.as_view(), name='matterDesc'),
    path('novocurso/', CourseCreateView.as_view(), name='newCourse'),
    path('novamateria/', MatterCreateView.as_view(), name='nova_materia'),
    path('novoestudante/', StudentCreateView.as_view(), name='novo_estudante'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_desc'),

]

# como colocar uma url atrás da outra?
