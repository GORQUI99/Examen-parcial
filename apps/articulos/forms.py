#forms.py
from django import forms
from common.models import Articulos

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = [ 'descripcion', 'unidad_medida', 'grupo', 'linea', 'sublinea', 'empresa', 'factor_compra', 'factor_reparto', 'marca']
