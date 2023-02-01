from django import forms
from .models import ReporteTechnician

class ReporteTechnicianForm(forms.ModelForm):
    class Meta:
        model = ReporteTechnician
        fields = ["content", "quantity"]
        widgets={
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

