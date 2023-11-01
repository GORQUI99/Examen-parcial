#serializers.py
from rest_framework import serializers
from common.models import Articulos

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulos
        fields = '__all__'
