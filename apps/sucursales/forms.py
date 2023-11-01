#forms.py
from django import forms
from common.models import Sucursales

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursales
        fields = ['empresa', 'nombre_comercial', 'direccion']
