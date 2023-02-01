from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import ReporteTechnician

# Register your models here.

@admin.register(ReporteTechnician)
class ReporteTechnicianAdmin(admin.ModelAdmin):
    list_display = ('id', 'estimate', 'technician', 'content', 'quantity')