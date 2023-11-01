from rest_framework import generics
from common.models import Inventarios
from .serializers import InventariosSerializer

class InventariosListCreateView(generics.ListCreateAPIView):
    queryset = Inventarios.objects.all()
    serializer_class = InventariosSerializer

class InventariosRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventarios.objects.all()
    serializer_class = InventariosSerializer
