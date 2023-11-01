import django_filters
from common.models import Personal

class PersonalFilter(django_filters.FilterSet):
    class Meta:
        model = Personal
        fields = ['nombre_personal', 'direccion_personal', 'tipo_documento', 'nro_documento', 'empresa']
