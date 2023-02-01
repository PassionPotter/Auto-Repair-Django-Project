from django.db import models

# Create your models here.
from ManoObra.models import ManoObra
from ckeditor.fields import RichTextField



class Detalle(models.Model):

    que_hara = models.ForeignKey(ManoObra, on_delete=models.SET_NULL, null=True)
    reclamo_no=models.IntegerField()
    #BUSCAR RICHTEXT FIELD
    notas = RichTextField(blank=True, null=True)


    def __str__(self):
        return f'{self.que_hara} {self.reclamo_no} {self.notas}'