# En forms.py
from django import forms
from common.models import Marcas

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marcas
        fields = [ 'marca_nombre']