from django import forms
from common.models import SublineasArticulos

class SublineaForm(forms.ModelForm):
    class Meta:
        model = SublineasArticulos
        fields = ['sublinea_descripcion', 'linea', 'estado']
