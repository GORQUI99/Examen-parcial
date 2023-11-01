# serializers.py
from rest_framework import serializers
from common.models import UnidadesMedida

class UnidadMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadesMedida
        fields = '__all__'
