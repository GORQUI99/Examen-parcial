from django import forms
from common.models import LineasArticulos

class LineasArticulosForm(forms.ModelForm):
    class Meta:
        model = LineasArticulos
        fields = ['linea_descripcion', 'grupo', 'activo', 'responsable_linea']
