from datetime import datetime
from django.test import TestCase
from AppWeb.models import Curso, Entregable,Profesor


# Create your tests here.

class ViewTestCase(TestCase):
    def test_create_curso(self):

        curso = Curso.objects.create(
            nombre="Curso Marcos", 
            camada=123456
        )  
        assert type(curso.nombre) == str
        assert len(curso.nombre) < 40
        assert type(curso.camada) == int

    def test_create_entregable(self):
        entregable = {}
        entregable["entregable_1"] = Entregable.objects.create(
            nombre="Final", 
            fecha_de_entrega=datetime.now(),
            entregado = True
        )  
        entregable["entregable_2"] = Entregable.objects.create(
            nombre = "Tesina, El Señor de los Anillos",
            fecha_de_entrega= None,
            entregado = False
        )

        assert entregable["entregable_1"].nombre == "Final"
        assert entregable["entregable_1"].fecha_de_entrega != None
        assert entregable["entregable_1"].entregado == True
        assert entregable["entregable_2"].fecha_de_entrega is None 

    def test_create_profesor(self):
        profesor = Profesor.objects.create(nombre="Annn", apellido="ElMalo",profesion="Historiador", email="")
        
        assert profesor.nombre != ''
        assert profesor.email == None
        assert len(profesor.apellido) <= 30
        
        