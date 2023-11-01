from rest_framework import generics
from common.models import GruposProveedor
from .serializers import GruposProveedorSerializer

class GruposProveedorListCreateView(generics.ListCreateAPIView):
    queryset = GruposProveedor.objects.all()
    serializer_class = GruposProveedorSerializer

class GruposProveedorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GruposProveedor.objects.all()
    serializer_class = GruposProveedorSerializer
