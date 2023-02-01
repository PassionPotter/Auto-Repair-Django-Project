from django import forms
from .models import ClienteEmpresa


class ClienteEmpresasForm(forms.ModelForm):
    class Meta:
        model=ClienteEmpresa
        fields=['empresa','nombre','apellido','telefono','fax','celular','posicion', 'correo']