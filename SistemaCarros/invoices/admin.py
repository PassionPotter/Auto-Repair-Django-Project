from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Invoices

# Register your models here.

@admin.register(Invoices)
class InvoicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', )