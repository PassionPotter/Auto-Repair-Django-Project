from datetime import datetime

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from Presupuestos.models import Presupuestos


class Parte(models.Model):
    STATUS = (
        ('Ok', 'Ok'),
        ('Pending', 'Pending'),
    )
    # resumen = models.TextField()
    dealer = models.CharField(max_length=255, blank=True, null=True)
    invoiceNumber=models.IntegerField(blank=True, null=True)
    minimumInventory=models.IntegerField(blank=True, null=True)
    status=models.CharField(max_length=255,choices=STATUS,default='Ok')
    codigo=models.IntegerField()
    descripcion=models.CharField(max_length=255,blank=True, null=True)
    quantity=models.FloatField()
    unit_price=models.FloatField()
    # descuento=models.CharField(max_length=255,default="0")
    total_price=models.FloatField(blank=True, null=True)
    tax_free=models.BooleanField(blank=True, null=True)
    # descuentoTotal= models.IntegerField()
    descuento_parte = models.IntegerField(default=100)
    comprado_cliente=models.BooleanField(blank=True, default=False)
    estimate_id=models.ForeignKey(Presupuestos, on_delete=models.SET_NULL, null=True)
    # total=models.IntegerField()

    def getTotalDiscount(self):
        return self.quantity*self.unit_price * (100 - self.descuento_parte) / 100;
    # estatus = models.BooleanField()
    # def __str__(self):
    #     return f'{self.codigo}: {self.estatus} {s
    #     elf.descripcion}'




    def __str__(self):
        return f'{self.codigo}: {self.descripcion} {self.quantity} {self.unit_price} {self.total_price}' \
               f' {self.tax_free}{self.descuento_parte}' \
               f'{self.comprado_cliente}' 

