from email.policy import default
from django import forms



class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()



class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField() 



class EntregableForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    fecha_de_entrega = forms.DateField()
    entregado = forms.BooleanField(required = False)




class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    profesion = forms.CharField(max_length=30)
    email = forms.EmailField()