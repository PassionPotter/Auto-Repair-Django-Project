from datetime import datetime

from django.db import models

# Create your models here.



class InformacionTiendas(models.Model):

    #nombre=models.CharField(max_length=255)
    registro_desde=models.DateTimeField(default=datetime.now)
    tax_id=models.IntegerField()
    pais=models.CharField(max_length=200)
    direccion=models.CharField(max_length=255)
    ciudad=models.CharField(max_length=255)
    estado=models.CharField(max_length=255)
    zip=models.IntegerField()
    telefono_1=models.IntegerField()
    telefono_2=models.IntegerField()
    fax=models.IntegerField()
    email=models.CharField(max_length=255)
    website=models.URLField(max_length=200)
    tax_productos=models.IntegerField()
    tax_precios=models.IntegerField()
    logo = models.ImageField(upload_to='uploads',blank=True)
    nombre_taller=models.CharField(max_length=255)
    plan = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.registro_desde} {self.tax_id} {self.pais} ' \
               f'{self.direccion}{self.ciudad}{self.estado}{self.zip}{self.telefono_1}' \
               f'{self.telefono_2}{self.fax}{self.email}{self.website}{self.tax_productos}' \
               f'{self.tax_precios}{self.logo}{self.nombre_taller}{self.plan}{self.status}'


