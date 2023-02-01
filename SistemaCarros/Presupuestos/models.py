from django.db import models

# Create your models here.
from Clientes.models import Clientes
from carros.models import Carro
from tecnicos.models import Tecnicos


class Presupuestos(models.Model):
    PRESUPUESTO_STATUS = (
        ('PENDING', 'pending'),
        ('CANCELED', 'canceled'),
        ('PAID', 'paid'),
    )
    cliente= models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True)
    carro=models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True)
    garantia=models.CharField(max_length=255,default=0)
    tecnicos=models.ForeignKey(Tecnicos, on_delete=models.SET_NULL, null=True)
    total_parte=models.FloatField(null=True,blank=True, default=0)
    descuentoTotal_parte= models.FloatField(default=0, null=True)
    total_manaobra=models.FloatField(null=True,blank=True, default=0)
    descuentoTotal_manaobra= models.FloatField(default=0, null=True)
    total_paid = models.FloatField(default=0,null=True,)
    status = models.CharField(choices=PRESUPUESTO_STATUS,default="PENDING", max_length=10)
    resumen=models.CharField(max_length=255,blank=True)
    register_time=models.DateTimeField(auto_now=True)

    @property
    def total(self):
        return self.total_manaobra+self.total_parte
    #detalle=models.ForeignKey(Detalle, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.cliente} {self.carro}{self.garantia}' \
               f'{self.tecnicos}'\
               f'{self.descuentoTotal_parte} {self.total_parte}'\
               f' {self.descuentoTotal_manaobra} {self.total_manaobra}'



