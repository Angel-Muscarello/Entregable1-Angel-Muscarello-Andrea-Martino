from django.shortcuts import render

from AppWeb.models import Curso

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

def cursoFormulario(request):
    
    if request.method == 'POST':

        CURSO = Curso(request.POST['curso'], request.POST['camada'])
        curso.save()

        return render(request, "AppWeb/inicio.html")
    
    return render(request, "AppWeb/cursoFormulario.html")