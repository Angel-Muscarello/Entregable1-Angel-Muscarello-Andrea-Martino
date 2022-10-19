from django.urls import path
from AppWeb.views import *

urlpatterns = [
#Ventanas de la pagina

  #Paginas principales
    path('', inicio, name="Padre"),

    #Formularios de analisis y vista de datos 
    path("buscarCurso", buscarCurso, name="BuscarCurso"),
    path("buscarEstudiante", buscarEstudiante, name="BuscarEstudiante"),
    path("buscarEntregable", buscarEntregable, name="BuscarEntregable"),
    path("buscarProfesor", buscarProfesor, name="BuscarProfesor"),

    #Formularios para pedir la informacion
    path("formularios", formularios, name="Formulario"),
    path("pedirDatosCurso", PedirDatosCurso, name="DatosdeCursos"),
    path("pedirDatosEstudiante", PedirDatosEstudiante, name="DatosdeEstudiantes"),
    path("pedirDatosEntregable", PedirDatosEntregable, name="DatosdeEntregables"),
    path("pedirDatosProfesor", PedirDatosProfesor, name="DatosdeProfesores"),

    #----LOGIN---LOGOUT,  AUTHENTICATE
    path("login", MyLogin.as_view(), name="Login"),
    path("logout", MyLogout.as_view(), name="Logout"),

    #listClass
    path("listCurso", ListCurso.as_view(), name="listCurso"),
    path("listEntregable", ListEntregable.as_view(), name="listEntregable"),
    path("listEstudiante", ListEstudiante.as_view(), name="listEstudiante"),
    path("listProfesor", ListProfesor.as_view(), name="listProfesor"),

    #detailClass
    path(r'^(?P<pk>\d+)$', DetailCurso.as_view(), name="detailCurso"),
    path(r'^(?P<pk>\d+)$', DetailEntregable.as_view(), name="detailEntregable"),
    path(r'^(?P<pk>\d+)$', DetailEstudiante.as_view(), name="detailEstudiante"),
    path(r'^(?P<pk>\d+)$', DetailProfesor.as_view(), name="detailProfesor"),

    #createClass
    path("cursoCreate", CreateCurso.as_view(), name="cursoNuevo"),
    path("entregableCreate", CreateEntregable.as_view(), name="entregableNuevo"),
    path("estudianteCreate", CreateEstudiante.as_view(), name="estudianteNuevo"),
    path("profesorCreate", CreateProfesor.as_view(), name="profesorNuevo"),

    #updateCurso
    path(r'^cursoUpdate/(?P<pk>)\d+)$', UpdateCurso.as_view(), name="cursoEditar"),
    path(r'^entregableUpdate/(?P<pk>)\d+)$', UpdateEntregable.as_view(), name="entregableEditar"),
    path(r'^estudianteUpdate/(?P<pk>)\d+)$', UpdateEstudiante.as_view(), name="estudianteEditar"),
    path(r'^profesorUpdate/(?P<pk>)\d+)$', UpdateProfesor.as_view(), name="profesorEditar"),

    #deleteCurso
    path(r'^cursoDelete/(?P<pk>)\d+)$', DeleteCurso.as_view(), name="cursoDelete"),
    path(r'^entregableDelete/(?P<pk>)\d+)$', DeleteEntregable.as_view(), name="entregableDelete"),
    path(r'^estudianteDelete/(?P<pk>)\d+)$', DeleteEstudiante.as_view(), name="estudianteDelete"),
    path(r'^profesorDelete/(?P<pk>)\d+)$', DeleteProfesor.as_view(), name="profesorDelete"),
]
