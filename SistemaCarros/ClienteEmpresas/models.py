from django.db import models

# Create your models here.
from carros.models import Carro


class ClienteEmpresa(models.Model):
    empresa=models.CharField(max_length=255)
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    telefono=models.CharField(max_length=255)
    fax=models.CharField(max_length=255,blank=True)
    celular=models.CharField(max_length=255)
    posicion=models.CharField(max_length=255)
    correo=models.EmailField(max_length=255)
    vehiculos_poseidos = models.ManyToManyField(
        Carro, blank=True)

    def __str__(self):
        return f'{self.empresa}: {self.nombre} {self.apellido} {self.telefono} {self.fax} {self.celular} {self.posicion} {self.correo} {self.vehiculos_poseidos}'
