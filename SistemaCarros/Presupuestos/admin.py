from django.contrib import admin

# Register your models here.
from .models import Presupuestos

# Register your models here.

@admin.register(Presupuestos)
class PresupuestosAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'total_parte', 'total_manaobra', 'total_paid', 'status')