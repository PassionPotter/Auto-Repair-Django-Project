from django import forms
from Clientes.models import Clientes
from django.utils.translation import gettext_lazy as _



# PAIS = (
#     ('United States',  _('United States')),
#     ('Canada', _('Canada')),
#     ('Other', _('Other')),
# )

TIPO = (
    ('corporative', _('Corporative')),
    ('person', _('Person')),
)





class ClientesForm(forms.ModelForm):

    tipo = forms.ChoiceField(
        choices=TIPO,
        widget=forms.RadioSelect(attrs={'class':'custom-radio-list', 'onclick':'showForm(this)'}),

    )
    #
    # pais = forms.ChoiceField(
    #     choices=PAIS,
    #     widget=forms.RadioSelect(attrs={'class':'custom-radio-list'}),
    #
    # )


    class Meta:
        model = Clientes
        fields = ['titulo','tipo','nombre', 'apellido', 'telefono', 'alternativeContactName', 'alternativeContactPhoneNumber','fax', 'correo', 'taxId',
                  'ciudad','estado','zip','corporacion', 'website','social_media','department','tel',
                   'representative','nameRepresentative','phoneRepresentative','emailRepresentative','notesRepresentative']
        exclude = ['fecha_registro']
        widgets = {

            'titulo': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'corporacion': forms.TextInput(
                # required=True,
                attrs={
                    'class': 'form-control',
                    # 'required': True,
                }
            ),
            'tel': forms.TextInput(
                # required=True,
                attrs={
                    'class': 'form-control',
                    # 'required': True,

                }
            ),
            'nombre': forms.TextInput(
                # required=True,
                attrs={
                    'class': 'form-control',
                    # 'required': True,


                }
            ),
            'apellido': forms.TextInput(
                # required=True,
                attrs={
                    'class': 'form-control',
                    # 'required': True,
                }
            ),
            'telefono': forms.TextInput(
                # required=True,
                attrs={
                    'class': 'form-control',
                    # 'required': True,
                }
            ),
            'alternativeContactName': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'alternativeContactPhoneNumber': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'department': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'phoneRepresentative': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'emailRepresentative': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'notesRepresentative': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'fax': forms.TextInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'correo': forms.TextInput(
                # required=True,
                attrs={
                    'class': 'form-control',
                    # 'required': True,
                }
            ),

            'website': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'social_media': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'representative': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nameRepresentative': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'taxId': forms.TextInput(
                # required=True,
                attrs={
                    'class': 'form-control',
                    # 'required': True,
                }
            ),
            'ciudad': forms.TextInput(
                # required=True,
                attrs={
                    'class': 'form-control',
                    # 'required': True,
                }
            ),
            'estado': forms.TextInput(
                # required=True,
                attrs={
                    'class': 'form-control',
                    # 'required': True,
                }
            ),
            'zip': forms.TextInput(
                # required=True,
                attrs={
                    'class': 'form-control',
                    # 'required': True,
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
