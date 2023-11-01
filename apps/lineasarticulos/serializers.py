from rest_framework import serializers
from common.models import LineasArticulos

class LineasArticulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineasArticulos
        fields = '__all__'
