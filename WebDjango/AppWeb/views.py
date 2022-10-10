import email
from django.http import HttpResponse
from django.shortcuts import render
from AppWeb.models import Curso, Entregable, Estudiante, Profesor
from AppWeb.forms import CursoForm, EstudianteForm, EntregableForm, ProfesorForm
# Create your views here.

def inicio(request):
    return render(request, "AppWeb/padre.html")

def curso(request):    
    return render(request, "AppWeb/curso.html")

def profesor(request):
    return render(request, "AppWeb/profesor.html")

def estudiante(request):
    return render(request, "AppWeb/estudiante.html")

def entregable(request):
    return render(request, "AppWeb/entregable.html")

def busquedaCadama(request):
    return render(request, "AppWeb/busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET['camada']
        curso = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppWeb/resultadoPorBusqueda.html", {"curso":curso, "camada":camada})
   
    else:
        respuesta = "No se enviaron datos"

    return render(request, "AppWeb/padre.html", {"respuesta":respuesta})

#FORMULARIOS.............

def formularios(request):
    return render(request, "AppWeb/formularios.html")

def cursoFormulario(request):

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
        
    return render(request, "AppWeb/cursoFormulario.html", {"formulario" : mi_formulario})

    

    

def entregableFormulario(request):
    
    if  request.method == "POST":
        mi_formulario = EntregableForm(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:
            datos_cargados = mi_formulario.cleaned_data

            entregable = Entregable(
                nombre= datos_cargados["nombre"], 
                fecha_de_entrega= datos_cargados['fecha_de_entrega'],
                entregado= datos_cargados["entregado"]
            )
            entregable.save()
            return render(request, "AppWeb/padre.html")
    else:
        mi_formulario = EntregableForm()
            
    return render(request, "AppWeb/entregableFormulario.html", {"formulario" : mi_formulario})
    

def estudianteFormulario(request):
    
    if  request.method == "POST":
        mi_formulario = EstudianteForm(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:
            datos_cargados = mi_formulario.cleaned_data

            estudiante = Estudiante(
                nombre= datos_cargados["nombre"], 
                apellido= datos_cargados["apellido"],
                email= datos_cargados["email"]
            )
            estudiante.save()
            return render(request, "AppWeb/padre.html")
    else:
        mi_formulario = ProfesorForm()    

    return render(request, "AppWeb/estudianteFormulario.html", {"formulario" : mi_formulario})

def profesorFormulario(request):

    if  request.method == "POST":
        mi_formulario = ProfesorForm(request.POST)#info que llega del html
        print(mi_formulario)

        if mi_formulario.is_valid:#si paso la validasion django
            datos_cargados = mi_formulario.cleaned_data

            profesor = Profesor(
                nombre= datos_cargados["nombre"], 
                apellido= datos_cargados['apellido'],
                profesion = datos_cargados["profesion"],
                email= datos_cargados["email"]
            )
            profesor.save()
            return render(request, "AppWeb/padre.html")

    else:
        mi_formulario = ProfesorForm()    

    return render(request, "AppWeb/profesorFormulario.html", {"formulario" : mi_formulario})
