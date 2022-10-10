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
    path("buscarCurso", views.buscarCurso, name="BusquedaCamada"),
    path("buscarEstudiante", views.buscarEstudiante, name="busquedaEstudiante"),
    path("buscarEntregable", views.buscarEntregable, name="busquedaEntregable"),
    path("buscarProfesor", views.buscarProfesor, name="busquedaProfesor"),
    path("buscar", views.buscar)
    
]    