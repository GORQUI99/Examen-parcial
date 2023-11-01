import django_filters
from common.models import SublineasArticulos

class SublineaFilter(django_filters.FilterSet):
    class Meta:
        model = SublineasArticulos
        fields = ['codigo_sublinea', 'sublinea_descripcion', 'linea']
