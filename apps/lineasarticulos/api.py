from rest_framework import generics
from common.models import LineasArticulos
from .serializers import LineasArticulosSerializer

class LineasArticulosListCreateView(generics.ListCreateAPIView):
    queryset = LineasArticulos.objects.all()
    serializer_class = LineasArticulosSerializer

class LineasArticulosRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LineasArticulos.objects.all()
    serializer_class = LineasArticulosSerializer
