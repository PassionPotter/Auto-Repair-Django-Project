from django import forms
from  ManoObra.models import ManoObra


class ManoObraForm(forms.ModelForm):
    class Meta:
        model=ManoObra
        fields=['codigo','tecnico','horas','minutos','tarifa',
            'descripcion'] 
