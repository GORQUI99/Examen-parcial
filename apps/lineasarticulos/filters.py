import django_filters
from common.models import LineasArticulos

class LineasArticulosFilter(django_filters.FilterSet):
    class Meta:
        model = LineasArticulos
        fields = ['codigo_linea',  'grupo', 'activo', 'responsable_linea']
