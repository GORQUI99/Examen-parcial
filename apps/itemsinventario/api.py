from rest_framework import generics
from common.models import ItemsInventario
from .serializers import ItemsInventarioSerializer

class ItemInventarioListCreateView(generics.ListCreateAPIView):
    queryset = ItemsInventario.objects.all()
    serializer_class = ItemsInventarioSerializer

class ItemInventarioRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ItemsInventario.objects.all()
    serializer_class = ItemsInventarioSerializer
