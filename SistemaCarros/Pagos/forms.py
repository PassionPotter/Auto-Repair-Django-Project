from django import forms
from .models import Pagos


class PagosForm(forms.ModelForm):
    class Meta:
        model=Pagos
        fields=['tipo_pago','cantidad_pagada','numero_transaccion']
        #fields=['tipo_pago','fecha_pago','cantidad_pago','total','cantidad_pagada','saldo_adeudado'] 
