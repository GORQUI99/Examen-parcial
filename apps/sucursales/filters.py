# filters.py

import django_filters
from common.models import Sucursales

class SucursalFilter(django_filters.FilterSet):
    class Meta:
        model = Sucursales
        fields = ['empresa', 'nombre_comercial']
