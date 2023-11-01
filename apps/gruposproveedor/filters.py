import django_filters
from common.models import GruposProveedor

class GruposProveedorFilter(django_filters.FilterSet):
    class Meta:
        model = GruposProveedor
        fields = ['codigo_grupo', 'empresa', 'activo', 'responsable_grupo']
