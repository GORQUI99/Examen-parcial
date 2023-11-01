from django import forms
from common.models import Inventarios

class InventariosForm(forms.ModelForm):
    class Meta:
        model = Inventarios
        fields = ['empresa', 'sucursal', 'fecha_inventario', 'nro_inventario', 'responsable', 'hora_inicio', 'hora_fin', 'total_inventario', 'estado', 'creado_por', 'cerrado_por']
        widgets = {
            'fecha_inventario': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_inicio': forms.DateInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'hora_fin': forms.DateInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }
