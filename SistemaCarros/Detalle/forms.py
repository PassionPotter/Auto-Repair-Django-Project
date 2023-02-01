from django import forms
from .models import Detalle


class DetalleForm(forms.ModelForm):
    class Meta:
        model=Detalle
        fields=['que_hara', 'reclamo_no', 'notas']