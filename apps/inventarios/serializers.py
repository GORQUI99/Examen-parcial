from rest_framework import serializers
from common.models import Inventarios

class InventariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventarios
        fields = ['id', 'empresa', 'sucursal', 'fecha_inventario', 'nro_inventario', 'responsable', 'hora_inicio', 'hora_fin', 'total_inventario', 'estado', 'creado_por', 'cerrado_por', 'fecha_creacion']
