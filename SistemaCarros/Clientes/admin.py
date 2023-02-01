from django.contrib import admin
from .models import Clientes

# Register your models here.

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
