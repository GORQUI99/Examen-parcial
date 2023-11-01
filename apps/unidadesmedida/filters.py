# filters.py
import django_filters
from common.models import UnidadesMedida

class UnidadMedidaFilter(django_filters.FilterSet):
    class Meta:
        model = UnidadesMedida
        fields = ['unidad_nombre']
