from django import forms
from .models import InformacionTiendas
from django.utils.translation import gettext_lazy as _


PAIS = (
    ('United States', _('United States')),
    ('Canada', _('Canada')),
    ('Other', _('Other')),
)


STATUS = (
    ('Active', _('Active')),
    ('Inactive', _('Inactive')),
)


PLAN=(
    ('Monthly', _('Monthly')),
    ('Annual', _('Annual')),
)


class InformacionTiendasForm(forms.ModelForm):

    class Meta:
        model = InformacionTiendas
        fields = '__all__'
        widgets = {

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'registro_desde': forms.DateInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tax_id': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'pais': forms.RadioSelect(choices=PAIS,
                 attrs={
                    'class': "custom-radio-list"
                 }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'zip': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono_1': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono_2': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fax': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'website': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tax_productos': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tax_precios': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'logo': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre_taller': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'plan': forms.RadioSelect(choices=PLAN,
                 attrs={
                    'class': "custom-radio-list"
                 }
            ),
            'status': forms.RadioSelect(choices=STATUS,
                 attrs={
                    'class': "custom-radio-list"
                 }
            ),
        }