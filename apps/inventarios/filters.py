from django import forms
import django_filters
from common.models import Inventarios

class DateTimeWidget(forms.widgets.DateTimeInput):
    input_type = 'datetime-local'

class DateWidget(forms.widgets.DateInput):
    input_type = 'date'

class InventariosFilter(django_filters.FilterSet):
    fecha_inventario = django_filters.DateFilter(widget=DateWidget(attrs={'type': 'date'}))
    hora_inicio = django_filters.DateTimeFilter(widget=DateTimeWidget(attrs={'type': 'datetime-local'}))
    hora_fin = django_filters.DateTimeFilter(widget=DateTimeWidget(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Inventarios
        fields = ['empresa',
            'sucursal',
            'fecha_inventario',
            'hora_inicio',
            'hora_fin',
            'estado',]
