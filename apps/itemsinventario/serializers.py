from rest_framework import serializers
from common.models import ItemsInventario

class ItemsInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsInventario
        fields = '__all__'
