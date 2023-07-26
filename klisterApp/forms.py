from django import forms
from .models import formPage


class formPageForm(forms.ModelForm):
    class Meta:
        model = formPage
        fields = ['name', 'age', 'stadsdel', 'idrott', 'önskad_idrott', 'in_a_union']
        widgets = {
            'level': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'in_a_union': forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox', 'role': 'switch'})
        }
