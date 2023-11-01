# forms.py
from django import forms
from common.models import UnidadesMedida

class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadesMedida
        fields = ['unidad_nombre']
