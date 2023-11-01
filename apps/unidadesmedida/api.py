# api.py
from rest_framework import generics
from common.models import UnidadesMedida
from .serializers import UnidadMedidaSerializer

class UnidadMedidaListCreateView(generics.ListCreateAPIView):
    queryset = UnidadesMedida.objects.all()
    serializer_class = UnidadMedidaSerializer

class UnidadMedidaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnidadesMedida.objects.all()
    serializer_class = UnidadMedidaSerializer
