from django import forms
from inventory.models import Inventory



class InventoryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ['dealer', 'codigoInventory', 'invoiceNumber', 'descriptionInventory', 'quantityInventory',
                  'unitPriceInventory','minimumInventory','status']
        exclude = ['fecha_registro']
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
            'codigoInventory': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'invoiceNumber': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descriptionInventory': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'quantityInventory': forms.TextInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'unitPriceInventory': forms.TextInput(
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