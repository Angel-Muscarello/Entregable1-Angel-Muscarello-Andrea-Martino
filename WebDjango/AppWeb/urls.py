from unicodedata import name
from django.urls import path
from AppWeb import views

urlpatterns = [
#Ventanas de la pagina
  #Paginas principales
    #Formularios de carga de datos en BD SQLlite
    path('', views.inicio, name="Padre"),
    path("curso", views.curso, name="Curso"),
    path("profesor", views.profesor, name="Profesor"),
    path("estudiante", views.estudiante, name="Estudiante"),
    path("entregable", views.entregable, name="Entregable"),
    #Formularios de analisis y vista de datos 
    path("buscarCurso", views.buscarCurso, name="BuscarCurso"),
    path("buscarEstudiante", views.buscarEstudiante, name="BuscarEstudiante"),
    path("buscarEntregable", views.buscarEntregable, name="BuscarEntregable"),
    path("buscarProfesor", views.buscarProfesor, name="BuscarProfesor"),
    #Formularios para pedir la informacion
    path("formularios", views.formularios, name="Formulario"),
    path("pedirDatosCurso", views.PedirDatosCurso, name="DatosdeCursos"),
    path("pedirDatosEstudiante", views.PedirDatosEstudiante, name="DatosdeEstudiantes"),
    path("pedirDatosEntregable", views.PedirDatosEntregable, name="DatosdeEntregables"),
    path("pedirDatosProfesor", views.PedirDatosProfesor, name="DatosdeProfesores")
]    