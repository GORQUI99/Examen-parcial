# En serializers.py
from rest_framework import serializers
from common.models import Marcas

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marcas
        fields = '__all__'