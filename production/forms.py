from django import forms
from .models import ProductionOrder

class ProductionOrderForm(forms.ModelForm):
    class Meta:
        model = ProductionOrder
        fields = '__all__'
