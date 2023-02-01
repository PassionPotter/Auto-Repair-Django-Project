from django import forms
from django.forms import formset_factory

from .models import Parte


class ParteForm(forms.ModelForm):

    class Meta:
        model = Parte
        fields = ['dealer', 'codigo', 'invoiceNumber', 'descripcion', 'quantity',
                  'unit_price','minimumInventory','status']
        widgets = {

            'dealer': forms.TextInput(
                attrs={
                    'class': 'autocomplete-input',
                    # 'placeholder': "Type your dealer's name",
                    'id': 'dealer-list',
                    'name': 'dealer-list',
                    'autocomplete': 'off',

        }
            ),
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'invoiceNumber': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'quantity': forms.TextInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'unit_price': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'minimumInventory': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'status':  forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

class DateRangeForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField() 





