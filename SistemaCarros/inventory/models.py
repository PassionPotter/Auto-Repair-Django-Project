from datetime import datetime

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Inventory(models.Model):
    STATUS = (
        ('Ok', 'Ok'),
        ('Pending', 'Pending'),
    )
    dealer = models.CharField(max_length=255, blank=True, null=True)
    codigoInventory=models.CharField(max_length=255,blank=True)
    invoiceNumber=models.IntegerField()
    descriptionInventory= models.CharField(max_length=255, blank=True, null=True)
    quantityInventory=models.IntegerField(default=0)
    unitPriceInventory=models.IntegerField()
    minimumInventory=models.IntegerField()

    # invoice_number=models.IntegerField()
    status=models.CharField(max_length=255,choices=STATUS,default='Ok')
    fecha_registro = models.DateTimeField(default=datetime.now)



    def __str__(self):
        return f'{self.dealer}: {self.codigoInventory} {self.invoiceNumber} {self.descriptionInventory} ' \
               f'{self.quantityInventory} {self.unitPriceInventory}{self.minimumInventory}{self.status}{self.fecha_registro}'