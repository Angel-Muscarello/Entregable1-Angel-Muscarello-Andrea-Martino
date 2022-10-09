from unicodedata import name
from django.urls import path
from AppWeb import views

urlpatterns = [
    path('', views.inicio, name="Padre"),
    path("curso", views.curso, name="Curso"),
    path("profesor", views.profesor, name="Profesor"),
    path("estudiante", views.estudiante, name="Estudiante"),
    path("entregable", views.entregable, name="Entregable"),
    path("cursoFormulario", views.cursoFormulario, name="cursoFormulario"),
    
]    