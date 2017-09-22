from django.db import models
from django.utils import timezone
import datetime


class CentroDeAcopio(models.Model):
    ciudad = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    centro = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    urgencia = models.CharField(max_length=10)
    brigadistas = models.CharField(max_length=2)
    contacto = models.CharField(max_length=200)
    telefono = models.IntegerField(default=0)
    viveres = models.CharField(max_length=5000)
    medicamentos = models.CharField(max_length=5000)
    herramientas = models.CharField(max_length=5000)
    ubicacion = models.CharField(max_length=1000)
    infoAdicional = models.CharField(max_length=2000)
    updated_at = models.DateTimeField(auto_now=True)
