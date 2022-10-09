from unicodedata import name
from django.urls import path
from AppWeb import views

urlpatterns = [
    path('', views.inicio, name="Padre"),
    path("curso", views.curso, name="Curso"),
    path("profesor", views.profesor, name="Profesor"),
    path("estudiante", views.estudiante, name="Estudiante"),
    path("entregable", views.entregable, name="Entregable"),
    path("formularios", views.formularios, name="Formulario"),
    path("cursoFormulario", views.cursoFormulario, name="Formulario-Curso"),
    path("entregableFormulario", views.entregableFormulario, name="Formulario-Estudiante"),
    path("estudianteFormulario", views.estudianteFormulario, name="Formulario-Entregable"),
    path("profesorFormulario", views.profesorFormulario, name="Formulario-Profesor"),
    
]    