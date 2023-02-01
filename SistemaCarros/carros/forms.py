from django import forms
from .models import Carro


class CarroForm(forms.ModelForm):
    class Meta:
        model=Carro
        fields = ['placas','año','modelo','marca','tipo','motor','vin','color',
                  'agente_seguros','compañia_seguros','no_politica','cliente','fotosCarro','garantia']
        exclude = ['fecha_registros']
        widgets = {
            'placas': forms.TextInput(
                attrs={

                    'class': 'form-control',

                }
            ),
            'año': forms.TextInput(
                attrs={

                    'class': 'form-control'
                }
            ),
            'marca': forms.TextInput(
                attrs={

                    'class': 'form-control'
                }
            ),
            'modelo': forms.TextInput(
                attrs={

                    'class': 'form-control'
                }
            ),
            'tipo': forms.TextInput(
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
            'motor': forms.TextInput(
                attrs={

                    'class': 'form-control'
                }
            ),
            'agente_seguros': forms.TextInput(
                attrs={

                    'class': 'form-control'
                }
            ),
            'compañia_seguros': forms.TextInput(
                attrs={

                    'class': 'form-control'
                }
            ),
            'no_politica': forms.TextInput(
                attrs={

                    'class': 'form-control'
                }
            ),
            'cliente': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'fotosCarro':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    # 'multiple': True,
                    'id': 'file-input',
                    'onchange':'preview()',
                }
            ),
            'garantia':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    # 'multiple': True,
                    'id': 'file-inputz',
                    'onchange': 'preview()',
                    # 'id':'pro-images',
                    # 'click': "$('#pro-images').click()",
                }
            ),
            'fecha_registros': forms.DateInput(
                attrs={
                    'class': 'form-control',
                }
            ),

        }


class DateRangeForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField() 
