#serializers.py
from rest_framework import serializers
from common.models import Sucursales

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursales
        fields = '__all__'

