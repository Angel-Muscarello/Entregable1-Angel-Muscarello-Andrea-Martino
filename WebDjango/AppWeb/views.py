import email
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AppWeb.models import Curso, Entregable, Estudiante, Profesor
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin #Permiten restrigir las views (clases) a no usuarios...
from django.contrib.auth.decorators import login_required #Permiten restrigir las views (funciones) a no usuarios...

# Create your views here.

@login_required
def inicio(request):
    return render(request, "AppWeb/padre.html")

@login_required
def PedirDatosCurso(request):
    return render(request, "AppWeb/PedirDatosCurso.html")

@login_required
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

@login_required 
def PedirDatosEstudiante(request):
    return render(request, "AppWeb/PedirDatosEstudiante.html")

@login_required
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
   
@login_required
def PedirDatosEntregable(request):
    return render(request, "AppWeb/PedirDatosEntregable.html")

@login_required
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

@login_required
def PedirDatosProfesor(request):
    return render(request, "AppWeb/PedirDatosProfesor.html")

@login_required
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

@login_required   
def formularios(request):
    return render(request, "AppWeb/formularios.html")

#--REGISTER

def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppWeb/confirmacion_registro.html", {"form":form})
    else:
        form = UserCreationForm()
    
    return render(request, "AppWeb/register.html", {"form":form})


#CLASS LISTVIEW
#CLASS IN VIEWS

class ListCurso(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "AppWeb/listCursos.html"

class ListEntregable(LoginRequiredMixin, ListView):
    model = Entregable
    template_name = "AppWeb/listEntregables.html"

class ListEstudiante(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = "AppWeb/listEstudiantes.html"

class ListProfesor(LoginRequiredMixin, ListView):
    model = Profesor
    template_name = "AppWeb/listProfesores.html"

#CLASS DETALLE in views

class DetailCurso(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "AppWeb/detialCurso.html"

class DetailEntregable(LoginRequiredMixin, DetailView):
    model = Entregable
    template_name = "AppWeb/detailEntregable.html"

class DetailEstudiante(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name = "AppWeb/detailEstudiante.html"

class DetailProfesor(LoginRequiredMixin, DetailView):
    model = Profesor
    template_name = "AppWeb/detailProfesor.html"

#CLASS CREATE in views

class CreateCurso(LoginRequiredMixin, CreateView):
    model = Curso
    success_url = "/AppWeb/listCurso"
    fields = ["nombre", "camada"]

class CreateEntregable(LoginRequiredMixin, CreateView):
    model = Entregable
    success_url = "/AppWeb/listEntregable"
    fields = ["nombre", "fecha_de_entrega"]

class CreateEstudiante(LoginRequiredMixin, CreateView):
    model = Estudiante
    success_url = "/AppWeb/listEstudiante"
    fields = ["nombre", "apellido", "email"]

class CreateProfesor(LoginRequiredMixin, CreateView):
    model = Profesor
    success_url = "/AppWeb/listProfesor"
    fields = ["nombre", "apellido", "profesion", "email"]


#Class UPDATE

class UpdateCurso(LoginRequiredMixin, UpdateView):
    model = Curso
    success_url = "/AppWeb/listCurso"
    fields = ["nombre", "camada"]

class UpdateEntregable(LoginRequiredMixin, UpdateView):
    model = Entregable
    success_url = "/AppWeb/listEntregable"
    fields = ["nombre", "fecha_de_entrega"]

class UpdateEstudiante(LoginRequiredMixin, UpdateView):
    model = Estudiante
    success_url = "/AppWeb/listEstudiante"
    fields = ["nombre", "apellido", "email"]

class UpdateProfesor(LoginRequiredMixin, UpdateView):
    model = Profesor
    success_url = "/AppWeb/listProfesor"
    fields = ["nombre", "apellido", "profesion", "email"]

#CLASS DELETE

class DeleteCurso(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = "/AppWeb/listCurso"
    fields = ["nombre", "camada"]

class DeleteEntregable(LoginRequiredMixin, DeleteView):
    model = Entregable
    success_url = "/AppWeb/listEntregable"

class DeleteEstudiante(LoginRequiredMixin, DeleteView):
    model = Estudiante
    success_url = "/AppWeb/listEstudiante"

class DeleteProfesor(LoginRequiredMixin, DeleteView):
    model = Profesor
    success_url = "/AppWeb/listProfesor"

#---LOGIN---LOGOUT---

class MyLogin(LoginView):
    template_name = "AppWeb/login.html"

class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "AppWeb/logout.html"
    





