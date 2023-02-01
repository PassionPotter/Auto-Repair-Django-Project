from datetime import datetime

from django.db import models

# Create your models here.



class Tecnicos(models.Model):


    nombreTecnico= models.CharField(max_length=255,blank=True)
    apellidoTecnico= models.CharField(max_length=255,blank=True)
    emailTecnico=models.EmailField(max_length=255,blank=True)
    telTecnico=models.CharField(max_length=11,blank=True)
    telTecnico2=models.CharField(max_length=11,blank=True)
    notasTecnico=models.TextField(max_length=255,blank=True)
    fecha_registro = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return f'{self.apellidoTecnico}'
