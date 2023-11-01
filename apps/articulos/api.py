#api.py
from rest_framework import generics
from common.models import Articulos
from .serializers import ArticuloSerializer

class ArticuloListCreateView(generics.ListCreateAPIView):
    queryset = Articulos.objects.all()
    serializer_class = ArticuloSerializer

class ArticuloRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulos.objects.all()
    serializer_class = ArticuloSerializer
