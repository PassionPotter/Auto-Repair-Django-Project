from django import forms
from .models import Foto


class FotoForm(forms.ModelForm):
    class Meta:
        model=Foto
        fields=['imagenes']