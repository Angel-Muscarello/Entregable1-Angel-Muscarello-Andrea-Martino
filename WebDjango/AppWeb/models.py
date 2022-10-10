from contextlib import nullcontext
from email.policy import default
from django.db import models

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
        return f"{self.nombre} {self.apellido}, Asignatura: {self.profesion}, Emial: {self.email}"

class Entregable(models.Model):

    nombre = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField(null=True)
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"Nombre: {self.nombre}, Fecha: {self.fecha_de_entrega}"