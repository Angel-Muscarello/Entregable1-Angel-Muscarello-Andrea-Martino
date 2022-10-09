from django.contrib import admin

from AppWeb.models import Curso, Entregable, Estudiante, Profesor

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Profesor)