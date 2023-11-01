from django import forms
from common.models import ItemsInventario

class ItemsInventarioForm(forms.ModelForm):
    class Meta:
        model = ItemsInventario
        fields = ['inventario', 'nro_item', 'articulo', 'stock_fisico', 'devoluciones_pendientes', 'total_unidades_stock', 'precio_costo', 'total_item']
