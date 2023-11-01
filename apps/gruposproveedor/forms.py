from django import forms
from common.models import GruposProveedor

class GruposProveedorForm(forms.ModelForm):
    class Meta:
        model = GruposProveedor
        fields = ['grupo_descripcion', 'empresa', 'activo', 'responsable_grupo']
