from django.shortcuts import render

from AppWeb.models import Curso, Entregable, Estudiante, Profesor

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



#FORMULARIOS.............

def formularios(request):
    return render(request, "AppWeb/formularios.html")

def cursoFormulario(request):
    
    if request.method == 'POST':

        CURSO = Curso(request.POST['curso'], request.POST['camada'], request.POST['fecha_de_entrega'])
        curso.save()

        return render(request, "AppWeb/inicio.html")
    
    return render(request, "AppWeb/cursoFormulario.html")

def entregableFormulario(request):
    
    if request.method == 'POST':

        ENTREGABLE = Entregable(request.POST['entregable'], request.POST['fecha de entrega'], request.POST['entregado'])
        curso.save()

        return render(request, "AppWeb/inicio.html")
    
    return render(request, "AppWeb/entregableFormulario.html")

def estudianteFormulario(request):
    
    if request.method == 'POST':

        ESTUDIANTE = Estudiante(request.POST['nombre'], request.POST['apellido'])
        curso.save()

        return render(request, "AppWeb/inicio.html")
    
    return render(request, "AppWeb/estudianteFormulario.html")

def profesorFormulario(request):
    
    if request.method == 'POST':

        PROFESOR = Profesor(request.POST['nombre'], request.POST['apelldio'], request.POST['profesion'])
        curso.save()

        return render(request, "AppWeb/inicio.html")
    
    return render(request, "AppWeb/profesorFormulario.html")