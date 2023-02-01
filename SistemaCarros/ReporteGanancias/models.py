from django.db import models

# Create your models here.
from Clientes.models import Clientes
from Foto.models import Foto
from django.db import models

# Create your models here.
from Clientes.models import Clientes
from Foto.models import Foto
from ManoObra.models import ManoObra
from Pagos.models import Pagos
from Parte.models import Parte
from carros.models import Carro
from inventory.models import Inventory
from Presupuestos.models import Presupuestos
from tecnicos.models import Tecnicos
class ReporteGanancias(models.Model):

    cliente= models.ForeignKey(Clientes, on_delete=models.CASCADE)
    carro=models.ForeignKey(Carro, on_delete=models.CASCADE)
    mano_obra=models.ForeignKey(ManoObra, on_delete=models.CASCADE)
    parteInventory=models.ForeignKey(Inventory, on_delete=models.CASCADE)
    garantia=models.CharField(max_length=255,default=0)
    pago = models.ForeignKey(Pagos, on_delete=models.CASCADE)
    foto = models.ForeignKey(Foto, on_delete=models.CASCADE)


    def __str__(self):
        #return f'{self.cliente} {self.presupuesto} {self.mano_obra} {self.parte} {self.subcontratar_trabajos} {self.otros_costos} {self.descuento}'
        return f'{self.cliente} {self.carro}{self.mano_obra} {self.parte}{self.garantia}{self.pago}{self.foto}'


class ReporteTechnician(models.Model):
    estimate = models.ForeignKey(Presupuestos, on_delete=models.CASCADE)
    technician = models.ForeignKey(Tecnicos, on_delete=models.CASCADE)
    content = models.CharField(max_length=255, blank=False)
    quantity = models.FloatField(default=0, null=False)
    register_time=models.DateTimeField(auto_now=True)





