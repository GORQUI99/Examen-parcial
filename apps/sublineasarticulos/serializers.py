from rest_framework import serializers
from common.models import SublineasArticulos

class SublineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SublineasArticulos
        fields = '__all__'
