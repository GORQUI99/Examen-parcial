from rest_framework import serializers
from common.models import GruposProveedor

class GruposProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = GruposProveedor
        fields = '__all__'
