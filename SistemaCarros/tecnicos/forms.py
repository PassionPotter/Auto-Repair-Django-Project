from django import forms
from django.forms import formset_factory

from tecnicos.models import Tecnicos


class TecnicosForm(forms.ModelForm):

    class Meta:
        model = Tecnicos
        fields = ['nombreTecnico', 'apellidoTecnico', 'emailTecnico', 'telTecnico', 'telTecnico2', 'notasTecnico']
        exclude = ['fecha_registro']
        widgets = {
            'nombreTecnico': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellidoTecnico': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'emailTecnico': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telTecnico': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telTecnico2': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'notasTecnico': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fecha_registro': forms.DateInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class DateRangeForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()