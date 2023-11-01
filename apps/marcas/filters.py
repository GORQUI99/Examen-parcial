# En filters.py

import django_filters
from common.models import Marcas

class MarcaFilter(django_filters.FilterSet):
    class Meta:
        model = Marcas
        fields = ['codigo_marca', 'marca_nombre']
