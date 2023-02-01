from django.db import models

# Create your models here.
class Foto(models.Model):

    imagenes = models.ImageField(null=True,blank=True, upload_to="imagenes/")

    def __str__(self):
        return f'{self.imagenes}'