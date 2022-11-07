from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
 
class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=150)