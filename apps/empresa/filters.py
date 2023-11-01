import django_filters
from common.models import Empresa

class EmpresaFilter(django_filters.FilterSet):
    class Meta:
        model = Empresa
        fields = ['nro_documento', 'razon_social']
