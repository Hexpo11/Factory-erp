from django import forms
from .models import RawMaterial

class RawMaterialForm(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = ['name', 'quantity', 'unit', 'min_quantity']
