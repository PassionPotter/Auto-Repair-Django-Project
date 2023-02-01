
from datetime import timezone, datetime
from django.db import models

# Create your models here.
from Clientes.models import Clientes
import json

class Carro(models.Model):
    placas=models.CharField(max_length=255, blank=True)
    tipo=models.CharField(max_length=255, blank=True)
    marca=models.CharField(max_length=255, blank=True)
    modelo=models.CharField(max_length=255, blank=True)
    año=models.IntegerField()
    vin=models.CharField(max_length=255, blank=True)
    color=models.CharField(max_length=255, blank=True)
    motor=models.CharField(max_length=255, blank=True)
    agente_seguros=models.CharField(max_length=255, blank=True)
    compañia_seguros=models.CharField(max_length=255, blank=True)
    no_politica=models.CharField(max_length=255,blank=True)
    cliente= models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True,blank=True)
    fotosCarro=models.TextField(null=True,blank=True)
    garantia=models.TextField(null=True,blank=True)
    fecha_registros = models.DateTimeField(default=datetime.now, null=True,blank=True)

#customize model property for main view of fotosCarro
    @property
    def new_name(self):
        if self.fotosCarro == '':
            return None
        temp=json.loads(self.fotosCarro)
        if len(temp) == 0:
            return None
        tempkey=sorted(temp.keys())
        for item in reversed(tempkey):
            if temp[item][1]=="on":
                return item;
        return list(json.loads(self.fotosCarro).keys())[0]

    @property
    def garantia_name(self):
        if self.garantia == '':
            return None
        temp=json.loads(self.garantia)
        if len(temp) == 0:
            return None
        tempkey=sorted(temp.keys())
        for item in reversed(tempkey):
            if temp[item][1]=="on":
                return item;
        return list(json.loads(self.garantia).keys())[0]
    def orig_name(self):
        return list(json.loads(self.fotosCarro).values())[0]
    def __str__(self):
        return f'{self.placas} {self.año}{self.marca} {self.modelo} {self.tipo}{self.motor}{self.vin}{self.color}' \
               f'{self.agente_seguros}{self.compañia_seguros}{self.no_politica}{self.cliente}{self.fotosCarro}{self.garantia}' \
               f'{self.fecha_registros}'
