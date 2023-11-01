from django import forms
from common.models import Personal

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['nombre_personal', 'direccion_personal', 'tipo_documento', 'nro_documento', 'empresa']
