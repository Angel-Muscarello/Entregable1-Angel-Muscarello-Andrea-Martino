import email
from django.http import HttpResponse
from django.shortcuts import render
from AppWeb.models import Curso, Entregable, Estudiante, Profesor
from AppWeb.forms import CursoForm, EstudianteForm, EntregableForm, ProfesorForm
# Create your views here.

def inicio(request):
    return render(request, "AppWeb/padre.html")

#Formularios de Carga
def curso(request):    
    if  request.method == "POST":
        mi_formulario = CursoForm(request.POST)#llega la informacion del html
        print(mi_formulario)
        if mi_formulario.is_valid:#corrborar si pasa la validacion de django
            datos_cargados = mi_formulario.cleaned_data

            curso = Curso(
                nombre= datos_cargados["nombre"], 
                camada= datos_cargados["camada"],
            )
            curso.save()
            return render(request, "AppWeb/padre.html")#vuelvo al html que quiera
    else:
        mi_formulario = CursoForm()#formulario vacio para construir el html
        
    return render(request, "AppWeb/curso.html", {"formulario" : mi_formulario})


def profesor(request):
    if  request.method == "POST":
        mi_formulario = ProfesorForm(request.POST)#llega la informacion del html
        print(mi_formulario)
        if mi_formulario.is_valid:#corrborar si pasa la validacion de django
            datos_cargados = mi_formulario.cleaned_data

            profesor = Profesor(
                nombre= datos_cargados["nombre"], 
                apellido= datos_cargados["apellido"],
                profesion= datos_cargados["profesion"],
                email= datos_cargados["email"]
            )
            profesor.save()
            return render(request, "AppWeb/padre.html")#vuelvo al html que quiera
    else:
        mi_formulario = ProfesorForm()#formulario vacio para construir el html
    return render(request, "AppWeb/profesor.html", {"formulario" : mi_formulario})

def estudiante(request):
    if  request.method == "POST":
        mi_formulario = EstudianteForm(request.POST)#llega la informacion del html
        print(mi_formulario)
        if mi_formulario.is_valid:#corrborar si pasa la validacion de django
            datos_cargados = mi_formulario.cleaned_data

            estudiante = Estudiante(
                nombre= datos_cargados["nombre"], 
                apellido= datos_cargados["apellido"],
                email= datos_cargados["email"]
            )
            estudiante.save()
            return render(request, "AppWeb/padre.html")#vuelvo al html que quiera
    else:
        mi_formulario = EstudianteForm()#formulario vacio para construir el html
        
    return render(request, "AppWeb/estudiante.html", {"formulario" : mi_formulario})

def entregable(request):
    if  request.method == "POST":
        mi_formulario = EntregableForm(request.POST)#llega la informacion del html
        print(mi_formulario)
        if mi_formulario.is_valid:#corrborar si pasa la validacion de django
            datos_cargados = mi_formulario.cleaned_data

            entregable = Entregable(
                nombre= datos_cargados["nombre"], 
                fecha_de_entrega= datos_cargados["fecha_de_entrega"],
                entregado= datos_cargados["entregado"]
            )
            entregable.save()
            return render(request, "AppWeb/padre.html")#vuelvo al html que quiera
    else:
        mi_formulario = EntregableForm()#formulario vacio para construir el html
        
    return render(request, "AppWeb/entregable.html", {"formulario" : mi_formulario})

#Formularios de Busqueda
def PedirDatosCurso(request):
    return render(request, "AppWeb/PedirDatosCurso.html")

def buscarCurso(request):
    if not request.GET["camada"]:
        respuesta = "No se enviaron datos"
        return HttpResponse(respuesta)
    else:
        camada_a_bucar = request.GET["camada"]
        curso = Curso.objects.filter(camada=camada_a_bucar)
        contexto = {
            "cursos_encontrados":curso, 
            "camada":camada_a_bucar
        }

        return render(request, "AppWeb/ResultadoCurso.html", context= contexto)

   
def PedirDatosEstudiante(request):
    return render(request, "AppWeb/PedirDatosEstudiante.html")

def buscarEstudiante(request):
    if not request.GET["apellido"]:
        respuesta = "No se enviaron datos"
        return HttpResponse(respuesta)
    else:
        estudiante_a_bucar = request.GET["apellido"]
        estudiante = Estudiante.objects.filter(apellido=estudiante_a_bucar)
        contexto = {
            "estudiantes_encontrados":estudiante, 
            "apellido":estudiante_a_bucar
        }

        return render(request, "AppWeb/ResultadoEstudiante.html", context= contexto)
   
   
def PedirDatosEntregable(request):
    return render(request, "AppWeb/PedirDatosEntregable.html")

def buscarEntregable(request):
    if not request.GET["nombre"]:
        respuesta = "No se enviaron datos"
        return HttpResponse(respuesta)
    else:
        entreglable_a_bucar = request.GET["nombre"]
        entregable = Entregable.objects.filter(nombre= entreglable_a_bucar)
        contexto = {
            "entreglables_encontrados":entregable, 
            "nombre":entreglable_a_bucar
        }

        return render(request, "AppWeb/ResultadoEntregable.html", context= contexto)
   

def PedirDatosProfesor(request):
    return render(request, "AppWeb/PedirDatosProfesor.html")

def buscarProfesor(request):
    if not request.GET["apellido"]:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
    else:
        profesor_a_bucar = request.GET["apellido"]
        profesor = Profesor.objects.filter(apellido=profesor_a_bucar)
        contexto = {
            "profesores_encontrados":profesor, 
            "apellido":profesor_a_bucar
        }

        return render(request, "AppWeb/ResultadoProfesor.html", context= contexto)
   


def buscar(request):
    respuesta = f"Estoy buscando: {request.GET['camada']}"
    return HttpResponse(respuesta)

#FORMULARIOS.............

def formularios(request):
    return render(request, "AppWeb/formularios.html")


