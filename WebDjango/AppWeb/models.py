from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    def __str__(self):
        return f"Curso: {self.nombre}, Camada: {self.camada}"


class Estudiante(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length = 30, default="corre@correo.com") 
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, Email: {self.email}"

class Profesor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length = 30, default="corre@correo.com") 
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, Asignatura: {self.profesion}, Emial: {self.email}"

class Entregable(models.Model):

    nombre = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField(null=True)
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"Nombre: {self.nombre}, Fecha: {self.fecha_de_entrega}"


class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default="avatares/administrador.png", upload_to="avatares", null=True, blank=True)