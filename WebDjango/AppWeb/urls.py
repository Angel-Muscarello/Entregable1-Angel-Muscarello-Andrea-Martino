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
    path("busquedaCamada", views.busquedaCadama, name="BusquedaCamada"),
    path("busquedaEstudiante", views.busquedaCadama, name="busquedaEstudiante"),
    path("busquedaEntregable", views.busquedaCadama, name="busquedaEntregable"),
    path("busquedaProfesor", views.busquedaCadama, name="busquedaProfesor"),
    path("buscar", views.buscar)
    
]    