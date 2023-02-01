from django import forms
from django.forms import formset_factory

from Clientes import models
from Foto.models import Foto
from Parte.forms import ParteForm
from Presupuestos.models import Presupuestos
from carros.models import Carro
from  Clientes.models import Clientes
from  Parte.models import Parte
from  ManoObra.models import ManoObra
from  Pagos.models import Pagos
from tecnicos.models import Tecnicos

DESCUENTO = (
    ('Quantity', 'Quantity'),
    ('Percentage', 'Percentage'),
)

DISCOUNT= (
    ('Quantity', 'Quantity'),
    ('Percentage', 'Percentage'),
)





class PresupuestosClientesForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ['titulo', 'nombre','apellido','correo','telefono','tel']
        exclude = ['corporacion', 'fax','website','social_media','social_media2',
                   'social_media3','contacto_alternativo','contacto_alternativo2','contacto_alternativo3',
                   'pais','direccion','ciudad','estado','zip']
        widgets = {
            'titulo': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class PresupuestosVehiculosForm(forms.ModelForm):


    class Meta:
        model = Carro
        fields = ['placas','año','modelo','marca','tipo','motor','vin','color','fotosCarro']
        exclude = ['agente_seguros', 'compañia_seguros','no_politica','garantia',
                   'cliente','fecha_registros']
        widgets = {
            'placas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'año': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'modelo':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'motor': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'vin': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'color': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fotosCarro':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'car-input'
                }
            ),


        }




class PresupuestosParteForm(forms.ModelForm):
    class Meta:
        model = Parte
        fields = ['codigo','quantity','unit_price','total_price','tax_free','comprado_cliente','descripcion','descuento_parte']
        exclude = ['estimate_id']
        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id_form-0-codigo',
                }
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control-quantity',
                    'id':'id_form-0-quantity',
                    'onchange':'multiplicar(this)',
                }
            ),
            'unit_price': forms.NumberInput(
                attrs={
                    'class': 'form-control-unit-price',
                    'id': 'id_form-0-unit_price',
                    'onchange':'multiplicar(this)',
                    'pattern': '[0-9]{1,}\.[0-9]{1,}',
                    'step':'any',
                }
            ),
            'total_price': forms.NumberInput(
                attrs={
                    'class': 'form-control-total-price',
                    'id': 'id_form-0-total_price',
                    'pattern': '[0-9]{1,}\.[0-9]{1,}',
                    'step': 'any',
                    'readOnly': True,

                }
            ),
            'tax_free': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'onclick': 'multiplicar(this)',
                    'id': 'id_form-0-tax_free',
                }
            ),
            'comprado_cliente': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'onclick': 'multiplicar(this)',
                    'id': 'id_form-0-comprado_cliente',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id_form-0-descripcion',
                }
            ),
            'descuento_parte': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id_form-0-descuento_parte',
                    'onchange': 'multiplicar(this)',
                    'min':0,
                    'max':100,
                    'value':100,
                }
            ),
        }
    # def __init__(self):
    #     helper = FormHelper()
    #     helper.form_show_labels = False

#ParteFormset = formset_factory(ParteForm, extra=1)

class PresupuestosManoObraForm(forms.ModelForm):
    class Meta:
        model = ManoObra
        fields = ['codigo','tarifa','tecnico', 'tarifa_total','horas','minutos','libre_impuestos','descripcion']
        exclude = ['estimate_id']
        widgets = {
            'codigo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id_form-0-codigo',
                }
            ),
            'horas': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'onchange':'convTarifa(this)',
                    'id': 'id_form-0-horas',
                    'min':'0',
                }
            ),
            'minutos': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'onchange': 'convTarifa(this)',
                    'id': 'id_form-0-minutos',
                    'min':'0',
                    'max':'59',
                }
            ),
            'tarifa': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'onchange': 'convTarifa(this)',
                    'id': 'id_form-0-tarifa',
                    'step': 'any',
                    'pattern': '[0-9]{1,}\.[0-9]{1,}'
                }
            ),
            'tarifa_total': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id_form-0-tarifa_total',
                    'step' : 'any',
                    'pattern' : '[0-9]{1,}\.[0-9]{1,}',
                    'readOnly':True,
        }
            ),
            'libre_impuestos': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'id': 'id_form-0-libre_impuestos',
                    'onchange': 'convTarifa(this)',

                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }
    def __init__(self, *args, **kwargs):
        super(PresupuestosManoObraForm, self).__init__(*args, **kwargs)
        self.fields['tecnico'] = forms.ModelChoiceField(queryset=Tecnicos.objects.all(),
                                                        empty_label=None,
                                                   widget=forms.Select(attrs={
                                                       'class': 'form-select',
                                                       'id': 'id__manoobra-0-tecnico'}))



class PresupuestosPagosForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = ['tipo_pago','cantidad_pagada','numero_transaccion']
        exclude = ['estimate']
        widgets = {
            'tipo_pago': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'cantidad_pagada': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'numero_transaccion': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),

        }

class PresupuestosForm(forms.ModelForm):
    class Meta:
        model = Presupuestos
        #fields = ['descuento_parte','descuentoTotal_parte','total_parte','resumen','descuento_manaobra','descuentoTotal_manaobra','total_manaobra']
        fields = ['resumen']
        widgets = {
            #  'descuento_parte': forms.RadioSelect(choices=DISCOUNT,
            #      attrs={
            #         'class': "custom-radio-list"
            #      }
            # ),
            # 'descuentoTotal_parte': forms.NumberInput(
            #     attrs={
            #         'class': 'form-control',
            #         'onchange': 'descuentoTotalFuncion()',
            #         'placeholder': 'put the number',
            #         'min':0,
            #         'max':100,
            #         'value':100,
            #
            #     }
            # ),
            # 'total_parte': forms.NumberInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': '$0.00',
            #         'disabled':True,
            #     }
            # ),

            'resumen': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 2, 'cols': 5,
                    'disabled':True,
                }
            ),
            # 'descuento_manaobra': forms.RadioSelect(choices=DISCOUNT,
            #     attrs={
            #         'class': "custom-radio-list"
            #     }
            # ),
            # 'descuentoTotal_manaobra': forms.NumberInput(
            #     attrs={
            #         'class': 'form-control',
            #         'onchange': 'descuentoManaObraFuncion()',
            #         'placeholder': 'put the number',
            #
            #     }
            # ),
            # 'total_manaobra': forms.NumberInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': '$0.00',
            #         'disabled': True,
            #     }
            # ),

        }