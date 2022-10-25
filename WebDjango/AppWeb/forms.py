from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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



#CLASS EDIT USER
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Editar Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]

        