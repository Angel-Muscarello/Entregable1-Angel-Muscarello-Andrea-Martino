import email
from django.http import HttpResponse
from django.shortcuts import render
from AppWeb.models import Curso, Entregable, Estudiante, Profesor
from AppWeb.forms import CursoForm, EstudianteForm, EntregableForm, ProfesorForm
# Create your views here.

def inicio(request):
    return render(request, "AppWeb/padre.html")

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
            curso.save()
            return render(request, "AppWeb/padre.html")#vuelvo al html que quiera
    else:
        mi_formulario = EntregableForm()#formulario vacio para construir el html
        
    return render(request, "AppWeb/entregable.html", {"formulario" : mi_formulario})

def busquedaCadama(request):
    return render(request, "AppWeb/busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET['camada']
        curso = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppWeb/padre.html", {"curso":curso, "camada":camada})
   
    else:
        respuesta = "No se enviaron datos"

    return render(request, "AppWeb/padre.html", {"respuesta":respuesta})

#FORMULARIOS.............

def formularios(request):
    return render(request, "AppWeb/formularios.html")


