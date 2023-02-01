from datetime import datetime

from django.db import models

# Create your models here.
from Presupuestos.models import Presupuestos

from Clientes.models import Clientes

class Invoices(models.Model):

    estimate = models.ForeignKey(Presupuestos, on_delete=models.SET_NULL, null=True)
    date_register=models.DateTimeField(default=datetime.now)
    amount=models.FloatField(default=0)
    status=models.CharField(max_length=10,default='pending')

    def getBillingName(self):
        clientID=Presupuestos.objects.get(pk=self.estimate_id).cliente_id

        return Clientes.objects.get(pk=clientID).nombre
    def __str__(self):
        return f'{self.estimate} {self.date_register}{self.amount}'
