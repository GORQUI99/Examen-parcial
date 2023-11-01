# En api.py
from rest_framework import generics
from common.models import Marcas
from .serializers import MarcaSerializer

class MarcaListCreateView(generics.ListCreateAPIView):
    queryset = Marcas.objects.all()
    serializer_class = MarcaSerializer

class MarcaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marcas.objects.all()
    serializer_class = MarcaSerializer