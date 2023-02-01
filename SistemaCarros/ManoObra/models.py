from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from Presupuestos.models import Presupuestos
from tecnicos.models import Tecnicos

class ManoObra(models.Model):
    codigo=models.IntegerField()
    descripcion=models.TextField(blank=True,default='')
    tecnico=models.ForeignKey(Tecnicos, on_delete=models.SET_NULL, null=True)
    horas=models.IntegerField()
    minutos=models.IntegerField(default=0)
    tarifa=models.FloatField()
    tarifa_total = models.FloatField()
    libre_impuestos=models.BooleanField()
    estimate_ids=models.ForeignKey(Presupuestos, on_delete=models.SET_NULL, null=True)

    # descuento=models.CharField(max_length=255)
    # numeroDescuento=models.IntegerField()
    # total = models.IntegerField()



    def __str__(self):
        return f'{self.codigo} {self.tecnico} {self.horas}{self.minutos} {self.tarifa}' \
               f'{self.libre_impuestos}{self.tarifa_total}{self.descripcion}'
