from django.db import models

from Presupuestos.models import Presupuestos


class Pagos(models.Model):

    PAGO=(
        ('Cash', 'Cash'),
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Mobile', 'Mobile'),
        ('QR', 'QR'),
        ('Cryptocurrency', 'Cryptocurrency'),
    )
    tipo_pago=models.CharField(max_length=200, null=True,choices=PAGO,default='Crédito')
    #fecha_pago = models.DateTimeField(default=timezone.now)
    #cantidad_pago = models.CharField(max_length=255)
    #total=models.CharField(max_length=255)
    #saldo_adeudado = models.CharField(max_length=255)
    numero_transaccion=models.IntegerField()
    cantidad_pagada=models.FloatField(default=0)
    estimate=models.ForeignKey(Presupuestos, on_delete=models.SET_NULL, null=True)



#    def __str__(self):
#        return f'{self.tipo_pago} {self.fecha_pago} {self.cantidad_pago} {self.total} {self.cantidad_pagada} {self.saldo_adeudado}'

    def __str__(self):
        return f'{self.tipo_pago}{self.numero_transaccion}{self.cantidad_pagada}' 
