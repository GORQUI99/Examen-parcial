import django_filters
from common.models import ItemsInventario

class ItemsInventarioFilter(django_filters.FilterSet):
    class Meta:
        model = ItemsInventario
        fields = ['inventario', 'articulo']
