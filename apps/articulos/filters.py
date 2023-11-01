#filters.py
import django_filters
from common.models import Articulos

class ArticuloFilter(django_filters.FilterSet):
    class Meta:
        model = Articulos
        fields = ['codigo_sku',  'empresa', 'marca']
