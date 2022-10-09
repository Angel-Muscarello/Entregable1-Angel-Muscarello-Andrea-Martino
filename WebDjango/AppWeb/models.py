from django.db import models

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    fecha_de_entrega = models.DateField(null=True)
    def __str__(self):
        return f"{self.nombre}, Camada: {self.camada}"


class Estudiante(models.Model):

    nombre = models.CharField(max_length=30)
    apelldio = models.CharField(max_length=30)
    email = models.EmailField() 
    
    def __str__(self):
        return f"{self.nombre} {self.apelldio}"

class Profesor(models.Model):

    nombre = models.CharField(max_length=30)
    apelldio = models.CharField(max_length=30)
    email = models.EmailField() 
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} {self.apelldio}, Asignatura: {self.profesion}"

class Entregable(models.Model):

    nombre = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField(null=True)
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre}, {self.entregado}"